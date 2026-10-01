import json
import os

RAW_PATH = "/Users/fmillar/.gemini/antigravity-ide/brain/e2af3e28-2370-48e8-a2d2-27b78225ea95/.system_generated/steps/2151/output.txt"
OUT_PATH = "fuentes/P02.json"

def main():
    with open(RAW_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    sources_raw = data['notebook'][0][1]

    manifest = {
        "pilar": "P02",
        "pilar_nombre": "Empresas y soluciones existentes",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "total_sources": len(sources_raw),
        "snapshot_at": "2026-10-01T01:21:00-03:00",
        "editorial_precedence_rule": "00_P02_GLOBAL_READ_ME_AND_ERRATA takes absolute precedence over all other sources in this notebook. Reconciles atlas count and corrects commercial vendor claims.",
        "sources": []
    }

    seen_ids = set()

    for s in sources_raw:
        # s[0] is a list containing the full UUID string, e.g. ['e08c2111-b14b-44d9-bd3c-54651ef434b5']
        sid = s[0][0]
        if sid in seen_ids:
            print(f"WARNING: Duplicate source ID detected: {sid}")
        seen_ids.add(sid)

        title = s[1]
        is_internal = title.startswith("00_") or title.startswith("P02_")

        url = None
        if len(s) > 7 and s[7] and isinstance(s[7], list) and len(s[7]) > 0:
            url = s[7][0]

        word_count = s[2][1] if (len(s) > 2 and s[2] and len(s[2]) > 1) else None
        status_code = s[3][1] if (len(s) > 3 and s[3] and len(s[3]) > 1) else None

        if is_internal:
            tipo = "sintesis_interna"
            text_status = "texto_sustantivo"
        elif status_code == 3 or word_count is None:
            tipo = "fuente_fallida"
            text_status = "fallida_o_bloqueada"
        else:
            tipo = "fuente_externa"
            text_status = "texto_sustantivo"

        source_entry = {
            "source_id": sid,
            "title": title,
            "type": tipo,
            "original_url": url,
            "status_code": status_code,
            "word_count": word_count,
            "text_status": text_status,
            "is_internal_synthesis": is_internal,
            "verified_at": "2026-10-01T01:21:00-03:00"
        }
        manifest["sources"].append(source_entry)

    usable_count = sum(1 for s in manifest["sources"] if s["text_status"] == "texto_sustantivo")
    failed_count = sum(1 for s in manifest["sources"] if s["text_status"] == "fallida_o_bloqueada")
    internal_count = sum(1 for s in manifest["sources"] if s["is_internal_synthesis"])

    manifest["counts"] = {
        "total": len(manifest["sources"]),
        "usable": usable_count,
        "failed_or_blocked": failed_count,
        "internal_synthesis": internal_count,
        "external_sources": len(manifest["sources"]) - internal_count
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated {OUT_PATH}:")
    print(f"  Total sources: {len(manifest['sources'])} (unique IDs: {len(seen_ids)})")
    print(f"  Usable: {usable_count}, Failed/Blocked: {failed_count}, Internal: {internal_count}")

if __name__ == "__main__":
    main()
