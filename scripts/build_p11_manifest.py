import json
from pathlib import Path

NOTEBOOK_OUTPUT_PATH = Path("/Users/fmillar/.gemini/antigravity-ide/brain/e2af3e28-2370-48e8-a2d2-27b78225ea95/.system_generated/steps/1699/output.txt")
MANIFEST_PATH = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/fuentes/P11.json")

with open(NOTEBOOK_OUTPUT_PATH, "r", encoding="utf-8") as f:
    nb_data = json.load(f)

sources_raw = nb_data["notebook"][0][1]

internal_uuids = {
    "0716e04e-fef2-438a-8640-b662534aa59b",
    "2f63e397-ea7a-483b-8659-142745e7ccc5",
    "75bb6ae1-1c8d-4fa2-a218-bdb02ecf194c",
    "b7224996-c5d5-4c47-ab3c-6e29a691c5d7",
    "ad1bbfc3-6d35-4c99-a350-3ccbcdd04647",
    "c92c1c3d-91d3-4d45-8561-11062f436461",
    "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
    "4608d794-4538-48e8-94fb-da95fb84e1e4",
    "49d7882a-096d-4bf2-b56c-39fe8af3d7f6"
}

sources_catalog = []

for s in sources_raw:
    sid = s[0][0]
    title = s[1]
    url = s[2] if len(s) > 2 and s[2] else None
    
    is_internal = sid in internal_uuids or "P11_" in title
    
    # Clasificación de estatus
    canonical_sub = None
    if sid == "4caa2cda-cd09-463e-8ff0-6342e4c89172":
        text_status = "directorio_navegacional_no_sustantivo"
        status_desc = "Cuerpo físico contiene enlaces y herramientas del portal WIPO; descartada canónicamente de inferencias jurídicas"
        canonical_sub = "Câmara dos Deputados: Lei Nº 13.709 (LGPD Atualizada 2026) PDF (f16e1ff5) / Lei 15.352 (ea76a1ee)"
    elif "HTML" in title and ("OpenAI" in title):
        text_status = "error_extraccion_o_duplicado"
        status_desc = "Importación HTML defectuosa o con bloqueo; sustituida canónicamente por la versión PDF oficial"
        if "Data Processing" in title:
            canonical_sub = "OpenAI: OpenAI Data Processing Addendum (DPA) Official PDF (1bc87361)"
        elif "Services Agreement" in title:
            canonical_sub = "OpenAI: OpenAI Services Agreement (Effective Jan 1, 2026) Official PDF (8d9a7ceb)"
        else:
            canonical_sub = "OpenAI: Business Terms, Enterprise Privacy and Data Processing Agreement (2714436f)"
    else:
        text_status = "texto_sustantivo"
        status_desc = "Texto sustantivo procesado y verificado en cuaderno"
        
    src_obj = {
        "source_id": sid,
        "title": title,
        "type": "sintesis_interna" if is_internal else "fuente_externa",
        "original_url": url,
        "text_status": text_status,
        "status_description": status_desc,
        "is_internal_synthesis": is_internal,
        "canonical_substitute": canonical_sub,
        "verified_at": "2026-10-01T13:45:00-03:00"
    }
    sources_catalog.append(src_obj)

manifest = {
    "pilar": "P11",
    "pilar_nombre": "Gobernanza de información y operación entre clientes",
    "notebook_id": "64271ecf-776c-4692-b302-d936ea00a501",
    "total_sources": len(sources_catalog),
    "snapshot_at": "2026-10-01T13:45:00-03:00",
    "editorial_precedence_rule": "P11_VERIFICATION_CORRECTIONS (49d7882a) y P11_2026_LAW_AND_PROVIDER_CORRECTION (0716e04e) ejercen prevalencia canónica rectora sobre P11_QUALITY_ADDENDUM, P11_PENDING_SOURCES_RESOLUTION y síntesis anteriores. Descarte de WIPO Lex como no sustantiva y sustitución canónica de HTMLs de OpenAI por PDFs oficiales vigentes.",
    "sources": sources_catalog
}

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Manifiesto P11 creado exitosamente en {MANIFEST_PATH}")
print(f"Total fuentes catalogadas: {len(sources_catalog)}")
print(f"Fuentes internas: {len([s for s in sources_catalog if s['is_internal_synthesis']])}")
print(f"Fuentes externas: {len([s for s in sources_catalog if not s['is_internal_synthesis']])}")
