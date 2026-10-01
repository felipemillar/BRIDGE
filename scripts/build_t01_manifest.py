import json
from pathlib import Path

NOTEBOOK_OUTPUT_PATH = Path("/Users/fmillar/.gemini/antigravity-ide/brain/e2af3e28-2370-48e8-a2d2-27b78225ea95/.system_generated/steps/1834/output.txt")
MANIFEST_PATH = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/fuentes/T01.json")

with open(NOTEBOOK_OUTPUT_PATH, "r", encoding="utf-8") as f:
    nb_data = json.load(f)

sources_raw = nb_data["notebook"][0][1]

internal_uuids = {
    "d3a3a8a3-5b4a-4234-adb0-efd38d55c800",
    "ab49ab0d-7a6d-48ff-a461-ae7af760fba9",
    "d37da869-4cd7-4611-961d-e7e2bcaf2fb3",
    "a8dd70ce-2151-4a96-99cd-a9e7c7a4dd40",
    "45782049-59e3-46e7-9175-aad6605fc98e",
    "ce4d8135-f66d-46f0-bc63-4f80f88f6b55",
    "64e8fef0-3b1f-440b-873d-238b351ed093",
    "0a59e98c-6000-4e4b-809b-57569da5687a",
    "35f1b7b2-55a0-4c09-946f-b9664022f733",
    "f5a15f9d-310f-4bfc-ae19-70ff8cc2bdcf"
}

# Mapeo de sustitutos canónicos para las 9 fichas /abs/
abs_to_pdf_map = {
    "71200684-fab2-47cb-b9f0-b719300fff6c": ("01d6cab0-4331-4f04-b66e-4ad6c3fa6f78", "Es et al. (2023) — Ragas: Automated Evaluation of Retrieval Augmented Generation (Full Paper PDF)"),
    "be91d779-b1bc-48b6-b472-de081bcb2117": ("01d6cab0-4331-4f04-b66e-4ad6c3fa6f78", "Es et al. (2023) — Ragas: Automated Evaluation of Retrieval Augmented Generation (Full Paper PDF)"),
    "391919fe-7e5b-4f12-9a2b-d67d7d5c59ef": ("e1a0171b-34f0-48f2-b343-29f7ec88bd31", "Gao et al. (2023) — Enabling Language Models to Generate Text with Citations (ALCE Full PDF)"),
    "692da01f-0996-4fab-ab21-1f64f96e434f": ("9df1af53-4f60-460c-a1b1-ddb96f0aa76f", "Fabbri et al. (2021) — SummEval: Re-evaluating Summarization Evaluation (Full PDF)"),
    "f4545a4e-492e-4af6-8249-f0608f896c8b": ("c103d2e1-3f2f-4416-8206-358ab4f15f27", "Manakul et al. (2023) — SelfCheckGPT: Zero-Resource Hallucination Detection (Full PDF)"),
    "6aae7b0a-aee9-47b7-9b0a-9b62ffaf7b50": ("142a9e37-de1d-438a-9ec4-96dfb18dbb09", "Vu et al. (2023) — FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation (Full PDF)"),
    "50ba2ef3-b531-48e8-bf97-681ede626980": ("dee0924c-f288-4ff9-818a-50bb65ce00e3", "Rebedea et al. (2023) — NeMo Guardrails: Controllable and Safe LLM Applications (Full PDF)"),
    "91c2adf9-9b85-46df-b6e9-21f714c9a2c5": ("bff33bd6-afbc-4544-b611-640f2023a150", "Saad-Falcon et al. (2023) — ARES: An Automated Evaluation Framework for RAG (Full PDF)"),
    "8ab467ce-8849-435d-9b20-6151acbe21df": ("45cf111e-3dc7-4a30-ad9f-a487a9d50b1e", "Sap et al. (2019) — Social IQa: Commonsense Reasoning about Social Interactions (Full PDF)"),
    "6dc9d978-cacd-49eb-ae4c-660e21a9e933": ("d19f3dcf-70e4-4517-a33f-9003a2f46a7f", "Inan et al. (2023) — Llama Guard: LLM-based Input-Output Safety (Full PDF)")
}

sources_catalog = []

for s in sources_raw:
    sid = s[0][0]
    title = s[1]
    url = s[2] if len(s) > 2 and s[2] else None
    
    is_internal = sid in internal_uuids or "T01_" in title
    
    canonical_sub = None
    if sid == "e315f267-1081-4cf8-abc1-d172dcbae54d":
        text_status = "atribucion_comercial_erronea"
        status_desc = "Agencia mexicana Bridge Studio (bridgestudio.mx); ratificada canónicamente como atribución errónea y ajena a thebridgeintelligence.ai"
        canonical_sub = "The Bridge Intelligence - Official Reference Website (6eca40e5-dfef-4b44-a26e-8b7af8c57e8c)"
    elif sid == "8901cfd4-08c2-4e4b-8a55-b5af3018f2b3":
        text_status = "fuente_fallida"
        status_desc = "Fallo de importación en NotebookLM; sustituida por la versión activa de OWASP Top 10"
        canonical_sub = "OWASP - Top 10 for Large Language Model Applications (2025 Edition) (2e41ac6a-6b9c-469f-b131-b81c402031c0)"
    elif sid == "60b9788f-d383-45a7-9132-d405cf135f07":
        text_status = "fuente_fallida"
        status_desc = "Fallo de importación en NotebookLM; sustituida por paper ArXiv 2023 de Action Items"
        canonical_sub = "ArXiv (2023) - Action-Item-Driven Summarization of Long Meeting Transcripts (6fac5239-00cb-4655-8001-85610f6b7823)"
    elif sid == "8d694d20-8ac1-4864-b964-e8bf0c51b286":
        text_status = "fuente_fallida"
        status_desc = "Fallo de importación en NotebookLM; sustituida por Sendelbach & Funk 2013 y D3 Security"
        canonical_sub = "Sendelbach & Funk (2013) (6ba9c5d2) / D3 Security (02470b46)"
    elif sid in abs_to_pdf_map:
        text_status = "ficha_abstract_duplicada"
        sub_id, sub_title = abs_to_pdf_map[sid]
        status_desc = f"Ficha abstract /abs/ duplicada; texto completo recuperado canónicamente en versión PDF ({sub_id[:8]})"
        canonical_sub = f"{sub_title} ({sub_id})"
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
        "verified_at": "2026-10-01T17:30:00-03:00"
    }
    sources_catalog.append(src_obj)

manifest = {
    "pilar": "T01",
    "pilar_nombre": "Evaluación y pilotos",
    "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
    "total_sources": len(sources_catalog),
    "snapshot_at": "2026-10-01T17:30:00-03:00",
    "editorial_precedence_rule": "T01_VERIFICATION_CORRECTIONS (f5a15f9d) ejerce prevalencia canónica rectora sobre T01_QUALITY_ADDENDUM (45782049) y las síntesis previas. Prevalencia de los 9 Full-Texts en PDF sobre las fichas /abs/; descarte canónico de Bridge Studio MX (bridgestudio.mx) como atribución errónea ajena a thebridgeintelligence.ai.",
    "sources": sources_catalog
}

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Manifiesto fuentes/T01.json generado exitosamente con {len(sources_catalog)} fuentes.")
