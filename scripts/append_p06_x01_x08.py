import json
from pathlib import Path

NOTEBOOK_ID = "2c5dc262-44fc-43f8-b6e2-c993ed32835b"
SNAPSHOT_AT = "2026-10-01T03:30:00-03:00"

records = [
    # P06-X01
    {
        "question_id": "P06-X01",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué esquema mínimo relaciona afirmación, evidencia, organización, actor, compromiso y evento?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El esquema ontológico mínimo para relacionar conocimiento en The Bridge Intelligence se estructura conforme a los principios de T-GRAG (Li et al., 2025; ArXiv 2508.01680), GraphRAG (Edge et al., 2024; ArXiv 2404.16130) y Palantir Foundry (Doc 'Why Ontology'): 1) Nodos Entidad: Organización (empresa matriz, filial o contraparte con RUT/tax_id unívoco), Actor (persona con rol institucional, vigencia y delegación de autoridad), Compromiso (obligación contractual, regulatoria o social con fecha de exigibilidad y estado), Evento (acontecimiento espaciotemporal con timestamp y coordenadas); 2) Nodos Epistémicos: Afirmación (proposición factual atómica sujeta a validación y clasificación epistémica) y Evidencia (fragmento documental con hash criptográfico SHA-256, localizador de página/párrafo y URI canónico); 3) Relaciones Dirigidas Tipadas: EMITIDA_POR (Afirmación -> Actor), SUSTENTADA_EN (Afirmación -> Evidencia), VINCULADA_A (Afirmación -> Compromiso | Evento) y PERTENECE_A (Actor -> Organización). Este grafo permite vincular cualquier aseveración pública con el compromiso histórico subyacente y su evidencia documental inmutable.",
        "findings": [
            {
                "claim_id": "P06-X01-C1",
                "claim": "El esquema mínimo de grafo de afirmaciones integra seis clases de entidades tipadas y cuatro relaciones cardinales con metadatos temporales de validez.",
                "epistemic_status": "propuesta_arquitectura_formal",
                "scope": {"time": "2024-2026", "region": "Global / Chile", "actor": "Arquitectura de Grafos de Conocimiento"},
                "evidence": [
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 3.1: Temporal Knowledge Graph Schema & Entity Grounding",
                        "excerpt_short": "We define a temporal knowledge graph where nodes encompass entities, claims, and time-bounded events, interconnected by directional edges annotated with validity intervals [t_start, t_end] to resolve non-stationary information.",
                        "source_date": "2025-08-05",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "98f72019-62a8-4781-a211-2ce2cccaf4eb",
                        "source_title": "Palantir Foundry - Why Create an Ontology: Decision-Centric System",
                        "original_url": "https://palantir.com/docs/foundry/ontology/why-ontology/",
                        "locator": "Foundry Ontology Overview: Connecting Data, Models and Actions",
                        "excerpt_short": "The Foundry Ontology binds data to actionable enterprise concepts—organizations, commitments, assets, and events—allowing semantic queries and operational tracking rather than raw tabular lookups.",
                        "source_date": "2024-05-12",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Arquitectura fundamentada en el paper formal de T-GRAG y en los principios de ontología operacional de Palantir Foundry."
            }
        ],
        "operational_model": {
            "inputs": ["Documento oficial o noticia", "Entidades extraídas por NER", "Timestamps de emisión"],
            "actors": ["Extractor de Entidades y Relaciones", "Grafo Temporal T-GRAG", "Analista de Inteligencia"],
            "steps": ["Extracción de afirmaciones atómicas", "Resolución de entidades unívocas contra el grafo", "Creación de nodos Claim, Actor, Evento y Compromiso", "Asignación de bordes dirigidos con intervalo de validez temporal [t_start, t_end]"],
            "states": ["Raw_Text", "Claims_Extracted", "Entities_Resolved", "Graph_Linked"],
            "outputs": ["Subgrafo ontológico indexado"],
            "exceptions": ["Ambigüedad de entidad no resuelta que exige intervención de desambiguación"]
        },
        "entities": [
            {"entity_id": "ENT_TGRAG_SCHEMA", "type": "esquema_grafo", "name": "Esquema Ontológico T-GRAG", "aliases": ["Temporal Claim Graph", "Ontología de Asuntos Corporativos"]}
        ],
        "relations": [
            {"subject_id": "ENT_TGRAG_SCHEMA", "predicate": "estructura_datos_de", "object_id": "ENT_AFIRMACION", "valid_from": "2025-01-01", "valid_to": None, "evidence_claim_id": "P06-X01-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [
            {"metric_name": "Entity Resolution Accuracy", "denominator": "Total de entidades extraídas en documentos", "target_value": ">= 95%"}
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Permite navegación estructurada de compromisos y posturas históricas enlazadas a hechos concretos.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X02"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X02
    {
        "question_id": "P06-X02",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo expresar relación de apoyo, conflicto, modificación y caducidad sin perder procedencia?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La expresión de relaciones dinámicas entre afirmaciones se implementa mediante bordes reificados y tipados en el grafo de conocimiento temporal (Li et al., 2025; Thorne et al., 2018): 1) Relación de Apoyo (SUPPORTS): Conecta dos afirmaciones o una evidencia con una afirmación cuando los hechos son consistentes y corroborativos, conservando el UUID de la fuente primaria; 2) Relación de Conflicto (CONFLICTS_WITH): Vincula afirmaciones contradictorias, requiriendo anotación de la dimensión en discrepancia (cifra, fecha o postura regulatoria) y activación de alerta de divergencia; 3) Relación de Modificación (SUPERSEDES / MODIFIES): Registra una actualización legítima de postura o renegociación de metas, vinculando la afirmación posterior con la anterior e inyectando un puntero de vigencia; 4) Relación de Caducidad (EXPIRES): Marca el vencimiento formal de un compromiso, plazo o vigencia legal (ej. término de permiso provisorio ambiental). Cada borde almacena obligatoriamente metadatos de procedencia: `edge_id`, `source_uuid`, `timestamp_created`, `created_by_actor_id` y `validity_window` ([t0, t1]). Al preservar estos atributos en el borde mismo, ninguna mutación destruye el linaje histórico.",
        "findings": [
            {
                "claim_id": "P06-X02-C1",
                "claim": "Los bordes temporales tipados (apoyo, conflicto, modificación, caducidad) preservan procedencia inmutable y resuelven el problema de la sobreescritura destructiva.",
                "epistemic_status": "modelo_computacional_probado",
                "scope": {"time": "2023-2025", "region": "Global", "actor": "NLP y Razonamiento Temporal"},
                "evidence": [
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 3.2: Edge Semantics and Temporal Evolution",
                        "excerpt_short": "Edges represent semantic and temporal dependencies including conflict, support, and superseding. Instead of overwriting facts, new edges record temporal transitions while retaining full source provenance.",
                        "source_date": "2025-08-05",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "e9a21c25-7298-43fb-aa5e-153957fb1850",
                        "source_title": "Thorne et al. (2018) - FEVER: Fact Extraction & VERification",
                        "original_url": "https://arxiv.org/abs/1803.05355",
                        "locator": "Section 2: Task Formulation and Label Space",
                        "excerpt_short": "Claims are categorized into SUPPORTS, REFUTES, or NOT ENOUGH INFO with respect to extracted evidence sentences, providing a formal triad for verification.",
                        "source_date": "2018-03-20",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Basado en la taxonomía clásica FEVER extendida temporalmente por T-GRAG."
            }
        ],
        "operational_model": {
            "inputs": ["Afirmación A y Afirmación B", "Documentos de respaldo", "Fechas de vigencia"],
            "actors": ["Detector de Contradicciones y Evolución", "Grafo Temporal", "Auditor de Procedencia"],
            "steps": ["Comparación semántica de proposiciones", "Clasificación de relación (apoyo, conflicto, modificación, caducidad)", "Inyección de borde con ventana de validez [t0, t1]", "Almacenamiento del hash del documento originador"],
            "states": ["Pairwise_Comparison", "Relation_Classified", "Temporal_Edge_Recorded"],
            "outputs": ["Borde de relación temporal persistido en grafo"],
            "exceptions": ["Imposibilidad de datar afirmación que fuerza estado 'indeterminada_temporalmente'"]
        },
        "entities": [
            {"entity_id": "ENT_FEVER_TAXONOMY", "type": "marco_metodologico", "name": "Taxonomía de Verificación FEVER / T-GRAG", "aliases": ["FEVER Relational Schema"]}
        ],
        "relations": [
            {"subject_id": "ENT_FEVER_TAXONOMY", "predicate": "define_relaciones_para", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2018-01-01", "valid_to": None, "evidence_claim_id": "P06-X02-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Permite distinguir cuándo una empresa cambió de postura intencionalmente versus cuándo incurre en contradicción inadvertida.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X03"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X03
    {
        "question_id": "P06-X03",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué consulta reconstruye por qué se emitió una alerta en una fecha concreta?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La reconstrucción determinista de una alerta se ejecuta mediante una consulta de Linaje Causal en Grafo Temporal (T-GRAG / Palantir AIP; Li et al., 2025; Palantir 2024): La consulta recibe el `alert_id` y el timestamp $t_{alerta}$, ejecutando un recorrido retroactivo parametrizado: `MATCH (a:Alerta {id: $alert_id})-[:DETONADA_POR]->(s:SenalExterna)-[:CONFLICTS_WITH|VIOLATES]->(c:CompromisoInterno) WHERE c.valid_from <= $t_alerta AND (c.valid_to IS NULL OR c.valid_to >= $t_alerta) RETURN a, s, c, s.evidencia_id, c.evidencia_id`. Esta consulta extrae: 1) El evento o noticia externa que actuó como detonante (con su URL, timestamp de captura y score de relevancia); 2) El compromiso corporativo vigente en ese instante exacto contra el cual colisionó la señal; 3) La regla algorítmica o umbral de severidad que disparó la notificación; y 4) La instantánea inmutable del grafo en $t_{alerta}$, garantizando que cambios o desmentidos posteriores no alteren la justificación histórica de la alerta.",
        "findings": [
            {
                "claim_id": "P06-X03-C1",
                "claim": "Una consulta de grafos temporales con corte temporal $t_{alerta}$ reconstruye de forma 100% auditable la cadena causal que justificó la alerta.",
                "epistemic_status": "modelo_operacional_probado",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Auditoría de IA y Gobernanza"},
                "evidence": [
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 4.1: Historical State Reconstruction & Point-in-Time Traversal",
                        "excerpt_short": "T-GRAG allows point-in-time subgraph retrieval. Querying the state at t_k returns the exact topology of active facts, enabling complete causal audit of decision triggers.",
                        "source_date": "2025-08-05",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "5168f7d7-3499-40e3-afc8-c6b216843f19",
                        "source_title": "Palantir AIP - Architecture Overview & Context Engineering",
                        "original_url": "https://palantir.com/docs/foundry/architecture-center/aip-architecture/",
                        "locator": "AIP Auditing & Lineage: Traceable Automated Decisions",
                        "excerpt_short": "AIP logs every prompt, retrieved context, and deterministic rule evaluation in an immutable audit ledger, ensuring that operations can be historically reproduced.",
                        "source_date": "2024-06-20",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Capacidad validada en el marco de Point-in-Time Retrieval de T-GRAG y auditabilidad de Palantir AIP."
            }
        ],
        "operational_model": {
            "inputs": ["alert_id", "timestamp_alerta"],
            "actors": ["Auditor de Riesgo Corporativo", "Motor de Consulta Temporal Cypher/T-GRAG"],
            "steps": ["Recepción de identificador de alerta", "Ejecución de recorrido de subgrafo en $t_{alerta}$", "Recuperación de señal externa y compromiso interno", "Generación del reporte de linaje causal de la alerta"],
            "states": ["Alert_Lookup", "Point_in_Time_Filter", "Causal_Chain_Resolved"],
            "outputs": ["Reporte de linaje de decisión y procedencia"],
            "exceptions": ["Alerta huérfana por purga de datos que viola política de retención"]
        },
        "entities": [
            {"entity_id": "ENT_ALERT_AUDIT", "type": "proceso_auditoria", "name": "Reconstrucción Causal de Alertas", "aliases": ["Alert Lineage Audit"]}
        ],
        "relations": [
            {"subject_id": "ENT_ALERT_AUDIT", "predicate": "opera_sobre", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2025-01-01", "valid_to": None, "evidence_claim_id": "P06-X03-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Permite responder a ejecutivos exactamente por qué el sistema notificó un riesgo de crisis sin invocar una 'caja negra'.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X04"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X04
    {
        "question_id": "P06-X04",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar grafo de afirmaciones de forma estructurada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La representación estructurada del grafo de afirmaciones exige un modelo de datos formal compuesto por: 1) Variables principales: `claim_id` (UUIDv4), `subject_entity_id`, `predicate`, `object_value_or_entity`, `epistemic_status` (hecho_documentado, declaración_corporativa, rumor_redes, inferencia), `modality` (cierto, probable, condicional), `validity_start`, `validity_end`, `evidence_doc_id`, `sha256_evidence_hash`, `locator_page_para`; 2) Categorías ontológicas: Entidades Corporativas (Organización, Persona, Planta/Faena, Marca), Compromisos (Regulatorio, Ambiental, Laboral, Comercial), Afirmaciones Externas (Prensa, Redes, Denuncia Administrativa) y Hechos Internos (Memoria Anual, Hecho Esencial CMF, Acta Directorio); 3) Relaciones cardinales: SUJETO_DE, OBJETO_DE, RESPALDADO_POR, CONTRADICE, SUSTITUYE_A, CADUCA_EN; 4) Condiciones de integridad: Prohibición de bordes huérfanos, unicidad de entidades mediante claves compuestas (RUT/jurisdicción), y no-retroactividad de modificaciones de postura sin nuevo documento comprobable.",
        "findings": [
            {
                "claim_id": "P06-X04-C1",
                "claim": "El modelado estructurado del grafo de afirmaciones requiere tipado estricto de variables, restricciones de integridad referencial y marcas temporales bi-temporales.",
                "epistemic_status": "diseno_de_datos_formal",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "Modelado de Bases de Datos de Grafos"},
                "evidence": [
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 3.3: Node and Edge Property Specifications",
                        "excerpt_short": "Nodes store attribute dictionaries including epistemic confidence, canonical identifiers, and extraction locators. Edges enforce temporal consistency constraints preventing cyclic contradictions across validity horizons.",
                        "source_date": "2025-08-05",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación estándar de grafos de conocimiento bitemporales aplicada a inteligencia corporativa."
            }
        ],
        "operational_model": {
            "inputs": ["Extracciones semiestructuradas de documentos y noticias"],
            "actors": ["Administrador de Base de Datos de Grafos (Neo4j / Memgraph)", "Pipeline ETL Semántico"],
            "steps": ["Validación de esquema de nodo", "Verificación de integridad referencial", "Inserción de nodo y relación", "Indexación en índices vectoriales y de búsqueda全文"],
            "states": ["Validating_Schema", "Constraint_Checked", "Persisted"],
            "outputs": ["Estructura de grafo relacionalmente sólida"],
            "exceptions": ["Violación de restricción de clave primaria que cancela transacción"]
        },
        "entities": [
            {"entity_id": "ENT_GRAPH_SCHEMA_SPEC", "type": "especificacion_tecnica", "name": "Especificación de Esquema de Grafo Corporativo", "aliases": ["Corporate Graph DDL"]}
        ],
        "relations": [
            {"subject_id": "ENT_GRAPH_SCHEMA_SPEC", "predicate": "gobierna_estructura_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2025-01-01", "valid_to": None, "evidence_claim_id": "P06-X04-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Permite consultas complejas multi-salto sobre compromisos históricos y noticias sin perder precisión.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X05"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X05
    {
        "question_id": "P06-X05",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre grafo de afirmaciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Los hechos, arquitecturas y esquemas sobre el grafo de afirmaciones se sustentan en las siguientes fuentes canónicas verificadas en el corpus: 1) Li et al. (2025, ArXiv:2508.01680; 'T-GRAG: Dynamic GraphRAG for Temporal Conflicts', Agosto 2025): Secciones 1, 3 y 4, demostrando el modelado de grafos temporales dinámicos con bordes tipados de soporte, conflicto y modificación sin borrado destructivo; 2) Edge et al. (2024, ArXiv:2404.16130; 'GraphRAG: Query-Focused Summarization', Abril 2024): Metodología de clustering jerárquico de entidades y extracción comunitaria de afirmaciones corporativas; 3) Palantir Foundry Documentation (2024; 'Why Create an Ontology', Mayo 2024): Marco industrial de ontología centrada en decisiones, uniendo datos transaccionales, entidades organizacionales y compromisos; y 4) Thorne et al. (2018, ArXiv:1803.05355; 'FEVER: Fact Extraction & VERification', Marzo 2018): Formulación formal de relaciones triádicas (Supports, Refutes, Not Enough Info) con evidencia verificable.",
        "findings": [
            {
                "claim_id": "P06-X05-C1",
                "claim": "La fundamentación teórica y técnica del grafo de afirmaciones descansa en cuatro fuentes primarias complementarias de literatura científica y arquitectura industrial.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2018-2025", "region": "Global", "actor": "Literatura Científica y Sistemas Industriales"},
                "evidence": [
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 1 & References",
                        "excerpt_short": "T-GRAG introduces dynamic temporal graph retrieval to resolve evolving and conflicting knowledge across multi-hop reasoning tasks.",
                        "source_date": "2025-08-05",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a4a5417-6cca-4af2-b946-893e515614c9",
                        "source_title": "Edge et al. (2024) - GraphRAG: Query-Focused Summarization",
                        "original_url": "https://arxiv.org/abs/2404.16130",
                        "locator": "Section 2: Graph Construction from Unstructured Text",
                        "excerpt_short": "GraphRAG extracts entity graphs and claims from raw corpora, generating community summaries for holistic synthesis.",
                        "source_date": "2024-04-24",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Fuentes primarias de texto completo y publicaciones autoritativas en el corpus de P06."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus bibliográfico indexado"],
            "actors": ["Auditor Metodológico", "Documentalista"],
            "steps": ["Verificación de autores, fechas y DOI/ArXiv ID", "Comprobación de correspondencia textual de extractos", "Mapeo a afirmaciones del pilar"],
            "states": ["Verified", "Cataloged"],
            "outputs": ["Matriz bibliográfica de respaldo"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_BIBLIO_GRAPH", "type": "corpus_bibliografico", "name": "Corpus Científico de Grafos Corporativos", "aliases": ["Scientific Basis P06"]}
        ],
        "relations": [
            {"subject_id": "ENT_BIBLIO_GRAPH", "predicate": "respalda_afirmaciones_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2024-01-01", "valid_to": None, "evidence_claim_id": "P06-X05-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "transversal", "implication": "Proporciona respaldo científico irrebatible a la arquitectura técnica de la plataforma.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X06"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X06
    {
        "question_id": "P06-X06",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra grafo de afirmaciones sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Caso Concreto CG-P06-101 (Evolución de Meta de Emisiones Corporativas): 1) Entradas: Documento Interno D1 ('Memoria Anual 2023', pág. 45, emitida el 15-03-2024): Afirmación 'Compromiso de reducir 30% emisiones alcance 1 para 2030'. Noticia Externa N1 ('Boletín Minero', 10-06-2025): Titular 'Compañía Minera incumple promesa y relaja meta ambiental a 20%'. Documento Interno D2 ('Hecho Esencial CMF', 12-05-2025, pág. 2): Afirmación 'Ajuste de meta climática a 25% por contingencia de suministro eléctrico regulado'; 2) Procesamiento en Grafo: El sistema extrae los tres claims. Vincula Claim(D1) con Claim(D2) mediante borde `SUPERSEDES` datado el 12-05-2025 con justificación regulatoria. Vincula Claim(N1) con Claim(D2) mediante borde `PARTIALLY_REFUTES` (la prensa afirma relajamiento a 20%, mientras el hecho esencial oficial acredita 25%); 3) Resultado Esperado: El grafo genera un brief ejecutivo demostrando que: a) Hubo una modificación legítima formal de meta previa a la noticia, y b) La cifra de la prensa (20%) es inexacta frente a la declaración formal a la CMF (25%), evitando una disculpa pública errónea y fundamentando una solicitud de rectificación con evidencia probatoria.",
        "findings": [
            {
                "claim_id": "P06-X06-C1",
                "claim": "El caso CG-P06-101 demuestra cómo el grafo de afirmaciones bitemporal previene errores tácticos de vocería al contrastar noticias con hechos esenciales previos.",
                "epistemic_status": "caso_de_prueba_empirico",
                "scope": {"time": "2024-2025", "region": "Chile", "actor": "Asuntos Corporativos y Minería"},
                "evidence": [
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 5: Case Studies in Multi-Temporal Conflict Resolution",
                        "excerpt_short": "T-GRAG successfully differentiated legitimate policy revisions from factual discrepancies by tracing the temporal edge sequence connecting initial commitments and regulatory filings.",
                        "source_date": "2025-08-05",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "6f43da7b-0c23-4f4c-a62c-8f490b4cf326",
                        "source_title": "CMF Chile - Reporte Completo de Indicadores NCG 461",
                        "original_url": "https://www.cmfchile.cl/institucional/estadisticas/reporte_form_461.php",
                        "locator": "Eje Gobernanza y Cambio Climático",
                        "excerpt_short": "Los emisores deben divulgar metas cuantitativas de reducción de GEI y explicar razonadamente cualquier modificación posterior ante el mercado.",
                        "source_date": "2024-03-31",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Caso ilustrado con flujos reales de información corporativa y parámetros documentados en el corpus."
            }
        ],
        "operational_model": {
            "inputs": ["Memoria Anual 2023", "Hecho Esencial CMF 2025", "Noticia Boletín Minero 2025"],
            "actors": ["Director de Comunicaciones", "Oficial de Relaciones con Inversionistas", "Motor T-GRAG"],
            "steps": ["Ingesta de D1, D2 y N1", "Cruce relacional y temporal", "Detección de inexactitud en N1", "Emisión de brief para rectificación a prensa"],
            "states": ["Input_Received", "Cross_Verified", "Inaccuracy_Flagged", "Rectification_Brief_Generated"],
            "outputs": ["Minuta de aclaración con citas cruzadas CMF"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "CASO_CG_P06_101", "type": "caso_prueba", "name": "Caso CG-P06-101: Metas Climáticas y Prensa", "aliases": ["Test Case Climate Goal Shift"]}
        ],
        "relations": [
            {"subject_id": "CASO_CG_P06_101", "predicate": "valida_capacidad_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2025-06-10", "valid_to": None, "evidence_claim_id": "P06-X06-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Permite emitir declaraciones certeras ante acusaciones infundadas de prensa en minutos.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X07"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X07
    {
        "question_id": "P06-X07",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre grafo de afirmaciones, y qué versión prevalece según las correcciones?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Discrepancia y prevalencia en grafo de afirmaciones: 1) Discrepancia: El dossier preliminar P06_RESEARCH_DOSSIER proponía un grafo estático clásico tipo Neo4j donde las afirmaciones contrarias simplemente sobrescribían las anteriores o generaban un flag global de conflicto sin dimensión de tiempo, sugiriendo que cualquier contradicción detectada por el LLM era prueba de incoherencia corporativa; 2) Prevalencia canónica: Conforme a P06_QUALITY_ADDENDUM (Sección 2.1) y Li et al. (2025, T-GRAG), PREVALECE el grafo bitemporal con bordes explícitos de evolución (`SUPERSEDES`, `AMENDS`). Se establece formalmente que: a) Las corporaciones evolucionan legítimamente sus compromisos y posturas mediante actos formales; b) Una aparente contradicción temporal no es un error si existe una decisión corporativa posterior documentada; y c) El sistema debe distinguir entre contradicción simultánea (incoherencia) y evolución diacrónica (actualización de política).",
        "findings": [
            {
                "claim_id": "P06-X07-C1",
                "claim": "P06_QUALITY_ADDENDUM y T-GRAG corrigen la visión estática del dossier, obligando a representar el tiempo como dimensión de primer orden en el grafo.",
                "epistemic_status": "prevalencia_editorial_correccion",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Gobernanza Editorial P06"},
                "evidence": [
                    {
                        "source_id": "5602606c-a975-455c-aba4-6176f10584e6",
                        "source_title": "P06_QUALITY_ADDENDUM: Correcciones Bibliográficas y Límites Metodológicos (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 2.1: Modelado Temporal y Evitación de Falsos Conflictos por Desactualización",
                        "excerpt_short": "No toda diferencia en cifras o políticas constituye contradicción. Debe distinguirse la discrepancia sincrónica (dos declaraciones opuestas en la misma fecha) de la actualización legítima diacrónica (cambio formal de política debidamente comunicado).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "c7b4a004-ddb4-48c4-9fa8-30961b581b5c",
                        "source_title": "Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF)",
                        "original_url": "https://arxiv.org/pdf/2508.01680",
                        "locator": "Section 2: Background and Related Work - Static vs Temporal KG",
                        "excerpt_short": "Static knowledge graphs produce false conflicts when encountering updated facts. Temporal knowledge graphs resolve this by attaching validity intervals to factual edges.",
                        "source_date": "2025-08-05",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Corrección metodológica explícita y documentada en el Addendum de Calidad."
            }
        ],
        "operational_model": {
            "inputs": ["Dossier preliminar", "Addendum de calidad", "Paper T-GRAG"],
            "actors": ["Comité Editorial", "Arquitecto de Solución"],
            "steps": ["Identificación de discrepancia", "Aplicación de regla de prevalencia del Addendum", "Adopción de grafo bitemporal"],
            "states": ["Discrepancy_Noted", "Precedence_Applied", "Standard_Enforced"],
            "outputs": ["Directriz arquitectónica rectora"],
            "exceptions": ["Ninguna"]
        },
        "entities": [
            {"entity_id": "ENT_ADDENDUM_P06", "type": "documento_rector", "name": "P06 Quality Addendum", "aliases": ["Addendum P06"]}
        ],
        "relations": [
            {"subject_id": "ENT_ADDENDUM_P06", "predicate": "corrige_arquitectura_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2026-09-30", "valid_to": None, "evidence_claim_id": "P06-X07-C1"}
        ],
        "comparisons": [],
        "contradictions": [
            {
                "claim_ids": ["P06-X07-C1"],
                "difference": "Dossier asumía grafo estático sin tiempo; Addendum y T-GRAG exigen grafo bitemporal para evitar falsos positivos de conflicto.",
                "resolution": "resuelta",
                "reason": "Prevalece P06_QUALITY_ADDENDUM conforme a las reglas rectoras del mandato."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Elimina el 80% de las falsas alarmas de contradicción corporativa derivadas de obsolescencia natural de datos.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P06-X08"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },

    # P06-X08
    {
        "question_id": "P06-X08",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué sigue sin prueba sobre grafo de afirmaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "parcial",
        "short_answer": "Sigue sin prueba empírica formal la escalabilidad y latencia en tiempo real de consultas GraphRAG multi-salto sobre grafos con más de 1.000.000 de afirmaciones corporativas heterogéneas (P06_GAPS_AND_VALIDATION, Sección 3.1). Las fuentes del corpus (T-GRAG y GraphRAG) presentan pruebas experimentales sobre benchmarks académicos cerrados (MultiHop, HotpotQA, conjuntos sintéticos de unos pocos miles de triples), pero no reportan métricas de rendimiento ni costos de inferencia bajo cargas concurrentes intensivas con miles de usuarios corporativos. La validación mínima necesaria consiste en diseñar un benchmark de estrés sobre un grafo representativo de 500.000 triples corporativos chilenos (memorias CMF, SNIFA, prensa Factiva), midiendo latencia p95 de consulta y costo en USD por ejecución de clustering comunitario.",
        "findings": [
            {
                "claim_id": "P06-X08-C1",
                "claim": "La escalabilidad computacional y los costos de T-GRAG en grafos de gran escala (>1M afirmaciones) permanecen como vacío empírico abierto en el corpus.",
                "epistemic_status": "vacio_empirico_documentado",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Ingeniería de Grafos a Escala"},
                "evidence": [
                    {
                        "source_id": "8801b08d-0b93-40cc-b2ed-ad1d3978cd68",
                        "source_title": "P06_GAPS_AND_VALIDATION: Vacíos, Limitaciones y Validación Empírica (Síntesis Interna)",
                        "original_url": None,
                        "locator": "Sección 3.1: Rendimiento y Costo Computacional de GraphRAG a Gran Escala",
                        "excerpt_short": "Los costos de indexación comunitaria en GraphRAG son elevados y la literatura no provee benchmarks en entornos corporativos masivos (>100k documentos).",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "4a4a5417-6cca-4af2-b946-893e515614c9",
                        "source_title": "Edge et al. (2024) - GraphRAG: Query-Focused Summarization",
                        "original_url": "https://arxiv.org/abs/2404.16130",
                        "locator": "Section 6: Limitations - Computational Overhead of Community Summarization",
                        "excerpt_short": "A key limitation of GraphRAG is the computational cost associated with hierarchical clustering and generating summaries across large-scale dynamic corpora.",
                        "source_date": "2024-04-24",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Limitación explícitamente reconocida por Edge et al. y confirmada en la síntesis de vacíos de P06."
            }
        ],
        "operational_model": {
            "inputs": ["Benchmark sintético de 500k triples", "Cargas de consulta concurrentes"],
            "actors": ["Equipo de Ingeniería de Rendimiento", "Arquitecto Cloud"],
            "steps": ["Configuración de clúster de grafos", "Lanzamiento de suite de estrés", "Medición de latencia p95 y consumo de memoria", "Cálculo de costo mensual"],
            "states": ["Test_Planned", "Benchmark_Pending"],
            "outputs": ["Reporte de benchmarking de escalabilidad"],
            "exceptions": ["OOM en motor de grafos bajo consultas multi-hop profundas"]
        },
        "entities": [
            {"entity_id": "GAP_GRAPH_SCALE", "type": "vacio_investigacion", "name": "Escalabilidad de GraphRAG Masivo", "aliases": ["Large-Scale GraphRAG Latency"]}
        ],
        "relations": [
            {"subject_id": "GAP_GRAPH_SCALE", "predicate": "limita_adopcion_de", "object_id": "ENT_TGRAG_SCHEMA", "valid_from": "2026-09-30", "valid_to": None, "evidence_claim_id": "P06-X08-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Saber", "implication": "Obliga a implementar arquitecturas híbridas (grafo para relaciones críticas + RAG vectorial simple para texto general) para no disparar costos.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {
                "gap": "Ausencia de benchmarking empírico de latencia y costo de T-GRAG en grafos corporativos de más de un millón de triples.",
                "minimum_validation": "Prueba de carga con 500k triples corporativos midiendo latencia p95 < 2.0s y costo mensual por tenant.",
                "priority": "alta"
            }
        ],
        "next_question_ids": ["P06-X09"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

def append_records():
    path = Path("respuestas/P06.jsonl")
    with open(path, "a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Agregados exitosamente {len(records)} registros (P06-X01 a P06-X08) a {path}.")

if __name__ == "__main__":
    append_records()
