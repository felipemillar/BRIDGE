import json
import random
import sys
from pathlib import Path

def run_p04_stratified_audit():
    p04_path = Path("respuestas/P04.jsonl")
    manifest_path = Path("fuentes/P04.json")
    
    if not p04_path.exists():
        print(f"Error: {p04_path} does not exist.")
        sys.exit(1)
    if not manifest_path.exists():
        print(f"Error: {manifest_path} does not exist.")
        sys.exit(1)
        
    records = [json.loads(line) for line in open(p04_path, "r", encoding="utf-8") if line.strip()]
    manifest = json.load(open(manifest_path, "r", encoding="utf-8"))
    
    print("=================================================================")
    print(" AUDITORÍA ESTRATIFICADA Y CONTROL DE CALIDAD - PILAR P04")
    print("=================================================================")
    print(f"Total registros cargados en P04.jsonl: {len(records)}")
    
    # 1. Total count check
    expected_count = 64
    if len(records) != expected_count:
        print(f"ERROR: Se esperaban {expected_count} registros y se encontraron {len(records)}")
        sys.exit(1)
    print(f"✅ Control 1: Conteo exacto de 64 registros cumplido (48 F + 16 C).")
    
    # 2. Sequence integrity check
    expected_f = [f"P04-F{i:02d}" for i in range(1, 49)]
    expected_c = [f"P04-C{i:02d}" for i in range(1, 17)]
    expected_ids = expected_f + expected_c
    
    actual_ids = [r["question_id"] for r in records]
    if actual_ids != expected_ids:
        print("ERROR: La secuencia de IDs no coincide exactamente con el orden F->C.")
        missing = set(expected_ids) - set(actual_ids)
        extra = set(actual_ids) - set(expected_ids)
        print(f"Faltantes: {missing}, Extras: {extra}")
        sys.exit(1)
    print("✅ Control 2: Secuencia exacta F01..F48 -> C01..C16 sin saltos ni duplicados.")
    
    # 3. Stratified sample (at least 10% = 7 records across F and C)
    random.seed(42)  # For deterministic reproducibility
    sample_f = random.sample(records[:48], 5)
    sample_c = random.sample(records[48:64], 2)
    sample = sample_f + sample_c
    sample_ids = [r["question_id"] for r in sample]
    print(f"\n✅ Muestra estratificada del 10%+ ({len(sample)} registros seleccionados): {sample_ids}")
    
    # Audit each sampled record
    manifest_sources_by_id = {s.get("source_id"): s for s in manifest.get("sources", [])}
    manifest_sources_by_title = {s.get("title"): s for s in manifest.get("sources", [])}
    
    for r in sample:
        qid = r["question_id"]
        findings = r.get("findings", [])
        if not findings:
            print(f"ERROR in {qid}: No findings found.")
            sys.exit(1)
            
        for f in findings:
            valid_statuses = ["hecho_documentado", "declaracion_comercial", "inferencia", "hipotesis"]
            if f.get("epistemic_status") not in valid_statuses:
                print(f"ERROR in {qid}: Invalid epistemic_status '{f.get('epistemic_status')}'.")
                sys.exit(1)
                
            evidence = f.get("evidence", [])
            if not evidence:
                print(f"ERROR in {qid}: No evidence attached to finding {f.get('claim_id')}.")
                sys.exit(1)
                
            for ev in evidence:
                sid = ev.get("source_id")
                stitle = ev.get("source_title")
                locator = ev.get("locator")
                excerpt = ev.get("excerpt_short")
                
                if not sid or not stitle or not locator or not excerpt:
                    print(f"ERROR in {qid}: Incomplete evidence tuple: sid={sid}, stitle={stitle}, loc={locator}")
                    sys.exit(1)
                    
                # Match against manifest
                match = manifest_sources_by_id.get(sid) or manifest_sources_by_title.get(stitle)
                if not match:
                    print(f"ERROR in {qid}: Source {sid} ('{stitle}') not found in manifest P04.json.")
                    sys.exit(1)
                    
        # Verify schema core attributes
        required_attrs = ["operational_model", "entities", "relations", "bridge_implications", "quality", "next_question_ids"]
        for attr in required_attrs:
            if attr not in r:
                print(f"ERROR in {qid}: Missing required schema attribute '{attr}'.")
                sys.exit(1)
                
        # If contrast question, check open_gaps
        if qid.startswith("P04-C"):
            if "open_gaps" not in r:
                print(f"ERROR in {qid}: Contrast question must define open_gaps.")
                sys.exit(1)
                
        print(f"  - {qid}: Validado correctamente (Claims: {len(findings)}, Evidencia cruzada con P04.json).")
        
    print("\n=================================================================")
    print(" RESULTADO AUDITORÍA ESTRATIFICADA P04: 100% APROBADO")
    print("=================================================================")
    return True

if __name__ == "__main__":
    run_p04_stratified_audit()
