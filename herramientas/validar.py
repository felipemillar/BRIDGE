"""Validador integral de integridad y conformidad de la base de conocimiento BRIDGE.

Verifica:
  1. Integridad física de las 864 preguntas en sus rutas canónicas.
  2. Conformidad con los vocabularios controlados (kb/esquemas/vocabularios.json).
  3. Integridad referencial de fuentes (source_id perteneciente al manifiesto de su pilar).
  4. Protocolo de verificación epistémica (pasaje, url_consultada, sha256_texto en verificada/refutada).
  5. Regla estricta de verificación: prohibición de verificar citas sintéticas o síntesis interna exclusiva.
  6. Si existe kb/grafo/mapa_ids.jsonl: integridad referencial y de predicados del grafo.

Sale con código 0 si todo es válido, o código 1 ante cualquier infracción.
"""
import collections
import json
import logging
import os
import re
import sys
from pathlib import Path

_RAIZ = Path(__file__).resolve().parent.parent
if str(_RAIZ) not in sys.path:
    sys.path.insert(0, str(_RAIZ))

try:
    from herramientas.kb import (
        PILARES,
        cargar_banco,
        cargar_manifiestos,
        raiz,
        slug,
    )
except ModuleNotFoundError:
    from kb import (
        PILARES,
        cargar_banco,
        cargar_manifiestos,
        raiz,
        slug,
    )

logger = logging.getLogger("validar")


def cargar_vocabularios(r: Path) -> dict:
    """Carga y retorna kb/esquemas/vocabularios.json."""
    vp = r / "kb" / "esquemas" / "vocabularios.json"
    if not vp.exists():
        raise FileNotFoundError("kb/esquemas/vocabularios.json no existe")
    return json.loads(vp.read_text(encoding="utf-8"))


def pilar_dir(p: str, titulos: dict[str, str]) -> str:
    """Retorna el nombre de directorio canónico de un pilar."""
    return f"{p}-{slug(titulos[p])}"


