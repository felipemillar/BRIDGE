import json
from pathlib import Path

METADATA_STEP_OUTPUT = Path("/Users/fmillar/.gemini/antigravity-ide/brain/e2af3e28-2370-48e8-a2d2-27b78225ea95/.system_generated/steps/1467/output.txt")
TARGET = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/fuentes/P09.json")

raw = open(METADATA_STEP_OUTPUT, "r", encoding="utf-8").read()
data = json.loads(raw)
notebook = data["notebook"][0]
pilar_nombre = notebook[0]
sources_raw = notebook[1]

internal_titles = [
    "P09_EVIDENCE_MAP",
    "P09_GAPS_AND_VALIDATION",
    "P09_OECD_SCOPE_CORRECTION",
    "P09_PENDING_SOURCES_RESOLUTION",
    "P09_QUALITY_ADDENDUM: Auditoría Canónica, Reconciliación y Calibración Epistémica (Síntesis Interna)",
    "P09_RESEARCH_DOSSIER",
    "P09_SOURCE_INDEX",
    "P09_VERIFICATION_CORRECTIONS: Rectificación Canónica y Auditoría de Cuerpos (Síntesis Interna)"
]

sources_manifest = []

for s in sources_raw:
    sid = s[0][0]
    stitle = s[1]
    word_count = s[2][1] if len(s[2]) > 1 else None
    url = s[2][7][0] if len(s[2]) > 7 and s[2][7] else None
    
    is_internal = any(stitle.startswith(it) or it in stitle for it in [
        "P09_EVIDENCE_MAP", "P09_GAPS_AND_VALIDATION", "P09_OECD_SCOPE_CORRECTION",
        "P09_PENDING_SOURCES_RESOLUTION", "P09_QUALITY_ADDENDUM", "P09_RESEARCH_DOSSIER",
        "P09_SOURCE_INDEX", "P09_VERIFICATION_CORRECTIONS"
    ])
    
    if word_count is None:
        text_status = "fallida_o_bloqueada"
        status_desc = "FAILED (inaccesible o error HTTP)"
    elif sid == "fb02f5bf-f767-419e-a214-e305e3b8c582":
        text_status = "solo_navegacion"
        status_desc = "Landing institucional / resumen introductorio no sustantivo"
    else:
        text_status = "texto_sustantivo"
        status_desc = "Texto sustantivo procesado íntegramente"
        
    src_type = "sintesis_interna" if is_internal else "fuente_externa"
    
    substitute = None
    if text_status == "fallida_o_bloqueada":
        if "Darzin" in stitle:
            substitute = "Boréalis (00e3a352) y Tractivity (8b347889)"
        elif "INDH" in stitle:
            substitute = "Kancha Investigación (c726d144) y SEA Chile (f519980d)"
        elif "OECD" in stitle:
            substitute = "OECD: The Regulation of Lobbying and Influence in Chile (2024) — Official Report PDF (49910d9b, 86.856 tokens)"
        elif "PRSA" in stitle:
            substitute = "Prowly (73c2f92c) y Guideflow (4d89f574)"
        elif "SustaiNet" in stitle:
            substitute = "Boréalis (27ce9bc8) y Simply Stakeholders (f962cf2b)"
            
    sources_manifest.append({
        "source_id": sid,
        "title": stitle,
        "type": src_type,
        "original_url": url,
        "word_count": word_count,
        "text_status": text_status,
        "status_description": status_desc,
        "is_internal_synthesis": is_internal,
        "canonical_substitute": substitute,
        "verified_at": "2026-10-01T08:15:00-03:00"
    })

manifest = {
    "pilar": "P09",
    "pilar_nombre": "Memoria de relaciones y gestión de compromisos",
    "notebook_id": "9117c80e-9317-4b6b-9c74-292bae6f5769",
    "total_sources": len(sources_manifest),
    "snapshot_at": "2026-10-01T08:15:00-03:00",
    "editorial_precedence_rule": "En P09, P09_VERIFICATION_CORRECTIONS y P09_OECD_SCOPE_CORRECTION prevalecen sobre P09_QUALITY_ADDENDUM y síntesis preliminares. El informe OECD PDF complementa la Ley 20.730 pero no es norma vinculante.",
    "sources": sources_manifest
}

with open(TARGET, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Manifiesto P09 congelado exitosamente en {TARGET}. Total fuentes: {len(sources_manifest)}")
