import json
from pathlib import Path

step_output = Path("/Users/fmillar/.gemini/antigravity-ide/brain/e2af3e28-2370-48e8-a2d2-27b78225ea95/.system_generated/steps/1220/output.txt")
with open(step_output, "r", encoding="utf-8") as f:
    data = json.load(f)

sources_raw = data['notebook'][0][1]

manifest = {
    "pilar": "P07",
    "pilar_nombre": "Preparación ejecutiva y apoyo estratégico",
    "notebook_id": "521c2c59-1c43-493b-abd9-7de2c7cf9dce",
    "total_sources": len(sources_raw),
    "snapshot_at": "2026-10-01T04:00:00-03:00",
    "editorial_precedence_rule": "P07_EVIDENCE_MAP, P07_RESEARCH_DOSSIER, P07_GAPS_AND_VALIDATION and P07_SOURCE_INDEX govern executive preparation, briefing architectures, media training techniques (bridging, hooking, flagging), message houses, scenario wargaming, regulatory governance (Ley 20.730, Ley 18.045, CMF NCG 461), and human review gates.",
    "sources": []
}

for s in sources_raw:
    raw_id = s[0]
    while isinstance(raw_id, list):
        raw_id = raw_id[0]
    sid = str(raw_id)
    title = s[1]
    
    is_internal = title.startswith("00_") or title.startswith("P07_")
    
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
    elif status_code == 3 or word_count is None or word_count == 0:
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
        "verified_at": "2026-10-01T04:00:00-03:00"
    }
    manifest["sources"].append(source_entry)

with open("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/fuentes/P07.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Manifiesto P07 generado exitosamente con {len(manifest['sources'])} fuentes.")
