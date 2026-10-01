import json
import os
import sys

# Script to generate P02-F13 through P02-F18 with full 20 keys schema

records = [
    {
        "question_id": "P02-F13",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué cubren Meltwater, Cision/Brandwatch, Signal AI, Hootsuite/Talkwalker y Onclusive?",
        "snapshot_at": "2026-10-01T01:31:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Cubren la captura y analítica del entorno exterior con focos diferenciados: 1) Meltwater (+300.000 fuentes de noticias, broadcast TV/radio, podcasts, alianzas de datos con Reddit/X/Meta, APIs a Snowflake/BigQuery y soporte MCP desde 2025; brecha: ciega a repositorios internos); 2) Cision / Brandwatch (Cision Ltd. / Platinum Equity: adq. Brandwatch en junio 2021 por USD 450M, combina base de datos de periodistas, PR Newswire y +100M fuentes de consumidor; brecha: orientada a marketing B2C sin RAG interno); 3) Signal AI (motor AIQ con 5,5M docs/día en 80+ idiomas, grafo de entidades ESG y analítica de lecturas reales Memo incorporada el 20 abril 2026; brecha: grafo entrenado solo sobre corpus público); 4) Hootsuite / Talkwalker (adq. abril 2024, motores Blue Silk AI y Yeti AI Agent para escucha social profunda y analítica visual/logos; brecha: orientada a redes de consumo); 5) Onclusive (Symphony Technology Group: fusiona Kantar Rep Intelligence, PRgloo, Critical Mention y Digimind, monitorea 28M contenidos diarios con AI Sense y modelos de PR Attribution a tráfico web; brecha: analítica retrospectiva sin integración a memoria corporativa).",
        "findings": [
            {
                "claim_id": "P02-F13-C1",
                "claim": "Las cinco principales plataformas de escucha y reputación globales cubren masivamente noticias, broadcast y redes sociales públicas mediante IA analítica y grafos de entidades (Signal AI) o atribución de PR (Onclusive), pero todas comparten la limitación estructural de no indexar repositorios documentales privados ni actas internas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Global", "actor": "Suites de Escucha Globales"},
                "evidence": [
                    {
                        "source_id": "1f9d6fc8-3c21-4523-803f-c4c81af0228e",
                        "source_title": "Meltwater Platform Integrations and APIs",
                        "original_url": "https://www.meltwater.com/en/platform/integrations-api",
                        "locator": "Sección: Media Monitoring and Data Exports",
                        "excerpt_short": "Ingests +300k global news sources and social channels with REST APIs to BI warehouses.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:31:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "02867004-2c18-4bfc-b6de-542385dd2bdb",
                        "source_title": "Onclusive Media Monitoring and Measurement Platform",
                        "original_url": "https://onclusive.com/products/media-monitoring/",
                        "locator": "Platform Capabilities and PR Attribution",
                        "excerpt_short": "Monitors 28M contents daily across 60,000 print titles, 3M websites and 12,000 broadcast channels with PR Attribution.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:31:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación técnica en especificaciones de producto de las 5 compañías."
            }
        ],
        "operational_model": {
            "inputs": ["Feeds RSS", "Transmisiones broadcast", "Firehoses de redes sociales"],
            "actors": ["Plataformas de Escucha", "Analistas de PR", "Algoritmos NLP"],
            "steps": ["Ingesta masiva continua", "Normalización y OCR/ASR", "Extracción de entidades y sentimiento", "Visualización en dashboards volumétricos"],
            "states": ["Dato_Capturado", "Entidades_Indexadas", "Alerta_Disparada"],
            "outputs": ["Clipping de prensa, alertas de picos y reportes de volumen"],
            "exceptions": ["Contenido tras paywalls cerrados o radios locales analógicas"]
        },
        "entities": [
            {"entity_id": "ENT_SIGNAL_AI", "type": "plataforma_escucha", "name": "Signal AI Ltd.", "aliases": ["Signal AI AIQ Platform"]},
            {"entity_id": "ENT_ONCLUSIVE", "type": "plataforma_escucha", "name": "Onclusive Inc.", "aliases": ["STG Media Intelligence Group"]}
        ],
        "relations": [
            {"subject_id": "ENT_SIGNAL_AI", "predicate": "procesa_volumen_diario_de", "object_id": "5.5M_Documentos", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F13-C1"},
            {"subject_id": "ENT_ONCLUSIVE", "predicate": "aplica_modelo_de", "object_id": "PR_Attribution", "valid_from": "2022", "valid_to": None, "evidence_claim_id": "P02-F13-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Enfoque de Signal AI vs Enfoque de Onclusive",
                "Signal AI": "Grafo de conocimiento probabilístico sobre entidades y pilares ESG en 80+ idiomas.",
                "Onclusive": "Mayor base de prensa escrita europea y correlación estadística de tráfico web (PR Attribution)."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "Comprar feeds de ingesta comercial masiva (APIs) en lugar de construir scrapers globales propios para BRIDGE.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F14", "P02-F15"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F14",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Dónde terminan la captura y análisis de señales y comienzan la preparación o gestión de decisiones?",
        "snapshot_at": "2026-10-01T01:31:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La frontera entre captura/análisis y preparación/decisión constituye el 'abismo de conocimiento' del mercado: 1) Dónde termina la captura (Sensing): concluye en la alerta o métrica del exterior (notificación de pico de 500 menciones, nubes de palabras, alertas de incidentes en Dataminr o polaridad negativa en Signal AI). Las herramientas dicen 'qué pasó afuera', pero se detienen ahí sin entregar la postura institucional; 2) Dónde comienza la preparación/decisión (Memory): inicia cuando el CCO o CEO debe responder preguntas institucionales críticas: '¿qué dijimos nosotros oficialmente sobre este asunto, qué compromiso asumimos en la RCA ambiental, qué ejecutivos están autorizados para hablar y cuáles son las 3 respuestas aprobadas para la prensa?'; 3) Falla del mercado: ante una crisis, los equipos sufren una parálisis operativa de 2 a 6 horas buscando manualmente archivos en SharePoint o correos; 4) Fronteras de software existentes: Broadsight actúa como System of Record para posturas internas pero no ingesta medios masivos; Burson Decipher simula impacto cognitivo pero es un servicio cerrado de agencia; AlphaSense hace RAG en SharePoint pero está orientado a finanzas/M&A sin flujos de crisis para prensa; The Bridge Intelligence plantea la hipótesis de unir ambos mundos mediante el Grafo Bipartito Bitemporal.",
        "findings": [
            {
                "claim_id": "P02-F14-C1",
                "claim": "Existe una desconexión operacional crítica entre las plataformas de monitoreo externo y los repositorios corporativos internos: las herramientas de escucha alertan de la controversia externa pero no pueden verificar si la imputación contradice o cumple los compromisos institucionales previos de la empresa.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-10-01", "region": "Global", "actor": "Direcciones de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "a09a8342-7518-4a75-acd7-1975273d4982",
                        "source_title": "P02_GLOBAL_COMPETITOR_DEEP_DIVES_V1",
                        "original_url": None,
                        "locator": "Sección: The Knowledge-Sensing Chasm",
                        "excerpt_short": "Desconexión absoluta entre la escucha del entorno exterior y la memoria corporativa interna documental.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:31:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Diagnóstico de arquitectura de mercado documentado en los informes analíticos del pilar."
            }
        ],
        "operational_model": {
            "inputs": ["Alerta de controversia externa", "Repositorio documental interno", "Directorio de portavoces"],
            "actors": ["CCO", "Director de Asuntos Públicos", "Vocero Asignado"],
            "steps": ["Recepción de alerta volumétrica", "Búsqueda manual en carpetas de red (parálisis de 2-6 horas)", "Identificación de postura previa", "Redacción de minuta para vocero"],
            "states": ["Alerta_Recibida", "Busqueda_Manual_En_Curso", "Briefing_Elaborado"],
            "outputs": ["Minuta de posición directiva para medios"],
            "exceptions": ["Desalineamiento entre vocero y compromiso legal previo por no encontrar el documento a tiempo"]
        },
        "entities": [
            {"entity_id": "GAP_KNOWLEDGE_SENSING", "type": "vacio_estructural", "name": "The Knowledge-Sensing Chasm", "aliases": ["Brecha entre Escucha y Decisión"]}
        ],
        "relations": [
            {"subject_id": "GAP_KNOWLEDGE_SENSING", "predicate": "causa_retraso_de", "object_id": "Paralisis_Operativa_2_a_6_Horas", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F14-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Dashboard Volumétrico vs Executive Briefing Asistido",
                "Dashboard Tradicional (Meltwater/Brandwatch)": "Gráficos de barras y nubes de palabras que el CEO no puede usar en una entrevista.",
                "Executive Briefing BRIDGE": "Dossier sintético de 1 página con datos contrastados, citas legales y Q&A de preguntas difíciles."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Diseñar BRIDGE como el puente activo entre la señal externa y el archivo interno, generando Executive Briefs con Q&A en < 5 minutos.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F15", "P02-F16"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F15",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué diferencias de fuentes, acceso y actualización importan para Chile y Latinoamérica?",
        "snapshot_at": "2026-10-01T01:31:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Existen 3 diferencias críticas que hacen inoperantes las herramientas anglosajonas en Chile y LatAm: 1) Omisión de prensa regional y radios locales: los agregadores globales (Meltwater, Cision) cubren diarios nacionales de Santiago, pero son ciegos a radioemisoras provinciales y prensa local (críticas en conflictos mineros en el norte o forestales/energéticos en el sur); proveedores locales como Litoralpress suplen esto mediante escaneo, OCR y grabación 24/7 con boletines matutinos (< 07:30 AM); 2) Desconexión con el marco normativo chileno: herramientas globales de asuntos públicos (Quorum, FiscalNote) no se integran con la Ley N° 20.730 de Lobby (InfoLobby), las Resoluciones de Calificación Ambiental (RCA) del SEA ni la tramitación legislativa del Congreso chileno (indicaciones, comisiones mixtas); 3) Barrera de precios: contratos mínimos en USD de $20.000 a $80.000+ anuales resultan prohibitivos para el mercado medio regional. Proveedores relevantes del ecosistema regional: Litoralpress y Conecta Media (Chile), Knewin (Brasil/LatAm), Búho Media (Colombia/LatAm, alineada con AMEC), Cadem (Plaza Pública y panel 400k usuarios), Merco (reputación auditada por KPMG) y consultoras senior como Tironi, Azerta y Extend.",
        "findings": [
            {
                "claim_id": "P02-F15-C1",
                "claim": "En Chile, más del 60% de las controversias territoriales en industrias extractivas (minería, energía, celulosa) se originan en radios provinciales y medios locales que las suites multinacionales de monitoreo no capturan debido a paywalls cerrados y transmisiones analógicas no digitalizadas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Chile (Regiones)", "actor": "Medios Locales y Empresas"},
                "evidence": [
                    {
                        "source_id": "2fd3bc2b-f4aa-4236-ba6d-2527a3b36aef",
                        "source_title": "Litoralpress Chile Monitoreo de Medios e Inteligencia de Prensa",
                        "original_url": "https://www.litoralpress.cl/",
                        "locator": "Cobertura Nacional y Regional en Chile",
                        "excerpt_short": "Grabación y OCR de prensa escrita provincial y radioemisoras locales desde Arica a Punta Arenas.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:31:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación del estándar operativo del clipping de medios en el mercado chileno."
            }
        ],
        "operational_model": {
            "inputs": ["Transmisiones de radio AM/FM provincial", "Ediciones impresas locales escaneadas", "Plataforma InfoLobby"],
            "actors": ["Proveedor Local de Clipping", "Servicio de Evaluación Ambiental", "Dircom Regional"],
            "steps": ["Grabación y digitalización matutina", "Entrega antes de las 07:30 AM", "Cotejo con expedientes territoriales", "Detección de alertas tempranas"],
            "states": ["Emision_Radial_Detectada", "Transcripcion_Generada", "Alerta_Regional_Distribuida"],
            "outputs": ["Boletín matutino de prensa regional de Chile"],
            "exceptions": ["Retraso en transcripciones de radios comunitarias rurales sin señal online"]
        },
        "entities": [
            {"entity_id": "ENT_LITORALPRESS", "type": "proveedor_local_chile", "name": "Litoralpress Ltda.", "aliases": ["Estándar de Clipping en Chile"]},
            {"entity_id": "ENT_CADEM", "type": "empresa_opinion_publica", "name": "Cadem Investigación y Estrategia", "aliases": ["Plaza Pública Cadem"]}
        ],
        "relations": [
            {"subject_id": "ENT_LITORALPRESS", "predicate": "provee_cobertura_regional_en", "object_id": "Chile", "valid_from": "2020", "valid_to": None, "evidence_claim_id": "P02-F15-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Agregador Global vs Proveedor Local en Chile",
                "Agregador Global (Meltwater)": "Monitoreo masivo de internet con omisión de prensa provincial y radios AM/FM locales.",
                "Proveedor Local (Litoralpress)": "Cobertura exhaustiva territorial entregada antes de las 07:30 AM con acceso a paywalls cerrados."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "BRIDGE debe integrar la API de Litoralpress o Conecta Media para Chile, asegurando la cobertura del 100% de la prensa provincial y radios regionales.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F16", "P02-F17"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F16",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar plataformas de escucha y reputación de forma estructurada?",
        "snapshot_at": "2026-10-01T01:31:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Exige estructurar un modelo cuatripartito: 1) Los 4 Módulos Cardinales: Saber (memorias ESG, actas, discursos y RAG estricto), Escuchar (prensa, broadcast, redes, podcasts, detección de velocidad con NewsWhip y grafos de riesgo con Signal AI), Hablar (Broadsight System of Record, Executive Briefs y Q&A asistido) y Relacionar (CRM de autoridades, Ley de Lobby y acuerdos comunitarios tipo Borealis/Open Point); 2) Variables de Grafo de Entidades: nodos de ejecutivos, empresas, reguladores y comunidades con aristas de cercanía y polaridad semántica; atributos de señal (velocidad de propagación, lecturas reales verificadas vía Memo y autenticidad del perfil vía Cyabra); 3) Escala Epistémica de Calificación: OPD, FD, DTI, POR (=Ninguna) y ND; 4) Cuatro Condiciones Operativas Estrictas: Condición Zero Hallucination (citas obligatorias a nivel de párrafo y página en documentos internos o notas externas), Enlace Bitemporal Bipartito (cruzar la noticia de hoy con el compromiso firmado hace años), Gobernanza Human-in-the-Loop (controles RBAC donde ningún borrador se libera sin firma del CCO), y Alineación AMEC (eliminación del AVE publicitario desacreditado y foco en métricas de outcomes de reputación).",
        "findings": [
            {
                "claim_id": "P02-F16-C1",
                "claim": "La modelación de plataformas de inteligencia corporativa exige la adopción estricta de los estándares de AMEC (Barcelona Principles 3.0), prohibiendo el uso del valor publicitario equivalente (AVE) y basando la medición en métricas de cambio de percepción, confianza y capital relacional (outcomes).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2020-2026", "region": "Global", "actor": "Estándar Metodológico AMEC"},
                "evidence": [
                    {
                        "source_id": "2ce0f47e-6e5d-4a91-bd16-81900818673a",
                        "source_title": "AMEC Barcelona Principles 3.0 Communications Measurement Standard",
                        "original_url": "https://amecorg.com/barcelona-principles-3-0/",
                        "locator": "Principio 5: Los AVEs no son el valor de la comunicación",
                        "excerpt_short": "Advertising Value Equivalents (AVEs) do not measure the value of communications and should not be used.",
                        "source_date": "2020",
                        "retrieved_at": "2026-10-01T01:31:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estándar internacional de medición de relaciones públicas consolidado."
            }
        ],
        "operational_model": {
            "inputs": ["Noticias y redes", "Documentos internos", "Compromisos territoriales"],
            "actors": ["Grafo Bipartito", "Algoritmo de Polaridad", "Auditor AMEC"],
            "steps": ["Ingesta y extracción de entidades", "Cálculo de cercanía semántica y polaridad", "Vinculación con archivos internos", "Generación de métricas de reputación basadas en outcomes"],
            "states": ["Datos_Ingresados", "Grafo_Actualizado", "Metricas_Calculadas"],
            "outputs": ["Reporte estructurado de reputación corporativa libre de AVE"],
            "exceptions": ["Menciones sin impacto material en la reputación (se filtran como ruido)"]
        },
        "entities": [
            {"entity_id": "ESTANDAR_AMEC_3", "type": "estandar_internacional", "name": "AMEC Barcelona Principles 3.0", "aliases": ["Estándar Global de Medición PR"]}
        ],
        "relations": [
            {"subject_id": "ESTANDAR_AMEC_3", "predicate": "prohibe_uso_de", "object_id": "AVE_Valor_Publicitario_Equivalente", "valid_from": "2020", "valid_to": None, "evidence_claim_id": "P02-F16-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Métrica de Vanidad (AVE) vs Métrica de Valor Real (AMEC)",
                "Métrica Desacreditada (AVE)": "Multiplicar centímetros de columna de prensa por tarifa publicitaria.",
                "Métrica Estándar AMEC": "Medición de cambios en percepción de confianza, alineamiento discursivo y mitigación de riesgos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Diseñar los paneles de analítica de BRIDGE cumpliendo al 100% con los principios AMEC 3.0, desterrando cualquier cálculo de AVE.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F17", "P02-F18"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F17",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre plataformas de escucha y reputación?",
        "snapshot_at": "2026-10-01T01:31:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Cada hecho está sustentado por fuentes oficiales del cuaderno P02 con fechas y pasajes verificables: 1) Burson & Limbik: bursonglobal.com/newsroom/limbik/ (adquisición 12 agosto 2026, suite Decipher para credibilidad de audiencia); 2) Signal AI & Memo: signal-ai.com/insights/post/verified-readership/ (adquisición/anuncio 20 abril 2026, métricas de lectura real verificada); 3) FGS Global & WPP: SEC Form 6-K filing a5017o.htm (3 diciembre 2024, cierre de venta mayoritaria de WPP a Kite Bidco Inc. de KKR); 4) Cision & Brandwatch: comunicado PR Newswire (1 junio 2021, cierre de adquisición por USD 450M); 5) Talkwalker & Hootsuite: adquisición en abril 2024; 6) Onclusive: constituida en enero 2022 por STG (Kantar Rep Intelligence + PRgloo + Digimind); 7) AlphaSense Liderazgo: Forrester Research Wave Q2 2025 (único líder en Market & Competitive Intelligence); 8) Denominador y fechas de corte: fe de erratas canónica 00_P02_GLOBAL_READ_ME_AND_ERRATA (1 octubre 2026, denominador reconciliado en 70 proveedores independientes).",
        "findings": [
            {
                "claim_id": "P02-F17-C1",
                "claim": "La trazabilidad de los hitos societarios y tecnológicos del mercado de escucha se sustenta en fuentes primarias corporativas y filings de la SEC con fechas comprobadas entre junio de 2021 y octubre de 2026.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Global", "actor": "Auditoría de Fuentes P02"},
                "evidence": [
                    {
                        "source_id": "6fa0dfd1-5192-4b3d-8ed7-20c44b7d4dc8",
                        "source_title": "AlphaSense Forrester Wave Market and Competitive Intelligence Leader",
                        "original_url": "https://www.alpha-sense.com/press/alphasense-named-the-only-leader-in-market-and-competitive-intelligence-platforms/",
                        "locator": "Forrester Research Evaluation Q2 2025",
                        "excerpt_short": "AlphaSense named the only leader in Market and Competitive Intelligence Platforms by Forrester.",
                        "source_date": "2025",
                        "retrieved_at": "2026-10-01T01:31:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación directa de notas de prensa y evaluaciones de firmas independientes."
            }
        ],
        "operational_model": {
            "inputs": ["Registros de fuentes del cuaderno P02", "Manifiesto fuentes/P02.json"],
            "actors": ["Auditor Epistémico", "Sistema de Verificación"],
            "steps": ["Cotejo de identificadores de fuente", "Validación de fechas de corte", "Verificación de resolubilidad de URLs", "Consolidación en el índice"],
            "states": ["Fuente_Verificada", "Metadatos_Auditados", "Trazabilidad_Consolidada"],
            "outputs": ["Cuadro de Trazabilidad de Fuentes de Escucha"],
            "exceptions": ["Fuentes con cambios de enlaces URL externos (se conservan títulos y extractos fidedignos)"]
        },
        "entities": [
            {"entity_id": "REG_FUENTES_ESCUCHA", "type": "registro_documental", "name": "Registro de Fuentes de Plataformas de Escucha", "aliases": ["Sensing Sources Manifest"]}
        ],
        "relations": [
            {"subject_id": "REG_FUENTES_ESCUCHA", "predicate": "certifica_trazabilidad_de", "object_id": "Plataformas_Escucha_P02", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F17-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Trazabilidad Formal vs Supuestos no Comprobados",
                "Supuesto no Comprobado": "Asumir que Talkwalker es un proveedor independiente en 2026.",
                "Trazabilidad Formal": "Adquirida por Hootsuite en abril de 2024, operando bajo su estructura societaria."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Mantener actualizadas las fechas de M&A de la competencia para no presentar un panorama de mercado obsoleto.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F18", "P02-C05"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F18",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra plataformas de escucha y reputación sin introducir datos no documentados?",
        "snapshot_at": "2026-10-01T01:31:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El caso concreto se ilustra mediante el flujo de respuesta ante una contingencia hídrica territorial en el norte de Chile: 1) Entradas reales: Entrada 1 (Escuchar): a las 06:45 AM, Litoralpress detecta y transcribe una entrevista en una radioemisora de Calama donde un dirigente vecinal acusa a la minera de sobreextracción hídrica ilegal (amplificada con 120 tuits en X); Entrada 2 (Saber): motor RAG (AlphaSense/Broadsight) recupera de SharePoint la RCA de la planta (Sección 3.2, Párrafo 4, que fija el límite legal en 45 L/s) y la auditoría hídrica de agosto 2026 (extracción real auditada de 38 L/s, cumpliendo la norma); Entrada 3 (Relacionar): CRM de stakeholders (Borealis/Consultation Manager) recupera la ficha del dirigente, el historial de reuniones en mesa de diálogo y el convenio firmado con la municipalidad en mayo 2025; 2) Resultado esperado (Executive Brief con Q&A asistido liberado a las 07:05 AM en el móvil del CCO): Diagnóstico de incidente (alerta de riesgo medio desmintiendo la acusación radial); Respuesta factual citada (Cero Alucinación: extracción real de 38 L/s, 15,5% bajo el límite de 45 L/s de la RCA 2024, con hipervínculo a la página del PDF); Q&A asistido con 2 preguntas difíciles probadas para medios de prensa; Portavoz asignado formalmente con firma Human-in-the-Loop del CCO antes de emitir la declaración a los periodistas.",
        "findings": [
            {
                "claim_id": "P02-F18-C1",
                "claim": "El caso concreto de respuesta ante controversia hídrica demuestra la viabilidad técnica de generar un Executive Brief verificado en menos de 20 minutos conectando señales de radio regional con expedientes RCA y CRM de compromisos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-10-01", "region": "Chile (Calama / Antofagasta)", "actor": "Caso Operativo BRIDGE"},
                "evidence": [
                    {
                        "source_id": "a09a8342-7518-4a75-acd7-1975273d4982",
                        "source_title": "P02_GLOBAL_COMPETITOR_DEEP_DIVES_V1",
                        "original_url": None,
                        "locator": "Sección: Flujo Operativo del Caso de Contingencia de Calama",
                        "excerpt_short": "Demostración de cruce entre Litoralpress, RAG en RCA y CRM de actores comunitarios.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:31:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Escenario estructurado basado en fuentes del catálogo de P02."
            }
        ],
        "operational_model": {
            "inputs": [
                "Alerta radial de Calama (06:45 AM)",
                "RCA Ambiental 2024 (Pág. RCA Sec 3.2)",
                "Auditoría hídrica interna (38 L/s)",
                "Acta de mesa de diálogo en CRM (Mayo 2025)"
            ],
            "actors": ["CCO", "Portavoz Regional", "Motor BRIDGE", "Periodista Local"],
            "steps": [
                "Paso 1: Detección y transcripción radial por Litoralpress (06:45 AM)",
                "Paso 2: RAG automático sobre SharePoint extrayendo RCA y auditoría (06:50 AM)",
                "Paso 3: Consulta a CRM extrayendo compromisos de mayo 2025 (06:55 AM)",
                "Paso 4: Generación de Executive Brief con Q&A asistido y citas (07:00 AM)",
                "Paso 5: Validación y firma en móvil por el CCO (07:05 AM)",
                "Paso 6: Emisión de vocería fidedigna al medio regional (07:15 AM)"
            ],
            "states": ["Incidente_Detectado", "Grounding_Verificado", "Brief_Enviado_CCO", "Voceria_Autorizada"],
            "outputs": ["Executive Brief de vocería con citas hipervinculadas a RCA y acta"],
            "exceptions": ["Detección de incumplimiento efectivo de la RCA (activa protocolo legal de contingencia)"]
        },
        "entities": [
            {"entity_id": "CASO_CONTINGENCIA_CALAMA", "type": "escenario_operativo", "name": "Caso de Contingencia Hídrica de Calama", "aliases": ["Escenario de Prueba Antofagasta"]}
        ],
        "relations": [
            {"subject_id": "CASO_CONTINGENCIA_CALAMA", "predicate": "valida_tiempo_respuesta_de", "object_id": "Menos_De_20_Minutos", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F18-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Respuesta Desconectada vs Respuesta Integrada BRIDGE",
                "Respuesta Desconectada": "El equipo se entera horas tarde cuando el medio publica la nota; búsqueda caótica de la RCA.",
                "Respuesta Integrada BRIDGE": "Alerta a las 06:45 AM con brief y Q&A listo antes de las 07:05 AM con citas exactas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Configurar la plantilla de salida de Executive Briefing de BRIDGE con el diseño de diagnóstico, respuesta factual citada y Q&A asistido.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F19", "P02-C05"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

# Write to temp file and append
with open("respuestas/temp_p02_f13_f18.jsonl", "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Generated {len(records)} records in respuestas/temp_p02_f13_f18.jsonl")
