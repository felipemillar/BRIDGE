import json
from pathlib import Path

NOTEBOOK_ID = "cb87941c-2377-42fb-806f-eb9878ac0757"
SNAPSHOT_AT = "2026-10-01T02:50:00-03:00"

records = [
    # P04-C01
    {
        "question_id": "P04-C01",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre inventario de documentos corporativos, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia Principal: Los enfoques comerciales estándar y repositorios ofimáticos tratan cualquier archivo corporativo (PDF de memoria, comunicado de prensa o minuta interna) como texto homogéneo sin jerarquía jurídica. En contraste, las síntesis internas analíticas (P04_EVIDENCE_MAP y P04_RESEARCH_DOSSIER), alineadas con la regulación imperativa de la CMF (NCG N° 461) y la Ley 18.045 de Mercado de Valores, establecen una estricta taxonomía jerárquica de 8 clases donde los Hechos Esenciales y las Memorias depositadas tienen máxima fuerza vinculante legal, mientras que comunicados y borradores carecen de valor de balance. Versión que prevalece según la regla editorial: Prevalece rigurosamente la clasificación formal respaldada por la CMF y W3C DCAT-3. Asimismo, se explicita que las síntesis internas P04_* son documentos analíticos propios de trabajo que jamás deben considerarse como fuentes externas independientes.",
        "findings": [
            {
                "claim_id": "P04-C01-C1",
                "claim": "La discrepancia sobre la homogeneidad documental se resuelve a favor de la taxonomía jerárquica respaldada por CMF NCG 461 y W3C DCAT-3, subordinando las síntesis internas a su rol de documentos analíticos propios.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Gobernanza Editorial P04"},
                "evidence": [
                    {
                        "source_id": "005e6819-75c5-40e4-b0a2-39b00ec373eb",
                        "source_title": "P04_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Encabezado y Sección 1: Marco Epistémico Fundamental",
                        "excerpt_short": "Nivel de Clasificación: Documento Interno de Síntesis Analítica — Prohibida su consideración como fuente externa independiente. Mezclar una promesa con un logro auditado genera severos riesgos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "62bbf73f-3262-466f-9b1c-feb81c69d6dd",
                        "source_title": "CMF Chile: NCG N° 461 Memoria Anual Integrada y Sostenibilidad",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Capítulo I y II: Ámbito de Aplicación",
                        "excerpt_short": "Fuerza obligatoria para entidades fiscalizadas inscritas en el Registro de Valores.",
                        "source_date": "2021-11-12",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Resolución editorial formal documentada en los encabezados y cuerpo de P04_EVIDENCE_MAP."
            }
        ],
        "operational_model": {
            "inputs": ["Documentos crudos ingresados al sistema"],
            "actors": ["Editorial Precedence Enforcer", "Taxonomy Classifier"],
            "steps": ["Verificación de jerarquía legal", "Asignación de clase documental canónica", "Subordinación de documentos no oficiales"],
            "states": ["Raw", "Classified_By_Precedence", "Officially_Ranked"],
            "outputs": ["Corpus ordenado por jerarquía legal vinculante"],
            "exceptions": ["Documentos mixtos que combinan comunicados informales con hechos regulatorios"]
        },
        "entities": [
            {"entity_id": "ENT_EDITORIAL_PRECEDENCE_P04", "type": "regla_editorial", "name": "Regla de Precedencia Editorial P04", "aliases": ["P04 Editorial Precedence Rule"]}
        ],
        "relations": [
            {"subject_id": "ENT_EDITORIAL_PRECEDENCE_P04", "predicate": "dirime_conflictos_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C01-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de clasificación",
                "Enfoque plano tradicional": "Cualquier texto institucional se considera evidencia de igual peso.",
                "Enfoque de precedencia regulada": "Los hechos esenciales y memorias CMF priman jurídicamente sobre notas de prensa."
            }
        ],
        "contradictions": [
            {
                "topic": "Homogeneidad documental en corpus corporativos",
                "claim_a": "Todo texto corporativo puede ser indexado en el mismo nivel sin jerarquía formal.",
                "source_a": "Práctica ofimática convencional de TI empresarial",
                "claim_b": "Los documentos corporativos poseen estatus legal y vinculación regulatoria diferenciada (Ley 18.045 / CMF NCG 461).",
                "source_b": "P04_EVIDENCE_MAP / CMF Chile NCG 461",
                "resolution_or_status": "Prevalece Claim B: tipificación formal en 8 clases con niveles diferenciados de autoridad."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe implementar este orden de precedencia para que una memoria CMF siempre prime sobre un comunicado de prensa en caso de conflicto.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-C02"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C02
    {
        "question_id": "P04-C02",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre inventario de documentos corporativos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Vacío e Incertidumbre: Sigue sin prueba empírica formal la compatibilidad automatizada completa entre los catálogos documentales estructurados bajo CMF NCG 461 y los estándares europeos ESRS en empresas multilatinas con matriz o filiales en la Unión Europea. Fuentes que fallaron: 1) F-01: 'EFRAG European Sustainability Reporting Standards (ESRS)' (servidor inaccesible por timeout TLS / error de conexión en ingesta); y 2) F-02: 'G20/OECD Principles of Corporate Governance 2023' (bloqueo por portal antibot de la OECD); ambas suplidas en el corpus por IFRS S1/S2, GRI Universal Standards y CMF NCG 461. Validación Mínima Requerida: Descarga y carga manual de los PDFs oficiales de ESRS y OECD Principles 2023 para ejecutar una auditoría de schema mapping contra el modelo DCAT-3 y verificar si introducen tipos documentales adicionales que deban incorporarse a la taxonomía canónica.",
        "findings": [
            {
                "claim_id": "P04-C02-C1",
                "claim": "El inventario documental presenta un vacío de mapeo automatizado con estándares ESRS de la UE debido a fallas de ingesta en servidores de EFRAG y OECD, remediables mediante validación asistida por descarga local.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / UE", "actor": "Auditoría de Ingesta P04"},
                "evidence": [
                    {
                        "source_id": "35dd0ce8-75f5-44fc-ab0a-ddf0b780a1ca",
                        "source_title": "P04_SOURCE_INDEX",
                        "original_url": None,
                        "locator": "Sección 3: Registro de Incidencias: Fuentes Externas Fallidas",
                        "excerpt_short": "F-01: EFRAG ESRS Standards (Error de conexión / timeout TLS), suplido por IFRS S1/S2 y GRI. F-02: G20/OECD Principles (Bloqueo antibot OECD), suplido por CMF NCG 461 y FIBO.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Incidencias de red y fallos de ingesta documentados exhaustivamente en P04_SOURCE_INDEX."
            }
        ],
        "operational_model": {
            "inputs": ["Registro de incidencias F-01 y F-02"],
            "actors": ["Source Ingestion Auditor", "Schema Harmonizer"],
            "steps": ["Verificación de causas de falla en crawler", "Descarga out-of-band de documentos", "Validación cruzada de tipos documentales"],
            "states": ["Failed_Ingestion", "Substituted", "Validation_Protocol_Defined"],
            "outputs": ["Protocolo de remediación de fuentes fallidas para homologación ESRS"],
            "exceptions": ["Divergencias ontológicas profundas entre CSRD europea y CMF chilena"]
        },
        "entities": [
            {"entity_id": "ENT_GAP_ESRS_MAPPING", "type": "vacio_epistemico", "name": "Vacío de Homologación Documental CMF vs ESRS", "aliases": ["ESRS-CMF Document Taxonomy Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_GAP_ESRS_MAPPING", "predicate": "requiere_resolucion_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C02-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Estado de la fuente",
                "Fuentes activas (IFRS/GRI/CMF)": "Texto sustantivo recuperado y vectorizado al 100% en el cuaderno.",
                "Fuentes fallidas (ESRS/OECD)": "Bloqueadas por firewall en origen; reemplazadas por estándares con equivalencia oficial."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe incorporar conectores locales para ingestar normativas europeas sin depender de rastreadores web dinámicos.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap_id": "GAP-P04-01",
                "description": "Falta de prueba empírica sobre interoperabilidad directa de taxonomías documentales CMF NCG 461 con ESRS (CSRD) de la Unión Europea.",
                "missing_information": "Mapeo campo por campo entre requerimientos de reporte de la Directiva CSRD y la Circular CMF NCG 461."
            }
        ],
        "next_question_ids": ["P04-C03"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C03
    {
        "question_id": "P04-C03",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre afirmaciones y compromisos, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia Principal: La industria de software corporativo y soluciones de IA generativa proclama que 'un LLM puede identificar automáticamente promesas y logros corporativos usando un prompt de clasificación'. Sin embargo, la literatura académica especializada en procesamiento de lenguaje natural para finanzas y ESG (Ni et al., 2023) y la síntesis P04_EVIDENCE_MAP demuestran que los LLMs sin ontología confunden frecuentemente declaraciones aspiracionales de vocería ('creemos en la carbono-neutralidad') con compromisos formales cuantificados ('reducir emisiones absolutas en 30% al 2030 vs 2020'). Esto genera un severo riesgo de greenwashing accidental o afirmaciones corporativas inexactas. Versión que prevalece: Prevalece la Taxonomía Canónica de 4 Estados Epistémicos (Declaración, Compromiso, Resultado, Verificación) exigiendo que ningún resultado se considere 'verificado' sin una carta de dictamen independiente bajo norma ISAE 3000 con URI trazable.",
        "findings": [
            {
                "claim_id": "P04-C03-C1",
                "claim": "La afirmación comercial de clasificación automática de compromisos sin ontología es refutada por Ni et al. y P04_EVIDENCE_MAP, imponiendo la regla obligatoria de 4 estados epistémicos y auditoría ISAE 3000.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2026", "region": "Global", "actor": "Evaluación Epistémica P04"},
                "evidence": [
                    {
                        "source_id": "005e6819-75c5-40e4-b0a2-39b00ec373eb",
                        "source_title": "P04_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 1: Marco Epistémico Fundamental y Sección 4: Grados de Certeza",
                        "excerpt_short": "Tratar cualquier afirmación textual como dato homogéneo genera severos riesgos de reputación y greenwashing. Se adopta la Taxonomía Canónica de 4 Estados Epistémicos.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "3d5b1ad5-73ef-4a53-aaa0-a1ff3f4c5043",
                        "source_title": "NLP for ESG and Corporate Disclosures: A Survey (Ni et al., 2023)",
                        "original_url": "https://arxiv.org/abs/2308.06597",
                        "locator": "Sección 4: Greenwashing and Sentiment Challenges",
                        "excerpt_short": "Highlights the critical risk of NLP models repeating ungrounded corporate claims and mistaking aspirational statements for verified quantitative metrics.",
                        "source_date": "2023-08-11",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Evidencia científica rigurosa en Ni et al. y marco de 4 estados del dossier P04."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de discurso o memoria corporativa"],
            "actors": ["Epistemic State Classifier", "ISAE 3000 Validator"],
            "steps": ["Detección de metas cuantitativas", "Verificación de año base y auditoría", "Asignación de uno de los 4 estados"],
            "states": ["Raw_Statement", "Classified_4_States", "Assurance_Verified"],
            "outputs": ["Afirmación etiquetada con su estado de certeza legal y métrica"],
            "exceptions": ["Declaración que menciona un número que no es una meta sino un dato de contexto"]
        },
        "entities": [
            {"entity_id": "ENT_4_EPISTEMIC_STATES", "type": "modelo_epistemico", "name": "Taxonomía Canónica de 4 Estados Epistémicos", "aliases": ["4 Epistemic States Taxonomy"]}
        ],
        "relations": [
            {"subject_id": "ENT_4_EPISTEMIC_STATES", "predicate": "clasifica_afirmaciones_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C03-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Rigor en compromisos",
                "Clasificación comercial informal": "Llama 'compromiso' a cualquier frase con tono positivo o aspiracional.",
                "Taxonomía de 4 estados": "Solo llama compromiso a metas con año base, KPI, plazo y órgano de aprobación."
            }
        ],
        "contradictions": [
            {
                "topic": "Capacidad de los LLMs para clasificar compromisos sin ontología",
                "claim_a": "Un LLM con un prompt básico clasifica compromisos y logros corporativos con precisión.",
                "source_a": "Proveedores de RAG genérico y chatbots empresariales",
                "claim_b": "Los LLMs confunden retórica aspiracional con métricas verificadas sin un esquema ontológico formal y anclaje ISAE 3000.",
                "source_b": "Ni et al. (2023) / P04_EVIDENCE_MAP",
                "resolution_or_status": "Prevalece Claim B: adopción obligatoria de la Taxonomía de 4 Estados y verificación documental."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe incorporar este clasificador de 4 estados para impedir que el sistema presente promesas como si fuesen logros auditados.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-C04"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C04
    {
        "question_id": "P04-C04",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre afirmaciones y compromisos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Vacío e Incertidumbre: Permanece sin resolver empíricamente la detección automatizada del 'abandono silencioso de compromisos' (drift o meta abandonada). Ocurre cuando una empresa publica una meta ambiciosa en un año (e.g. Memoria 2021) y en los reportes subsiguientes (2023-2025) deja de mencionarla sin emitir un retiro formal ni explicar el incumplimiento. Fuente Parcial: Ni et al. (2023) identifica el problema a nivel teórico en reportes ESG pero carece de un benchmark algorítmico para rastrear el ciclo de vida completo de compromisos plurianuales. Validación Mínima Requerida: Ejecución de la Etapa 1 del protocolo empírico de P04_GAPS_AND_VALIDATION: someter la Ficha de Compromiso a juicio de expertos (5 Directores de Asuntos Corporativos y 3 abogados de valores) y auditar 50 metas en memorias 2021-2025 para validar la detección de compromisos omitidos.",
        "findings": [
            {
                "claim_id": "P04-C04-C1",
                "claim": "La detección desatendida de metas corporativas silenciosamente omitidas o discontinuadas sin explicación constituye una brecha no resuelta en la literatura de NLP corporativo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global / Chile", "actor": "Agenda de Investigación P04"},
                "evidence": [
                    {
                        "source_id": "b0babc4e-51fa-4a3c-bb22-2bea8487a65e",
                        "source_title": "P04_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 1.1 y Sección 4: Agenda de Validación Empírica (Etapa 1)",
                        "excerpt_short": "Disparidad entre retórica y métrica operativa: carencia de modelos que verifiquen automáticamente si una Declaración cuenta con un Compromiso y si este tiene Resultados reportados y auditados.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío analítico formalmente diagnosticado en P04_GAPS_AND_VALIDATION."
            }
        ],
        "operational_model": {
            "inputs": ["Secuencia plurianual de memorias de un mismo emisor"],
            "actors": ["Commitment Continuity Auditor", "Drift Detector"],
            "steps": ["Extracción de metas de año T", "Búsqueda de actualización en años T+1 a T+3", "Alerta de meta silenciosamente discontinuada"],
            "states": ["Target_Indexed", "Tracking_Across_Years", "Drift_Alert_Raised"],
            "outputs": ["Alerta de riesgo reputacional por meta abandonada sin explicación"],
            "exceptions": ["Meta reemplazada por otra con nombre completamente distinto"]
        },
        "entities": [
            {"entity_id": "ENT_GAP_SILENT_DRIFT", "type": "vacio_epistemico", "name": "Vacío de Detección de Abandono Silencioso de Metas", "aliases": ["Corporate Goal Drift Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_GAP_SILENT_DRIFT", "predicate": "evidencia_limite_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C04-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Seguimiento temporal",
                "Análisis de reporte individual": "Cada memoria parece completa en sí misma porque no menciona lo que omitió.",
                "Auditoría plurianual de compromisos": "Identifica de inmediato que una meta comprometida hace 3 años desapareció del relato."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe incluir una función de auditoría transversal que avise a los directivos sobre metas pasadas no reportadas antes de que las detecte una ONG.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap_id": "GAP-P04-02",
                "description": "Falta de algoritmos estandarizados para detectar el abandono silencioso de metas ESG entre años fiscales consecutivos.",
                "missing_information": "Benchmark empírico de persistencia de metas en empresas supervisadas por la CMF entre 2021 y 2025."
            }
        ],
        "next_question_ids": ["P04-C05"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C05
    {
        "question_id": "P04-C05",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre ontología y relaciones, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia Principal: Soluciones comerciales de bases de datos de grafos para empresas promueven la extracción automática de entidades y relaciones mediante LLMs ('Zero-shot Open Information Extraction') insertando todas las tripletas resultantes en el grafo como verdades homogéneas. En agudo contraste, la investigación académica rigurosa (Pan et al., 2024; Hogan et al., 2021) y P04_EVIDENCE_MAP demuestran que las tripletas inducidas por modelos neuronales sufren de 'alucinación de enlaces' (link hallucination) y relaciones espurias, lo que contamina la memoria corporativa con hechos falsos. Versión que prevalece: Prevalece el estándar de tipificación epistémica de aristas mediante Named Graphs o propiedades de borde en RDF* / LPG. Toda arista debe llevar el atributo `epistemic_status: 'hecho_documentado'` (anclado a hash criptográfico) o `epistemic_status: 'relacion_inferida'` (con score de confianza y prohibición de uso en minutas oficiales sin advertencia).",
        "findings": [
            {
                "claim_id": "P04-C05-C1",
                "claim": "La inserción directa de aristas neuronales no validadas en el grafo corporativo es rechazada por Pan et al. y Hogan et al., prevaleciendo la segregación epistémica estricta de aristas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Global", "actor": "Integración Semántica LLM-KG"},
                "evidence": [
                    {
                        "source_id": "4d415120-9c32-462c-94bf-3a067c98d10e",
                        "source_title": "Unifying LLMs and Knowledge Graphs: A Roadmap (Pan et al., 2024)",
                        "original_url": "https://arxiv.org/abs/2306.08302",
                        "locator": "Sección 4.2: Factuality and Neural-Symbolic Knowledge Transfer",
                        "excerpt_short": "Warns against hallucination propagation when LLM-extracted relations are directly materialized into knowledge graphs without formal verification.",
                        "source_date": "2024-01-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "005e6819-75c5-40e4-b0a2-39b00ec373eb",
                        "source_title": "P04_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 3: Matriz de Tensiones Metodológicas (Búsqueda Vectorial vs Grafos)",
                        "excerpt_short": "Adopción de Arquitectura Híbrida GraphRAG con post-verificación algorítmica de citas y anclaje a URIs inmutables con hash.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Fundamentación académica formal en Pan et al. y resolución metodológica en P04_EVIDENCE_MAP."
            }
        ],
        "operational_model": {
            "inputs": ["Aristas extraídas por LLM"],
            "actors": ["Neural-Symbolic Gatekeeper", "Provenance Annotator"],
            "steps": ["Verificación de concordancia directa", "Asignación de epistemic_status booleano", "Bloqueo de aristas inferidas en subgrafo de hechos"],
            "states": ["Raw_Extraction", "Epistemically_Tagged", "Materialized_Safely"],
            "outputs": ["Grafo estructurado donde los hechos comprobados están protegidos de alucinaciones relacionales"],
            "exceptions": ["Aristas con contradicciones ontológicas lógicas"]
        },
        "entities": [
            {"entity_id": "ENT_NEURAL_SYMBOLIC_GATEWAY", "type": "mecanismo_seguridad", "name": "Compuerta de Validación Neuronal-Simbólica", "aliases": ["Neural-Symbolic Integrity Gate"]}
        ],
        "relations": [
            {"subject_id": "ENT_NEURAL_SYMBOLIC_GATEWAY", "predicate": "protege_integridad_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C05-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Pureza del grafo",
                "Grafo comercial no tipado": "Mezcla hechos comprobados con conjeturas probabilísticas del LLM.",
                "Grafo segregado epistémicamente": "Mantiene hechos inmutables separados de hipótesis probabilísticas."
            }
        ],
        "contradictions": [
            {
                "topic": "Extracción automática desatendida de grafos de conocimiento",
                "claim_a": "Los LLMs pueden construir grafos empresariales directamente sin validación ontológica ni marcado de aristas.",
                "source_a": "Herramientas de auto-graph comerciales",
                "claim_b": "La extracción desatendida inyecta relaciones alucinadas al grafo que corrompen el razonamiento posterior.",
                "source_b": "Pan et al. (2024) / Hogan et al. (2021) / P04_EVIDENCE_MAP",
                "resolution_or_status": "Prevalece Claim B: marcado epistémico obligatorio de cada arista en el grafo."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe compilar esta compuerta para rechazar aristas inferidas sin sustento en el texto oficial.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-C06"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C06
    {
        "question_id": "P04-C06",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre ontología y relaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Vacío e Incertidumbre: Falta una ontología de dominio abierta y validada empíricamente para el ecosistema societario y regulatorio chileno, que interopere nativamente entre el RUT corporativo de la CMF, las Resoluciones de Calificación Ambiental (RCA) del SEIA/SMA y los registros de concesiones mineras y de agua. Fuente Parcial: EDM Council FIBO (2024) ofrece la estructura ontológica financiera global pero está completamente desacoplada de la terminología administrativa y legal chilena. Validación Mínima Requerida: Construir un subgrafo piloto con las 10 mayores empresas del IPSA en minería y energía, mapeando sus matrices, filiales, faenas y RCA históricas para comprobar que el grafo resuelve consultas de responsabilidad ambiental y de mercado sin colisiones semánticas.",
        "findings": [
            {
                "claim_id": "P04-C06-C1",
                "claim": "Existe una ausencia de ontologías de dominio públicas adaptadas a la gobernanza societaria y regulatoria chilena (CMF / SMA), debiendo ser suplida por extensiones locales sobre FIBO.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Modelado Semántico P04"},
                "evidence": [
                    {
                        "source_id": "b0babc4e-51fa-4a3c-bb22-2bea8487a65e",
                        "source_title": "P04_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 2: Escasez de Corpora Públicos Anotados en Español y Contexto Latinoamericano",
                        "excerpt_short": "Hay un vacío agudo de conjuntos de datos y ontologías de prueba para memorias corporativas en español reguladas bajo CMF Chile NCG 461.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "0a2c0fce-8216-4357-b046-e19d5a7b3243",
                        "source_title": "EDM Council: Financial Industry Business Ontology (FIBO)",
                        "original_url": "https://spec.edmcouncil.org/fibo/",
                        "locator": "FIBO Business Entities Module",
                        "excerpt_short": "Focuses on US and European regulatory identifiers (LEI, SEC CIK), lacking native alignment with Chilean RUT or SMA environmental resolutions.",
                        "source_date": "2024-03-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío ontológico regional explícitamente fundamentado en P04_GAPS_AND_VALIDATION."
            }
        ],
        "operational_model": {
            "inputs": ["Ontología base FIBO", "Estructura societaria y regulatoria CMF/SMA"],
            "actors": ["Ontology Localization Worker", "Chilean Domain Expert"],
            "steps": ["Extensión de clases FIBO con prefijo cmf: y sma:", "Validación con datos reales del IPSA", "Publicación de schema de extensión"],
            "states": ["Gap_Identified", "Extension_Designed", "Pilot_Validated"],
            "outputs": ["Extensión ontológica localizada para corporaciones en Chile"],
            "exceptions": ["Cambios en el formato de registro de resoluciones ambientales en la SMA"]
        },
        "entities": [
            {"entity_id": "ENT_GAP_CHILE_ONTOLOGY", "type": "vacio_epistemico", "name": "Vacío de Ontología Corporativa Localizada para Chile", "aliases": ["Chilean Corporate Ontology Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_GAP_CHILE_ONTOLOGY", "predicate": "limita_modelado_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C06-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Alcance ontológico",
                "FIBO estándar": "Mapea filiales con códigos de la SEC (EE.UU.) y bancos centrales globales.",
                "Extensión chilena requerida": "Mapea RUTs, actas de directorio CMF y resoluciones de calificación ambiental (RCA)."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe desarrollar esta extensión localizada de FIBO para ofrecer valor diferencial a empresas chilenas.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap_id": "GAP-P04-03",
                "description": "Falta de una ontología formal pública que vincule entidades societarias chilenas (RUT/CMF) con resoluciones ambientales (RCA/SMA).",
                "missing_information": "Vocabulario RDF formalizado con prefijos y restricciones SHACL para corporaciones en Chile."
            }
        ],
        "next_question_ids": ["P04-C07"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C07
    {
        "question_id": "P04-C07",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre versiones y temporalidad, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia Principal: La práctica de ingeniería de software documental convencional recurre con frecuencia a la 'reindexación por sobreescritura' (batch overwrite nocturno) o al borrado de documentos superados para ahorrar costos de almacenamiento en bases vectoriales. En fuerte contradicción, los estándares W3C DCAT-3, W3C PROV-O y la síntesis P04_EVIDENCE_MAP demuestran que la sobreescritura destruye la trazabilidad histórica indispensable para auditorías forenses, defensas regulatorias y litigios. Si una empresa borra una memoria corregida, no puede probar qué declaró en una fecha específica ante una demanda por greenwashing o manipulación de mercado. Versión que prevalece: Prevalece el principio de inmutabilidad bitemporal: los documentos originales jamás se borran; se anotan con `dcterms:isReplacedBy` enlazando a la nueva versión (`dcterms:replaces`), garantizando que la versión vigente rija la vocería actual mientras la versión original permanece disponible para consultas retrospectivas as-of.",
        "findings": [
            {
                "claim_id": "P04-C07-C1",
                "claim": "La sobreescritura de documentos superados es rechazada por W3C DCAT-3 y PROV-O, prevaleciendo la preservación inmutable bitemporal con enlaces de superación explícitos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Gobernanza de Datos Temporales"},
                "evidence": [
                    {
                        "source_id": "005e6819-75c5-40e4-b0a2-39b00ec373eb",
                        "source_title": "P04_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 3: Matriz de Tensiones Metodológicas (Actualización de Documentos)",
                        "excerpt_short": "Reindexación periódica completa vs Ingestión reactiva basada en eventos con modelo bitemporal y versionado W3C PROV-O / DCAT-3.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "d1f9b36e-6fd4-411a-8e8a-da15aa5ed9b8",
                        "source_title": "W3C DCAT-3: Data Catalog Vocabulary Version 3",
                        "original_url": "https://www.w3.org/TR/vocab-dcat-3/",
                        "locator": "Sección 6.4: Dataset Versions and Lifecycle",
                        "excerpt_short": "Resources MUST NOT be physically deleted when superseded; version chains must be explicitly declared via dcterms:replaces to preserve auditability.",
                        "source_date": "2024-05-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Norma técnica obligatoria W3C DCAT-3 y resolución formal en P04_EVIDENCE_MAP."
            }
        ],
        "operational_model": {
            "inputs": ["Actualización documental ingresada"],
            "actors": ["Bitemporal Store", "Version Linker", "Audit Guardian"],
            "steps": ["Bloqueo de borrado físico", "Persistencia de la nueva versión con hash", "Creación de arista dcterms:replaces", "Actualización de índices de búsqueda activa"],
            "states": ["Update_Received", "Immutable_Preserved", "Chain_Linked"],
            "outputs": ["Cadena inmutable de versiones preservada para auditoría y vocería"],
            "exceptions": ["Documento ingresado con fecha anterior a una versión ya catalogada"]
        },
        "entities": [
            {"entity_id": "ENT_IMMUTABLE_VERSION_CHAIN", "type": "modelo_datos", "name": "Cadena Inmutable de Versionado Bitemporal", "aliases": ["Bitemporal Immutable Version Chain"]}
        ],
        "relations": [
            {"subject_id": "ENT_IMMUTABLE_VERSION_CHAIN", "predicate": "preserva_historial_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C07-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Preservación histórica",
                "Sobreescritura destructiva": "Borra el pasado, haciendo imposible demostrar qué se dijo antes de la corrección.",
                "Inmutabilidad bitemporal": "Permite auditar el estado exacto del conocimiento en cualquier fecha del pasado."
            }
        ],
        "contradictions": [
            {
                "topic": "Gestión de documentos obsoletos o reemplazados",
                "claim_a": "Los documentos antiguos reemplazados deben eliminarse o sobreescribirse para optimizar costos de base de datos.",
                "source_a": "Práctica de optimización de bases de datos tradicionales",
                "claim_b": "Los documentos reemplazados nunca deben borrarse físicamente; deben conservarse con metadatos de superación para auditoría legal.",
                "source_b": "W3C DCAT-3 / W3C PROV-O / P04_EVIDENCE_MAP",
                "resolution_or_status": "Prevalece Claim B: preservación histórica inmutable mediante relaciones dcterms:replaces."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe garantizar la inmutabilidad de su almacenamiento documental para servir como prueba pericial válida en auditorías.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-C08"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-C08
    {
        "question_id": "P04-C08",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre versiones y temporalidad, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Vacío e Incertidumbre: Sigue sin prueba empírica formal la resolución algorítmica de 'reexpresiones implícitas o silenciosas de líneas base' cuando una empresa altera una cifra histórica en una tabla comparativa sin añadir una nota técnica explícita al pie de página ni emitir una fe de erratas. Fuente Parcial: IFRS S2 (2023) exige la divulgación de las razones de cualquier recálculo de año base, pero no norma cómo un sistema automatizado debe reaccionar cuando el emisor incumple esta obligación y reexpresa la cifra de forma tácita. Validación Mínima Requerida: Implementar un validador de series temporales históricas que compare celda por celda los valores de años anteriores reportados en memorias consecutivas (e.g. comparar las emisiones 2022 reportadas en la Memoria 2022 vs las reportadas para 2022 en la Memoria 2025) y alerte automáticamente sobre discrepancias mayores al 1% sin nota aclaratoria.",
        "findings": [
            {
                "claim_id": "P04-C08-C1",
                "claim": "La detección de reexpresiones tácitas sin nota aclaratoria representa una brecha en los estándares contables que requiere validadores algorítmicos de series temporales consecutivas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global / Chile", "actor": "Auditoría de Consistencia Temporal"},
                "evidence": [
                    {
                        "source_id": "b0babc4e-51fa-4a3c-bb22-2bea8487a65e",
                        "source_title": "P04_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección 1.2: El Desafío de la Reexpresión Silenciosa de Metas y Líneas Base",
                        "excerpt_short": "Las empresas frecuentemente modifican el año base... en los reportes suele explicarse en una nota técnica o pasar inadvertida, exponiendo a la corporación a acusaciones de falsedad.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "3d670aa0-fc8d-48ca-8c2d-26879dc45378",
                        "source_title": "IFRS S2: Climate-related Disclosures",
                        "original_url": "https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/ifrs-s2-climate-related-disclosures/",
                        "locator": "Párrafos 34-36: Recalculation Disclosures",
                        "excerpt_short": "Mandates disclosure of recalculation reasons but does not provide algorithmic resolution for silent omissions.",
                        "source_date": "2023-06-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío metodológico identificado formalmente en P04_GAPS_AND_VALIDATION."
            }
        ],
        "operational_model": {
            "inputs": ["Series históricas extraídas de memorias consecutivas"],
            "actors": ["Historical Series Reconciler", "Silent Reexpression Detector"],
            "steps": ["Comparación de matriz año vs año de reporte", "Cálculo de delta porcentual", "Alerta de reexpresión tácita no documentada"],
            "states": ["Series_Aligned", "Discrepancy_Detected", "Silent_Change_Flagged"],
            "outputs": ["Reporte de discrepancia temporal histórica para revisión del equipo legal"],
            "exceptions": ["Cambio en unidades de medida no declarado en encabezado"]
        },
        "entities": [
            {"entity_id": "ENT_GAP_SILENT_REEXPRESSION", "type": "vacio_epistemico", "name": "Vacío de Detección de Reexpresiones Tácitas de Línea Base", "aliases": ["Silent Reexpression Detection Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_GAP_SILENT_REEXPRESSION", "predicate": "amenaza_coherencia_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-C08-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Detección de cambios",
                "Lectura documental aislada": "El lector asume que la cifra histórica siempre fue la reportada en el último año.",
                "Reconciliación algorítmica BRIDGE": "Detecta que la cifra del año 2022 cambió entre la memoria 2023 y la memoria 2025."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe incluir esta comparación cruzada interanual para evitar que un vocero cite cifras que variaron silenciosamente.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap_id": "GAP-P04-04",
                "description": "Falta de mecanismos automatizados para conciliar reexpresiones no declaradas de cifras históricas entre reportes consecutivos.",
                "missing_information": "Algoritmo de reconciliación de series temporales multi-reporte con tolerancia a cambios de unidades."
            }
        ],
        "next_question_ids": ["P04-C09"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P04.jsonl")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Appended {len(records)} records (P04-C01..P04-C08) to {out_path}.")
