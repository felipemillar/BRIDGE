import json
import sys
from pathlib import Path

def append_response(jsonl_path: str, record: dict):
    path = Path(jsonl_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Ensure UTF-8 single line JSON
    line = json.dumps(record, ensure_ascii=False)
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Appended {record.get('question_id')} to {jsonl_path}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        target_path = sys.argv[1]
        data = json.loads(sys.argv[2])
        append_response(target_path, data)
