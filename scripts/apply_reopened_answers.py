import json
import os
import re

import sys
sys.path.insert(0, ".")

from scripts.record_builder import (
    extract_canonical_questions,
    get_step_text,
    split_answers_by_qid,
    build_json_record,
    MANDATO_PATH
)

P06_STEP_MAP = {
    2219: ["P06-F01"],
    2235: ["P06-F02", "P06-F03"],
    2267: ["P06-F04", "P06-F05", "P06-F06"],
    2269: ["P06-C01", "P06-C02"],
    2271: ["P06-F07", "P06-F08", "P06-F09"],
    2273: ["P06-F10", "P06-F11", "P06-F12"],
    2275: ["P06-C03", "P06-C04"],
    2277: ["P06-F13", "P06-F14", "P06-F15"],
    2279: ["P06-F16", "P06-F17", "P06-F18"],
    2281: ["P06-C05", "P06-C06"],
    2283: ["P06-F19", "P06-F20", "P06-F21"],
    2285: ["P06-F22", "P06-F23", "P06-F24"],
    2287: ["P06-C07", "P06-C08"],
    2289: ["P06-F25", "P06-F26", "P06-F27"],
    2291: ["P06-F28", "P06-F29", "P06-F30"],
    2293: ["P06-C09", "P06-C10"],
    2295: ["P06-F31", "P06-F32", "P06-F33"],
    2297: ["P06-F34", "P06-F35", "P06-F36"],
    2299: ["P06-C11", "P06-C12"],
    2301: ["P06-F37", "P06-F38", "P06-F39"],
    2303: ["P06-F40", "P06-F41", "P06-F42"],
    2305: ["P06-C13", "P06-C14"],
    2307: ["P06-F43", "P06-F44", "P06-F45"],
    2309: ["P06-F46", "P06-F47", "P06-F48"],
    2311: ["P06-C15", "P06-C16"]
}

P01_STEP_MAP = {
    2313: ["P01-F13", "P01-F14", "P01-F15"],
    2315: ["P01-F19", "P01-F20", "P01-F21"],
    2317: ["P01-F25", "P01-F26", "P01-F27"],
    2319: ["P01-F31", "P01-F32", "P01-F33"],
    2321: ["P01-F37", "P01-F38", "P01-F39"],
    2323: ["P01-F43", "P01-F44", "P01-F45"]
}

def main():
    canonical = extract_canonical_questions(MANDATO_PATH)
    print(f"Total canonical mandate questions: {len(canonical)}")

    # 1. Build P06 new records
    p06_new_records = {}
    for step_num, qids in P06_STEP_MAP.items():
        step_text = get_step_text(step_num)
        split_dict = split_answers_by_qid(step_text, qids)
        for qid in qids:
            raw_text = split_dict.get(qid, "")
            ctext = canonical[qid]
            record = build_json_record("P06", qid, ctext, raw_text)
            p06_new_records[qid] = record

    print(f"Generated {len(p06_new_records)} authentic P06 records from NotebookLM.")

    # Apply to respuestas/P06.jsonl
    p06_out_lines = []
    with open("respuestas/P06.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            obj = json.loads(line)
            qid = obj.get("question_id")
            if qid in p06_new_records:
                p06_out_lines.append(json.dumps(p06_new_records[qid], ensure_ascii=False) + "\n")
            else:
                # X01..X32: ensure canonical question text is exact
                if qid in canonical:
                    obj["question_text"] = canonical[qid]
                p06_out_lines.append(json.dumps(obj, ensure_ascii=False) + "\n")

    with open("respuestas/P06.jsonl", "w", encoding="utf-8") as f:
        f.writelines(p06_out_lines)
    print("Updated respuestas/P06.jsonl successfully.")

    # 2. Build P01 new records
    p01_new_records = {}
    for step_num, qids in P01_STEP_MAP.items():
        step_text = get_step_text(step_num)
        split_dict = split_answers_by_qid(step_text, qids)
        for qid in qids:
            raw_text = split_dict.get(qid, "")
            ctext = canonical[qid]
            record = build_json_record("P01", qid, ctext, raw_text)
            p01_new_records[qid] = record

    print(f"Generated {len(p01_new_records)} authentic P01 records from NotebookLM.")

    # Apply to respuestas/P01.jsonl
    p01_out_lines = []
    with open("respuestas/P01.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            obj = json.loads(line)
            qid = obj.get("question_id")
            if qid in p01_new_records:
                p01_out_lines.append(json.dumps(p01_new_records[qid], ensure_ascii=False) + "\n")
            else:
                # Update question_text to canonical for all other P01 questions
                if qid in canonical:
                    obj["question_text"] = canonical[qid]
                p01_out_lines.append(json.dumps(obj, ensure_ascii=False) + "\n")

    with open("respuestas/P01.jsonl", "w", encoding="utf-8") as f:
        f.writelines(p01_out_lines)
    print("Updated respuestas/P01.jsonl successfully.")

    # 3. Update P02-C01, P02-C02
    p02_out_lines = []
    with open("respuestas/P02.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            obj = json.loads(line)
            qid = obj.get("question_id")
            if qid in canonical:
                obj["question_text"] = canonical[qid]
            p02_out_lines.append(json.dumps(obj, ensure_ascii=False) + "\n")
    with open("respuestas/P02.jsonl", "w", encoding="utf-8") as f:
        f.writelines(p02_out_lines)
    print("Updated respuestas/P02.jsonl canonical question texts.")

    # 4. Update P11-C01, P11-C02
    p11_out_lines = []
    with open("respuestas/P11.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            obj = json.loads(line)
            qid = obj.get("question_id")
            if qid in canonical:
                obj["question_text"] = canonical[qid]
            p11_out_lines.append(json.dumps(obj, ensure_ascii=False) + "\n")
    with open("respuestas/P11.jsonl", "w", encoding="utf-8") as f:
        f.writelines(p11_out_lines)
    print("Updated respuestas/P11.jsonl canonical question texts.")

if __name__ == "__main__":
    main()
