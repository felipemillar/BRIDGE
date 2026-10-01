import json
import random
from pathlib import Path

TARGET = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/respuestas/P11.jsonl")

with open(TARGET, "r", encoding="utf-8") as f:
    lines = [json.loads(line) for line in f if line.strip()]

print(f"Total registros cargados en {TARGET}: {len(lines)}")
assert len(lines) == 64, f"Se esperaban 64 registros, encontrados {len(lines)}"

f_records = [r for r in lines if "-F" in r["question_id"]]
c_records = [r for r in lines if "-C" in r["question_id"]]

print(f"Preguntas Fundamentales (F): {len(f_records)}")
print(f"Preguntas de Contraste (C): {len(c_records)}")

assert len(f_records) == 48, f"Se esperaban 48 F, encontrados {len(f_records)}"
assert len(c_records) == 16, f"Se esperaban 16 C, encontrados {len(c_records)}"

# Verificación de unicidad de IDs
ids = [r["question_id"] for r in lines]
assert len(ids) == len(set(ids)), "Existen IDs duplicados en el archivo"

# Verificación global de reglas canónicas en todos los registros
DISQUALIFIED_WIPO_ID = "4caa2cda"
HTML_OPENAI_IDS = ["0a6b1eb9", "055a3999"]
for r in lines:
    qid = r["question_id"]
    for finding in r.get("findings", []):
        for ev in finding.get("evidence", []):
            sid = ev.get("source_id", "")
            if DISQUALIFIED_WIPO_ID in sid:
                raise ValueError(f"Violación canónica en {qid}: WIPO Lex ({sid}) citada como fuente sustantiva!")
            for hid in HTML_OPENAI_IDS:
                if hid in sid:
                    raise ValueError(f"Violación canónica en {qid}: HTML no oficial de OpenAI ({sid}) citado en lugar de PDF canónico!")

print("✅ Verificación canónica global de 64 registros superada: 0 citas a WIPO Lex, 0 citas a HTMLs reemplazados.")

# Muestreo estratificado de 10%+ (7 registros: 5 F + 2 C)
random.seed(42)  # semilla reproducible
sample_f = random.sample(f_records, 5)
sample_c = random.sample(c_records, 2)
sample = sample_f + sample_c

print(f"\nMuestra estratificada seleccionada (7 preguntas / 10.9%): {[r['question_id'] for r in sample]}\n")

required_top_keys = [
    "question_id", "notebook_id", "question_text", "snapshot_at",
    "answer_status", "short_answer", "findings", "operational_model",
    "entities", "relations", "comparisons", "contradictions",
    "metrics_and_denominators", "bridge_implications", "open_gaps",
    "next_question_ids", "quality"
]

required_quality_keys = [
    "original_citations_resolved", "correction_precedence_checked",
    "duplicate_sources_counted_once", "human_review_needed"
]

required_op_keys = [
    "inputs", "actors", "steps", "states", "outputs", "exceptions"
]

all_passed = True
for r in sample:
    qid = r["question_id"]
    print(f"--- Auditando {qid} ---")
    
    # 1. Esquema top-level
    missing_top = [k for k in required_top_keys if k not in r]
    if missing_top:
        print(f"  [FAIL] Claves faltantes top-level: {missing_top}")
        all_passed = False
    else:
        print(f"  [PASS] Esquema top-level completo (17 claves).")
        
    # 2. Esquema quality
    missing_qual = [k for k in required_quality_keys if k not in r.get("quality", {})]
    if missing_qual:
        print(f"  [FAIL] Claves faltantes en quality: {missing_qual}")
        all_passed = False
    else:
        print(f"  [PASS] Bloque quality completo (4 claves).")
        
    # 3. Operational Model
    op_model = r.get("operational_model", {})
    missing_op = [k for k in required_op_keys if k not in op_model]
    if missing_op:
        print(f"  [FAIL] Claves faltantes en operational_model: {missing_op}")
        all_passed = False
    else:
        print(f"  [PASS] Operational model completo (6 claves).")
        
    # 4. Findings y Citas
    findings = r.get("findings", [])
    if not findings:
        print(f"  [FAIL] Sin findings registrados.")
        all_passed = False
    else:
        ev_count = sum(len(f.get("evidence", [])) for f in findings)
        quotes_ok = all(len(ev.get("substantive_quote", "").strip()) > 15 for f in findings for ev in f.get("evidence", []))
        uuids_ok = all(len(ev.get("source_id", "").strip()) >= 8 for f in findings for ev in f.get("evidence", []))
        if ev_count > 0 and quotes_ok and uuids_ok:
            print(f"  [PASS] Findings y evidencias robustas ({len(findings)} claims, {ev_count} evidencias citadas con citas sustantivas y UUIDs).")
        else:
            print(f"  [FAIL] Evidencias deficientes (quotes_ok={quotes_ok}, uuids_ok={uuids_ok}).")
            all_passed = False
            
    # 5. Longitud y completitud de respuesta directa
    short_ans = r.get("short_answer", "")
    if len(short_ans) < 100:
        print(f"  [FAIL] Respuesta directa demasiado corta ({len(short_ans)} caracteres).")
        all_passed = False
    else:
        print(f"  [PASS] Respuesta directa exhaustiva ({len(short_ans)} caracteres).")

print("\n==========================================")
if all_passed:
    print("🏆 RESULTADO AUDITORÍA ESTRATIFICADA P11: 100% PASS (7/7 registros aprobados)")
else:
    print("❌ RESULTADO AUDITORÍA ESTRATIFICADA P11: FALLÓ")
print("==========================================")

assert all_passed, "La auditoría estratificada de P11 no pasó el 100% de los controles."