def validar_preguntas_y_fuentes(
    r: Path,
    banco: dict,
    titulos: dict,
    vocabs: dict,
    manifiestos: dict,
) -> tuple[list[str], set[str]]:
    """Valida los 864 archivos de pregunta y su conformidad con reglas epistémicas y fuentes."""
    errores = []
    all_claims = set()

    epi_canon = set(vocabs.get("epistemic_status", []))
    conf_canon = set(vocabs.get("confidence", []))
    ts_canon = set(vocabs.get("text_status", []))
    verif_canon = set(vocabs.get("verificacion_estado", []))
    ans_canon = set(vocabs.get("answer_status", []))

    # Verificar que existan las 864 preguntas en el banco
    if len(banco) != 864:
        errores.append(f"El banco del mandato tiene {len(banco)} preguntas (se esperan 864)")

    # Verificar fuentes de cada pilar
    fuentes_por_pilar = {}
    for p in PILARES:
        m = manifiestos.get(p, {})
        fuentes_por_pilar[p] = {s["source_id"]: s for s in m.get("sources", [])}

    # Escaneo físico de archivos de pregunta
    preguntas_encontradas = list((r / "kb" / "pilares").glob("*/ejes/*/*.json"))
    if len(preguntas_encontradas) != 864:
        errores.append(f"Se encontraron {len(preguntas_encontradas)} archivos de pregunta en kb/pilares/ (se esperan 864)")

    for qid, b in banco.items():
        p = b["pilar"]
        p_d = pilar_dir(p, titulos)
        ed = b["eje_dir"]
        ruta_esperada = r / "kb" / "pilares" / p_d / "ejes" / ed / f"{qid}.json"

        if not ruta_esperada.exists():
            errores.append(f"Archivo de pregunta ausente en ruta esperada: {ruta_esperada.relative_to(r)}")
            continue

        try:
            d = json.loads(ruta_esperada.read_text(encoding="utf-8"))
        except Exception as err:
            errores.append(f"Error al leer JSON de {qid}: {type(err).__name__} (detalles omitidos por seguridad)")
            continue

        # Validar campos de ubicación y cabecera
        if d.get("question_id") != qid:
            errores.append(f"{qid}: question_id no coincide con el archivo ({d.get('question_id')})")
        for k in ("pilar", "eje", "subeje", "eje_n", "tipo"):
            if d.get(k) != b.get(k):
                errores.append(f"{qid}: campo '{k}' valor '{d.get(k)}' no coincide con banco '{b.get(k)}'")

        ans_st = d.get("answer_status")
        if ans_st not in ans_canon:
            errores.append(f"{qid}: answer_status '{ans_st}' fuera de vocabulario")

        # Validar hallazgos (findings)
        findings = d.get("findings", [])
        for f in findings:
            cid = f.get("claim_id")
            if not cid:
                errores.append(f"{qid}: hallazgo sin claim_id")
                continue
            all_claims.add(cid)

            # Vocabulario epistémico y confianza
            ep_st = f.get("epistemic_status")
            if ep_st not in epi_canon:
                errores.append(f"{qid}/{cid}: epistemic_status '{ep_st}' fuera de vocabulario canónico")

            conf = f.get("confidence")
            if conf not in conf_canon:
                errores.append(f"{qid}/{cid}: confidence '{conf}' fuera de vocabulario canónico")

            # Validación de estado de verificación
            verif = f.get("verificacion")
            if not isinstance(verif, dict):
                errores.append(f"{qid}/{cid}: campo 'verificacion' ausente o no es objeto")
                continue

            v_est = verif.get("estado")
            if v_est not in verif_canon:
                errores.append(f"{qid}/{cid}: verificacion.estado '{v_est}' fuera de vocabulario")

            # Regla de verificada / refutada: requiere pasaje, url_consultada y sha256_texto
            if v_est in ("verificada", "refutada"):
                pasaje = verif.get("pasaje")
                url_c = verif.get("url_consultada")
                sha_t = verif.get("sha256_texto")
                if not (isinstance(pasaje, str) and pasaje.strip()):
                    errores.append(f"{qid}/{cid}: estado '{v_est}' sin 'pasaje' de texto válido")
                if not (isinstance(url_c, str) and url_c.strip()):
                    errores.append(f"{qid}/{cid}: estado '{v_est}' sin 'url_consultada' válida")
                if not (isinstance(sha_t, str) and sha_t.strip()):
                    errores.append(f"{qid}/{cid}: estado '{v_est}' sin 'sha256_texto' válido")

            # Validar evidencias y fuentes
            evidencias = f.get("evidence", [])
            ev_sintetica = False
            ev_interna_count = 0

            for ev in evidencias:
                sid = ev.get("source_id")
                if not sid or sid not in fuentes_por_pilar[p]:
                    errores.append(f"{qid}/{cid}: source_id '{sid}' inexistente en el manifiesto de pilar {p}")

                ev_ts = ev.get("text_status")
                if ev_ts not in ts_canon:
                    errores.append(f"{qid}/{cid}: text_status '{ev_ts}' en evidencia fuera de vocabulario")

                if ev.get("cita_sintetica"):
                    ev_sintetica = True
                if ev.get("fuente_es_sintesis_interna"):
                    ev_interna_count += 1

            # Regla: ningún hallazgo con cita_sintetica o solo_sintesis_interna puede estar verificada
            if v_est == "verificada":
                if ev_sintetica:
                    errores.append(f"{qid}/{cid}: hallazgo con 'cita_sintetica' no puede estar en estado 'verificada'")
                if evidencias and ev_interna_count == len(evidencias):
                    errores.append(f"{qid}/{cid}: hallazgo respaldado exclusivamente por síntesis interna no puede estar en estado 'verificada'")

    return errores, all_claims


