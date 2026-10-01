import json
import datetime

with open("/Users/fmillar/.gemini/antigravity-ide/brain/e2af3e28-2370-48e8-a2d2-27b78225ea95/.system_generated/steps/491/output.txt") as f:
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

for s in sources_raw:
    sid = s[0][0][0]
    title = s[1]
    
    # Check if failed or internal
    is_internal = title.startswith("00_") or title.startswith("P02_")
    url = None
    if len(s) > 7 and s[7] and isinstance(s[7], list) and len(s[7]) > 0:
        url = s[7][0]
    
    # Text length or word count indicator if present
    # s[2][1] often contains char count or word count, e.g. 582, 3445, etc.
    word_count = s[2][1] if (len(s) > 2 and s[2] and len(s[2]) > 1) else None
    
    # Status
    # Check if source failed: in P02, some sources have null in word_count and status 3 (e.g. Borealis, Cision Media Monitoring, FiscalNote ESG360, GlobalNews Group, Muck Rack)
    # s[3] has [null, 3] for failed/empty, and [null, 2] for usable!
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

with open("fuentes/P02.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Generated fuentes/P02.json: Total={manifest['counts']['total']}, Usable={usable_count}, Failed={failed_count}, Internal={internal_count}")
