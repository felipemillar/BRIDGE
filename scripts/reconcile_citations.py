import json
import glob
import os

def load_manifests():
    manifests = {}
    for mpath in sorted(glob.glob("fuentes/*.json")):
        pilar = os.path.basename(mpath).replace(".json", "")
        with open(mpath, "r", encoding="utf-8") as f:
            mdata = json.load(f)
        sources = mdata.get("sources", mdata.get("fuentes", []))
        manifests[pilar] = {
            "by_id": {s.get("source_id") or s.get("id"): s for s in sources},
            "by_title": {s.get("title").strip().lower(): s for s in sources},
            "raw_sources": sources
        }
    return manifests

# Specific explicit mappings for the 31 orphans and fuzzy title mismatches
P01_ORPHAN_MAP = {
    "902d5a37-56ef-46c5-8fdf-97305943b0d2": {
        "source_id": "11566961-aace-42d0-bdcc-6b9171cecded",
        "source_title": "Dircom - El Estado de la Comunicación en España (ECE 2025): Reporte al CEO y Comité Ejecutivo"
    },
    "d1607ef8-5777-44bc-9a1b-417c80dffeb4": {
        "source_id": "b6f21f15-0ec9-4e85-b6ae-aca2f29e1ed1",
        "source_title": "McKinsey & Company - Upgrading corporate affairs for a new geopolitical era"
    },
    "1bc7878d-6979-4674-8b63-0cf41f89bb73": {
        "source_id": "64f69761-40f4-4f00-82b4-5878cf7be69d",
        "source_title": "EUPRERA - Latin American Communication Monitor (LCM) Portal y Resultados"
    },
    "a904d924-f726-444f-b9f1-320ec2c50dd3": {
        "source_id": "4861a93d-b9c4-4972-bfeb-1d0902d65dd0",
        "source_title": "Global Alliance - Global Capability Framework Official Benchmark"
    },
    "f5108429-197e-4009-b684-2a6c1e95cfc9": {
        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo"
    }
}

P02_ORPHAN_MAP = {
    "52857476-0bf1-4770-b1cb-918d363d6f46": {
        "source_id": "2fd3bc2b-f4aa-4236-ba6d-2527a3b36aef",
        "source_title": "Litoralpress Chile Monitoreo de Medios e Inteligencia de Prensa"
    }
}

P07_ORPHAN_MAP = {
    "P07-C02": {
        "source_id": "c1105d8b-4367-4fce-9787-a339e4e48d3e",
        "source_title": "IPR: Communicator's Guide to Research, Analysis, and Evaluation"
    },
    "P07-C04": {
        "source_id": "7ed2eb90-1f62-42d0-bd97-2def6536115d",
        "source_title": "DINFOS: Five Key Things to Prep Your Subject Matter Expert (Bridging & Flagging)"
    },
    "P07-C06": {
        "source_id": "abe770ff-31f7-401a-941c-a3954e851a0d",
        "source_title": "IPR & CIPR: Ethics Guide for Artificial Intelligence in PR"
    },
    "P07-C10": {
        "source_id": "48eb3b70-3946-45c0-ae2f-bb245af96324",
        "source_title": "OECD: G20/OECD Principles of Corporate Governance"
    }
}

P08_ORPHAN_MAP = {
    "f5e9c12b-3e4a-4a2c-8a1d-7c2a1e0b9d3f": {
        "source_id": "537c6470-2429-43ec-82ba-7d7a3436031f",
        "source_title": "P08_QUALITY_ADDENDUM"
    }
}

def reconcile():
    manifests = load_manifests()
    fixed_counts = {"P01": 0, "P02": 0, "P07": 0, "P08": 0, "P11": 0}

    for rpath in sorted(glob.glob("respuestas/*.jsonl")):
        pilar = os.path.basename(rpath).replace(".jsonl", "")
        m = manifests.get(pilar)
        if not m:
            continue

        updated_lines = []
        with open(rpath, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                except Exception as err:
                    print(f"Error reading JSON in {rpath}: {type(err).__name__} (detalles omitidos por seguridad)")
                    updated_lines.append(line)
                    continue

                qid = obj.get("question_id")
                findings = obj.get("findings", [])
                modified = False

                for finding in findings:
                    for ev in finding.get("evidence", []):
                        sid = ev.get("source_id")
                        stitle = ev.get("source_title", "")
                        norm_title = stitle.strip().lower()

                        # 1. Check P07 specific C orphan mapping
                        if pilar == "P07" and qid in P07_ORPHAN_MAP and sid == "521c2c59-1c43-493b-abd9-7de2c7cf9dce":
                            mapping = P07_ORPHAN_MAP[qid]
                            ev["source_id"] = mapping["source_id"]
                            ev["source_title"] = mapping["source_title"]
                            ev["text_status"] = "fallida_o_bloqueada"
                            modified = True
                            fixed_counts["P07"] += 1
                            continue

                        # 2. Check P08 specific orphan mapping
                        if pilar == "P08" and sid in P08_ORPHAN_MAP:
                            mapping = P08_ORPHAN_MAP[sid]
                            ev["source_id"] = mapping["source_id"]
                            ev["source_title"] = mapping["source_title"]
                            modified = True
                            fixed_counts["P08"] += 1
                            continue

                        # 3. Check P01 specific orphan mapping
                        if pilar == "P01" and sid in P01_ORPHAN_MAP:
                            mapping = P01_ORPHAN_MAP[sid]
                            ev["source_id"] = mapping["source_id"]
                            ev["source_title"] = mapping["source_title"]
                            modified = True
                            fixed_counts["P01"] += 1
                            continue

                        # 4. Check P02 specific orphan mapping
                        if pilar == "P02" and sid in P02_ORPHAN_MAP:
                            mapping = P02_ORPHAN_MAP[sid]
                            ev["source_id"] = mapping["source_id"]
                            ev["source_title"] = mapping["source_title"]
                            modified = True
                            fixed_counts["P02"] += 1
                            continue

                        # 5. Check if title matches manifest, but ID doesn't
                        if sid not in m["by_id"] and norm_title in m["by_title"]:
                            target_source = m["by_title"][norm_title]
                            canonical_id = target_source.get("source_id") or target_source.get("id")
                            ev["source_id"] = canonical_id
                            ev["source_title"] = target_source.get("title")
                            modified = True
                            fixed_counts[pilar] = fixed_counts.get(pilar, 0) + 1
                            continue

                if modified:
                    updated_lines.append(json.dumps(obj, ensure_ascii=False) + "\n")
                else:
                    updated_lines.append(line)

        with open(rpath, "w", encoding="utf-8") as f:
            f.writelines(updated_lines)

    print("Reconciliation complete. Fixed citations by pilar:", fixed_counts)

if __name__ == "__main__":
    reconcile()
