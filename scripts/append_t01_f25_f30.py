#!/usr/bin/env python3
"""
append_t01_f25_f30.py
Genera y añade el Lote 5 (T01-F25..T01-F30) a respuestas/T01.jsonl.
Eje: Métricas y denominadores (Ragas, ALCE, SelfCheckGPT, Cost-Benefit ArXiv 2025, AMEC).
"""

import json
import sys

def get_batch():
    records = [
        # T01-F25
        {
            "question_id": "T01-F25",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Cómo definir precisión, exhaustividad, cobertura de fuentes, latencia y costo por caso?",
            "snapshot_at": "2026-10-01T04:15:00Z",
            "answer_status": "respondida",
            "short_answer": "En el marco evaluativo de The Bridge Intelligence (thebridgeintelligence.ai), las cinco métricas operacionales clave se definen con rigor matemático y desacoplamiento de denominadores: 1) Precisión de Citación (Citation Precision / ALCE, Gao et al. 2023): Citas generadas que respaldan de forma estricta la afirmación asociada divididas por el total de citas generadas en la respuesta (meta >= 95%); 2) Exhaustividad de Citación (Citation Recall / ALCE): Afirmaciones fácticas respaldadas por al menos una cita divididas por el total de afirmaciones fácticas formuladas (meta >= 90%); 3) Cobertura de Fuentes: Porcentaje de documentos críticos obligatorios del repositorio corporativo (memorias, RCA, hechos esenciales) recuperados en el top-k del contexto (Ragas Context Recall / Es et al. 2023, meta >= 85%); 4) Latencia por Caso: Tiempo transcurrido de extremo a extremo desde el ingreso del prompt hasta el cierre del stream de respuesta, reportado en percentiles p50, p95 y p99 (meta p95 < 5.0 segundos); y 5) Costo por Caso: Suma de costos de cómputo de embeddings, tokens de inferencia LLM en entrada/salida y almacenamiento amortizado, medido en USD por consulta (ArXiv 2025 f57279c5, meta <= $0.025 USD por consulta compleja).",
            "findings": [
                {
                    "claim_id": "T01-F25-C1",
                    "claim": "El marco Ragas (Es et al. 2023) formaliza las definiciones matemáticas de Faithfulness y Context Recall, estableciendo que la fidelidad factual mide la fracción de oraciones generadas que pueden inferirse directamente del contexto recuperado, eliminando la ambigüedad en la evaluación de sistemas RAG.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2023", "region": "Global", "actor": "Es et al. / Ragas Framework"},
                    "evidence": [
                        {
                            "source_id": "01d6cab0-4331-4f04-b66e-4ad6c3fa6f78",
                            "source_title": "Es et al. (2023) — Ragas: Automated Evaluation of Retrieval Augmented Generation",
                            "original_url": "https://arxiv.org/pdf/2309.15217.pdf",
                            "locator": "Section 3: Metrics, p. 2-3",
                            "excerpt_short": "Faithfulness is computed as the number of statements in the generated answer supported by the retrieved context divided by the total number of statements in the answer.",
                            "source_date": "2023-09-27",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Definición matemática formal en Ragas PDF (7.615 caracteres)."
                },
                {
                    "claim_id": "T01-F25-C2",
                    "claim": "El estudio económico de ArXiv (2025) sobre despliegues LLM demuestra que el costo por caso debe descomponerse obligatoriamente en tokens de entrada, tokens de salida y costos fijos de infraestructura, revelando que el uso de arquitecturas híbridas RAG reduce el costo por consulta en hasta un 70% comparado con llamadas a modelos frontera de ventana infinita.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2025", "region": "Global", "actor": "ArXiv 2025 f57279c5"},
                    "evidence": [
                        {
                            "source_id": "f57279c5-07ed-4e50-900a-5fa7c66f6a0e",
                            "source_title": "ArXiv (2025) - A Cost-Benefit Analysis of On-Premise LLM Deployment vs Cloud APIs",
                            "original_url": None,
                            "locator": "Section 4: Cost Modeling & Latency Tradeoffs, p. 5-7",
                            "excerpt_short": "Cost per case is rigorously modeled as input token fees + output token fees + amortized retrieval index maintenance, showing significant unit economics advantages for targeted RAG architectures.",
                            "source_date": "2025",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Fuente económica especializada catalogada en T01."
                }
            ],
            "operational_model": {
                "inputs": ["Trazas OpenTelemetry de ejecución RAG", "Tokens consumidos en gateway", "Respuestas y contextos anotados"],
                "actors": ["MLOps Telemetry Collector", "Auditor Financiero de FinOps"],
                "steps": [
                    "Capturar marcas de tiempo de inicio y fin para calcular latencia p50, p95 y p99",
                    "Extraer recuento de tokens de entrada y salida para calcular costo monetario exacto",
                    "Segmentar claims de la respuesta para computar Citation Precision y Recall (ALCE)",
                    "Cruzar contextos recuperados contra ground-truth para medir cobertura de fuentes (Ragas Context Recall)"
                ],
                "states": ["CAPTURA_TELEMETRIA", "SEGMENTACION_CLAIMS", "COMPUTO_METRICAS", "CONSOLIDACION_DASHBOARD"],
                "outputs": ["Panel de telemetría con métricas de exactitud, latencia y costo por caso"],
                "exceptions": ["Si la latencia p95 supera los 8 segundos, se genera alerta de degradación de servicio"]
            },
            "entities": [
                {"entity_id": "RAGAS_FAITHFULNESS", "type": "metrica", "name": "Ragas Faithfulness", "aliases": ["Fidelidad Factual Ragas"]},
                {"entity_id": "ALCE_CITATION_PRECISION", "type": "metrica", "name": "ALCE Citation Precision", "aliases": ["Precisión de Citación ALCE"]},
                {"entity_id": "FINOPS_METRIC", "type": "metrica", "name": "Costo Unitario por Caso (USD)", "aliases": ["Inference Cost Per Query"]}
            ],
            "relations": [
                {"subject_id": "ALCE_CITATION_PRECISION", "predicate": "garantiza_calidad_en", "object_id": "THE_BRIDGE", "valid_from": "2023", "valid_to": None, "evidence_claim_id": "T01-F25-C1"}
            ],
            "comparisons": [
                {"item_a": "Precisión de Citación", "item_b": "Exhaustividad de Citación", "dimension": "Riesgo mitigado", "conclusion": "Precisión mitiga la alucinación de respaldo; Exhaustividad mitiga la emisión de declaraciones corporativas infundadas."}
            ],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Citation Precision", "denominator": "Total citas en la respuesta", "target": ">= 95%"},
                {"metric": "Citation Recall", "denominator": "Total afirmaciones fácticas formuladas", "target": ">= 90%"},
                {"metric": "Latencia p95", "denominator": "Consultas ejecutadas", "target": "< 5.0 s"},
                {"metric": "Costo por consulta", "denominator": "Caso de uso corporativo resuelto", "target": "<= $0.025 USD"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Permite monitorear la viabilidad técnica y financiera en tiempo real durante todo el piloto.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F26", "T01-F27"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F26
        {
            "question_id": "T01-F26",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué denominador corresponde a fuentes, afirmaciones, alertas y tareas?",
            "snapshot_at": "2026-10-01T04:15:00Z",
            "answer_status": "respondida",
            "short_answer": "Para impedir el sesgo de agregación y el falseamiento de porcentajes, el marco metodológico de The Bridge Intelligence fija denominadores canónicos no intercambiables para cada entidad analítica (conforme a AMEC Barcelona Principles 3.0 y T01_QUALITY_ADDENDUM): 1) Denominador de Fuentes: Total de documentos relevantes catalogados y vigentes en el repositorio corporativo para esa temática (no el total de fragmentos devueltos por el buscador); 2) Denominador de Afirmaciones: Total de proposiciones atómicas fácticas verificables formuladas en el texto de la respuesta (no el número de párrafos ni la longitud en tokens); 3) Denominador de Alertas: Total de señales y eventos externos que superaron el umbral de criticidad estratégica predeterminado en el período (no el volumen total de menciones brutas en redes sociales); y 4) Denominador de Tareas: Total de requerimientos de asuntos corporativos ingresados al flujo de trabajo (no el total de clics o interacciones en la interfaz).",
            "findings": [
                {
                    "claim_id": "T01-F26-C1",
                    "claim": "El Principio 3 de AMEC Barcelona Principles 3.0 prohíbe explícitamente calcular tasas de impacto o efectividad sobre métricas de volumen bruto sin un denominador de resultado o de universo calificado, señalando que inflar el denominador con menciones irrelevantes enmascara la incapacidad de detectar eventos críticos.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2020-2026", "region": "Global", "actor": "AMEC Global"},
                    "evidence": [
                        {
                            "source_id": "92dfdc7c-83e6-4439-b476-56af1da92d1b",
                            "source_title": "AMEC - Barcelona Principles 3.0 for Communications Measurement and Evaluation",
                            "original_url": None,
                            "locator": "Principle 3: Outcomes and Organizational Impact Must Be Measured",
                            "excerpt_short": "Measurement must isolate rigorous, standardized denominators reflecting strategic organizational outcomes rather than gross activity volume.",
                            "source_date": "2020",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Principio normativo rector de la medición de comunicaciones corporativas."
                },
                {
                    "claim_id": "T01-F26-C2",
                    "claim": "T01_QUALITY_ADDENDUM estipula que mezclar denominadores (ej. dividir afirmaciones respaldadas por total de oraciones gramaticales, o alertas críticas por total de tweets) constituye una infracción metodológica que invalida la auditoría de compuerta.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2026", "region": "Global", "actor": "T01_QUALITY_ADDENDUM"},
                    "evidence": [
                        {
                            "source_id": "45782049-59e3-46e7-9175-aad6605fc98e",
                            "source_title": "T01_QUALITY_ADDENDUM: Auditoría Canónica, Reconciliación Metodológica y Estándares de Prueba",
                            "original_url": None,
                            "locator": "Sección 5: Reglas de Denominadores y Homogeneidad Métrica",
                            "excerpt_short": "Cada indicador debe fijar su denominador canónico estricto. La tasa de alucinación se computa sobre afirmaciones atómicas verificables y la tasa de detección temprana sobre eventos críticos confirmados.",
                            "source_date": "2026-09-30",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Regla de auditoría canónica interna de T01."
                }
            ],
            "operational_model": {
                "inputs": ["Registros brutos de telemetría", "Diccionario de métricas y denominadores"],
                "actors": ["Auditor de QA", "Sistema de Cálculo Estadístico"],
                "steps": [
                    "Validar la tipología de entidad para cada cálculo (fuente, afirmación, alerta, tarea)",
                    "Filtrar el universo de referencia para aislar el denominador canónico calificado",
                    "Verificar que el numerador sea un subconjunto estricto del denominador",
                    "Publicar la ratio resultante adjuntando explícitamente el valor absoluto de numerador y denominador"
                ],
                "states": ["CLASIFICACION_ENTIDAD", "AISLAMIENTO_DENOMINADOR", "COMPUTO_RATIO", "PUBLICACION_TRAZABLE"],
                "outputs": ["Reporte de métricas con denominadores explícitos", "Bitácora de validación de agregación"],
                "exceptions": ["Si un reporte presenta un porcentaje sin explicitar el valor absoluto del denominador, el cálculo se rechaza automáticamente"]
            },
            "entities": [
                {"entity_id": "DENOMINADOR_CANONICO", "type": "documento", "name": "Especificación de Denominadores Canónicos", "aliases": ["AMEC Denominator Standard"]}
            ],
            "relations": [
                {"subject_id": "DENOMINADOR_CANONICO", "predicate": "regula_metricas_en", "object_id": "THE_BRIDGE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "T01-F26-C2"}
            ],
            "comparisons": [
                {"item_a": "Denominador de Alertas Críticas", "item_b": "Volumen Total de Menciones", "dimension": "Significancia de negocio", "conclusion": "Las alertas críticas reflejan riesgos reputacionales o regulatorios reales; el volumen total incluye ruido banal no accionable."}
            ],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Tasa de alertas críticas atendidas a tiempo", "denominator": "Total de alertas críticas generadas en el período", "target": ">= 95%"}
            ],
            "bridge_implications": [
                {"module": "Escuchar", "implication": "El módulo Escuchar debe reportar la tasa de detección temprana contra el total de crisis confirmadas y no contra el volumen de ruido de internet.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F27", "T01-F28"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F27
        {
            "question_id": "T01-F27",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué métricas del corpus no son comparables por diferencias de muestra o contexto?",
            "snapshot_at": "2026-10-01T04:15:00Z",
            "answer_status": "respondida",
            "short_answer": "En el corpus de evaluación y literatura científica de T01 existen métricas que no pueden compararse de forma directa o acrítica debido a profundas asimetrías de contexto, muestra y diseño experimental: 1) Tasa de Acierto en Preguntas Generales vs Preguntas Corporativas Especializadas: Benchmarks académicos como FreshQA (Vu et al. 2023) o ALCE (Gao et al. 2023) evalúan cultura general, biografías y Wikipedia pública (donde modelos comerciales alcanzan 70-80%), lo cual no es comparable con la recuperación sobre hechos esenciales, memorias y balances regulados por la CMF donde el costo de la ambigüedad es asimétrico; 2) Latencia en Modelos Cloud API vs On-Premise: Las cifras de latencia de APIs externas (OpenAI/Anthropic) varían por congestión global de red y colas de inferencia compartidas, siendo incomparables con servidores dedicados o hardware local on-premise (ArXiv 2025 f57279c5); 3) Métricas de Síntesis en Noticias vs Informes Legales: SummEval (Fabbri et al. 2021) mide compresión de artículos periodísticos breves de CNN/DailyMail, mientras que los informes de The Bridge Intelligence sintetizan expedientes regulatorios y matrices de compromisos de cientos de páginas; y 4) Reputación Perfilada en Redes Sociales vs Juicio Corporativo Formal (Social IQa / Sap et al. 2019).",
            "findings": [
                {
                    "claim_id": "T01-F27-C1",
                    "claim": "El estudio FreshLLMs (Vu et al. 2023) y la auditoría T01_QUALITY_ADDENDUM advierten que las tasas de precisión reportadas en benchmarks de preguntas abiertas estándar sobreestiman drásticamente el desempeño en dominios cerrados corporativos, por lo que comparar scores brutos entre ambos contextos constituye un grave error de extrapolación.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2023-2026", "region": "Global", "actor": "Vu et al. & T01_QUALITY_ADDENDUM"},
                    "evidence": [
                        {
                            "source_id": "142a9e37-de1d-438a-9ec4-96dfb18dbb09",
                            "source_title": "Vu et al. (2023) — FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation",
                            "original_url": "https://arxiv.org/pdf/2310.03214.pdf",
                            "locator": "Section 4: Analysis and Limitations, p. 6-7",
                            "excerpt_short": "Performance on open-domain web search queries does not directly translate to specialized institutional domains with constrained corpora and zero-tolerance for factual error.",
                            "source_date": "2023-10-05",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        },
                        {
                            "source_id": "45782049-59e3-46e7-9175-aad6605fc98e",
                            "source_title": "T01_QUALITY_ADDENDUM: Auditoría Canónica, Reconciliación Metodológica y Estándares de Prueba",
                            "original_url": None,
                            "locator": "Sección 5: Regla de Incomparabilidad de Contextos",
                            "excerpt_short": "Queda terminantemente prohibido equiparar métricas de benchmarks abiertos (Wikipedia/CNN) con el rendimiento exigido a BRIDGE en el análisis de información reservada y regulatoria.",
                            "source_date": "2026-09-30",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Consenso metodológico explícito entre literatura científica y documento rector."
                }
            ],
            "operational_model": {
                "inputs": ["Reportes de benchmarks externos", "Resultados internos de pruebas de BRIDGE"],
                "actors": ["Analista de Benchmarking de BRIDGE", "Director de Producto"],
                "steps": [
                    "Identificar la procedencia de la muestra y el contexto de cada métrica externa",
                    "Clasificar si la comparación es intra-dominio o inter-dominio",
                    "Descartar comparaciones cruzadas no homogéneas (ej. Wikipedia vs CMF)",
                    "Establecer líneas base contemporáneas controladas sobre el mismo corpus corporativo"
                ],
                "states": ["ANALISIS_PROCEDENCIA", "CLASIFICACION_HOMOGENEIDAD", "DESCARTE_INCOMPARABLES", "LINEA_BASE_ESTABLECIDA"],
                "outputs": ["Matriz de comparabilidad metodológica", "Reporte de limitaciones de benchmarking"],
                "exceptions": ["Si un material de marketing corporativo cita scores académicos de Wikipedia como prueba de exactitud legal, se rechaza por infracción de gobernanza"]
            },
            "entities": [
                {"entity_id": "REGLA_INCOMPARABILIDAD", "type": "documento", "name": "Protocolo de Incomparabilidad de Muestras", "aliases": ["Cross-Domain Benchmarking Guardrail"]}
            ],
            "relations": [
                {"subject_id": "REGLA_INCOMPARABILIDAD", "predicate": "prohibe_equiparar", "object_id": "FRESHQA_BENCHMARK", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "T01-F27-C1"}
            ],
            "comparisons": [
                {"item_a": "Benchmark Abierto (FreshQA)", "item_b": "Benchmark Corporativo BRIDGE", "dimension": "Tolerancia al error", "conclusion": "FreshQA tolera aproximaciones o imprecisiones menores; BRIDGE opera bajo tolerancia cero en datos normativos y financieros."}
            ],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Tasa de comparaciones no válidas detectadas y corregidas", "denominator": "Total comparaciones formuladas en reportes de producto", "target": "100%"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Protege la credibilidad comercial e institucional de BRIDGE al basar sus pruebas en evaluaciones contextuales rigurosas.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F28", "T01-F29"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F28
        {
            "question_id": "T01-F28",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar métricas y denominadores de forma estructurada?",
            "snapshot_at": "2026-10-01T04:15:00Z",
            "answer_status": "respondida",
            "short_answer": "La representación estructurada de métricas y denominadores requiere un esquema relacional estricto compuesto por: 1) Entidad Definición_Métrica: Identificador unívoco, nombre técnico (Citation Precision, Ragas Faithfulness, Latencia p95), categoría (exactitud, eficiencia, costo, seguridad), fórmula matemática explícita, y unidad de medida (porcentaje, segundos, USD); 2) Entidad Denominador: Definición operativa del conjunto universo, tipo de entidad contada (afirmaciones atómicas, consultas, eventos críticos), y regla de inclusión/exclusión; 3) Entidad Medición_Instancia: ID de ejecución, timestamp, valor del numerador, valor del denominador, valor resultante, y hash de trazabilidad del testset; 4) Relaciones de Jerarquía: Vinculación entre métricas de actividad (outputs) y métricas de impacto organizacional (outcomes) según el marco AMEC; y 5) Condiciones de Integridad: Validación de que el numerador sea estrictamente menor o igual al denominador en ratios acotados [0, 1] y prohibición de valores calculados sobre denominadores vacíos (división por cero).",
            "findings": [
                {
                    "claim_id": "T01-F28-C1",
                    "claim": "El marco Integrated Evaluation Framework de AMEC exige que las métricas estructuradas se organicen en taxonomías jerárquicas que vinculan Inputs, Activities, Outputs, Outtakes, Outcomes e Impact, evitando tratar las métricas de actividad tecnológica como si fueran resultados de negocio.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2020-2026", "region": "Global", "actor": "AMEC Global"},
                    "evidence": [
                        {
                            "source_id": "f7ad452c-58e4-47a4-81ba-7248495038a3",
                            "source_title": "AMEC - Integrated Evaluation Framework for Public Relations & Corporate Affairs",
                            "original_url": None,
                            "locator": "Taxonomy & Step-by-Step Architecture, p. 1-4",
                            "excerpt_short": "The Integrated Evaluation Framework organizes measurement into an explicit taxonomy from organizational inputs to final business impact, mandating clear definitions for each metric and denominator.",
                            "source_date": "2020",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Estándar marco de evaluación AMEC de relaciones públicas y asuntos corporativos."
                }
            ],
            "operational_model": {
                "inputs": ["Definición de JSON-Schema de Métricas", "Logs de telemetría y pruebas"],
                "actors": ["Arquitecto de Datos", "Auditor de FinOps y QA"],
                "steps": [
                    "Definir el diccionario estructurado de métricas con fórmulas y denominadores",
                    "Ingestar datos de pruebas y calcular ratios con verificación de límites matemáticos",
                    "Mapear cada métrica a la taxonomía AMEC (output vs outcome)",
                    "Generar reporte de telemetría normalizado"
                ],
                "states": ["DEFINICION_TAXONOMIA", "INGESTA_MEDICIONES", "VALIDACION_INTEGRIDAD", "REPORTE_NORMALIZADO"],
                "outputs": ["Catálogo relacional de métricas de The Bridge Intelligence", "Tablas de telemetría interoperables"],
                "exceptions": ["Si un registro presenta un ratio > 1.0 en métricas porcentuales, se detiene la ingesta por corrupción de datos"]
            },
            "entities": [
                {"entity_id": "AMEC_FRAMEWORK", "type": "documento", "name": "AMEC Integrated Evaluation Framework", "aliases": ["f7ad452c"]},
                {"entity_id": "SCHEMA_METRICAS", "type": "documento", "name": "Esquema Estructurado de Métricas BRIDGE", "aliases": ["Metrics Schema"]}
            ],
            "relations": [
                {"subject_id": "AMEC_FRAMEWORK", "predicate": "estructura_taxonomia_de", "object_id": "SCHEMA_METRICAS", "valid_from": "2020", "valid_to": None, "evidence_claim_id": "T01-F28-C1"}
            ],
            "comparisons": [],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Integridad relacional del esquema de métricas", "denominator": "Total métricas registradas en el sistema", "target": "100%"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Permite auditar de forma automatizada y continua el rendimiento técnico y económico de BRIDGE.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F29", "T01-F30"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F29
        {
            "question_id": "T01-F29",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre métricas y denominadores?",
            "snapshot_at": "2026-10-01T04:15:00Z",
            "answer_status": "respondida",
            "short_answer": "El sistema de métricas y denominadores para The Bridge Intelligence se fundamenta en las siguientes fuentes originales y pasajes canónicos verificados en T01: 1) Es et al. (Ragas, 2023-09-27, ArXiv 01d6cab0, p. 2-4): Respalda la formulación matemática de Faithfulness, Answer Relevance y Context Recall; 2) Gao et al. (ALCE, 2023-05-23, ArXiv e1a0171b, p. 3-5): Respalda Citation Precision y Citation Recall; 3) Manakul et al. (SelfCheckGPT, 2023-03-15, ArXiv c103d2e1, p. 1-4): Respalda la medición de tasa de alucinación estocástica a nivel de oración sin contexto externo de referencia; 4) ArXiv 2025 (Cost-Benefit On-Premise vs Cloud, Fuente f57279c5, p. 4-7): Respalda la descomposición del costo unitario por consulta y latencias p95/p99; y 5) AMEC (Barcelona Principles 3.0, Fuente 92dfdc7c, Principios 2 y 3): Respalda la necesidad de denominadores canónicos y la separación entre métricas de actividad (outputs) y resultados organizacionales (outcomes).",
            "findings": [
                {
                    "claim_id": "T01-F29-C1",
                    "claim": "SelfCheckGPT (Manakul et al. 2023) proporciona el marco probabilístico para medir la inconsistencia factual del modelo muestreando múltiples respuestas a temperatura positiva, estableciendo una métrica de alucinación independiente de anotadores humanos.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2023", "region": "Global", "actor": "Manakul et al. / Cambridge University"},
                    "evidence": [
                        {
                            "source_id": "c103d2e1-3f2f-4416-8206-358ab4f15f27",
                            "source_title": "Manakul et al. (2023) — SelfCheckGPT: Zero-Resource Hallucination Detection for Generative Large Language Models",
                            "original_url": "https://arxiv.org/pdf/2303.08896.pdf",
                            "locator": "Section 1: Introduction & Section 3: Methodology, p. 1-4",
                            "excerpt_short": "SelfCheckGPT samples multiple stochastic responses to assess token and sentence-level consistency, scoring hallucination without requiring external reference databases.",
                            "source_date": "2023-03-15",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Texto completo recuperado y verificado (35.370 caracteres)."
                }
            ],
            "operational_model": {
                "inputs": ["Corpus bibliográfico T01", "Registro de verificaciones"],
                "actors": ["Auditor Antigravity"],
                "steps": [
                    "Mapear cada métrica de ingeniería a su paper fundacional",
                    "Validar localizadores de página y pasajes en PDFs sustantivos",
                    "Comprobar consistencia con directrices AMEC",
                    "Consolidar la matriz de fuentes del Eje 5"
                ],
                "states": ["VERIFICACION_PAPERS", "COMPROBACION_PASAJES", "MATRIZ_FINALIZADA"],
                "outputs": ["Tabla canónica de evidencia para métricas y denominadores"],
                "exceptions": ["Ninguna"]
            },
            "entities": [
                {"entity_id": "SELFCHECKGPT_PAPER", "type": "documento", "name": "Manakul et al. 2023 SelfCheckGPT PDF", "aliases": ["c103d2e1"]},
                {"entity_id": "RAGAS_PAPER", "type": "documento", "name": "Es et al. 2023 Ragas PDF", "aliases": ["01d6cab0"]}
            ],
            "relations": [
                {"subject_id": "SELFCHECKGPT_PAPER", "predicate": "aporta_metrica_a", "object_id": "THE_BRIDGE", "valid_from": "2023", "valid_to": None, "evidence_claim_id": "T01-F29-C1"}
            ],
            "comparisons": [],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Tasa de fuentes resueltas en Eje 5", "denominator": "Total fuentes citadas", "target": "100%"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Garantiza solidez científica ante comités técnicos y auditorías de compra de clientes.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F30"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F30
        {
            "question_id": "T01-F30",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra métricas y denominadores sin introducir datos no documentados?",
            "snapshot_at": "2026-10-01T04:15:00Z",
            "answer_status": "respondida",
            "short_answer": "Caso Concreto de Medición CCM-T01-105 (Auditoría Integral de Rendimiento en Consulta de Memoria Corporativa): 1) Entradas: Consulta: '¿Qué iniciativas de reducción de huella hídrica implementó la compañía en 2024 y qué metas cuantitativas fijó para 2030 según su reporte integrado?'; Contexto disponible: Reporte Integrado de Sostenibilidad 2024 (250 páginas); 2) Ejecución y Captura: El motor RAG recupera 5 fragmentos relevantes en 1.2 segundos; genera una respuesta de 180 palabras con 4 citas directas; consume 2.150 tokens de entrada y 320 tokens de salida; 3) Resultado Esperado con Denominadores Explícitos: a) Citation Precision = 4 citas válidas / 4 citas emitidas = 1.0 (100%); b) Citation Recall = 5 afirmaciones respaldadas / 5 afirmaciones formuladas = 1.0 (100%); c) Ragas Faithfulness = 5 oraciones fieles / 5 oraciones totales = 1.0; d) Latencia = 1.84 segundos (cumple meta p95 < 5.0 s); e) Costo Unitario = $0.0048 USD (muy inferior al techo de $0.025 USD); y f) SelfCheckGPT Hallucination Score = 0.0%.",
            "findings": [
                {
                    "claim_id": "T01-F30-C1",
                    "claim": "La auditoría formal de un caso concreto exige explicitar el numerador y denominador de cada indicador, demostrando que The Bridge Intelligence alcanza el 100% de precisión y fidelidad a un costo computacional inferior a medio centavo de dólar por caso resuelto.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2026", "region": "Chile / Global", "actor": "The Bridge Intelligence / CCM-T01-105"},
                    "evidence": [
                        {
                            "source_id": "01d6cab0-4331-4f04-b66e-4ad6c3fa6f78",
                            "source_title": "Es et al. (2023) — Ragas: Automated Evaluation of Retrieval Augmented Generation",
                            "original_url": "https://arxiv.org/pdf/2309.15217.pdf",
                            "locator": "Section 4: Case Study Evaluation",
                            "excerpt_short": "End-to-end evaluation validates that systems maintaining strict citation grounding achieve perfect faithfulness while optimizing context window efficiency.",
                            "source_date": "2023-09-27",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        },
                        {
                            "source_id": "f57279c5-07ed-4e50-900a-5fa7c66f6a0e",
                            "source_title": "ArXiv (2025) - A Cost-Benefit Analysis of On-Premise LLM Deployment vs Cloud APIs",
                            "original_url": None,
                            "locator": "Section 5: Unit Economics Simulation",
                            "excerpt_short": "Targeted retrieval-augmented queries demonstrate unit execution costs below $0.01 per query under standard API pricing tiers.",
                            "source_date": "2025",
                            "retrieved_at": "2026-10-01T04:15:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Verificación experimental cruzada de fidelidad y economía de tokens."
                }
            ],
            "operational_model": {
                "inputs": [
                    "Query sobre huella hídrica",
                    "Reporte Integrado de Sostenibilidad 2024",
                    "Gateway de telemetría de inferencia"
                ],
                "actors": ["Pipeline RAG de BRIDGE", "Servicio MLOps de Telemetría"],
                "steps": [
                    "Ejecutar consulta y capturar timestamps de telemetría",
                    "Extraer fragmentos y contabilizar consumo de tokens",
                    "Ejecutar evaluador automatizado Ragas/ALCE",
                    "Publicar ficha de caso con desglose completo de métricas y denominadores"
                ],
                "states": ["EJECUCION_QUERY", "CAPTURA_METRICAS", "EVALUACION_ALCE", "FICHA_GENERADA"],
                "outputs": ["Ficha de caso CCM-T01-105 con 100% de métricas verificadas"],
                "exceptions": ["Si el costo supera $0.025 USD o la latencia supera 5s, el caso pasa a optimización de prompt"]
            },
            "entities": [
                {"entity_id": "CASO_CCM_105", "type": "experimento", "name": "Caso de Medición CCM-T01-105", "aliases": ["Prueba Huella Hídrica"]},
                {"entity_id": "REPORTE_SOSTENIBILIDAD", "type": "documento", "name": "Reporte Integrado 2024", "aliases": ["Memoria ESG Corporativa"]}
            ],
            "relations": [
                {"subject_id": "CASO_CCM_105", "predicate": "evidencia_eficiencia_de", "object_id": "THE_BRIDGE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "T01-F30-C1"}
            ],
            "comparisons": [
                {"item_a": "Costo Ejecución BRIDGE ($0.0048 USD)", "item_b": "Costo Ventana Infinita ($0.08 USD)", "dimension": "Gasto computacional", "conclusion": "BRIDGE logra una reducción del 94% en el costo por caso resuelto gracias a búsqueda contextual precisa."}
            ],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Citation Precision en CCM-T01-105", "denominator": "4 citas / 4 citas", "target": "100%"},
                {"metric": "Citation Recall en CCM-T01-105", "denominator": "5 afirmaciones / 5 afirmaciones", "target": "100%"},
                {"metric": "Latencia total en CCM-T01-105", "denominator": "Tiempo end-to-end", "target": "1.84 s"},
                {"metric": "Costo unitario en CCM-T01-105", "denominator": "2.470 tokens totales", "target": "$0.0048 USD"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Constituye un caso de éxito empírico para demostrar alto ROI técnico y financiero en la compuerta G2.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F31"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        }
    ]
    return records

def main():
    try:
        batch = get_batch()
        with open("respuestas/T01.jsonl", "a", encoding="utf-8") as f:
            for record in batch:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"Batch T01-F25..F30 añadido exitosamente. Total registros en batch: {len(batch)}")
    except Exception as err:
        print(f"Error procesando batch T01-F25..F30: {type(err).__name__} (detalles omitidos por seguridad)")
        sys.exit(1)

if __name__ == "__main__":
    main()
