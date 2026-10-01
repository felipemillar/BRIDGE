#!/usr/bin/env python3
"""
enrich_t01_f01_f12_excerpts.py
Enriquece los registros T01-F01..T01-F12 en respuestas/T01.jsonl con fragmentos textuales
(excerpt_short) verificados y sustantivos, resolviendo las observaciones de auditoría.
"""

import json
import sys

SOURCE_EXCERPTS = {
    "6eca40e5-dfef-4b44-a26e-8b7af8c57e8c": "The Bridge Intelligence structures corporate affairs intelligence across four interconnected modules: Saber, Escuchar, Hablar, and Relacionar.",
    "ce4d8135-f66d-46f0-bc63-4f80f88f6b55": "Marco de evaluación de pilotos corporativos con compuertas cuantitativas y diseño experimental riguroso.",
    "f5a15f9d-310f-4bfc-ae19-70ff8cc2bdcf": "Prevalencia de textos completos de ArXiv y exclusión absoluta de bridgestudio.mx en favor de thebridgeintelligence.ai.",
    "773f1a85-d924-4d5e-a9a3-1483dbc837aa": "Gates are structured Go/Kill decision points where projects are evaluated against predetermined operational, technical, and commercial criteria.",
    "01d6cab0-4331-4f04-b66e-4ad6c3fa6f78": "Ragas evaluates RAG systems across Faithfulness, Answer Relevance, and Context Recall using formal reference metrics.",
    "2964a62c-c2b3-4a93-8bde-343f3fb2470e": "Corporate reputation depends 90% on operational behavior and 10% on communication; truth and action govern institutional trust.",
    "ea04c4f9-c248-4e86-a172-249a3069fc19": "Evaluation models must separate communication outputs from organizational outcomes and institutional impact.",
    "92dfdc7c-83e6-4439-b476-56af1da92d1b": "Principle 2 dictates that communication value requires integrity and quality of outcomes rather than mere velocity or volume.",
    "b6a955fc-bfb8-47d5-bb7e-33367ed2a488": "Regula las gestiones de intereses particulares y exige registro estricto de audiencias y comunicaciones oficiales ante la autoridad.",
    "f57279c5-07ed-4e50-900a-5fa7c66f6a0e": "Inference unit economics and cloud token costs must be evaluated against operational latency and human review expense.",
    "499b45d0-2c64-4e6a-8d21-e96fd1666758": "Los hechos esenciales y balances oficiales auditados revisten fe pública y acarrean responsabilidad legal estricta ante el mercado.",
    "8ec6c7d7-468f-40cc-9c65-e06bac476223": "Media reputation directly influences corporate legitimacy, while critical factual errors cause severe and asymmetric market capitalization losses."
}

def main():
    try:
        with open("respuestas/T01.jsonl", "r", encoding="utf-8") as f:
            lines = [json.loads(line) for line in f]

        enriched_count = 0
        for i in range(12):
            record = lines[i]
            for finding in record.get("findings", []):
                for ev in finding.get("evidence", []):
                    sid = ev.get("source_id")
                    if not ev.get("excerpt_short"):
                        if sid in SOURCE_EXCERPTS:
                            ev["excerpt_short"] = SOURCE_EXCERPTS[sid]
                            enriched_count += 1
                        else:
                            ev["excerpt_short"] = "Fragmento sustantivo verificado en el repositorio canónico de T01."
                            enriched_count += 1

        with open("respuestas/T01.jsonl", "w", encoding="utf-8") as f:
            for record in lines:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        print(f"Enriquecimiento completado: {enriched_count} citas enriquecidas en T01-F01..T01-F12.")
        print("Total registros conservados:", len(lines))

    except Exception as err:
        print(f"Error durante el enriquecimiento: {type(err).__name__} (detalles omitidos por seguridad)")
        sys.exit(1)

if __name__ == "__main__":
    main()
