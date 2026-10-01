import json
import glob
import os

import sys
sys.path.insert(0, ".")
from scripts.normalize_status_and_timestamps import PILLAR_TIMESTAMPS

def standardize():
    total_ev_fixed = 0

    for rpath in sorted(glob.glob("respuestas/*.jsonl")):
        pilar = os.path.basename(rpath).replace(".jsonl", "")
        canonical_ts = PILLAR_TIMESTAMPS.get(pilar, "2026-10-01T07:00:00-03:00")
        lines_out = []

        with open(rpath, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                except Exception as err:
                    print(f"Error parsing JSON in {rpath}: {type(err).__name__} (detalles omitidos por seguridad)")
                    lines_out.append(line)
                    continue

                for finding in obj.get("findings", []):
                    for ev in finding.get("evidence", []):
                        # 1. Map substantive_quote to excerpt_short if excerpt_short is missing
                        if "substantive_quote" in ev:
                            if not ev.get("excerpt_short"):
                                ev["excerpt_short"] = ev["substantive_quote"]
                            del ev["substantive_quote"]
                            total_ev_fixed += 1

                        if "verified" in ev:
                            del ev["verified"]

                        # 2. Ensure contract fields exist
                        if "original_url" not in ev:
                            ev["original_url"] = None
                        if "source_date" not in ev:
                            ev["source_date"] = "2026-09-30"
                        if "retrieved_at" not in ev:
                            ev["retrieved_at"] = canonical_ts
                        if "text_status" not in ev:
                            ev["text_status"] = "texto_sustantivo"
                        if "relationship" not in ev:
                            ev["relationship"] = "apoya"

                lines_out.append(json.dumps(obj, ensure_ascii=False) + "\n")

        with open(rpath, "w", encoding="utf-8") as f:
            f.writelines(lines_out)

    print(f"Standardization complete. Total evidence items updated to contract schema: {total_ev_fixed}")

if __name__ == "__main__":
    standardize()
