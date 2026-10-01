import json
from pathlib import Path

NOTEBOOK_ID = "cb87941c-2377-42fb-806f-eb9878ac0757"
SNAPSHOT_AT = "2026-10-01T02:50:00-03:00"

records = [
    # P04-F07
    {
        "question_id": "P04-F07",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se registra una afirmación corporativa con cifra, fecha, alcance, fuente y responsable?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Una afirmación corporativa con valor cuantitativo se registra mediante la 'Ficha Canónica de Compromiso Corporativo' (Corporate Commitment Data Sheet) estructurada en JSON-Schema. El registro captura obligatoriamente: 1) Cifra y unidad métrica en un objeto `baseline` o `target` con valor numérico flotante (`target_value`), unidad estandarizada (`unit`: e.g. 'l/s', 'tCO2e', '%') y tipo de métrica (`metric_type`: Reducción Absoluta, Intensidad o Cobertura); 2) Temporalidad estricta (`baseline_year`, `target_year` e hitos intermedios `interim_milestones`); 3) Alcance geográfico y operacional (`issuing_entity`: filial o división operativa; `geographical_scope`: faena o región); 4) Trazabilidad de origen documental inmutable (`source_traceability`: título del documento, tipo documental, año de edición, número exacto de página, cita textual literal entrecomillada y hash criptográfico SHA-256 del PDF original); y 5) Gobernanza y responsable institucional (`governance`: rol ejecutor responsable `accountable_role`, órgano colegiado aprobador `approving_body` y fecha formal de aprobación `approval_date`).",
        "findings": [
            {
                "claim_id": "P04-F07-C1",
                "claim": "El registro fáctico de una afirmación corporativa cuantitativa exige un esquema formal que desacople la cifra y la unidad de la narrativa, vinculándola a un rol responsable, un horizonte temporal y un hash de página inmutable.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Gestión de Datos Corporativos"},
                "evidence": [
                    {
                        "source_id": "878711bf-fc7d-4332-beb7-c0d3bf31fa18",
                        "source_title": "P04_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3: Ficha Estructurada de Compromiso Corporativo",
                        "excerpt_short": "Schema CorporateCommitmentDataSheet: properties baseline (year, value, unit), target (target_year, target_value, metric_type), governance (accountable_role, approving_body, approval_date) y source_traceability (page_number, exact_quote, hash_sha256).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación JSON-Schema formalizada en el entregable central del dossier P04."
            }
        ],
        "operational_model": {
            "inputs": ["Párrafo o tabla con afirmación corporativa", "Metadatos del documento fuente"],
            "actors": ["Commitment Parser", "Fact Extractor", "Audit Registry"],
            "steps": ["Extracción de entidades numéricas y unidades", "Identificación de rol responsable", "Vinculación de hash de página", "Serialización en schema canónico"],
            "states": ["Raw_Text", "Extracted_Fields", "Validated_Commitment_Record"],
            "outputs": ["Instancia JSON de la Ficha Canónica de Compromiso"],
            "exceptions": ["Afirmación cuantitativa sin unidad métrica o sin fecha base identificable"]
        },
        "entities": [
            {"entity_id": "ENT_COMMITMENT_DATASHEET", "type": "schema", "name": "Ficha Canónica de Compromiso Corporativo", "aliases": ["Corporate Commitment Data Sheet"]}
        ],
        "relations": [
            {"subject_id": "ENT_COMMITMENT_DATASHEET", "predicate": "estructura_registro_de", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-F07-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Modelo de registro",
                "Texto libre en PDF": "Cifras incrustadas en párrafos narrativos sujetas a ambigüedad y pérdida de contexto.",
                "Ficha Canónica Estructurada": "Parámetros numéricos tipados, unidades normalizadas y trazabilidad de auditoría SHA-256."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe parsear y almacenar toda afirmación de vocería bajo la Ficha Canónica para permitir auditorías algorítmicas instantáneas.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-F08"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-F08
    {
        "question_id": "P04-F08",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué campos distinguen promesa, meta, avance, incumplimiento y rectificación?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La diferenciación entre los estados de un compromiso corporativo se rige por campos específicos en el modelo de datos: 1) Promesa / Declaración de Intención: tipificada como `corp:Statement`, caracterizada por `has_quantitative_target: false`, ausencia de `baseline_year` y horizonte indefinido; 2) Meta Formal: tipificada como `corp:Commitment`, caracterizada por `status: 'Activo / En Curso'`, `baseline: {year, value, unit}`, `target_year`, `target_value` y aprobación formal de directorio; 3) Avance Anual: registrado en el array `reported_outcomes` con `reporting_year`, `achieved_value`, `pct_progress_vs_target` y referencia al documento de reporte anual; 4) Incumplimiento: derivado automáticamente cuando la fecha actual supera el `target_year` o un hito intermedio y el `achieved_value` no alcanza el valor comprometido, asignando `status: 'Incumplido'` o `'En Riesgo / Rezago'`; y 5) Rectificación / Reexpresión: tipificada con `status: 'Reexpresado / Modificado'`, que exige los campos `previous_baseline`, `revised_baseline`, `reexpression_justification` (e.g. adquisición o cambio de metodología bajo IFRS S2) y la relación PROV-O `prov:wasRevisionOf`.",
        "findings": [
            {
                "claim_id": "P04-F08-C1",
                "claim": "Los estados de promesa, meta, avance, incumplimiento y rectificación se distinguen unívocamente mediante la combinación de tipo ontológico, año base, array de outcomes y flags de reexpresión según IFRS S2.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Estándares IFRS / GRI"},
                "evidence": [
                    {
                        "source_id": "878711bf-fc7d-4332-beb7-c0d3bf31fa18",
                        "source_title": "P04_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2.2: Ontología Corporativa y Sección 3.1: Estructura de Campos",
                        "excerpt_short": "status enum: Propuesto, Activo/En Curso, Cumplido, En Riesgo/Rezago, Incumplido, Reexpresado/Modificado, Retirado. reported_outcomes array (reporting_year, achieved_value, pct_progress).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "3d670aa0-fc8d-48ca-8c2d-26879dc45378",
                        "source_title": "IFRS S2: Climate-related Disclosures",
                        "original_url": "https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/ifrs-s2-climate-related-disclosures/",
                        "locator": "Párrafos 33-36: Targets and Re-expressions",
                        "excerpt_short": "An entity shall disclose how it tracks progress against its targets, whether the target is absolute or intensity-based, and any revisions to base year emissions or targets.",
                        "source_date": "2023-06-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Norma contable internacional IFRS S2 y modelo de datos del dossier P04."
            }
        ],
        "operational_model": {
            "inputs": ["Memoria Anual o Reporte de Sostenibilidad", "Compromiso original indexado"],
            "actors": ["Commitment Tracker", "Discrepancy Detector", "State Transition Engine"],
            "steps": ["Comparación de valor reportado vs meta", "Evaluación de vencimiento temporal", "Actualización de enum status y registro de reexpresión si aplica"],
            "states": ["Active", "Progress_Recorded", "Breached", "Reexpressed", "Fulfilled"],
            "outputs": ["Estado actualizado del compromiso con historial de transiciones"],
            "exceptions": ["Reexpresión de línea base no explicada en nota técnica"]
        },
        "entities": [
            {"entity_id": "ENT_COMMITMENT_STATES", "type": "taxonomia", "name": "Estados Operativos de Compromisos Corporativos", "aliases": ["Corporate Commitment Lifecycle States"]}
        ],
        "relations": [
            {"subject_id": "ENT_COMMITMENT_STATES", "predicate": "monitorea_cumplimiento_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-F08-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza del dato",
                "Promesa (Declaración)": "Aspiración sin indicador cuantificable; no genera obligación matemática.",
                "Meta (Compromiso)": "Obligación formal con año base, valor objetivo, plazo y auditoría externa obligatoria."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe alertar proactivamente a los directivos si una meta entra en estado 'En Riesgo / Rezago' antes de que sea expuesta en medios.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-F09"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-F09
    {
        "question_id": "P04-F09",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se enlazan afirmaciones y compromisos con documentos, actores y decisiones posteriores?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El enlace relacional entre afirmaciones, compromisos, documentos y decisiones se implementa mediante un Grafo de Conocimiento fundamentado en el estándar W3C PROV-O y el vocabulario FIBO (Financial Industry Business Ontology). Se configuran cuatro aristas direccionales tipadas: 1) Linaje Documental (`corp:wasStatedIn`): conecta la afirmación con el `corp:DocumentArtifact` y el hash de fragmento de origen; 2) Cadena de Responsabilidad (`prov:wasAttributedTo` / `prov:wasApprovedBy`): vincula el compromiso con el `org:BoardOfDirectors`, el comité temático o el directivo emisor; 3) Conciliación de Cumplimiento (`corp:reportsProgressFor` / `corp:fulfillsCommitment`): une los resultados (`corp:Outcome`) publicados en memorias posteriores con el nodo del compromiso original (`corp:Commitment`); y 4) Evolución y Sustitución (`prov:wasRevisionOf` / `dcterms:replaces`): enlaza decisiones de rectificación o retiro con el acta de directorio o hecho esencial que autorizó el cambio.",
        "findings": [
            {
                "claim_id": "P04-F09-C1",
                "claim": "La vinculación ontológica basada en W3C PROV-O y FIBO permite conectar un compromiso corporativo con su documento de origen, su aprobador colegiado y las memorias anuales que reportan su avance o modificación.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Ingeniería de Grafos Semánticos"},
                "evidence": [
                    {
                        "source_id": "5737d422-55c7-4103-9b0c-8148106d1fa0",
                        "source_title": "W3C PROV-O: The PROV Ontology",
                        "original_url": "https://www.w3.org/TR/prov-o/",
                        "locator": "Sección 3: Starting Point Terms",
                        "excerpt_short": "Defines core classes: Entity, Activity, Agent, and properties wasDerivedFrom, wasAttributedTo, wasRevisionOf, wasGeneratedBy to establish explicit provenance chains.",
                        "source_date": "2013-04-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "878711bf-fc7d-4332-beb7-c0d3bf31fa18",
                        "source_title": "P04_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 2.3: Trazabilidad Bitemporal y Linaje W3C PROV-O",
                        "excerpt_short": "corp:Outcome prov:wasDerivedFrom corp:Commitment, corp:Commitment prov:wasAttributedTo org:BoardOfDirectors, corp:Statement_v2 prov:wasRevisionOf corp:Statement_v1.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estándar formal W3C PROV-O y modelo relacional del dossier P04."
            }
        ],
        "operational_model": {
            "inputs": ["Compromiso indexado", "Reportes anuales subsecuentes", "Actas de Directorio"],
            "actors": ["Graph Builder", "Entity Linker", "Provenance Resolver"],
            "steps": ["Identificación de entidades comunes", "Generación de tripletas RDF/LPG", "Inserción en base de datos de grafos"],
            "states": ["Isolated_Fact", "Graph_Linked", "Fully_Attributed"],
            "outputs": ["Subgrafo corporativo que traza el ciclo de vida íntegro de la afirmación"],
            "exceptions": ["Reporte posterior que menciona una cifra sin enlazar al compromiso original"]
        },
        "entities": [
            {"entity_id": "ENT_PROVENANCE_GRAPH", "type": "ontologia", "name": "Grafo de Procedencia y Linaje Corporativo", "aliases": ["Corporate Provenance Knowledge Graph"]}
        ],
        "relations": [
            {"subject_id": "ENT_PROVENANCE_GRAPH", "predicate": "conecta_ciclo_vida_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-F09-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Capacidad de trazabilidad",
                "Búsqueda por texto plano": "Incapaz de determinar qué documento posterior modificó una meta previa.",
                "Grafo W3C PROV-O": "Trazado determinístico de la cadena causal desde la promesa inicial hasta su última auditoría."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe permitir navegar el subgrafo de cada compromiso para responder con certeza sobre antecedentes históricos y decisiones tomadas.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-F10"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-F10
    {
        "question_id": "P04-F10",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar afirmaciones y compromisos de forma estructurada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La representación estructurada de afirmaciones y compromisos exige: 1) Variables métricas e identitarias (`commitment_id`, `title`, `description`, `baseline_value`, `target_value`, `unit`, `metric_type`); 2) Categorías temáticas normalizadas (`category`: Ambiental/Clima, Social/Comunidad, Gobierno Corporativo, Operacional/Seguridad, Diversidad e Inclusión; marcos de alineación: CMF NCG 461, GRI, IFRS S1/S2); 3) Relaciones ontológicas dirigidas (`hasBaseline`, `hasTargetYear`, `wasApprovedBy`, `hasReportedOutcome`, `isAssuredBy`); y 4) Condiciones de consistencia lógica y gobernanza (Condición 1: todo compromiso cuantitativo debe poseer un año base y unidad métrica válida; Condición 2: ningún resultado puede ser catalogado como 'auditado' sin dictamen ISAE 3000 con URI verificable; Condición 3: toda modificación de meta debe referenciar la versión previa vía `prov:wasRevisionOf` garantizando no-destrucción de la historia).",
        "findings": [
            {
                "claim_id": "P04-F10-C1",
                "claim": "El modelado estructurado de afirmaciones corporativas requiere variables tipadas, taxonomías temáticas ESG, relaciones dirigidas de linaje y tres condiciones lógicas obligatorias de consistencia y no-destrucción histórica.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Arquitectura de Datos Corporativos"},
                "evidence": [
                    {
                        "source_id": "878711bf-fc7d-4332-beb7-c0d3bf31fa18",
                        "source_title": "P04_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3.1: Estructura de Campos (Schema) y 2.2: Ontología",
                        "excerpt_short": "Schema properties: required [commitment_id, title, category, issuing_entity, baseline, target, status, governance, source_traceability]. Condiciones de integridad en Fase 4 de actualización.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación de schema e integridad referencial documentada en el dossier P04."
            }
        ],
        "operational_model": {
            "inputs": ["Schema JSON de compromiso", "Registros candidatos"],
            "actors": ["Schema Validator", "Consistency Enforcer"],
            "steps": ["Validación de tipos de datos", "Comprobación de condiciones lógicas", "Persistencia en grafo y almacén relacional"],
            "states": ["Validating", "Passed_Integrity", "Committed_To_Store"],
            "outputs": ["Entidad estructurada y validada lista para indexación semántica"],
            "exceptions": ["Compromiso cuantitativo que omite el año base"]
        },
        "entities": [
            {"entity_id": "ENT_INTEGRITY_RULES", "type": "reglas", "name": "Reglas de Consistencia Lógica de Compromisos", "aliases": ["Commitment Data Integrity Rules"]}
        ],
        "relations": [
            {"subject_id": "ENT_INTEGRITY_RULES", "predicate": "asegura_calidad_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-F10-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Control de consistencia",
                "Almacenamiento no estructurado": "Permite inconsistencias numéricas y omisión de años base sin validación.",
                "Modelo estructurado con reglas": "Rechaza o marca como incompleta cualquier afirmación que no cumpla las condiciones lógicas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe incorporar validadores automáticos en la ingesta para rechazar o clasificar como incompletas las afirmaciones sin metadata.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-F11"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-F11
    {
        "question_id": "P04-F11",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre afirmaciones y compromisos?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Los hechos relativos al modelado de afirmaciones y compromisos se sustentan en cuatro pilares normativos y ontológicos: 1) IFRS S2 Climate-related Disclosures (junio 2023, párrs. 33-36), que exige la divulgación de metas absolutas/intensidad, años base, hitos intermedios y revisiones metodológicas; 2) GRI Standards 2: General Disclosures (2021, Contenido 2-23 y 2-24), que norma la formalización de compromisos de debida diligencia y sus mecanismos de integración operativa; 3) W3C PROV-O (abril 2013, Sección 3), que aporta los axiomas matemáticos para la derivación de resultados a partir de compromisos (`prov:wasDerivedFrom`); y 4) P04_EVIDENCE_MAP (30 de septiembre de 2026, Sección 1 y Dimensión B), que tipifica los 4 estados epistémicos y la exigencia de dictamen ISAE 3000 para el estado de Verificación.",
        "findings": [
            {
                "claim_id": "P04-F11-C1",
                "claim": "El marco de afirmaciones y compromisos cuenta con respaldo cruzado entre estándares financieros globales (IFRS ISSB), reportabilidad de sostenibilidad (GRI) y ontologías computacionales de procedencia (W3C).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2013-2026", "region": "Internacional", "actor": "ISSB / GRI / W3C"},
                "evidence": [
                    {
                        "source_id": "3d670aa0-fc8d-48ca-8c2d-26879dc45378",
                        "source_title": "IFRS S2: Climate-related Disclosures",
                        "original_url": "https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/ifrs-s2-climate-related-disclosures/",
                        "locator": "Párrafos 33-36: Metrics and Targets",
                        "excerpt_short": "Exige explicitar el año base, métrica cuantitativa, validación externa y avances intermedios.",
                        "source_date": "2023-06-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "b2351b3a-e90c-42c5-a012-55bef2861520",
                        "source_title": "GRI Standards: Universal Standards (GRI 1, 2, 3)",
                        "original_url": "https://www.globalreporting.org/standards/standards-development/universal-standards/",
                        "locator": "GRI 2: General Disclosures, Contenido 2-23",
                        "excerpt_short": "Policy commitments and how they are embedded throughout the organization's activities and business relationships.",
                        "source_date": "2021-10-01",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "5737d422-55c7-4103-9b0c-8148106d1fa0",
                        "source_title": "W3C PROV-O: The PROV Ontology",
                        "original_url": "https://www.w3.org/TR/prov-o/",
                        "locator": "Sección 3: Starting Point Terms",
                        "excerpt_short": "wasDerivedFrom is a relation between an entity and another entity that was used in the creation of the former.",
                        "source_date": "2013-04-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación directa de citas y definiciones normativas en las fuentes del corpus P04."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus normativo P04"],
            "actors": ["Audit Framework", "Cross-Standard Harmonizer"],
            "steps": ["Verificación de cláusulas IFRS y GRI", "Mapeo de requerimientos normativos a tripletas PROV-O"],
            "states": ["Mapped", "Audited_Normative_Base"],
            "outputs": ["Matriz de conformidad regulatoria de compromisos"],
            "exceptions": ["Divergencias terminológicas entre GRI e IFRS"]
        },
        "entities": [
            {"entity_id": "ENT_COMMITMENT_SOURCES", "type": "corpus", "name": "Corpus Normativo de Compromisos Corporativos", "aliases": ["Normative Commitment Frameworks"]}
        ],
        "relations": [
            {"subject_id": "ENT_COMMITMENT_SOURCES", "predicate": "fundamenta_esquema_de", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-F11-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque normativo",
                "IFRS S2": "Foco en riesgos financieros, materialidad financiera y metas climáticas.",
                "GRI Standards": "Foco en impactos sobre la economía, el medio ambiente y las personas (doble materialidad)."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe permitir clasificar compromisos bajo la taxonomía IFRS y GRI simultáneamente para satisfacer audiencias financieras y comunitarias.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-F12"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P04-F12
    {
        "question_id": "P04-F12",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra afirmaciones y compromisos sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Caso Canónico: Seguimiento del compromiso ambiental 'Reducción de extracción de agua continental en operaciones mineras' (ID: COM-ENV-2023-089). Entradas documentadas: 1) Declaración original en Memoria 2023: Reducción del 40% al 2030 respecto a la línea base 2021 (1.250 l/s), meta objetivo 750 l/s, meta intermedia 2025 de 1.050 l/s, aprobada por Comité de Sostenibilidad; 2) Reporte intermedio en Memoria 2025 (pág. 84): Caudal promedio alcanzado de 1.040 l/s (avance del 42% vs meta final, superando el hito intermedio); 3) Dictamen de aseguramiento independiente: Deloitte Auditores SpA bajo norma ISAE 3000 con nivel de seguridad 'Limitada'. Resultado esperado en el sistema: 1) El compromiso se mantiene en `status: 'Activo / En Curso'`; 2) Se registra automáticamente un nuevo `reported_outcome` para 2025; 3) Se vincula la relación `isAssuredBy: Deloitte_ISAE3000`; y 4) Ante una consulta de prensa sobre cumplimiento hídrico, el sistema responde: 'La empresa reportó para 2025 un consumo de 1.040 l/s, cumpliendo con holgura su hito intermedio (1.050 l/s), con aseguramiento externo independiente bajo ISAE 3000 (Memoria 2025, p. 84)'.",
        "findings": [
            {
                "claim_id": "P04-F12-C1",
                "claim": "El caso empírico de transición hídrica ejemplifica la captura estructurada de año base, metas intermedias, avances auditados bajo ISAE 3000 y generación de minutas de vocería con citas precisas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2026", "region": "Chile (Región de Antofagasta)", "actor": "Minera Cordillera Andina"},
                "evidence": [
                    {
                        "source_id": "878711bf-fc7d-4332-beb7-c0d3bf31fa18",
                        "source_title": "P04_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección 3.2: Ejemplo Concreto: Compromiso de Transición Hídrica",
                        "excerpt_short": "commitment_id COM-ENV-2023-089: baseline 2021 (1250 l/s), target 2030 (750 l/s), milestone 2025 (1050 l/s), outcome 2025 (1040 l/s), assurance Deloitte ISAE 3000.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Caso exhaustivo completamente desarrollado y consistente en el dossier P04."
            }
        ],
        "operational_model": {
            "inputs": ["Ficha COM-ENV-2023-089", "Fragmento p. 84 Memoria 2025", "Dictamen ISAE 3000"],
            "actors": ["Commitment Tracker", "Assurance Validator", "Briefing Generator"],
            "steps": ["Verificación de concordancia métrica", "Validación de firma auditora", "Generación de minuta de vocería fundada"],
            "states": ["Tracking", "Outcome_Verified", "Briefing_Ready"],
            "outputs": ["Minuta de prensa y vocería 100% trazable a página y dictamen"],
            "exceptions": ["Diferencia en metodología de medición de caudal entre períodos"]
        },
        "entities": [
            {"entity_id": "ENT_WATER_COMMITMENT_CASE", "type": "caso_empirico", "name": "Caso de Transición Hídrica COM-ENV-2023-089", "aliases": ["Water Transition Commitment Case"]}
        ],
        "relations": [
            {"subject_id": "ENT_WATER_COMMITMENT_CASE", "predicate": "valida_seguimiento_en", "object_id": "BRIDGE_Modulo_Memoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P04-F12-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Resultado de vocería",
                "Respuesta no estructurada": "Respuesta vaga afirmando que 'la empresa cuida el agua y avanza según lo planeado'.",
                "Respuesta fundada estructurada": "Cita exacta de 1.040 l/s logrados vs 1.050 l/s de hito intermedio, con mención de auditor Deloitte bajo ISAE 3000."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Memoria", "implication": "BRIDGE debe sintetizar minutas de este tipo exacto para dotar a los directivos de defensas factuales inexpugnables ante escrutinio público.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P04-F13"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_path = Path("respuestas/P04.jsonl")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Appended {len(records)} records (P04-F07..P04-F12) to {out_path}.")
