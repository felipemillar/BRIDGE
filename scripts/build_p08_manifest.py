import json
from pathlib import Path

step_output = Path("/Users/fmillar/.gemini/antigravity-ide/brain/e2af3e28-2370-48e8-a2d2-27b78225ea95/.system_generated/steps/1346/output.txt")
with open(step_output, "r", encoding="utf-8") as f:
    data = json.load(f)

sources_raw = data['notebook'][0][1]

manifest = {
    "pilar": "P08",
    "pilar_nombre": "Viabilidad, modelos de negocio y oportunidades",
    "notebook_id": "afe8fdb7-d63d-43ab-84e6-060fe6b8fd24",
    "total_sources": len(sources_raw),
    "snapshot_at": "2026-10-01T07:00:00-03:00",
    "editorial_precedence_rule": "P08_EVIDENCE_MAP, P08_QUALITY_ADDENDUM, P08_RESEARCH_DOSSIER, P08_GAPS_AND_VALIDATION and P08_SOURCE_INDEX govern business models, SaaS pricing tiers, TAM/SAM/SOM sizing in Chile/LatAm, buyer willingness-to-pay, API cost structures, and data privacy governance (Ley 21.719, Ley 20.730, CMF).",
    "sources": []
}

for s in sources_raw:
    raw_id = s[0]
    while isinstance(raw_id, list):
        raw_id = raw_id[0]
    sid = str(raw_id)
    title = s[1]
    
    is_internal = title.startswith("00_") or title.startswith("P08_")
    
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
        "verified_at": "2026-10-01T07:00:00-03:00"
    }
    manifest["sources"].append(source_entry)

with open("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/fuentes/P08.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Manifiesto P08 generado exitosamente con {len(manifest['sources'])} fuentes.")