def validar_grafo(
    r: Path,
    vocabs: dict,
    all_claims: set[str],
) -> list[str]:
    """Valida la integridad del grafo de conocimiento si existe kb/grafo/mapa_ids.jsonl."""
    mapa_path = r / "kb" / "grafo" / "mapa_ids.jsonl"
    if not mapa_path.exists():
        return []

    errores = []
    tipos_entidad = set(vocabs.get("tipo_entidad", []))
    predicados = set(vocabs.get("predicado", []))

    # Validar entidades
    ent_path = r / "kb" / "grafo" / "entidades.jsonl"
    entidades_ids = set()
    if not ent_path.exists():
        errores.append("kb/grafo/entidades.jsonl no existe")
    else:
        with open(ent_path, "r", encoding="utf-8") as fh:
            for n_line, line in enumerate(fh, start=1):
                if not line.strip():
                    continue
                try:
                    e = json.loads(line)
                except Exception as err:
                    errores.append(f"entidades.jsonl:{n_line}: JSON inválido: {type(err).__name__} (detalles omitidos por seguridad)")
                    continue

                eid = e.get("entity_id")
                if not eid or not re.match(r"^[a-z]+:[a-z0-9][a-z0-9-]*$", str(eid)):
                    errores.append(f"entidades.jsonl:{n_line}: entity_id inválido '{eid}'")
                elif eid in entidades_ids:
                    errores.append(f"entidades.jsonl:{n_line}: entity_id duplicado '{eid}'")
                else:
                    entidades_ids.add(eid)

                t = e.get("type")
                if t not in tipos_entidad:
                    errores.append(f"entidades.jsonl:{n_line}: type '{t}' fuera de tipo_entidad")

                if not str(e.get("canonical_name", "")).strip():
                    errores.append(f"entidades.jsonl:{n_line}: canonical_name vacío")

    # Validar relaciones si el archivo ha sido reconstruido con indice_legado (F4.3+)
    rel_path = r / "kb" / "grafo" / "relaciones.jsonl"
    if rel_path.exists():
        es_reconstruido = False
        with open(rel_path, "r", encoding="utf-8") as fh:
            primera = fh.readline()
            if primera.strip():
                try:
                    es_reconstruido = "indice_legado" in json.loads(primera)
                except Exception:
                    es_reconstruido = False
        if es_reconstruido:
            with open(rel_path, "r", encoding="utf-8") as fh:
                for n_line, line in enumerate(fh, start=1):
                    if not line.strip():
                        continue
                    try:
                        rel = json.loads(line)
                    except Exception as err:
                        errores.append(f"relaciones.jsonl:{n_line}: JSON inválido: {type(err).__name__} (detalles omitidos por seguridad)")
                        continue

                    sub = rel.get("subject_id")
                    obj = rel.get("object_id")
                    pred = rel.get("predicate")

                    if sub not in entidades_ids:
                        errores.append(f"relaciones.jsonl:{n_line}: subject_id '{sub}' no existe en entidades")
                    if obj not in entidades_ids:
                        errores.append(f"relaciones.jsonl:{n_line}: object_id '{obj}' no existe en entidades")
                    if pred not in predicados:
                        errores.append(f"relaciones.jsonl:{n_line}: predicate '{pred}' fuera de vocabulario")

                    cids = rel.get("evidence_claim_ids", [])
                    for cid in cids:
                        if cid not in all_claims:
                            errores.append(f"relaciones.jsonl:{n_line}: claim_id '{cid}' no existe en findings")

    # Validar contradicciones si el archivo ha sido normalizado (F4.4+)
    cont_path = r / "kb" / "grafo" / "contradicciones.jsonl"
    if cont_path.exists():
        es_normalizado = False
        with open(cont_path, "r", encoding="utf-8") as fh:
            primera = fh.readline()
            if primera.strip():
                try:
                    es_normalizado = "resolution_original" in json.loads(primera)
                except Exception:
                    es_normalizado = False
        if es_normalizado:
            with open(cont_path, "r", encoding="utf-8") as fh:
                for n_line, line in enumerate(fh, start=1):
                    if not line.strip():
                        continue
                    try:
                        c = json.loads(line)
                    except Exception as err:
                        errores.append(f"contradicciones.jsonl:{n_line}: JSON inválido: {type(err).__name__} (detalles omitidos por seguridad)")
                        continue

                    res = c.get("resolution")
                    if res not in ("resuelta", "abierta"):
                        errores.append(f"contradicciones.jsonl:{n_line}: resolution '{res}' debe ser 'resuelta' o 'abierta'")

    return errores


def validar_repositorio() -> list[str]:
    """Ejecuta la validación completa del repositorio."""
    r = raiz()
    vocabs = cargar_vocabularios(r)
    banco, titulos = cargar_banco()
    manifiestos = cargar_manifiestos()

    errores, all_claims = validar_preguntas_y_fuentes(r, banco, titulos, vocabs, manifiestos)
    errores_grafo = validar_grafo(r, vocabs, all_claims)
    errores.extend(errores_grafo)

    return errores


def main():
    """Punto de entrada CLI de herramientas/validar.py."""
    try:
        errores = validar_repositorio()
        if errores:
            print(f"FALLO DE VALIDACIÓN ({len(errores)} errores encontrados):")
            for err in errores[:25]:
                print(f"  - {err}")
            if len(errores) > 25:
                print(f"  ... y {len(errores) - 25} errores adicionales.")
            raise SystemExit(1)
        else:
            print("VALIDACIÓN EXITOSA: Repositorio conforme con vocabularios, fuentes y reglas epistémicas.")
    except SystemExit:
        raise
    except Exception as err:
        logger.error(f"Error inesperado al validar repositorio: {type(err).__name__} (detalles omitidos por seguridad)")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
