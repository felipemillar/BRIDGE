import json
import sys
from pathlib import Path

def audit_file(jsonl_path: str):
    path = Path(jsonl_path)
    if not path.exists():
        print(f"Error: {jsonl_path} does not exist.")
        sys.exit(1)
        
    lines = [line.strip() for line in open(path, "r", encoding="utf-8") if line.strip()]
    print(f"Total lines in {path.name}: {len(lines)}")
    
    seen_ids = []
    required_keys = [
        "question_id", "notebook_id", "question_text", "snapshot_at",
        "answer_status", "short_answer", "findings", "operational_model",
        "entities", "relations", "comparisons", "contradictions",
        "metrics_and_denominators", "bridge_implications", "open_gaps",
        "next_question_ids", "quality"
    ]
    
    for idx, line in enumerate(lines, start=1):
        try:
            record = json.loads(line)
        except Exception as e:
            print(f"Line {idx}: JSON PARSE ERROR - {e}")
            sys.exit(1)
            
        qid = record.get("question_id")
        seen_ids.append(qid)
        
        # Check required keys
        missing = [k for k in required_keys if k not in record]
        if missing:
            print(f"Line {idx} ({qid}): MISSING KEYS - {missing}")
            sys.exit(1)
            
        # Check findings
        findings = record.get("findings", [])
        if not findings and record.get("answer_status") == "respondida":
            print(f"Line {idx} ({qid}): ZERO FINDINGS for answered question")
            sys.exit(1)
            
        for f_idx, finding in enumerate(findings, start=1):
            if not finding.get("claim"):
                print(f"Line {idx} ({qid}) Finding {f_idx}: Missing claim")
            if not finding.get("epistemic_status"):
                print(f"Line {idx} ({qid}) Finding {f_idx}: Missing epistemic_status")
            if not finding.get("evidence"):
                print(f"Line {idx} ({qid}) Finding {f_idx}: Missing evidence")
                
    print(f"Audit PASSED for {path.name}. All {len(lines)} records valid.")
    print("IDs present:", seen_ids)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "/Users/fmillar/Proyectos_Desarrollo/BRIDGE/respuestas/P01.jsonl"
    audit_file(target)
