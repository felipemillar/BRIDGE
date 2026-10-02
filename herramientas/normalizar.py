"""Normalización anotativa de la base de conocimiento BRIDGE.

Aplica las reglas N1–N8 de auditoria/PLAN_MIGRACION_ANTIGRAVITY.md Anexo A.
Es idempotente y preserva los valores originales en campos *_original.
"""
import logging
from herramientas.kb import (
    cargar_respuestas,
    guardar_respuestas,
    cargar_manifiestos,
    guardar_manifiestos,
)

logger = logging.getLogger("normalizar")

EPI_CANON = {"hecho_documentado", "declaracion_proveedor", "inferencia", "hipotesis_diseno"}
EPI_MAPA = {
    "fact": "hecho_documentado",
    "hypothesis": "hipotesis_diseno",
    "propuesta_arquitectura_formal": "hipotesis_diseno",
    "diseno_de_datos_formal": "hipotesis_diseno",
    "diseno_experimental_formal": "hipotesis_diseno",
    "patron_diseno_ciberseguridad": "hipotesis_diseno",
    "control_de_ciberseguridad_formal": "hipotesis_diseno",
    "taxonomia_operacional_gobernanza": "hipotesis_diseno",
    "regla_control_riesgo_reputacional": "hipotesis_diseno",
    "principio_metodologico_formal": "hipotesis_diseno",
    "modelo_computacional_probado": "inferencia",
    "modelo_operacional_probado": "inferencia",
    "caso_de_prueba_empirico": "inferencia",
    "estandar_seguridad_comprobado": "inferencia",
    "prevalencia_editorial_correccion": "inferencia",
    "vacio_empirico_documentado": "inferencia",
    "patologia_epistemica_documentada": "inferencia",
    "principio_de_impacto_amec": "inferencia",
}

TS_CANON = {"texto_sustantivo", "resumen_parcial", "solo_navegacion", "captcha", "fallida", "duplicada", "desconocida"}
TS_MAPA = {
    "fallida_o_bloqueada": "fallida",
    "error_extraccion": "fallida",
    "fuente_fallida": "fallida",
    "error_extraccion_o_duplicado": "fallida",
    "directorio_navegacional_no_sustantivo": "solo_navegacion",
    "ficha_abstract_duplicada": "duplicada",
    "atribucion_comercial_erronea": "desconocida",
}

LOCALIZADOR_SINTETICO = "Sección sustantiva vinculada"
SNAPSHOT_NOTA = (
    "Valor original sobrescrito el 2026-10-01 por scripts/normalize_status_and_timestamps.py "
    "con una constante por pilar; no proviene de un registro del conector."
)


def url_de(x):
    """Extrae la URL cruda de NotebookLM cuando se almacena como lista en metadata."""
    if isinstance(x, list):
        try:
            x = x[7][0]
        except (TypeError, IndexError):
            x = None
    return x if isinstance(x, str) and x.startswith("http") else None


