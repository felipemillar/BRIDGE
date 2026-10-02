"""Genera el índice navegable del repositorio para agentes.

Salidas (en auditoria/):
  indice_preguntas.jsonl  864 filas: ubicación exacta, eje, métricas y banderas de calidad por pregunta.
  indice_fuentes.jsonl    una fila por fuente de manifiesto, con las preguntas que la citan.
  resumen_indice.json     conteos agregados por pilar.

Uso: python3 auditoria/construir_indice.py  (desde la raíz del repo; solo lectura sobre los datos).
"""
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "auditoria"
MANDATO = ROOT / "docs_mandato" / "mandato-antigravity-investigacion-asuntos-corporativos.md"
PILARES = ["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09", "P10", "P11", "T01"]

# Mapeo propuesto pilar -> módulo del flujo Saber/Escuchar/Hablar/Relacionar (no proviene del corpus).
MODULO = {
    "P01": "transversal_usuarios", "P02": "transversal_mercado", "P03": "Escuchar",
    "P04": "Saber", "P05": "Escuchar", "P06": "Saber+Escuchar", "P07": "Hablar",
    "P08": "transversal_negocio", "P09": "Relacionar", "P10": "Hablar",
    "P11": "transversal_gobernanza", "T01": "transversal_evaluacion",
}
EPI_CANON = {"hecho_documentado", "declaracion_proveedor", "inferencia", "hipotesis_diseno"}
EPI_ALIAS = {"fact": "hecho_documentado", "hypothesis": "hipotesis_diseno"}


def parse_mandato():
    """Devuelve {qid: (texto, eje, subeje)} y {pilar: titulo} desde el banco exacto."""
    banco, titulos = {}, {}
    pilar = eje = subeje = None
    for line in MANDATO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^### ((?:P\d\d|T01)) — (.+)$", line)
        if m:
            pilar, eje, subeje = m.group(1), None, None
            titulos[pilar] = m.group(2).strip()
            continue
        m = re.match(r"^\*\*Eje: (.+)\*\*$", line)
        if m:
            eje, subeje = m.group(1).strip(), None
            continue
        if line.startswith("**Profundización"):
            eje = "Profundización especializada"
            continue
        m = re.match(r"^\*([^*].+)\*$", line)
        if m and pilar:
            subeje = m.group(1).strip()
            continue
        m = re.match(r"^- \*\*((?:P\d\d|T01)-[FCX]\d\d)\.\*\* (.+)$", line)
        if m:
            banco[m.group(1)] = (m.group(2).strip(), eje, subeje)
    return banco, titulos


def norm_epi(value):
    if value in EPI_CANON:
        return value
    return EPI_ALIAS.get(value, "no_canonico")


