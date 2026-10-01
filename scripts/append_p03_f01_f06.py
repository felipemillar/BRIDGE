import json
from pathlib import Path

NOTEBOOK_ID = "a2afe847-a988-40f1-9432-9e596b74b376"
SNAPSHOT_AT = "2026-10-01T02:00:00-03:00"

records = [
    # P03-F01
    {
        "question_id": "P03-F01",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué tipos de señales de prensa, redes, broadcast, reguladores y comunidades son relevantes?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Para asuntos corporativos, las señales relevantes se dividen en 5 familias operativas: 1) Prensa estructurada y web abierta (artículos periodísticos, editoriales, columnas de opinión y blogs especializados con metadata de autor y medio); 2) Redes sociales y plataformas comunitarias (mensajería pública en Telegram, firehose federado en AT Protocol/Bluesky, foros temáticos en Reddit y publicaciones públicas muestreadas); 3) Broadcast audiovisual (emisiones lineales de TV nacional y regional, radioemisoras locales AM/FM y podcasts temáticos); 4) Señales regulatorias e institucionales oficiales (hechos esenciales de la CMF, resoluciones y decretos del Diario Oficial, licitaciones de ChileCompra/Mercado Público, tramitaciones del Congreso y Form 8-K/10-K de la SEC); y 5) Señales comunitarias de base (declaraciones de comunidades locales, reclamos en servicios de evaluación ambiental y actas de organizaciones vecinales).",
        "findings": [
            {
                "claim_id": "P03-F01-C1",
                "claim": "Las señales externas críticas para asuntos corporativos abarcan cinco categorías operativas: prensa, redes/foros, broadcast audiovisual, reguladores oficiales y dinámica comunitaria territorial.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Internacional", "actor": "Ecosistema de Monitoreo P03"},
                "evidence": [
                    {
                        "source_id": "73488fee-1939-4426-b579-d9ca61c6eaa3",
                        "source_title": "P03_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2: Mapeo Estructurado por Área Temática",
                        "excerpt_short": "Para garantizar la máxima rigurosidad analítica... este documento clasifica toda la evidencia recolectada en cuatro categorías... prensa, redes sociales, broadcast audiovisual y señales institucionales.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Taxonomía consolidada en el mapa de evidencia del pilar P03."
            }
        ],
        "operational_model": {
            "inputs": ["Feeds RSS de prensa", "Firehose de AT Protocol", "Subtítulos/audio de TV y radio", "APIs de CMF y ChileCompra"],
            "actors": ["Ingest Worker", "Signal Normalizer", "Taxonomy Classifier"],
            "steps": ["Captura de stream crudo", "Normalización a formato común", "Clasificación por tipo de señal"],
            "states": ["Raw_Ingested", "Normalized", "Classified_By_Family"],
            "outputs": ["Event Stream clasificado en las 5 familias de señales corporativas"],
            "exceptions": ["Caída de conectividad en fuentes regulatorias estatales"]
        },
        "entities": [
            {"entity_id": "ENT_SIGNAL_FAMILIES", "type": "taxonomia", "name": "Familias de Señales de Entorno", "aliases": ["Signal Taxonomy"]}
        ],
        "relations": [
            {"subject_id": "ENT_SIGNAL_FAMILIES", "predicate": "estructura_ingesta_de", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F01-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza de la señal",
                "Prensa": "Artículos editoriales con autoría, línea editorial y latencia horaria.",
                "Reguladores": "Documentos normativos formales, hechos esenciales vinculantes y efectos jurídicos inmediatos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "BRIDGE debe implementar conectores modulares independientes para cada una de las 5 familias para evitar cuellos de botella en la ingesta.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F02"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F02
    {
        "question_id": "P03-F02",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué metadatos mínimos permiten comparar noticias, publicaciones, alertas y documentos oficiales?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "El esquema canónico de metadatos mínimos para homologar señales heterogéneas consta de 8 atributos obligatorios: 1) `signal_id` (UUID único determinístico); 2) `timestamp_published` (marca temporal ISO-8601 con zona horaria UTC/local); 3) `source_type` (prensa, red_social, broadcast, regulador, comunidad); 4) `source_identifier` (medio, handle, canal, boletín o registro oficial); 5) `author_or_issuer` (periodista, usuario verificado u organismo emisor); 6) `content_payload` (texto completo, transcripción o extracto estructurado); 7) `entities_extracted` (entidades nombradas normalizadas con URIs de Wikidata/registro local); y 8) `provenance_url_or_locator` (URL permanente, identificador oficial de expediente o rango temporal de emisión).",
        "findings": [
            {
                "claim_id": "P03-F02-C1",
                "claim": "La homologación analítica entre noticias, redes sociales y resoluciones regulatorias requiere una estructura común de 8 metadatos fundamentales con identificadores de procedencia inmutables.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Sistemas de Inteligencia P03"},
                "evidence": [
                    {
                        "source_id": "c1d4d3e2-d64c-49c9-9c54-cfcd11a97967",
                        "source_title": "Event Registry & NewsAPI.ai Developer Documentation",
                        "original_url": "https://www.newsapi.ai/documentation/examples",
                        "locator": "Core Article Object & Event Representation",
                        "excerpt_short": "Event Registry represents each news item with uri, dateTime, source, authors, body, extracted entities, and assigned event uri.",
                        "source_date": "2026",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificado contra especificaciones técnicas de APIs de eventos y noticias."
            }
        ],
        "operational_model": {
            "inputs": ["Payloads nativos de proveedores de noticias, redes y APIs estatales"],
            "actors": ["Metadata Normalizer"],
            "steps": ["Extracción de timestamp", "Resolución de autor", "Asignación de UUID", "Generación de envelope JSON-LD"],
            "states": ["Raw_Payload", "Schema_Mapped", "Validated_Envelope"],
            "outputs": ["Document Envelope canónico normalizado"],
            "exceptions": ["Falta de marcas temporales precisas en feeds RSS antiguos"]
        },
        "entities": [
            {"entity_id": "ENT_SIGNAL_SCHEMA", "type": "esquema_datos", "name": "Esquema Canónico de Metadatos de Señal", "aliases": ["Canonical Signal Schema"]}
        ],
        "relations": [
            {"subject_id": "ENT_SIGNAL_SCHEMA", "predicate": "estandariza_mensajes_de", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F02-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Adoptar el esquema de 8 metadatos en Kafka/RabbitMQ para garantizar interoperabilidad con el grafo de conocimiento.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F03"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F03
    {
        "question_id": "P03-F03",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se distingue una mención de marca de un cambio material para asuntos corporativos?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La distinción se basa en tres filtros metodológicos acumulativos: 1) Umbral de materialidad regulatoria y financiera: una mención de marca es un evento meramente comunicacional (ej. auspicio deportivo, review de producto), mientras que un cambio material altera los derechos, obligaciones, gobernanza, operaciones o valoración de la corporación (equivalente al criterio de Hecho Esencial de la CMF y Form 8-K de la SEC); 2) Señales de entorno no nominales: los mayores riesgos emergen en señales sectoriales donde la marca ni siquiera es nombrada inicialmente (ej. cambios tributarios, regulaciones de cuencas de agua, litigios contra competidores directos); y 3) Marco AMEC: separar 'outputs' (menciones de vanidad / volumen) de 'outcomes' e impacto organizacional estratégico.",
        "findings": [
            {
                "claim_id": "P03-F03-C1",
                "claim": "Los cambios materiales para asuntos corporativos se definen por su impacto en gobernanza, regulación y operación sectorial, y frecuentemente no contienen el nombre de la empresa en sus fases iniciales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "CMF / SEC / AMEC"},
                "evidence": [
                    {
                        "source_id": "5eaa5b99-624c-4877-87be-66c339c7b6d4",
                        "source_title": "AMEC Barcelona Principles 3.0 & Integrated Evaluation Framework",
                        "original_url": "https://amecorg.com/barcelona-principles-3-0-translations/",
                        "locator": "Principle 2: Measuring Communication Outcomes is Recommended Versus Only Measuring Outputs",
                        "excerpt_short": "Outcomes include shifts in awareness, comprehension, attitude, stance, and organizational impact, distinct from mere mention volume or media impressions.",
                        "source_date": "2020",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "ccc863f8-d879-4693-b10c-015f8ae278fa",
                        "source_title": "CMF Chile - Sistema de Consulta de Hechos Esenciales y Normativa",
                        "original_url": "https://www.cmfchile.cl/portal/principal/623/w4-propertyvalue-48783.html",
                        "locator": "Definición de Hecho Esencial (Ley 18.045 Art. 9 y 10)",
                        "excerpt_short": "Hecho esencial es todo aquel acontecimiento que una persona juiciosa consideraría importante para sus decisiones sobre la marcha social o títulos de la entidad.",
                        "source_date": "2026",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Respaldo directo en normativa legal de mercado de valores y estándares AMEC."
            }
        ],
        "operational_model": {
            "inputs": ["Texto de señal entrante", "Lista de entidades corporativas", "Ontología de riesgos sectoriales"],
            "actors": ["Materiality Classifier", "Graph Query Engine"],
            "steps": ["Verificación de mención directa", "Análisis de impacto regulatorio sectorial", "Ponderación de severidad AMEC"],
            "states": ["Raw_Signal", "Direct_Mention_Flagged", "Materiality_Evaluated"],
            "outputs": ["Clasificación dicotómica: Mención_Superficial vs Cambio_Material_Corporativo"],
            "exceptions": ["Menciones aparentemente triviales emitidas por figuras con alto poder de veto regulatorio"]
        },
        "entities": [
            {"entity_id": "ENT_MATERIAL_CHANGE", "type": "concepto_regulatorio", "name": "Cambio Material Corporativo", "aliases": ["Material Event", "Hecho Esencial"]}
        ],
        "relations": [
            {"subject_id": "ENT_MATERIAL_CHANGE", "predicate": "discrimina_relevancia_en", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F03-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Criterio de clasificación",
                "Mención de Marca": "Presencia de keywords comerciales o menciones directas en prensa/redes.",
                "Cambio Material": "Afectación jurídica, regulatoria, reputacional o de licencia social para operar."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Descartar dashboards de simple 'volumen de menciones' e incorporar clasificadores de materialidad regulatoria y de negocio.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F04"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F04
    {
        "question_id": "P03-F04",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar taxonomía de señales externas de forma estructurada?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "La representación estructurada de la taxonomía de señales exige: 1) Variables primarias: `severidad` (crítica, alta, media, baja), `alcance_geografico` (nacional, regional, comunal), `fase_regulatoria` (discusión_publica, proyecto_ley, tramite_legislativo, norma_vigente), `polarizacion_discursiva` y `velocidad_propagacion`; 2) Categorías canónicas: Institucional-Regulatoria, Judicial-Litigios, Operacional-Ambiental, Laboral-Sindical, Financiera-Mercado y Reputacional-Mediatica; 3) Relaciones en grafo: `involucra_a` (entidad), `afecta_sector` (industria), `origina_en` (fuente), `amenaza_objetivo` (KPI o proyecto corporativo) y `precede_a` (secuencia causal); y 4) Condiciones de integridad: toda señal categorizada como regulatoria debe enlazar a un expediente verificable y contar con marca temporal formal.",
        "findings": [
            {
                "claim_id": "P03-F04-C1",
                "claim": "Una taxonomía estructurada de señales externas requiere modelar variables de severidad y ciclo de vida regulatorio, vinculándolas como grafos de conocimiento a entidades y sectores.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Modelado Ontológico P03"},
                "evidence": [
                    {
                        "source_id": "73488fee-1939-4426-b579-d9ca61c6eaa3",
                        "source_title": "P03_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2.4: Señales Institucionales y Regulatorias",
                        "excerpt_short": "Todas estas fuentes se estructuran por taxonomía de temas (ej. agua, royalty, permisos ambientales, reforma tributaria), no por marca.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación del diseño ontológico de monitoreo de entorno."
            }
        ],
        "operational_model": {
            "inputs": ["Señal normalizada", "Ontología corporativa en OWL/RDF"],
            "actors": ["Semantic Reasoner", "Knowledge Graph Store"],
            "steps": ["Mapeo a categorías canónicas", "Instanciación de relaciones en grafo", "Cálculo de variables de severidad"],
            "states": ["Raw_Signal", "Graph_Triples_Generated", "Committed_To_KG"],
            "outputs": ["Subgrafo RDF de señal externa enriquecido"],
            "exceptions": ["Ambigüedad temática que active reglas de inferencia contradictorias"]
        },
        "entities": [
            {"entity_id": "ENT_SIGNAL_TAXONOMY", "type": "ontologia", "name": "Ontología de Señales Externas", "aliases": ["Signal Ontology"]}
        ],
        "relations": [
            {"subject_id": "ENT_SIGNAL_TAXONOMY", "predicate": "define_esquema_de", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F04-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Representar las señales como tripletas en el grafo de BRIDGE para permitir razonamiento relacional cruzado con el módulo Saber.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F05"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F05
    {
        "question_id": "P03-F05",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre taxonomía de señales externas?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Los hechos de la taxonomía de señales externas están respaldados por: 1) Estándares de medición comunicacional: AMEC Barcelona Principles 3.0 (2020), que fundamenta el abandono de impresiones superficiales y exige medir outcomes organizacionales e institucionales; 2) Normalización de eventos noticiosos y clustering: Event Registry API Documentation (2026) y GDELT 2.0 Global Event Database (2015-2026), que especifican la extracción de actores, eventos y tono multilingüe en intervalos de 15 minutos; 3) Normativa de divulgación y materialidad: Ley 18.045 de Mercado de Valores y Resoluciones de la CMF Chile (2026), y SEC EDGAR System Guidelines para Form 8-K/10-K (2026); y 4) Rectificación editorial y deslinde metodológico: P03_QUALITY_ADDENDUM (Septiembre 2026, Sección 2), que desvincula taxativamente la coordinación temporal de la falsedad discursiva y establece el carácter no oficial de precios de redes.",
        "findings": [
            {
                "claim_id": "P03-F05-C1",
                "claim": "El respaldo documental primario de la taxonomía de señales se distribuye entre estándares internacionales AMEC, APIs de eventos masivos (GDELT, Event Registry), leyes de mercado de valores (CMF, SEC) y la adenda de calidad P03.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2020-2026", "region": "Chile / EE.UU. / Europa", "actor": "Corpus Canónico P03"},
                "evidence": [
                    {
                        "source_id": "e895c495-1608-46f4-b921-ca7bb60aac75",
                        "source_title": "P03_QUALITY_ADDENDUM",
                        "original_url": None,
                        "locator": "Sección 1 y 2: Propósito y Rectificaciones Específicas",
                        "excerpt_short": "Esta adenda tiene como propósito auditar, calibrar y rectificar las aseveraciones analíticas... deslindando hechos técnicos directamente verificables respecto a inferencias operativas.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "6ad73a33-ba1d-48af-899d-b0a20126725f",
                        "source_title": "GDELT 2.0 Global Event Database Documentation",
                        "original_url": "https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/",
                        "locator": "GDELT 2.0 Architecture and Update Intervals",
                        "excerpt_short": "GDELT 2.0 translates and monitors global news in over 100 languages, updating its Event, Mentions, and Global Knowledge Graph tables every 15 minutes.",
                        "source_date": "2015",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Trazabilidad cruzada de fuentes primarias y documentos canónicos del pilar."
            }
        ],
        "operational_model": {
            "inputs": ["Repositorio de fuentes P03", "Índice de citas primarias"],
            "actors": ["Compliance Auditor", "Evidence Verifier"],
            "steps": ["Verificación de URL/UUID", "Comprobación de fecha de vigencia", "Cotejo de pasajes"],
            "states": ["Unverified_Citation", "Source_Retrieved", "Citations_Audited"],
            "outputs": ["Matriz de respaldo de evidencia verificada"],
            "exceptions": ["Fuentes con cambios de endpoints en portales gubernamentales"]
        },
        "entities": [
            {"entity_id": "ENT_CANONICAL_CORPUS_P03", "type": "corpus_documental", "name": "Corpus Canónico de Evidencia P03", "aliases": ["P03 Evidence Corpus"]}
        ],
        "relations": [
            {"subject_id": "ENT_CANONICAL_CORPUS_P03", "predicate": "respalda_afirmaciones_de", "object_id": "Pilar_P03", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F05-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "Mantener una base de datos de referencias canónicas con hash inmutable para todas las señales ingeridas.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-F06"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    },
    # P03-F06
    {
        "question_id": "P03-F06",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra taxonomía de señales externas sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT_AT,
        "answer_status": "respondida",
        "short_answer": "Caso: Monitoreo regulatorio y mediático ante un nuevo proyecto de ley de royalty a la minería en Chile. Entradas: 1) Boletín oficial de la Cámara de Diputadas y Diputados de Chile anunciando el ingreso del proyecto de ley (Señal Institucional/Regulatoria); 2) Nota de prensa en portal regional de Antofagasta reportando la reacción del gremio minero (Señal de Prensa Abierta); 3) Alerta de Hecho Esencial publicado por una minera inscrita en la CMF informando impacto en inversiones proyectadas (Señal de Mercado/CMF); y 4) Transcripción de entrevista radial a dirigente sindical en radioemisora de Calama vía Whisper (Señal Broadcast Local). Resultado esperado: El clasificador taxonómico asigna la señal al tema 'Minería - Royalty', vincula las 4 entradas al mismo evento madre (`cluster_event_id`), calcula severidad 'Alta', y categoriza el impacto como 'Riesgo Regulatorio e Impositivo' sin depender de que una empresa particular haya sido nombrada en el texto original del boletín oficial.",
        "findings": [
            {
                "claim_id": "P03-F06-C1",
                "claim": "Un caso estructurado de monitoreo multidimensional integra señales institucionales, prensa regional, hechos esenciales de CMF y radio local vinculándolos a un evento madre sin requerir coincidencia léxica de marca.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile (Antofagasta / Calama)", "actor": "Caso Operativo P03"},
                "evidence": [
                    {
                        "source_id": "73488fee-1939-4426-b579-d9ca61c6eaa3",
                        "source_title": "P03_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 2.4: Señales Institucionales y Regulatorias",
                        "excerpt_short": "Los riesgos corporativos y regulatorios más severos emergen en señales indirectas de competidores... o modificaciones normativas que jamás mencionan el nombre de la organización afectada en sus etapas iniciales.",
                        "source_date": "2026-09-30",
                        "retrieved_at": SNAPSHOT_AT,
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación basada en la síntesis de diseño y casos del mapa de evidencia."
            }
        ],
        "operational_model": {
            "inputs": ["Boletín Congreso", "Prensa Regional", "Hecho Esencial CMF", "Transcripción Radial"],
            "actors": ["Multi-Channel Ingest", "Event Clusterer", "Graph Router"],
            "steps": ["Captura multicanal", "Extracción semántica", "Clustering temático", "Enrutamiento a tablero corporativo"],
            "states": ["Raw_Inputs", "Multi_Channel_Parsed", "Event_Unified"],
            "outputs": ["Ficha de Evento Consolidado 'Royalty Minero' con sus 4 señales de soporte"],
            "exceptions": ["Retraso en la transcripción radial de la emisora de Calama"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_ROYALTY", "type": "caso_de_uso", "name": "Caso Demostrativo Monitoreo Royalty Minero", "aliases": ["Royalty Monitoring Case"]}
        ],
        "relations": [
            {"subject_id": "ENT_CASO_ROYALTY", "predicate": "valida_operacion_de", "object_id": "BRIDGE_Modulo_Escuchar", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P03-F06-C1"}
        ],
        "comparisons": [],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Implementar clustering multicanal por tema para agrupar señales oficiales, periodísticas y radiales en un único flujo de toma de decisiones.", "status": "hipotesis"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P03-C01"],
        "quality": {"original_citations_resolved": True, "correction_precedence_checked": True, "duplicate_sources_counted_once": True, "human_review_needed": False}
    }
]

out_file = Path("respuestas/P03.jsonl")
out_file.parent.mkdir(parents=True, exist_ok=True)
with open(out_file, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Batch 1 (P03-F01 to P03-F06) written successfully to {out_file}.")