def normalizar(R: list[dict], M: dict[str, dict]) -> tuple[list[dict], dict[str, dict]]:
    """Aplica las reglas N1-N8 de normalización anotativa sobre respuestas y manifiestos."""
    S = {}
    for pilar, mdata in M.items():
        for s in mdata.get("sources", []):
            # Regla N3: text_status de fuentes
            cur_ts = s.get("text_status")
            if cur_ts not in TS_CANON:
                if "text_status_original" not in s:
                    s["text_status_original"] = cur_ts
                s["text_status"] = TS_MAPA.get(cur_ts, "desconocida")

            # Regla N4: original_url de fuentes
            if isinstance(s.get("original_url"), list):
                if "metadata_notebooklm_crudo" not in s:
                    s["metadata_notebooklm_crudo"] = s["original_url"]
                s["original_url"] = url_de(s["metadata_notebooklm_crudo"])

            S[s["source_id"]] = s

    for r in R:
        # Regla N7: Tiempos del registro
        if r.get("snapshot_at") is not None:
            if "snapshot_at_original" not in r:
                r["snapshot_at_original"] = r["snapshot_at"]
            r["snapshot_at"] = None
        if not r.get("snapshot_nota"):
            r["snapshot_nota"] = SNAPSHOT_NOTA

        fs = r.get("findings", [])
        for f in fs:
            # Regla N1: epistemic_status
            cur_epi = f.get("epistemic_status")
            if cur_epi not in EPI_CANON:
                if "epistemic_status_original" not in f:
                    f["epistemic_status_original"] = cur_epi
                f["epistemic_status"] = EPI_MAPA.get(cur_epi, "hipotesis_diseno")

            # Regla N2: confidence numérica
            cur_conf = f.get("confidence")
            if isinstance(cur_conf, (int, float)):
                if "confidence_original" not in f:
                    f["confidence_original"] = cur_conf
                f["confidence"] = "alta" if cur_conf >= 0.90 else ("media" if cur_conf >= 0.70 else "baja")

            # Regla N5: Evidencias
            evs = f.get("evidence", [])
            for e in evs:
                src = S.get(e.get("source_id"), {})
                src_ts = src.get("text_status")
                cur_e_ts = e.get("text_status")
                if cur_e_ts != src_ts:
                    if "text_status_original" not in e and cur_e_ts is not None:
                        e["text_status_original"] = cur_e_ts
                    e["text_status"] = src_ts

                e["cita_sintetica"] = bool(LOCALIZADOR_SINTETICO in (e.get("locator") or ""))
                e["fuente_es_sintesis_interna"] = bool(src.get("is_internal_synthesis"))

                if e.get("retrieved_at") is not None:
                    if "retrieved_at_original" not in e:
                        e["retrieved_at_original"] = e["retrieved_at"]
                    e["retrieved_at"] = None
                elif "retrieved_at_original" not in e:
                    e["retrieved_at_original"] = None

            # Regla N6: Verificación en hallazgo
            v = f.get("verificacion")
            if not v or v.get("estado") not in ("verificada", "refutada", "no_verificable"):
                has_cs = any(e.get("cita_sintetica") for e in evs)
                all_int = bool(evs) and all(e.get("fuente_es_sintesis_interna") for e in evs)
                if has_cs:
                    v_estado = "cita_sintetica"
                elif all_int:
                    v_estado = "solo_sintesis_interna"
                else:
                    v_estado = "no_verificada"

                motivos = []
                if has_cs:
                    motivos.append("cita_sintetica")
                if all_int:
                    motivos.append("solo_sintesis_interna")
                if any(e.get("text_status") != "texto_sustantivo" for e in evs):
                    motivos.append("fuente_no_sustantiva")
                if "confidence_original" in f:
                    motivos.append("confianza_numerica_original")
                if "epistemic_status_original" in f:
                    motivos.append("estado_epistemico_no_canonico_original")

                f["verificacion"] = {
                    "estado": v_estado,
                    "motivos": motivos,
                    "verificado_por": None,
                    "fecha": None,
                    "metodo": None,
                    "pasaje": None,
                }

        # Regla N8: Quality
        if "quality_original" not in r:
            r["quality_original"] = r.get("quality")
        estados = [f.get("verificacion", {}).get("estado") for f in fs]
        hr = (
            r.get("answer_status") == "parcial"
            or any(x in ("cita_sintetica", "solo_sintesis_interna", "refutada", "no_verificable") for x in estados)
            or any(e.get("text_status") != "texto_sustantivo" for f in fs for e in f.get("evidence", []))
        )
        r["quality"] = {
            "original_citations_resolved": bool(fs) and all(x == "verificada" for x in estados),
            "correction_precedence_checked": None,
            "duplicate_sources_counted_once": None,
            "human_review_needed": hr,
        }

    return R, M


def main():
    """Punto de entrada de normalización CLI."""
    try:
        R = cargar_respuestas()
        M = cargar_manifiestos()
        R_norm, M_norm = normalizar(R, M)
        guardar_respuestas(R_norm)
        guardar_manifiestos(M_norm)
        print(f"Normalización completada: {len(R_norm)} respuestas, {len(M_norm)} manifiestos procesados.")
    except Exception as err:
        logger.error(f"Error en normalización: {type(err).__name__} (detalles omitidos por seguridad)")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