def main():
    banco, titulos = parse_mandato()
    preguntas, fuentes, resumen = [], [], {}
    for p in PILARES:
        man = json.loads((ROOT / "fuentes" / f"{p}.json").read_text(encoding="utf-8"))
        srcs = {s["source_id"]: s for s in man["sources"]}
        citas_por_fuente = collections.defaultdict(list)
        agg = collections.Counter()
        path = ROOT / "respuestas" / f"{p}.jsonl"
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            r = json.loads(line)
            qid = r["question_id"]
            texto, eje, subeje = banco.get(qid, (None, None, None))
            epi = collections.Counter()
            ev_total = ev_sint = ev_interna = ev_fuente_no_sust = 0
            citadas = []
            for f in r.get("findings", []):
                epi[norm_epi(f.get("epistemic_status"))] += 1
                for e in f.get("evidence", []):
                    ev_total += 1
                    sid = e.get("source_id")
                    s = srcs.get(sid, {})
                    citadas.append(sid)
                    citas_por_fuente[sid].append(qid)
                    if "Sección sustantiva vinculada" in (e.get("locator") or ""):
                        ev_sint += 1
                    if s.get("is_internal_synthesis"):
                        ev_interna += 1
                    if s and s.get("text_status") != "texto_sustantivo":
                        ev_fuente_no_sust += 1
            hechos = [f for f in r.get("findings", []) if norm_epi(f.get("epistemic_status")) == "hecho_documentado"]
            hechos_solo_internos = sum(
                1 for f in hechos
                if f.get("evidence") and all(srcs.get(e.get("source_id"), {}).get("is_internal_synthesis") for e in f["evidence"])
            )
            banderas = []
            if r.get("question_text") != texto:
                banderas.append("texto_pregunta_distinto_mandato")
            if any(norm_epi(f.get("epistemic_status")) != f.get("epistemic_status") for f in r.get("findings", [])):
                banderas.append("epistemic_status_no_canonico")
            if any(not isinstance(f.get("confidence"), str) for f in r.get("findings", [])):
                banderas.append("confidence_numerica")
            if ev_sint:
                banderas.append("citas_sinteticas")
            if hechos_solo_internos:
                banderas.append("hecho_respaldado_solo_por_sintesis_interna")
            if ev_fuente_no_sust:
                banderas.append("cita_fuente_no_sustantiva")
            if r.get("answer_status") != "respondida":
                banderas.append(f"estado_{r.get('answer_status')}")
            chars = len(line)
            preguntas.append({
                "question_id": qid, "pilar": p, "pilar_titulo": titulos.get(p),
                "modulo_propuesto": MODULO[p], "tipo": qid.split("-")[1][0],
                "eje": eje, "subeje": subeje, "question_text": texto,
                "archivo": f"respuestas/{p}.jsonl", "linea": n,
                "chars": chars, "tokens_aprox": round(chars / 3.5),
                "answer_status": r.get("answer_status"),
                "short_answer_chars": len(r.get("short_answer") or ""),
                "n_findings": len(r.get("findings", [])),
                "epistemic": dict(epi), "n_evidencias": ev_total,
                "n_evidencias_sinteticas": ev_sint, "n_evidencias_sintesis_interna": ev_interna,
                "n_hechos_solo_sintesis_interna": hechos_solo_internos,
                "n_open_gaps": len(r.get("open_gaps", [])),
                "n_contradicciones": len(r.get("contradictions", [])),
                "fuentes_citadas": sorted(set(citadas)),
                "banderas": banderas,
            })
            agg["preguntas"] += 1
            agg["findings"] += len(r.get("findings", []))
            agg["evidencias"] += ev_total
            agg["evidencias_sinteticas"] += ev_sint
            agg["evidencias_sintesis_interna"] += ev_interna
            agg["hechos_solo_sintesis_interna"] += hechos_solo_internos
            agg["preguntas_con_banderas"] += bool(banderas)
            agg["tokens_aprox"] += round(chars / 3.5)
        for sid, s in srcs.items():
            fuentes.append({
                "pilar": p, "source_id": sid, "title": s.get("title"),
                "original_url": s.get("original_url"), "text_status": s.get("text_status"),
                "is_internal_synthesis": s.get("is_internal_synthesis"),
                "word_count": s.get("word_count"),
                "n_citas": len(citas_por_fuente.get(sid, [])),
                "preguntas_que_citan": sorted(set(citas_por_fuente.get(sid, []))),
            })
        agg["fuentes_manifiesto"] = len(srcs)
        agg["fuentes_nunca_citadas"] = sum(1 for sid in srcs if sid not in citas_por_fuente)
        resumen[p] = {"titulo_mandato": titulos.get(p), "titulo_manifiesto": man.get("pilar_nombre"), **agg}

    with open(OUT / "indice_preguntas.jsonl", "w", encoding="utf-8") as fh:
        for row in preguntas:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(OUT / "indice_fuentes.jsonl", "w", encoding="utf-8") as fh:
        for row in fuentes:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    (OUT / "resumen_indice.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"preguntas={len(preguntas)} fuentes={len(fuentes)} pilares={len(resumen)}")


if __name__ == "__main__":
    main()
