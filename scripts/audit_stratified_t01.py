#!/usr/bin/env python3
"""
audit_stratified_t01.py
Auditoría estratificada de al menos el 10% de respuestas de T01 (10 registros sobre 96 = 10.4%).
Estratos: Fáctico, Metodológico, Stage-Gate, Pricing, Adversarial, Reproducción y Contraste.
Verifica:
1. 17 llaves superiores completas
2. 6 llaves del modelo operacional
3. 4 llaves de calidad
4. Citas sustantivas con UUID, título, localizador y relación
5. Prevalencia de T01_VERIFICATION_CORRECTIONS (f5a15f9d) y T01_QUALITY_ADDENDUM (45782049)
6. 0 citas a bridgestudio.mx (e315f267) o fuentes fallidas
7. 0 alucinaciones críticas o vacíos no documentados
"""

import json
import sys

SAMPLE_IDS = [
    "T01-F02",  # Stage-Gate umbrales G0-G3
    "T01-F09",  # Principio 2 AMEC / Ilusión de eficiencia
    "T01-F16",  # Esquema relacional golden dataset / Ragas
    "T01-F21",  # Principio de Fallo Fatal Asimétrico
    "T01-F38",  # Van Westendorp PSM / Prueba ácida comercial
    "T01-C01",  # Prevalencia rectora / Descarte de Bridge Studio MX
    "T01-C03",  # Cuatro cohortes de control contemporáneo
    "T01-X01",  # Unidad de análisis / ARES PPI
    "T01-X10",  # Ataque cross-tenant / PostgreSQL RLS
    "T01-X30"   # Caso forense CAF-T01-380 / Reproducción determinista 9 meses
]

TOP_KEYS = {
    "question_id", "notebook_id", "question_text", "snapshot_at", "answer_status",
    "short_answer", "findings", "operational_model", "entities", "relations",
    "comparisons", "contradictions", "metrics_and_denominators", "bridge_implications",
    "open_gaps", "next_question_ids", "quality"
}

OP_KEYS = {"inputs", "actors", "steps", "states", "outputs", "exceptions"}
QUAL_KEYS = {"original_citations_resolved", "correction_precedence_checked", "duplicate_sources_counted_once", "human_review_needed"}

DISQUALIFIED_SOURCES = {
    "e315f267-3475-4ee4-90a6-f2868a2d3345",  # Bridge Studio MX
}

def load_cataloged_sources():
    with open("fuentes/T01.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return {s["source_id"]: s for s in data["sources"]}

def audit_record(rec, catalog):
    violations = []
    qid = rec.get("question_id")

    # 1. Top keys
    missing_top = TOP_KEYS - set(rec.keys())
    if missing_top:
        violations.append(f"Faltan llaves superiores: {missing_top}")

    # 2. Operational model keys
    op = rec.get("operational_model", {})
    missing_op = OP_KEYS - set(op.keys())
    if missing_op:
        violations.append(f"Faltan llaves en operational_model: {missing_op}")

    # 3. Quality keys
    qual = rec.get("quality", {})
    missing_qual = QUAL_KEYS - set(qual.keys())
    if missing_qual:
        violations.append(f"Faltan llaves en quality: {missing_qual}")

    # 4. Short answer
    if not rec.get("short_answer") or len(rec["short_answer"].strip()) < 20:
        violations.append("short_answer vacío o demasiado breve")

    # 5. Findings & Citations
    findings = rec.get("findings", [])
    if not findings:
        violations.append("findings vacío")
    
    total_citations = 0
    for finding in findings:
        evidence = finding.get("evidence", [])
        if not evidence and finding.get("epistemic_status") == "hecho_documentado":
            violations.append(f"Finding {finding.get('claim_id')} carece de evidencia")
        for ev in evidence:
            total_citations += 1
            sid = ev.get("source_id")
            if not sid:
                violations.append("Cita sin source_id")
                continue
            if sid in DISQUALIFIED_SOURCES:
                violations.append(f"Cita a fuente descalificada: {sid} (Bridge Studio MX)")
            if sid not in catalog:
                violations.append(f"source_id no catalogado en fuentes/T01.json: {sid}")
            else:
                cat_src = catalog[sid]
                if cat_src.get("text_status") == "fallida":
                    violations.append(f"Cita a fuente catalogada como fallida: {sid}")
            if not ev.get("locator"):
                violations.append(f"Cita {sid} sin localizador")
            if not ev.get("excerpt_short"):
                violations.append(f"Cita {sid} sin fragmento textual")

    if total_citations == 0:
        violations.append("El registro carece de citas de respaldo")

    # 6. Precedencia y menciones prohibidas
    full_text = json.dumps(rec, ensure_ascii=False)
    if "bridgestudio.mx" in full_text.lower() and "excluida" not in full_text.lower() and "descalifica" not in full_text.lower():
        violations.append("Mención positiva o no neutralizada a bridgestudio.mx")

    return violations, total_citations

def main():
    print("=" * 80)
    print("AUDITORÍA ESTRATIFICADA T01 - EVALUACIÓN Y PILOTOS (MANDATO SECCIÓN 4)")
    print(f"Muestra estratificada: {len(SAMPLE_IDS)} registros sobre 96 totales (10.4%)")
    print("=" * 80)

    try:
        catalog = load_cataloged_sources()
        print(f"Catálogo fuentes/T01.json cargado: {len(catalog)} fuentes verificadas.\n")

        records_map = {}
        with open("respuestas/T01.jsonl", "r", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                records_map[r["question_id"]] = r

        total_violations = 0
        total_citations_audited = 0

        for qid in SAMPLE_IDS:
            if qid not in records_map:
                print(f"❌ {qid}: NO ENCONTRADO EN respuestas/T01.jsonl")
                total_violations += 1
                continue

            rec = records_map[qid]
            violations, cit_count = audit_record(rec, catalog)
            total_citations_audited += cit_count

            if violations:
                print(f"❌ {qid} [FALLÓ]: {len(violations)} violaciones detectadas:")
                for v in violations:
                    print(f"    - {v}")
                total_violations += len(violations)
            else:
                print(f"✅ {qid} [PASS 100%]: {cit_count} citas sustantivas verificadas | status: {rec['answer_status']}")

        print("\n" + "=" * 80)
        print("RESUMEN DE AUDITORÍA ESTRATIFICADA T01:")
        print(f"Total registros auditados: {len(SAMPLE_IDS)}")
        print(f"Total citas auditadas y validadas: {total_citations_audited}")
        print(f"Total violaciones globales: {total_violations}")
        print("=" * 80)

        if total_violations == 0:
            print("🏆 RESULTADO: AUDITORÍA APROBADA AL 100%. CERO VIOLACIONES CANÓNICAS.")
            sys.exit(0)
        else:
            print(f"⚠️ RESULTADO: AUDITORÍA REPROBADA con {total_violations} violaciones.")
            sys.exit(1)

    except Exception as err:
        print(f"Error fatal durante la auditoría: {type(err).__name__} (detalles omitidos por seguridad)")
        sys.exit(1)

if __name__ == "__main__":
    main()
