import re
import json
import glob
import os

MANDATO_PATH = "docs_mandato/mandato-antigravity-investigacion-asuntos-corporativos.md"
RESPUESTAS_DIR = "/Users/fmillar/Proyectos_Desarrollo/BRIDGE/respuestas"

def extract_canonical_questions(mandato_path):
    questions = {}
    with open(mandato_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern matches: - **P01-F01.** ¿Qué decisiones...
    # or - **P01-F01:** ¿Qué decisiones...
    pattern = re.compile(r"^[-*]\s+\*\*([PT]\d{2}-[FCX]\d{2})[\.:]\*\*\s*(.*)$", re.MULTILINE)
    for match in pattern.finditer(content):
        qid = match.group(1).strip()
        qtext = match.group(2).strip()
        questions[qid] = qtext
    return questions

def load_stored_questions(respuestas_dir):
    stored = {}
    for filepath in sorted(glob.glob(os.path.join(respuestas_dir, "*.jsonl"))):
        with open(filepath, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                    qid = obj.get("question_id")
                    stored[qid] = {
                        "file": os.path.basename(filepath),
                        "line": line_no,
                        "question_text": obj.get("question_text", ""),
                        "short_answer": obj.get("short_answer", ""),
                        "answer_status": obj.get("answer_status", ""),
                        "raw_obj": obj
                    }
                except Exception as err:
                    print(f"Error parsing json in {filepath}:{line_no}: {type(err).__name__} (detalles omitidos por seguridad)")
    return stored

def main():
    canonical = extract_canonical_questions(MANDATO_PATH)
    print(f"Total canonical questions extracted from mandate: {len(canonical)}")

    stored = load_stored_questions(RESPUESTAS_DIR)
    print(f"Total stored questions in respuestas/*.jsonl: {len(stored)}")

    diffs = []
    by_pilar = {}

    for qid, ctext in sorted(canonical.items()):
        pilar = qid.split("-")[0]
        by_pilar.setdefault(pilar, {"total": 0, "diffs": 0, "divergent": []})
        by_pilar[pilar]["total"] += 1

        if qid not in stored:
            by_pilar[pilar]["diffs"] += 1
            by_pilar[pilar]["divergent"].append({"qid": qid, "type": "MISSING", "canonical": ctext})
            diffs.append({"qid": qid, "type": "MISSING", "canonical": ctext})
            continue

        stext = stored[qid]["question_text"]
        if stext != ctext:
            by_pilar[pilar]["diffs"] += 1
            divergence_info = {
                "qid": qid,
                "type": "TEXT_DIFF",
                "canonical": ctext,
                "stored": stext,
                "stored_short_answer": stored[qid]["short_answer"][:120] + "..." if stored[qid]["short_answer"] else "",
                "status": stored[qid]["answer_status"]
            }
            by_pilar[pilar]["divergent"].append(divergence_info)
            diffs.append(divergence_info)

    print(f"\nTotal differences found: {len(diffs)}")
    print("\nBreakdown by pilar:")
    for pilar, stats in sorted(by_pilar.items()):
        print(f"  {pilar}: {stats['diffs']}/{stats['total']} divergent")

    # Save details to analysis file
    out_path = "scripts/audit_question_diffs.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(diffs, f, indent=2, ensure_ascii=False)
    print(f"\nDetailed diffs written to {out_path}")

if __name__ == "__main__":
    main()
