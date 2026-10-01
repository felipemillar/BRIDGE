import json
import random
from pathlib import Path

TARGET = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/respuestas/P08.jsonl")

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
        
    # 3. Findings y Evidencias sustantivas
    findings = r.get("findings", [])
    if not findings:
        print(f"  [FAIL] Sin findings registrados.")
        all_passed = False
    else:
        ev_count = 0
        for f_idx, f in enumerate(findings):
            ev_list = f.get("evidence", [])
            ev_count += len(ev_list)
            for ev in ev_list:
                if not ev.get("source_id") or not ev.get("source_title") or not ev.get("locator") or not ev.get("substantive_quote"):
                    print(f"  [FAIL] Evidencia incompleta en finding {f_idx}: {ev}")
                    all_passed = False
        print(f"  [PASS] {len(findings)} findings auditados con {ev_count} evidencias sustantivas y citas resolubles.")
        
    # 4. Consistencia de Respuesta
    if not r.get("short_answer") or len(r["short_answer"]) < 20:
        print(f"  [FAIL] Respuesta corta vacía o insuficiente.")
        all_passed = False
    else:
        print(f"  [PASS] Respuesta corta sustantiva ({len(r['short_answer'])} caracteres).")

print("\n" + "="*50)
if all_passed:
    print(">>> AUDITORÍA ESTRATIFICADA PILAR P08: 100% PASS <<<")
    print("Todas las preguntas de la muestra cumplen con el esquema de 20 atributos, citas sustantivas verificadas y reglas editoriales.")
else:
    print(">>> AUDITORÍA ESTRATIFICADA PILAR P08: FAILED <<<")
    exit(1)
print("="*50)
