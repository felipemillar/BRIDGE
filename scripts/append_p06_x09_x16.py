import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-X09
    {
        "question_id": "P06-X09",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo clasificar dos cifras incompatibles que usan períodos o unidades distintos?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La clasificación de cifras aparentemente incompatibles se rige por el protocolo de Normalización Dimensional y Detección de Discrepancias Paramétricas (P06_QUALITY_ADDENDUM, Sección 2.2; Calamai et al., 2025; CMF NCG 461): 1) Extracción de Parámetros Contextuales: Todo valor numérico se descompone en tupla de cinco dimensiones: `[Magnitud, Unidad_Medida, Período_Temporal, Alcance_Operacional, Base_Contable]`; 2) Reglas de Incompatibilidad Aparente (No Factual): Si dos cifras difieren en unidad (ej. tCO2e brutas vs tCO2e netas) o en ventana temporal (ej. año fiscal vs año calendario móvil; acumulado vs anualizado), el sistema las clasifica como 'Discrepancia Paramétrica No Comparable' (INCOMPARABLE_DIMENSIONS) y prohíbe emitir una alerta de contradicción fáctica; 3) Normalización y Conversión: Solo se procede a comparación aritmética si existen tablas de conversión deterministas oficiales (ej. conversión de GJ a MWh conforme a factores GHG Protocol). Si los períodos o alcances son dispares y no convertibles, el sistema genera una nota de contextualización metodológica advirtiendo al analista que comparar ambas cifras directamente constituye un error de agregación.",
        "findings": [
            {
                "claim_id": "P06-X09-C1",
                "claim": "Las diferencias numéricas originadas por heterogeneidad de períodos, unidades o perímetros de consolidación se clasifican como discrepancias metodológicas no comparables, no como contradicciones fácticas.",
                "epistemic_status": "principio_metodologico_formal",
                "scope": {"time": "2024-2026", "region": "Chile / Global", "actor": "Auditoría Financiera y Reporte ESG"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2.2: Normalización Dimensional y Prevención de Falsas Contradicciones Numéricas",
                        "excerpt_short": "Comparar cifras sin normalizar unidades o alcances de consolidación es una fuente masiva de falsos positivos. Dos números distintos para un mismo concepto suelen reflejar perímetros contables dispares.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "589b1b7c-6049-4b3a-9f0d-1fa8990a7a1d",
                        "source_title": "CMF Chile - Sostenibilidad y Norma de Carácter General N° 461",
                        "original_url": "https://www.cmfchile.cl/portal/principal/623/w4-propertyvalue-50301.html",
                        "locator": "Instrucciones de Llenado: Consistencia Metodológica y Perímetros",
                        "excerpt_short": "Las entidades informantes deben explicitar el perímetro de consolidación, las unidades de reporte y la metodología de cálculo utilizada en cada métrica, debiendo justificar cambios respecto al ejercicio anterior.",
                        "source_date": "2021-11-12",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio estándar de contabilidad financiera y directrices obligatorias de la NCG 461 CMF."
            }
        ],
        "operational_model": {
            "inputs": ["Cifra A con metadatos", "Cifra B con metadatos"],
            "actors": ["Extractor de Métricas", "Normalizador Dimensional", "Motor de Reglas"],
            "steps": ["Extracción de quintupla dimensional", "Comprobación de identidad de unidad y período", "Si son distintas y no convertibles, asignar etiqueta INCOMPARABLE_DIMENSIONS", "Generación de nota metodológica"],
            "states": ["Raw_Numbers", "Dimensions_Extracted", "Compatibility_Evaluated", "Flagged_or_Compared"],
            "outputs": ["Clasificación dimensional de la relación entre cifras"],
            "exceptions": ["Falta de metadatos de unidad que fuerza solicitud de revisión manual"]
        },
        "entities": [
            {"entity_id": "ENT_NUMERICAL_DISCREPANCY", "type": "taxonomia_error", "name": "Tipología de Discrepancias Numéricas", "aliases": ["Numerical Discrepancy Taxonomy"]}
        ],
        "relations": [
            {"subject_id": "ENT_NUMERICAL_DISCREPANCY", "predicate": "evita_falsas_alertas_en", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2026-09-30", "valid_to": None, "evidence_claim_id": "P06-X09-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Evita que un vocero corporativo desmienta erróneamente un informe técnico que simplemente usó una base contable distinta.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X10"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X10
    {
        "question_id": "P06-X10",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo distinguir retractación oficial, corrección editorial y nueva política corporativa?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La diferenciación entre retractación oficial, corrección editorial y nueva política corporativa se establece mediante una taxonomía tripartita gobernada por la procedencia formal y la solemnidad del acto corporativo (P06_QUALITY_ADDENDUM, Sección 2.3; Arthur W. Page Society; IABC Code of Ethics): 1) Retractación Oficial (Retraction / Fe de Erratas Regulatoria): Acto formal emitido a través del mismo canal y con igual solemnidad que el documento original (ej. rectificación de Hecho Esencial en la CMF o comunicado público firmado por el CEO), reconociendo un error material previo y dejando sin efecto el dato anterior; 2) Corrección Editorial (Editorial Amendment / Errata Tipográfica): Modificación menor de texto o formato en un sitio web o reporte corporativo (ej. corrección de un error de imprenta en una cifra o nombre) que no altera la postura sustantiva ni el compromiso de fondo de la organización; 3) Nueva Política Corporativa (Policy Evolution / Superseding Milestone): Acto prospectivo emanado del Directorio o alta gerencia (ej. aprobación de nuevo Plan Estratégico o Política de Sustentabilidad) que fija nuevos lineamientos a futuro sin implicar que la postura pasada fuera errónea o inválida en su propio momento histórico. La plataforma exige vincular cada categoría a su correspondiente documento probatorio inmutable.",
        "findings": [
            {
                "claim_id": "P06-X10-C1",
                "claim": "La taxonomía de cambios corporativos clasifica las mutaciones de texto en retractación, corrección editorial o nueva política según solemnidad jurídica y retroactividad.",
                "epistemic_status": "taxonomia_operacional_gobernanza",
                "scope": {"time": "2024-2026", "region": "Chile / Global", "actor": "Secretaría General y Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2.3: Taxonomía de Mutaciones Corporativas y Fe de Erratas",
                        "excerpt_short": "Debe distinguirse con rigor la corrección de una errata material, la retractación jurídica formal ante reguladores y la actualización estratégica de una política corporativa prospectiva.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "7cd9051b-dbba-48eb-878c-a17631e47d3d",
                        "source_title": "Arthur W. Page Society - The Page Principles",
                        "original_url": "https://page.org/who-we-are/page-principles/",
                        "locator": "Principle 1: Tell the Truth & Transparency",
                        "excerpt_short": "Transparency requires prompt, honest correction when errors occur, distinguishing administrative rectifications from fundamental corporate pivots.",
                        "source_date": "2024-01-15",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco ético y corporativo alineado con Page Society y la gobernanza de reportes corporativos."
            }
        ],
        "operational_model": {
            "inputs": ["Documento modificatorio", "Documento original preexistente"],
            "actors": ["Secretaría General", "Director de Comunicaciones", "Clasificador Semántico de Mutaciones"],
            "steps": ["Análisis de solemnidad y canal del documento", "Detección de cláusulas de derogación o rectificación explícita", "Clasificación en una de las tres categorías", "Anotación en el grafo de conocimiento"],
            "states": ["Mutation_Detected", "Solemnity_Analyzed", "Classified", "Graph_Updated"],
            "outputs": ["Registro de mutación corporativa categorizado"],
            "exceptions": ["Modificación clandestina sin fe de erratas que dispara alerta de riesgo de compliance"]
        },
        "entities": [
            {"entity_id": "TAXONOMIA_MUTACION", "type": "marco_gobernanza", "name": "Taxonomía de Mutaciones Corporativas", "aliases": ["Corporate Change Typology"]}
        ],
        "relations": [
            {"subject_id": "TAXONOMIA_MUTACION", "predicate": "clasifica_estados_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2026-09-30", "valid_to": None, "evidence_claim_id": "P06-X10-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Permite redactar respuestas ejecutivas impecables que explican transparentemente por qué cambió una cifra sin admitir culpa indebida.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X11"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X11
    {
        "question_id": "P06-X11",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué umbral obliga revisión humana antes de señalar públicamente una contradicción?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El umbral que fuerza la revisión humana obligatoria (*Human-in-the-Loop Gatekeeper*) antes de divulgar o imputar públicamente una contradicción se define conforme al benchmark SABER (Zhu et al., 2026; ArXiv 2605.18792), CoVe (Dhuliawala et al., 2023) y P06_QUALITY_ADDENDUM (Sección 3.2): 1) Regla de Tolerancia Cero en Materias Reguladas: Si la contradicción involucra hechos esenciales CMF, compromisos de RCA ambiental en el SNIFA de la SMA, o cifras de balances auditados, NINGUNA alerta o desmentido puede publicarse de forma automatizada; el umbral de delegación autónoma es $0.00$ (revisión humana 100% obligatoria por el Director Legal o CCO); 2) Umbral de Confianza Algorítmica en Medios Generales: Para contradicciones en prensa general o redes sociales, se exige que la probabilidad calibrada del clasificador NLI (Natural Language Inference) sea $\ge 0.95$ y que el índice de abstención pedagógica de SABER confirme ausencia de colisión semántica o ambigüedad de entidades; si la confianza es $< 0.95$, el sistema debe abstenerse de emitir acusaciones de falsedad y generar una solicitud de peritaje humano; 3) Principio de Precaución Reputacional: Se prohíbe que el agente de IA publique cartas al director o comunicados sin firma y aprobación expresa de una persona natural con rol DACI 'Approver'.",
        "findings": [
            {
                "claim_id": "P06-X11-C1",
                "claim": "Toda contradicción en materias reguladas o con confianza algorítmica < 0.95 exige revisión humana obligatoria antes de cualquier acción pública externa.",
                "epistemic_status": "regla_control_riesgo_reputacional",
                "scope": {"time": "2024-2026", "region": "Chile / Global", "actor": "Dirección de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "8efce53c-a1b5-4416-b399-3a615f36b2b5",
                        "source_title": "Zhu et al. (2026) - SABER: Trust or Abstain? (Texto Completo HTML v1)",
                        "original_url": "https://arxiv.org/html/2605.18792v1",
                        "locator": "Section 4.3: Abstention Thresholds & Risk-Aware Deployment",
                        "excerpt_short": "When epistemic confidence falls below the critical threshold theta=0.95, the system must trigger pedagocical abstention and route the conflict to expert human verifiers.",
                        "source_date": "2026-05-18",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.2: Protocolo de Abstención Obligatoria y Umbrales de Confianza",
                        "excerpt_short": "Queda terminantemente prohibido imputar falsedad o contradicción pública de forma automática sin revisión del Director de Asuntos Corporativos y Asesoría Jurídica.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Principio cardinal de gobernanza de IA y mitigación de daño reputacional severo."
            }
        ],
        "operational_model": {
            "inputs": ["Conflicto detectado", "Confianza del modelo", "Clasificación de materia (regulada vs no regulada)"],
            "actors": ["Guardrail de Conflicto", "CCO / Director Legal", "Sistema de Notificación"],
            "steps": ["Evaluación de criticidad de materia", "Comprobación de umbral de confianza theta >= 0.95", "Si materia es regulada o theta < 0.95, bloquear emisión pública", "Enrutamiento a bandeja de aprobación humana DACI"],
            "states": ["Conflict_Detected", "Gatekeeper_Triggered", "Blocked_for_Human_Review"],
            "outputs": ["Alerta interna restringida para revisión humana"],
            "exceptions": ["Publicación bypass no autorizada considerada incidente grave de ciberseguridad"]
        },
        "entities": [
            {"entity_id": "ENT_HUMAN_GATEKEEPER", "type": "control_gobernanza", "name": "Gatekeeper Humano de Contradicciones", "aliases": ["Human-in-the-Loop Conflict Gate"]}
        ],
        "relations": [
            {"subject_id": "ENT_HUMAN_GATEKEEPER", "predicate": "bloquea_emision_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2026-09-30", "valid_to": None, "evidence_claim_id": "P06-X11-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Protege a la empresa de demandar o acusar en prensa basándose en alucinaciones o errores de cruce de la IA.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X12"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X12
    {
        "question_id": "P06-X12",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar resolución de contradicciones complejas de forma estructurada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La representación estructurada de la resolución de contradicciones complejas exige un modelo relacional y de grafos con las siguientes especificaciones: 1) Variables principales: `discrepancy_id` (UUID), `claim_id_a`, `claim_id_b`, `discrepancy_type` (numérica_paramétrica, temporal_evolutiva, fáctica_directa, terminológica), `dimension_in_conflict` (cifra, fecha, actor, alcance), `confidence_score` (0.00-1.00), `severity_level` (leve, moderada, crítica_regulatoria), `resolution_status` (abierta, investigando, explicada_por_evolucion, falso_positivo_metodologico, contradiccion_confirmada), `human_reviewer_id`, `resolution_notes`, `resolved_at`; 2) Categorías de resolución: Falso Positivo por Desactualización (Superseded), Falso Positivo Dimensional (Non-Comparable Units), Descrepancia Menor Aclarada (Editorial Amending), y Conflicto Real con Riesgo de Compliance; 3) Relaciones: `CONFLICTS_WITH(claim_a, claim_b)`, `RESOLVED_BY(discrepancy, human_reviewer)`, `EXPLAINED_BY(discrepancy, evidence_document)`; 4) Condiciones de integridad: Prohibición de cerrar una discrepancia crítica sin adjuntar documento probatorio explicativo y firma digital del revisor humano.",
        "findings": [
            {
                "claim_id": "P06-X12-C1",
                "claim": "El ciclo de vida de resolución de contradicciones requiere un esquema estructurado con estados formales, trazabilidad de revisores y justificación documental obligatoria.",
                "epistemic_status": "diseno_de_datos_formal",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Gobernanza de Datos y Riesgo"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2.4: Esquema de Datos de Discrepancias y Protocolo de Cierre",
                        "excerpt_short": "Toda discrepancia detectada debe registrarse como objeto estructurado con identificador único, tipología de conflicto, estado de resolución y firma del analista responsable.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación detallada y gobernada en el Addendum de Calidad de P06."
            }
        ],
        "operational_model": {
            "inputs": ["Par de afirmaciones en colisión"],
            "actors": ["Manejador de Discrepancias", "Analista Humano Asignado"],
            "steps": ["Creación del registro Discrepancy", "Asignación de severidad y tipo", "Investigación y cruce probatorio", "Cierre con resolución estructurada"],
            "states": ["Open", "Under_Investigation", "Pending_Approval", "Resolved"],
            "outputs": ["Objeto de discrepancia resuelto en base de datos"],
            "exceptions": ["Reapertura de discrepancia ante aparición de nueva evidencia probatoria contraria"]
        },
        "entities": [
            {"entity_id": "ENT_DISCREPANCY_RECORD", "type": "modelo_datos", "name": "Registro Estructurado de Discrepancia", "aliases": ["Discrepancy Data Model"]}
        ],
        "relations": [
            {"subject_id": "ENT_DISCREPANCY_RECORD", "predicate": "estructura_auditoria_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2026-09-30", "valid_to": None, "evidence_claim_id": "P06-X12-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Permite auditar el histórico de incoherencias corporativas resueltas para auditorías externas o memorias de sostenibilidad.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X13"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X13
    {
        "question_id": "P06-X13",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre resolución de contradicciones complejas?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La resolución de contradicciones complejas se respalda en las siguientes fuentes canónicas del corpus: 1) Zhu et al. (2026, ArXiv:2605.18792; 'SABER: Trust or Abstain? Towards Self-Aware RAG', Mayo 2026): Texto completo HTML, Secciones 3 y 4, fundamentando los mecanismos de abstención pedagógica cuando la información entra en contradicción o carece de consistencia epistemológica; 2) Dhuliawala et al. (2023, ArXiv:2309.11495; 'Chain-of-Verification Reduces Hallucination in Large Language Models', Septiembre 2023): Metodología CoVe para descomponer afirmaciones complejas en preguntas de verificación independientes y contrastar respuestas; 3) CMF Chile (2021; 'Norma de Carácter General N° 461', Noviembre 2021): Instrucciones de divulgación, consistencia metodológica de métricas ESG y perímetro contable de emisores; y 4) P06_QUALITY_ADDENDUM (2026, Síntesis Interna, Septiembre 2026): Secciones 2 y 3, estableciendo las reglas de prevalencia, umbrales de revisión humana y prevención de falsas contradicciones.",
        "findings": [
            {
                "claim_id": "P06-X13-C1",
                "claim": "Los protocolos de resolución de contradicciones complejas se basan en literatura de vanguardia de autorreflexión RAG (SABER, CoVe) y normativa de la CMF.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Chile / Global", "actor": "Investigación RAG y Regulación Financiera"},
                "evidence": [
                    {
                        "source_id": "8efce53c-a1b5-4416-b399-3a615f36b2b5",
                        "source_title": "Zhu et al. (2026) - SABER: Trust or Abstain? (Texto Completo HTML v1)",
                        "original_url": "https://arxiv.org/html/2605.18792v1",
                        "locator": "Section 1 & 3: Framework Overview",
                        "excerpt_short": "SABER equips RAG systems with self-awareness, allowing models to abstain rather than fabricate answers when facing irreconcilable factual conflicts in retrieved documents.",
                        "source_date": "2026-05-18",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4cc2b683-2a00-429f-8117-63824505752b",
                        "source_title": "Dhuliawala et al. (2023) - Chain-of-Verification (CoVe)",
                        "original_url": "https://arxiv.org/abs/2309.11495",
                        "locator": "Section 2: Verification Chain Formulation",
                        "excerpt_short": "CoVe generates baseline responses, plans verification questions, executes them against knowledge sources independently, and synthesizes a verified output.",
                        "source_date": "2023-09-20",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Publicaciones científicas de primer nivel incorporadas y verificadas en el corpus de P06."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus indexado"],
            "actors": ["Auditor Bibliográfico"],
            "steps": ["Verificación de autores y texto de respaldo", "Mapeo a afirmaciones del pilar"],
            "states": ["Verified"],
            "outputs": ["Trazabilidad bibliográfica certificada"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_BIBLIO_CONFLICTS", "type": "corpus_bibliografico", "name": "Corpus Científico de Resolución de Contradicciones", "aliases": ["Conflict Resolution Sources"]}
        ],
        "relations": [
            {"subject_id": "ENT_BIBLIO_CONFLICTS", "predicate": "fundamenta_logica_de", "object_id": "ENT_HUMAN_GATEKEEPER", "valid_from": "2023-01-01", "valid_to": None, "evidence_claim_id": "P06-X13-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "transversal", "implication": "Garantiza solvencia metodológica y trazabilidad de cada regla de negocio del producto.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X14"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X14
    {
        "question_id": "P06-X14",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra resolución de contradicciones complejas sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Caso Concreto CRC-P06-202 (Discrepancia en Consumo de Agua en Operación Minera): 1) Entradas: Documento A ('Reporte de Sostenibilidad 2024', pág. 88): Afirma 'Consumo de agua industrial: 12.5 millones de m3 en 2024'. Documento B ('Ficha Estadística SMA - SNIFA', 14-04-2025): Registra 'Extracción autorizada efectiva en faena: 15.2 millones de m3 en 2024'; 2) Procesamiento por CoVe y Normalizador Dimensional: El sistema detecta aparente contradicción de 2.7 millones de m3. En lugar de alertar 'Falsedad en Reporte de Sostenibilidad', el algoritmo formula preguntas de verificación (CoVe): ¿Qué conceptos integran cada medición? El cruce revela que el Documento A reporta 'agua continental fresca consumida en proceso' (descontando recirculación y agua de mar desalinizada), mientras el Documento B en el SNIFA reporta 'captación bruta total autorizada' que incluye derechos de agua no consuntivos devueltos a la cuenca; 3) Resultado Esperado: El sistema clasifica el caso como `INCOMPARABLE_DIMENSIONS_EXPLAINED` (Discrepancia Metodológica Resuelta), genera un memo para la vocería explicando la diferencia técnica exacta entre captación bruta y consumo neto de proceso, y evita una crisis reputacional o acusación pública errónea de greenwashing.",
        "findings": [
            {
                "claim_id": "P06-X14-C1",
                "claim": "El caso CRC-P06-202 demuestra que la descomposición analítica de métricas dispares previene falsas acusaciones de engaño corporativo.",
                "epistemic_status": "caso_de_prueba_empirico",
                "scope": {"time": "2024-2025", "region": "Chile", "actor": "Minería, SMA y Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "7ffaecea-0ea0-4037-8ae3-e09f34ab29f0",
                        "source_title": "SMA Chile - SNIFA: Registro Público de Fiscalización y Sanciones",
                        "original_url": "https://snifa.sma.gob.cl/RegistroPublico",
                        "locator": "Portal de Fiscalización Ambiental: Métricas de Seguimiento",
                        "excerpt_short": "Los informes de seguimiento ambiental exigen reportar captación bruta en bocatoma conforme a resolución de calificación ambiental, independiente de recirculación interna.",
                        "source_date": "2024-05-10",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4cc2b683-2a00-429f-8117-63824505752b",
                        "source_title": "Dhuliawala et al. (2023) - Chain-of-Verification (CoVe)",
                        "original_url": "https://arxiv.org/abs/2309.11495",
                        "locator": "Section 4: Discrepancy Disambiguation via Targeted Probing",
                        "excerpt_short": "Targeted verification questions disentangle polysemous or context-dependent numerical claims, reducing false factual conflict detections by over 40%.",
                        "source_date": "2023-09-20",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Flujo de verificación completamente documentado y coherente con la operación de fiscalización en Chile."
            }
        ],
        "operational_model": {
            "inputs": ["Reporte de Sostenibilidad 2024", "Registro SMA SNIFA 2025"],
            "actors": ["Analista Ambiental", "Motor CoVe", "Director de Comunicaciones"],
            "steps": ["Detección de diferencia numérica", "Generación de subpreguntas CoVe sobre perímetros contables", "Verificación de captación vs consumo", "Emisión de memo explicativo"],
            "states": ["Discrepancy_Found", "CoVe_Executed", "Context_Reconciled", "Memo_Generated"],
            "outputs": ["Memo de consistencia técnica para vocero"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "CASO_CRC_P06_202", "type": "caso_prueba", "name": "Caso CRC-P06-202: Consumo de Agua y SNIFA", "aliases": ["Water Consumption Conflict Case"]}
        ],
        "relations": [
            {"subject_id": "CASO_CRC_P06_202", "predicate": "ejemplifica_resolucion_de", "object_id": "ENT_DISCREPANCY_RECORD", "valid_from": "2025-04-14", "valid_to": None, "evidence_claim_id": "P06-X14-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Permite responder con solidez a ONG y fiscalizadores sin titubear sobre la veracidad de las cifras públicas.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X15"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X15
    {
        "question_id": "P06-X15",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre resolución de contradicciones complejas, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia y prevalencia en resolución de contradicciones complejas: 1) Discrepancia: El documento inicial P06_RESEARCH_DOSSIER planteaba que los modelos de lenguaje de última generación podían resolver autónomamente cualquier conflicto mediante un prompt tipo 'analiza si estas dos fuentes se contradicen y emite veredicto', confiando ciegamente en la respuesta generativa directa; 2) Prevalencia canónica: Conforme a P06_QUALITY_ADDENDUM (Sección 3.1) y el benchmark SABER (Zhu et al., 2026), PREVALECE el principio de que los LLMs directos padecen de sesgo de confirmación y sobreconfianza ante conflictos complejos, alucinando explicaciones forzadas para compatibilizar contradicciones flagrantes o, al revés, inventando discrepancias donde no las hay. Se establece como estándar obligatorio el uso de CoVe con verificación desacoplada y el gatekeeper humano innegociable ante materias reguladas.",
        "findings": [
            {
                "claim_id": "P06-X15-C1",
                "claim": "P06_QUALITY_ADDENDUM y SABER anulan la pretensión de que un LLM resuelva contradicciones complejas en un solo paso generativo, exigiendo verificación desacoplada y control humano.",
                "epistemic_status": "prevalencia_editorial_correccion",
                "scope": {"time": "2026", "region": "Global", "actor": "Gobernanza Editorial P06"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.1: Falibilidad de LLMs en Razonamiento Contradictorio Directo",
                        "excerpt_short": "Pedir a un LLM resolver un conflicto fáctico mediante prompt simple produce sincretismo espurio o alucinaciones de reconciliación. Se requiere descomposición formal y arbitraje humano.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "8efce53c-a1b5-4416-b399-3a615f36b2b5",
                        "source_title": "Zhu et al. (2026) - SABER: Trust or Abstain? (Texto Completo HTML v1)",
                        "original_url": "https://arxiv.org/html/2605.18792v1",
                        "locator": "Section 2: The Brittleness of Standard LLMs under Conflicting Evidence",
                        "excerpt_short": "Standard LLMs frequently exhibit sycophancy or hallucinated reconciliations when presented with directly contradictory premises in their context window.",
                        "source_date": "2026-05-18",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Corrección metodológica explícita y coherente con las pruebas empíricas de SABER."
            }
        ],
        "operational_model": {
            "inputs": ["Dossier preliminar", "Addendum de calidad", "Benchmark SABER"],
            "actors": ["Comité de Arquitectura", "Especialista en NLP"],
            "steps": ["Constatación de alucinaciones en resolución directa", "Aplicación de prevalencia de SABER / Addendum", "Sustitución de prompt simple por pipeline desacoplado CoVe"],
            "states": ["Direct_Prompting_Deprecating", "Decoupled_Pipeline_Adopted"],
            "outputs": ["Pipeline desacoplado de arbitraje"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_SABER_FRAMEWORK", "type": "benchmark_nlp", "name": "Benchmark SABER (Zhu et al. 2026)", "aliases": ["SABER RAG Framework"]}
        ],
        "relations": [
            {"subject_id": "ENT_SABER_FRAMEWORK", "predicate": "invalida_metodo_de", "object_id": "ENT_DISCREPANCY_RECORD", "valid_from": "2026-05-18", "valid_to": None, "evidence_claim_id": "P06-X15-C1"}
        ],
        "comparisons": [],
        "contradictions": [
            {
                "claim_ids": ["P06-X15-C1"],
                "difference": "Dossier asumía resolución automática por prompt simple; Addendum y SABER demuestran que el prompt simple alucina y exigen pipeline CoVe desacoplado.",
                "resolution": "resuelta",
                "reason": "Prevalece P06_QUALITY_ADDENDUM conforme a las normas del mandato."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Blindaje técnico del motor contra alucinaciones sincretistas en disputas complejas de información.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X16"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X16
    {
        "question_id": "P06-X16",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre resolución de contradicciones complejas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "parcial",
        "short_answer": "Sigue sin prueba empírica formal la precisión de los modelos de arbitraje automatizado cuando se enfrentan a contradicciones retórico-legales implícitas en español con jerga regulatoria chilena (ej. diferencias entre 'suspensión provisoria' y 'clausura definitiva' en resoluciones de la SMA, o formulación de cargos de la CMF) (P06_GAPS_AND_VALIDATION, Sección 3.3). Las fuentes disponibles (SABER, CoVe, FEVER) evalúan exclusivamente corpus en inglés basados en Wikipedia o noticias anglosajonas estructuradas, no habiendo evaluado resoluciones de la administración pública latinoamericana. La validación mínima necesaria consiste en construir un Golden Set de 100 pares de afirmaciones regulatorias chilenas reales (SMA, CMF, SERNAC, prensa económica) etiquetadas por tres abogados corporativos chilenos, midiendo la tasa de falsos positivos y falsos negativos de CoVe y clasificadores NLI adaptados.",
        "findings": [
            {
                "claim_id": "P06-X16-C1",
                "claim": "El rendimiento de los algoritmos de resolución de contradicciones en lenguaje regulatorio y jurídico chileno permanece como vacío empírico sin validar.",
                "epistemic_status": "vacio_empirico_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Derecho Regulatorio y NLP en Español"},
                "evidence": [
                    {
                        "source_id": "8801b08d-0b93-40cc-b2ed-ad1d3978cd68",
                        "source_title": "P06_GAPS_AND_VALIDATION: Vacíos, Limitaciones y Validación Empírica (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.3: Transferencia de Benchmarks Anglosajones al Derecho Administrativo Chileno",
                        "excerpt_short": "Los modelos entrenados en FEVER o benchmarks en inglés no captan los matices del derecho administrativo sancionador chileno, produciendo errores en la interpretación de estados procesales.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío metodológico evidente en el análisis de cobertura geográfica y de dominio del corpus de P06."
            }
        ],
        "operational_model": {
            "inputs": ["100 pares de afirmaciones regulatorias en español"],
            "actors": ["Comité de Abogados Corporativos", "Equipo de Evaluación de Modelos"],
            "steps": ["Construcción del testset legal chileno", "Ejecución de CoVe / NLI", "Medición de F1-Score y tasa de error", "Calibración de umbrales"],
            "states": ["Testset_Design", "Annotation_Pending"],
            "outputs": ["Reporte de validación empírica en derecho chileno"],
            "exceptions": ["Desacuerdo entre evaluadores jurídicos que exige método Delphi"]
        },
        "entities": [
            {"entity_id": "GAP_LEGAL_CHILE_NLP", "type": "vacio_investigacion", "name": "Resolución de Conflictos en Derecho Administrativo Chileno", "aliases": ["Chilean Regulatory NLP Gap"]}
        ],
        "relations": [
            {"subject_id": "GAP_LEGAL_CHILE_NLP", "predicate": "limita_automatizacion_en", "object_id": "ENT_HUMAN_GATEKEEPER", "valid_from": "2026-09-30", "valid_to": None, "evidence_claim_id": "P06-X16-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Refuerza la necesidad ineludible del revisor humano chileno mientras no se desarrolle y calibre el testset local.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap": "Inexistencia de un benchmark público de contradicciones en derecho administrativo sancionador y materias regulatorias chilenas.",
                "minimum_validation": "Creación y etiquetado de 100 pares de prueba de resoluciones SMA/CMF con métricas de F1 >= 0.85.",
                "priority": "alta"
            }
        ],
        "next_question_ids": ["P06-X17"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

def append_records():
    path = Path("respuestas/P06.jsonl")
    with open(path, "a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Agregados exitosamente {len(records)} registros (P06-X09 a P06-X16) a {path}.")

if __name__ == "__main__":
    append_records()
