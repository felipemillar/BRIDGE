import json
from pathlib import Path

step_output = Path("/Users/fmillar/.gemini/antigravity-ide/brain/e2af3e28-2370-48e8-a2d2-27b78225ea95/.system_generated/steps/928/output.txt")
with open(step_output, "r", encoding="utf-8") as f:
    data = json.load(f)

sources_raw = data['notebook'][0][1]

manifest = {
    "pilar": "P05",
    "pilar_nombre": "Metodologías de análisis y síntesis",
    "notebook_id": "0fc2e780-e279-4923-83c5-90fe621a4543",
    "total_sources": len(sources_raw),
    "snapshot_at": "2026-10-01T03:00:00-03:00",
    "editorial_precedence_rule": "P05_EVIDENCE_MAP, P05_QUALITY_ADDENDUM and P05_RESEARCH_DOSSIER govern analytical methodologies, structured analytic techniques (SATs), intelligence synthesis, and bias mitigation in this notebook.",
    "sources": []
}

for s in sources_raw:
    raw_id = s[0]
    while isinstance(raw_id, list):
        raw_id = raw_id[0]
    sid = str(raw_id)
    title = s[1]
    
    is_internal = title.startswith("00_") or title.startswith("P05_")
    
    # URL extraction
    url = None
    if len(s) > 2 and s[2] and len(s[2]) > 7 and s[2][7] and isinstance(s[2][7], list) and len(s[2][7]) > 0:
        url = s[2][7][0]
    
    # Word count / status
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
        "verified_at": "2026-10-01T03:00:00-03:00"
    }
    manifest["sources"].append(source_entry)

out_path = Path("fuentes/P05.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Frozen P05 manifest generated at {out_path} with {len(manifest['sources'])} sources.")
