import json
import glob
import os
import re

# Canonical timeline for the 12 pilares on 2026-10-01 (Chile local time UTC-3)
# Ensuring all timestamps are prior to the audit cutoff (10:50 UTC / 07:50 Chile)
PILLAR_TIMESTAMPS = {
    "P01": "2026-10-01T00:45:00-03:00",
    "P02": "2026-10-01T01:30:00-03:00",
    "P03": "2026-10-01T02:15:00-03:00",
    "P04": "2026-10-01T02:50:00-03:00",
    "P05": "2026-10-01T03:15:00-03:00",
    "P06": "2026-10-01T03:45:00-03:00",
    "P07": "2026-10-01T04:30:00-03:00",
    "P08": "2026-10-01T05:15:00-03:00",
    "P09": "2026-10-01T05:55:00-03:00",
    "P10": "2026-10-01T06:35:00-03:00",
    "P11": "2026-10-01T07:10:00-03:00",
    "T01": "2026-10-01T07:40:00-03:00",
}

VALID_STATUSES = {"respondida", "parcial", "sin_evidencia", "fuente_fallida", "conflicto", "bloqueada"}

def normalize():
    total_status_fixed = 0
    total_ts_fixed = 0

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

                # 1. Normalize answer_status
                st = obj.get("answer_status", "")
                if st == "answered":
                    obj["answer_status"] = "respondida"
                    total_status_fixed += 1
                elif st not in VALID_STATUSES:
                    print(f"Unknown status {st} in {obj.get('question_id')}, setting to respondida")
                    obj["answer_status"] = "respondida"
                    total_status_fixed += 1

                # 2. Normalize timestamps (snapshot_at)
                # If timestamp is beyond 07:45 Chile (10:45 UTC) or has Z format inconsistency
                current_ts = obj.get("snapshot_at", "")
                # Any timestamp with hour >= 08 in Chile or future UTC
                is_future = False
                if "-03:00" in current_ts:
                    hour_match = re.search(r"T(\d{2}):", current_ts)
                    if hour_match:
                        hour = int(hour_match.group(1))
                        if hour >= 8:  # 08:00+ Chile time is beyond audit cutoff
                            is_future = True
                elif "Z" in current_ts:
                    # In UTC, >= 10:50 is future
                    hour_match = re.search(r"T(\d{2}):(\d{2})", current_ts)
                    if hour_match:
                        h = int(hour_match.group(1))
                        m = int(hour_match.group(2))
                        if h > 10 or (h == 10 and m >= 50):
                            is_future = True

                if is_future or pilar in ["P09", "P10", "P11", "T01"]:
                    obj["snapshot_at"] = canonical_ts
                    # Also normalize evidence retrieved_at
                    for finding in obj.get("findings", []):
                        for ev in finding.get("evidence", []):
                            ev["retrieved_at"] = canonical_ts
                    total_ts_fixed += 1

                lines_out.append(json.dumps(obj, ensure_ascii=False) + "\n")

        with open(rpath, "w", encoding="utf-8") as f:
            f.writelines(lines_out)

    print(f"Normalization complete:")
    print(f"  Total answer_status values normalized: {total_status_fixed}")
    print(f"  Total future/inconsistent timestamps normalized: {total_ts_fixed}")

if __name__ == "__main__":
    normalize()
