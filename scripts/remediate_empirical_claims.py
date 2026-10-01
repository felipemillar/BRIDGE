import json
import os

T01_PATH = "respuestas/T01.jsonl"

def remediate_t01_x22(obj):
    if obj.get("question_id") != "T01-X22":
        return obj

    obj["short_answer"] = (
        "Escenario de Simulación y Protocolo de Evaluación CTH-T01-320 (Diseño de Prueba de Carga Cognitiva y Supervisión Humana): "
        "1) Entradas de Diseño: Simulación donde un analista de asuntos corporativos debe preparar minutas estratégicas ante un petitorio "
        "sindical; 2) Protocolo de Telemetría Propuesto: Monitoreo de consultas, tasa de apertura de citas primarias (CTR) y dwell time "
        "por fragmento; 3) Métrica Hipotética Objetivo: Se plantea como hipótesis de diseño alcanzar una reducción de tiempo y una disminución "
        "en la escala psicométrica NASA-TLX (demanda mental y frustración); 4) Estatus Epistémico Estricto: Se trata de un escenario simulado "
        "y marco de prueba; no existe a la fecha registro primario ni piloto empírico ejecutado en una empresa chilena con estas mediciones."
    )

    obj["findings"] = [
        {
            "claim_id": "T01-X22-C1",
            "claim": (
                "Como hipótesis de diseño de evaluación, se propone combinar métricas de ahorro de tiempo y reducción de carga mental "
                "(NASA-TLX) con telemetría de inspección de citas para evaluar la adopción humana; sin embargo, no existe un piloto operacional "
                "de The Bridge Intelligence que haya documentado empíricamente estas cifras en una empresa u organización real."
            ),
            "epistemic_status": "hipotesis_diseno",
            "scope": {
                "time": "2026",
                "region": "Chile / Global",
                "actor": "The Bridge Intelligence (Protocolo de Prueba)"
            },
            "evidence": [
                {
                    "source_id": "9df1af53-4f60-460c-a1b1-ddb96f0aa76f",
                    "source_title": "Fabbri et al. (2021) — SummEval: Re-evaluating Summarization Evaluation",
                    "original_url": "https://arxiv.org/pdf/2007.12626.pdf",
                    "locator": "Section 3: Human Evaluation Setup",
                    "excerpt_short": "Provides a comprehensive benchmark and protocol for human evaluation across dimensions of coherence, consistency, fluency, and relevance in natural language summarization.",
                    "source_date": "2021-04-12",
                    "retrieved_at": "2026-10-01T04:40:00Z",
                    "text_status": "texto_sustantivo",
                    "relationship": "contextualiza"
                },
                {
                    "source_id": "45cf111e-3dc7-4a30-ad9f-a487a9d50b1e",
                    "source_title": "Sap et al. (2019) — Social IQa: Commonsense Reasoning about Social Interactions",
                    "original_url": "https://arxiv.org/pdf/1904.09728.pdf",
                    "locator": "Section 1: Introduction",
                    "excerpt_short": "Introduces a benchmark for commonsense reasoning about social interactions, evaluating model comprehension of motivations, reactions, and social implications.",
                    "source_date": "2019-04-23",
                    "retrieved_at": "2026-10-01T04:40:00Z",
                    "text_status": "texto_sustantivo",
                    "relationship": "contextualiza"
                }
            ],
            "confidence": "media",
            "confidence_reason": (
                "Protocolo metodológico fundamentado en literatura de benchmarking de NLP (SummEval, Social IQa), "
                "pero clasificado estrictamente como hipótesis de diseño y escenario simulado ante la ausencia de mediciones de campo primarias."
            )
        }
    ]

    obj["operational_model"]["outputs"] = [
        "Protocolo de Evaluación Simulada CTH-T01-320 (Marco de Prueba para Piloto Prospectivo)"
    ]

    obj["open_gaps"] = [
        {
            "gap": "Ausencia de ejecución empírica de un piloto comercial u operacional de The Bridge Intelligence con telemetría de campo y pruebas psicométricas NASA-TLX en clientes reales.",
            "minimum_validation": "Ejecución de prueba piloto con usuarios reales en una corporación, registro auditado de telemetría de interacción y administración independiente del test NASA-TLX.",
            "priority": "alta"
        }
    ]

    obj["bridge_implications"] = [
        {
            "module": "Hablar",
            "implication": "Marco de referencia para la compuerta G2 de interacción humana; no debe presentarse a clientes como un caso probado o un resultado histórico.",
            "status": "hipotesis"
        }
    ]

    return obj

def remediate_all_claims():
    # Audit files: T01, P01, P02
    target_files = ["respuestas/T01.jsonl", "respuestas/P01.jsonl", "respuestas/P02.jsonl"]
    reclassified_count = 0

    for fpath in target_files:
        lines_out = []
        with open(fpath, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                obj = json.loads(line)
                qid = obj.get("question_id")

                if qid == "T01-X22":
                    obj = remediate_t01_x22(obj)
                    reclassified_count += 1
                else:
                    # Check other unbacked empirical claims
                    modified = False
                    for finding in obj.get("findings", []):
                        ep = finding.get("epistemic_status")
                        claim = finding.get("claim", "")
                        # If claiming operational pilot/advantage of Bridge as documented fact
                        if ep == "hecho_documentado":
                            if qid in ["T01-F48", "T01-F42", "T01-X04", "T01-X05", "T01-X06", "T01-X14", "T01-X28", "T01-X30", "P02-F43", "P01-F42", "P01-F48"]:
                                finding["epistemic_status"] = "hipotesis_diseno"
                                modified = True
                                reclassified_count += 1
                lines_out.append(json.dumps(obj, ensure_ascii=False) + "\n")

        with open(fpath, "w", encoding="utf-8") as f:
            f.writelines(lines_out)

    print(f"Empirical claims remediation complete. Total records reclassified/remediated: {reclassified_count}")

if __name__ == "__main__":
    remediate_all_claims()
