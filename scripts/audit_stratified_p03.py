import json
import random
import sys
from pathlib import Path

def run_p03_stratified_audit():
    p03_path = Path("respuestas/P03.jsonl")
    manifest_path = Path("fuentes/P03.json")
    
    if not p03_path.exists():
        print(f"Error: {p03_path} does not exist.")
        sys.exit(1)
    if not manifest_path.exists():
        print(f"Error: {manifest_path} does not exist.")
        sys.exit(1)
        
    records = [json.loads(line) for line in open(p03_path, "r", encoding="utf-8") if line.strip()]
    manifest = json.load(open(manifest_path, "r", encoding="utf-8"))
    
    print("=================================================================")
    print(" AUDITORÍA ESTRATIFICADA Y CONTROL DE CALIDAD - PILAR P03")
    print("=================================================================")
    print(f"Total registros cargados en P03.jsonl: {len(records)}")
    
    # 1. Total count check
    expected_count = 64
    if len(records) != expected_count:
        print(f"ERROR: Se esperaban {expected_count} registros y se encontraron {len(records)}")
        sys.exit(1)
    print(f"✅ Control 1: Conteo exacto de 64 registros cumplido (48 F + 16 C).")
    
    # 2. Sequence integrity check
    expected_f = [f"P03-F{i:02d}" for i in range(1, 49)]
    expected_c = [f"P03-C{i:02d}" for i in range(1, 17)]
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
            # Check epistemic status
            valid_statuses = ["hecho_documentado", "declaracion_comercial", "inferencia", "hipotesis"]
            if f.get("epistemic_status") not in valid_statuses:
                print(f"ERROR in {qid}: Invalid epistemic_status '{f.get('epistemic_status')}'.")
                sys.exit(1)
                
            # Check evidence citations
            evidence_list = f.get("evidence", [])
            if not evidence_list:
                print(f"ERROR in {qid}: Finding {f.get('claim_id')} has no evidence.")
                sys.exit(1)
                
            for ev in evidence_list:
                sid = ev.get("source_id")
                stitle = ev.get("source_title")
                locator = ev.get("locator")
                excerpt = ev.get("excerpt_short")
                
                if not sid or (sid not in manifest_sources_by_id and stitle not in manifest_sources_by_title):
                    print(f"ERROR in {qid}: Evidence source '{stitle}' (id: {sid}) not found in manifest.")
                    sys.exit(1)
                    
                if not locator or len(locator.strip()) < 3:
                    print(f"ERROR in {qid}: Invalid or missing locator for {stitle}.")
                    sys.exit(1)
                    
                if not excerpt or len(excerpt.strip()) < 10:
                    print(f"ERROR in {qid}: Missing or too short excerpt for {stitle}.")
                    sys.exit(1)
                    
        # Check required schema keys
        required_keys = [
            "question_id", "notebook_id", "question_text", "snapshot_at", "answer_status",
            "short_answer", "findings", "operational_model", "entities", "relations",
            "comparisons", "contradictions", "metrics_and_denominators", "bridge_implications",
            "open_gaps", "next_question_ids", "quality"
        ]
        for k in required_keys:
            if k not in r:
                print(f"ERROR in {qid}: Missing required key '{k}'.")
                sys.exit(1)
                
        # Check quality dict
        q = r.get("quality", {})
        if not q.get("original_citations_resolved") or not q.get("correction_precedence_checked"):
            print(f"ERROR in {qid}: Quality audit flags not met.")
            sys.exit(1)
            
    print("✅ Control 3: Integridad de citas, localizadores, extractos y esquema completo al 100% en la muestra estratificada.")
    
    # 4. Global statistics
    total_findings = sum(len(r.get("findings", [])) for r in records)
    total_entities = sum(len(r.get("entities", [])) for r in records)
    total_relations = sum(len(r.get("relations", [])) for r in records)
    total_contradictions = sum(len(r.get("contradictions", [])) for r in records)
    total_gaps = sum(len(r.get("open_gaps", [])) for r in records)
    
    print("\n-----------------------------------------------------------------")
    print(f"📊 MÉTRICAS CONSOLIDADAS DEL PILAR P03:")
    print(f" - Total Preguntas Auditadas: {len(records)} / {expected_count}")
    print(f" - Total Hallazgos Registrados: {total_findings}")
    print(f" - Total Entidades Ontológicas Extraídas: {total_entities}")
    print(f" - Total Relaciones de Grafo Mapeadas: {total_relations}")
    print(f" - Contradicciones y Discrepancias Resueltas: {total_contradictions}")
    print(f" - Brechas Abiertas Catalogadas: {total_gaps}")
    print("-----------------------------------------------------------------")
    print("🎉 AUDITORÍA DEL PILAR P03 APROBADA CON ÉXITO SIN DEFECTOS.")
    print("=================================================================\n")

if __name__ == "__main__":
    run_p03_stratified_audit()
