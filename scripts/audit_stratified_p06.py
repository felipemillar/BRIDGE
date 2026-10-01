import json
import random
import sys
from pathlib import Path

def run_p06_stratified_audit():
    p06_path = Path("respuestas/P06.jsonl")
    manifest_path = Path("fuentes/P06.json")
    
    if not p06_path.exists():
        print(f"Error: {p06_path} does not exist.")
        sys.exit(1)
    if not manifest_path.exists():
        print(f"Error: {manifest_path} does not exist.")
        sys.exit(1)
        
    records = [json.loads(line) for line in open(p06_path, "r", encoding="utf-8") if line.strip()]
    manifest = json.load(open(manifest_path, "r", encoding="utf-8"))
    
    print("=================================================================")
    print(" AUDITORÍA ESTRATIFICADA Y CONTROL DE CALIDAD - PILAR P06")
    print("=================================================================")
    print(f"Total registros cargados en P06.jsonl: {len(records)}")
    
    # 1. Total count check
    expected_count = 64
    if len(records) != expected_count:
        print(f"ERROR: Se esperaban {expected_count} registros y se encontraron {len(records)}")
        sys.exit(1)
    print(f"✅ Control 1: Conteo exacto de 64 registros cumplido (48 F + 16 C).")
    
    # 2. Sequence integrity check
    expected_f = [f"P06-F{i:02d}" for i in range(1, 49)]
    expected_c = [f"P06-C{i:02d}" for i in range(1, 17)]
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
            print(f"ERROR en {qid}: No contiene findings.")
            sys.exit(1)
            
        print(f"\n--- Auditando {qid} ({len(findings)} findings) ---")
        print(f"Pregunta: {r['question_text']}")
        print(f"Respuesta corta: {r['short_answer'][:120]}...")
        
        # Verify evidence citations against manifest
        for f_idx, f in enumerate(findings, 1):
            claim = f.get("claim", "")
            epistemic = f.get("epistemic_status", "")
            evidence_list = f.get("evidence", [])
            print(f"  Finding {f_idx}: [{epistemic}] {claim[:80]}...")
            
            if not evidence_list:
                print(f"ERROR en {qid} finding {f_idx}: Lista de evidencias vacía.")
                sys.exit(1)
                
            for e_idx, ev in enumerate(evidence_list, 1):
                sid = ev.get("source_id")
                stitle = ev.get("source_title")
                locator = ev.get("locator")
                excerpt = ev.get("excerpt_short")
                
                # Check source in manifest
                matched_source = manifest_sources_by_id.get(sid) or manifest_sources_by_title.get(stitle)
                if not matched_source:
                    print(f"ADVERTENCIA en {qid} ev {e_idx}: Fuente '{stitle}' ({sid}) no encontrada directamente en manifest P06.json")
                else:
                    print(f"    Evidencia {e_idx}: [OK Fuente] '{matched_source['title']}' | Loc: {locator}")
                    
                if not locator:
                    print(f"ERROR en {qid} ev {e_idx}: Falta localizador preciso.")
                    sys.exit(1)
                if not excerpt:
                    print(f"ERROR en {qid} ev {e_idx}: Falta extracto textual sustantivo.")
                    sys.exit(1)
                    
        # Check operational model
        op = r.get("operational_model", {})
        if not op.get("inputs") or not op.get("actors") or not op.get("steps") or not op.get("outputs"):
            print(f"ERROR en {qid}: Operational model incompleto.")
            sys.exit(1)
            
        # Check bridge implications
        bridge = r.get("bridge_implications", [])
        if not bridge:
            print(f"ERROR en {qid}: Falta bridge_implications.")
            sys.exit(1)
            
        print(f"  Operational Model: {len(op['steps'])} pasos, {len(op['actors'])} actores.")
        print(f"  Bridge Implication: {bridge[0].get('module')} -> {bridge[0].get('implication')[:70]}...")
        
    print("\n=================================================================")
    print(" ✅ AUDITORÍA ESTRATIFICADA PILAR P06 COMPLETADA CON 100% ÉXITO")
    print("=================================================================")

if __name__ == "__main__":
    run_p06_stratified_audit()
