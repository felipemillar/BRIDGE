import json
from pathlib import Path

NOTEBOOK_GET_FILE = Path("/Users/fmillar/.gemini/antigravity-ide/brain/e2af3e28-2370-48e8-a2d2-27b78225ea95/.system_generated/steps/1580/output.txt")
OUTPUT_MANIFEST = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/fuentes/P10.json")

data = json.loads(NOTEBOOK_GET_FILE.read_text(encoding="utf-8"))
notebook_info = data["notebook"][0]
title = notebook_info[0]
raw_sources = notebook_info[1]
notebook_id = notebook_info[2]

sources = []
for s in raw_sources:
    source_id = s[0][0]
    source_title = s[1]
    meta = s[2] if len(s) > 2 else []
    
    word_count = meta[1] if len(meta) > 1 and meta[1] is not None else 0
    url_info = meta[7] if len(meta) > 7 and meta[7] is not None else []
    original_url = url_info[0] if url_info else None
    
    status_code = s[3][1] if len(s) > 3 and s[3] and len(s[3]) > 1 else None
    
    # Internal synthesis check
    is_internal = "Sintesis Interna" in source_title or "Síntesis Interna" in source_title or source_title.startswith("P10_")
    
    # Text status check
    # In NotebookLM schema: status_code 2 is ready/active, status_code 3 is error/failed
    if status_code == 3 or word_count == 0:
        text_status = "error_extraccion"
        status_desc = "Falla de extracción o contenido vacío"
    else:
        text_status = "texto_sustantivo"
        status_desc = f"Texto sustantivo procesado ({word_count} palabras)"
        
    canonical_substitute = None
    if "CIPR & IPR: Ethics Guide" in source_title:
        canonical_substitute = "CIPR: Artificial Intelligence in Public Relations Policy and Ethics Guides (0f644aa9)"
    elif "Coombs (2007)" in source_title:
        canonical_substitute = "Anderson: Situational Crisis Communication Theory (SCCT) (ae1d0dbb)"
    elif "SEC: 17 CFR 240.10b-5" in source_title and status_code == 3:
        canonical_substitute = "Cornell LII: 17 CFR § 240.10b-5 (b689098d) / eCFR (8858106c)"
        
    sources.append({
        "source_id": source_id,
        "title": source_title,
        "type": "sintesis_interna" if is_internal else "fuente_externa",
        "original_url": original_url,
        "word_count": word_count,
        "text_status": text_status,
        "status_description": status_desc,
        "is_internal_synthesis": is_internal,
        "canonical_substitute": canonical_substitute,
        "verified_at": "2026-10-01T09:30:00-03:00"
    })

manifest = {
    "pilar": "P10",
    "pilar_nombre": "Gestión y aprobación de la comunicación corporativa",
    "notebook_id": notebook_id,
    "total_sources": len(sources),
    "snapshot_at": "2026-10-01T09:30:00-03:00",
    "editorial_precedence_rule": "P10_VERIFICATION_CORRECTIONS (f043631e) prevalece sobre P10_QUALITY_ADDENDUM (1da04c4e) y síntesis previas.",
    "sources": sources
}

OUTPUT_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Manifiesto fuentes/P10.json generado con {len(sources)} fuentes.")
for s in sources:
    status_mark = "FAILED" if s["text_status"] == "error_extraccion" else "OK"
    sub_str = f" -> Sustituto: {s['canonical_substitute']}" if s['canonical_substitute'] else ""
    print(f"  [{status_mark}] {s['source_id']} | {s['title'][:65]}{sub_str}")
