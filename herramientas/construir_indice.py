"""Construcción de índices navegables de la base de conocimiento BRIDGE.

Genera:
  kb/indices/preguntas.jsonl  (864 filas, con ruta en lugar de archivo/linea)
  kb/indices/fuentes.jsonl    (551 filas)
"""
import collections
import json
import logging
import os
import sys
from pathlib import Path

_RAIZ = Path(__file__).resolve().parent.parent
if str(_RAIZ) not in sys.path:
    sys.path.insert(0, str(_RAIZ))

try:
    from herramientas.kb import (
        cargar_banco,
        cargar_manifiestos,
        cargar_respuestas,
        raiz,
        slug,
    )
except ModuleNotFoundError:
    from kb import (
        cargar_banco,
        cargar_manifiestos,
        cargar_respuestas,
        raiz,
        slug,
    )

logger = logging.getLogger("construir_indice")

# Mapeo canónico pilar -> módulo según Anexo A y Mandato
MODULO = {
    "P01": "transversal",
    "P02": "transversal",
    "P03": "Escuchar",
    "P04": "Saber",
    "P05": "Escuchar",
    "P06": "Saber",
    "P07": "Hablar",
    "P08": "transversal",
    "P09": "Relacionar",
    "P10": "Hablar",
    "P11": "transversal",
    "T01": "transversal",
}


def construir_indices() -> tuple[list[dict], list[dict]]:
    """Construye y guarda kb/indices/preguntas.jsonl y kb/indices/fuentes.jsonl."""
    r = raiz()
    out_dir = r / "kb" / "indices"
    out_dir.mkdir(parents=True, exist_ok=True)

    banco, titulos = cargar_banco()
    respuestas = cargar_respuestas()
    manifiestos = cargar_manifiestos()

    citas_por_fuente = collections.defaultdict(list)
    preguntas = []

    for reg in respuestas:
        qid = reg["question_id"]
        b = banco[qid]
        p = b["pilar"]
        ruta = reg.get("__ruta")
        if not ruta:
            p_dir = f"{p}-{slug(titulos[p])}"
            ruta = f"kb/pilares/{p_dir}/ejes/{b['eje_dir']}/{qid}.json"

        # Fuentes del pilar para validación y trazabilidad
        srcs = {s["source_id"]: s for s in manifiestos.get(p, {}).get("sources", [])}

        epi = collections.Counter()
        ev_total = 0
        ev_sint = 0
        ev_interna = 0
        ev_fuente_no_sust = 0
        citadas = []

        findings = reg.get("findings", [])
        for f in findings:
            epi[f.get("epistemic_status")] += 1
            for e in f.get("evidence", []):
                ev_total += 1
                sid = e.get("source_id")
                s = srcs.get(sid, {})
                if sid:
                    citadas.append(sid)
                    citas_por_fuente[sid].append(qid)
                if e.get("cita_sintetica"):
                    ev_sint += 1
                if e.get("fuente_es_sintesis_interna"):
                    ev_interna += 1
                if e.get("text_status") != "texto_sustantivo":
                    ev_fuente_no_sust += 1

        hechos = [f for f in findings if f.get("epistemic_status") == "hecho_documentado"]
        hechos_solo_internos = sum(
            1 for f in hechos
            if f.get("evidence") and all(e.get("fuente_es_sintesis_interna") for e in f["evidence"])
        )

        banderas = []
        if reg.get("question_text") != b["question_text"]:
            banderas.append("texto_pregunta_distinto_mandato")
        if ev_sint:
            banderas.append("citas_sinteticas")
        if hechos_solo_internos:
            banderas.append("hecho_respaldado_solo_por_sintesis_interna")
        if ev_fuente_no_sust:
            banderas.append("cita_fuente_no_sustantiva")
        if reg.get("answer_status") != "respondida":
            banderas.append(f"estado_{reg.get('answer_status')}")

        short_ans = reg.get("short_answer") or ""
        chars = len(json.dumps(reg, ensure_ascii=False))

        preguntas.append({
            "question_id": qid,
            "pilar": p,
            "pilar_titulo": titulos.get(p),
            "modulo": MODULO.get(p, "transversal"),
            "tipo": b["tipo"],
            "eje": b["eje"],
            "eje_n": b["eje_n"],
            "subeje": b["subeje"],
            "question_text": b["question_text"],
            "ruta": ruta,
            "chars": chars,
            "tokens_aprox": round(chars / 3.5),
            "answer_status": reg.get("answer_status"),
            "short_answer_chars": len(short_ans),
            "n_findings": len(findings),
            "epistemic": dict(epi),
            "n_evidencias": ev_total,
            "n_evidencias_sinteticas": ev_sint,
            "n_evidencias_sintesis_interna": ev_interna,
            "n_hechos_solo_sintesis_interna": hechos_solo_internos,
            "n_open_gaps": len(reg.get("open_gaps", [])),
            "n_contradicciones": len(reg.get("contradictions", [])),
            "fuentes_citadas": sorted(set(citadas)),
            "banderas": banderas,
        })

    # Construir índice de fuentes
    fuentes = []
    for p in sorted(manifiestos.keys()):
        for s in manifiestos[p].get("sources", []):
            sid = s["source_id"]
            fuentes.append({
                "pilar": p,
                "source_id": sid,
                "title": s.get("title"),
                "original_url": s.get("original_url"),
                "text_status": s.get("text_status"),
                "is_internal_synthesis": bool(s.get("is_internal_synthesis")),
                "word_count": s.get("word_count"),
                "n_citas": len(citas_por_fuente.get(sid, [])),
                "preguntas_que_citan": sorted(set(citas_por_fuente.get(sid, []))),
            })

    # Guardar preguntas.jsonl
    preg_path = out_dir / "preguntas.jsonl"
    with open(preg_path, "w", encoding="utf-8") as fh:
        for p_row in preguntas:
            fh.write(json.dumps(p_row, ensure_ascii=False) + "\n")

    # Guardar fuentes.jsonl
    fuentes_path = out_dir / "fuentes.jsonl"
    with open(fuentes_path, "w", encoding="utf-8") as fh:
        for f_row in fuentes:
            fh.write(json.dumps(f_row, ensure_ascii=False) + "\n")

    return preguntas, fuentes


def main():
    """Punto de entrada CLI de construir_indice.py."""
    try:
        preguntas, fuentes = construir_indices()
        print(f"Índices generados con éxito: {len(preguntas)} preguntas, {len(fuentes)} fuentes.")
    except Exception as err:
        logger.error(f"Error al construir índices: {type(err).__name__} (detalles omitidos por seguridad)")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
