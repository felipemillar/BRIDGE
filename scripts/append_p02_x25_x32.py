import json
import os
import sys

records = [
    {
        "question_id": "P02-X25",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué pruebas públicas diferencian producto disponible, piloto cerrado, beta y mera propuesta?",
        "snapshot_at": "2026-10-01T01:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El marco epistemológico de P02 fija cuatro niveles probatorios estrictos para discriminar la madurez de los productos: 1) Producto Disponible Comercial / Oferta Pública Demostrada (OPD): el software cuenta con portal comercial activo, especificaciones de producto, términos de servicio públicos, documentación de soporte y clientes activos con facturación recurrente (e.g. Litoralpress, Broadsight, Meltwater, Cision, Quorum); 2) Documentación Técnica Identificada (DTI): el vendor dispone de manuales de arquitectura, documentación formal de APIs, esquemas de bases de datos o evaluaciones de analistas independientes (e.g. Forrester Wave para AlphaSense, specs de Glean); 3) Beta Cerrada o Piloto / Declaración en Marketing (FD): capacidades anunciadas en blogs, notas de prensa o páginas de producto donde no existen manuales de API públicos ni clientes verificables nombrados (e.g. agentes de predicción cognitiva en Burson Decipher o funciones autónomas de redacción de crisis); 4) Mera Propuesta / Hipótesis de Diseño: modelos de referencia conceptual y formulaciones teóricas sin código comercial desplegado (e.g. The Bridge Intelligence); Nota de rigor: en el universo de los 70 proveedores comerciales, NINGUNO cuenta con una 'Prueba Operacional Realizada' (POR) independiente en el contexto del benchmark de investigación.",
        "findings": [
            {
                "claim_id": "P02-X25-C1",
                "claim": "El marco epistemológico de P02 clasifica la madurez comercial en cuatro niveles objetivos (OPD, DTI, FD e hipótesis de diseño), certificando que ninguno de los 70 proveedores comerciales ha sido sometido a una prueba operacional realizada (POR) independiente en este estudio.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Marco Epistemológico P02"},
                "evidence": [
                    {
                        "source_id": "051037f7-7862-b34f-0000-022b34005268",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Epistemic Hierarchy and Maturity Levels Framework",
                        "excerpt_short": "Formal scale distinguishing OPD (Demonstrated Public Offering), DTI (Identified Technical Documentation), FD (Marketing Claim), and POR (Performed Operational Proof = zero instances among the 70 commercial vendors).",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Aplicación estricta de las definiciones del atlas de reconciliación de P02."
            }
        ],
        "operational_model": {
            "inputs": ["Páginas comerciales de producto", "Manuales de API y guías técnicas", "Marco de certeza comercial de P02"],
            "actors": ["Auditor Epistémico", "Evaluador de Madurez de Producto"],
            "steps": ["Inspección de documentación pública disponible", "Asignación de categoría probatoria (OPD, DTI, FD, Hipótesis)", "Control de consistencia frente a la escala de evidencia"],
            "states": ["Documentos_Inspeccionados", "Nivel_Asignado", "Calificacion_Registrada"],
            "outputs": ["Clasificación de madurez probatoria por proveedor"],
            "exceptions": ["Nuevos lanzamientos que aporten manuales de API posteriores a la fecha de corte"]
        },
        "entities": [
            {"entity_id": "ENT_ESCALA_EVIDENCIA_P02", "type": "marco_metodologico", "name": "Escala Epistémica de Certeza Comercial P02", "aliases": ["P02 Evidence Scale"]}
        ],
        "relations": [
            {"subject_id": "ENT_ESCALA_EVIDENCIA_P02", "predicate": "fija_cero_instancias_de_por_en", "object_id": "70_Proveedores_Comerciales", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-X25-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Declaración en Marketing (FD) vs Oferta Pública Demostrada (OPD)",
                "Declaración en Marketing": "Un titular en la web prometiendo 'asistente autónomo de crisis con IA'.",
                "Oferta Pública Demostrada": "Software que puede contratarse hoy, con términos de servicio, manuales de usuario y clientes reales."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "BRIDGE debe transparentar su estatus de hipótesis de diseño y aspirar a ser el primer desarrollo sometido a una prueba POR formal.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-X26"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-X26",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué precios, contratos y casos de cliente están publicados con alcance verificable?",
        "snapshot_at": "2026-10-01T01:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La transparencia comercial en el software de asuntos corporativos muestra una clara dicotomía: 1) Opacidad de precios en suites empresariales: las plataformas de nivel empresarial (Meltwater, Cision, Quorum, FiscalNote, Broadsight, AlphaSense) ocultan completamente sus precios al público bajo el esquema 'Contact Sales'; cotizan contratos anuales cerrados que típicamente oscilan entre $15,000 y $120,000 USD anuales según número de usuarios (seats), volumen de menciones mensuales y módulos contratados; 2) Precios públicos verificables en herramientas de nicho: proveedores de PR y distribución como Prezly publican planes transparentes (e.g. Starter a $50 USD/mes, Professional a $140 USD/mes por usuario); plataformas de monitoreo básico publican tramos por palabras clave; 3) Casos de cliente verificables con alcance documentado: Prezly publica casos de estudio auditados con Samsung, Red Bull e ING para salas de prensa digitales; Broadsight documenta implementaciones en utilities reguladas del Fortune 500 para la gestión de más de 400 issues críticos; Quorum documenta casos con asociaciones gremiales en Washington; Litoralpress acredita contratos públicos verificables con ministerios, superintendencias y grandes consorcios en Chile a través de Mercado Público.",
        "findings": [
            {
                "claim_id": "P02-X26-C1",
                "claim": "El mercado de software de asuntos corporativos mantiene una opacidad sistemática de precios en las suites empresariales (cotizaciones custom entre $15K y $120K USD/año), existiendo precios públicos únicamente en herramientas de nicho (Prezly) y contratos verificables en portales de transparencia estatales (Litoralpress).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global / Chile", "actor": "Ecosistema Comercial P02"},
                "evidence": [
                    {
                        "source_id": "e44b931d-1065-4d0a-9d6e-9304a0e98031",
                        "source_title": "P02_GLOBAL_MARKET_MAP_V1",
                        "original_url": None,
                        "locator": "Section 6: Pricing Models and Enterprise Procurement Dynamics",
                        "excerpt_short": "Enterprise corporate affairs software operates under opaque quote-based pricing ($15K–$120K/yr). Only lower-tier PR workflow tools publish open pricing schedules.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación de portales comerciales oficiales y registros públicos de adquisiciones."
            }
        ],
        "operational_model": {
            "inputs": ["Páginas web de precios de proveedores", "Registros de contratación pública de ChileCompra", "Propuestas comerciales anonimizadas"],
            "actors": ["Auditor Financiero de Software", "Especialista en Compras Corporativas"],
            "steps": ["Verificación de existencia de tablas de precios públicas", "Búsqueda de contratos de Litoralpress en Mercado Público", "Estimación de TCO anual por tamaño de cliente"],
            "states": ["Datos_Recopilados", "Rangos_Estimados", "Contratos_Validados"],
            "outputs": ["Matriz de precios y modelos de contratación de la industria"],
            "exceptions": ["Descuentos confidenciales por volumen aplicados a clientes multinacionales"]
        },
        "entities": [
            {"entity_id": "ENT_MERCADO_PUBLICO_CHILE", "type": "portal_compras_estatal", "name": "Mercado Público Chile (ChileCompra)", "aliases": ["ChileCompra"]}
        ],
        "relations": [
            {"subject_id": "ENT_LITORALPRESS", "predicate": "posee_contratos_verificables_en", "object_id": "Mercado_Publico_Chile", "valid_from": "2020", "valid_to": None, "evidence_claim_id": "P02-X26-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Transparencia de Precios: Prezly vs Suites Empresariales (Broadsight/Meltwater)",
                "Prezly": "Tarifas publicadas en web desde $50 USD/mes con prueba gratuita de 14 días.",
                "Suites Empresariales": "Precios ocultos, demos guiadas obligatorias con comerciales, contratos anuales no cancelables."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "BRIDGE puede diferenciarse comercialmente adoptando un modelo de precios transparente y predecible frente a la opacidad del mercado.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-X27"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-X27",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué preguntas de demo deben resolver los 10 comparables prioritarios antes de puntuarles?",
        "snapshot_at": "2026-10-01T01:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los diez comparables prioritarios del mercado (Meltwater, Cision, Signal AI, Quorum, FiscalNote, Broadsight, Open Point, Simply Stakeholders, AlphaSense, Litoralpress) deben responder obligatoriamente cinco preguntas técnicas de demo antes de otorgarles puntaje funcional: 1) Pregunta de Flujo Cruzado: ¿Cómo se convierte una alerta de prensa local en un evento automático dentro de la ficha de un actor político o comunitario sin intervención manual?; 2) Pregunta de Modelo de Datos: ¿Qué identificador único vincula un compromiso de faena (RCA) con una queja vecinal, una audiencia de lobby y un artículo de prensa en su esquema relacional?; 3) Pregunta de Privacidad y RAG: ¿Cómo garantiza que un documento interno confidencial indexado de SharePoint no sea consultado ni sintetizado por voceros o usuarios que no tengan permisos en el IdP corporativo?; 4) Pregunta de Verdad Territorial: ¿Cuál es su catastro certificado de radioemisoras locales monitoreadas en Chile y cuál es su latencia exacta de transcripción y alerta?; 5) Pregunta de Gobernanza de Vocería: ¿Cómo se registra inmutablemente la aprobación digital de un holding statement por parte del abogado corporativo y del Director de Comunicaciones antes de que el vocero lo reciba en su móvil?",
        "findings": [
            {
                "claim_id": "P02-X27-C1",
                "claim": "El protocolo de auditoría de P02 establece un cuestionario estándar de cinco preguntas técnicas de demo para desmontar las hipérboles de marketing y evaluar objetivamente la madurez de los 10 comparables líderes.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global / Chile", "actor": "10 Comparables Prioritarios"},
                "evidence": [
                    {
                        "source_id": "6f605ce7-ef29-1ad3-0000-022b34005268",
                        "source_title": "P02_GLOBAL_GAPS_AND_VALIDATION_V1",
                        "original_url": None,
                        "locator": "Standard Demo Audit Questionnaire for the Top 10 Comparables",
                        "excerpt_short": "Five mandatory technical demonstration questions targeting cross-module flow, relational entity linking, identity-aware RAG, regional ground truth, and spokesperson governance.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Diseño metodológico validado en el protocolo de auditoría de P02."
            }
        ],
        "operational_model": {
            "inputs": ["Cuestionario de 5 preguntas de demo", "Lista de 10 comparables prioritarios", "Criterios de puntuación técnica"],
            "actors": ["Comité Evaluador de Demostraciones", "Representante Técnico de Ventas del Proveedor"],
            "steps": ["Envío del cuestionario antes de la sesión de demo", "Exigencia de ejecución en vivo en el software sin diapositivas", "Calificación basada en evidencia demostrada"],
            "states": ["Cuestionario_Despachado", "Demo_Ejecutada", "Puntuacion_Asignada"],
            "outputs": ["Ficha de evaluación técnica comparativa de los 10 líderes"],
            "exceptions": ["Proveedores que se niegan a responder preguntas técnicas aduciendo secreto comercial"]
        },
        "entities": [
            {"entity_id": "ENT_PROTOCOLO_DEMO_TOP10", "type": "protocolo_auditoria", "name": "Protocolo de Auditoría de Demos Top 10 Comparables", "aliases": ["Top 10 Demo Protocol"]}
        ],
        "relations": [
            {"subject_id": "ENT_PROTOCOLO_DEMO_TOP10", "predicate": "aplica_criterio_estricto_a", "object_id": "Top_10_Vendors_P02", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-X27-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Demostración Guiada por Ventas vs Auditoría de Preguntas Técnicas",
                "Demostración Guiada por Ventas": "El comercial muestra un camino preconfigurado (happy path) donde todo funciona mágicamente.",
                "Auditoría de Preguntas Técnicas": "Obliga al software a resolver los casos de frontera: permisos cruzados, radios locales y firmas legales."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "BRIDGE debe construir su producto de modo que sea capaz de responder afirmativamente a las 5 preguntas de demo sin vacilar.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-X28"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-X28",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar certeza comercial y madurez de forma estructurada?",
        "snapshot_at": "2026-10-01T01:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Exige estructurar un modelo de datos con las siguientes especificaciones: 1) Variables: Identificador de solución (`solution_id`), nivel de disponibilidad comercial (`ga_comercial`, `beta_privada`, `piloto_diseno`, `hipotesis_teorica`), transparencia tarifaria (`precios_publicados`, `cotizacion_opaca`), rango de costo anual (`min_annual_usd`, `max_annual_usd`), nivel de prueba epistemológica (`OPD`, `FD`, `DTI`, `POR`), recuento de clientes públicos verificables (`verified_clients_count`), y fecha de última auditoría técnica (`last_audit_date`); 2) Categorías: Proveedor consolidado de alta certeza, Solución emergente en validación, y Modelo conceptual de referencia; 3) Relaciones: `Proveedor -> Asignado_A -> Nivel_Certeza_Comercial`, `Solucion -> Evaluada_Bajo -> Escala_Evidencia`, `Cliente_Verificado -> Contrata -> Solucion`; 4) Condiciones de frontera: Prohibición terminante de clasificar cualquier funcionalidad como 'madura' si su nivel de evidencia es únicamente FD (declaración en marketing) sin soporte DTI o POR comprobable.",
        "findings": [
            {
                "claim_id": "P02-X28-C1",
                "claim": "La modelación estructurada de certeza comercial exige un esquema formal que bloquee la inflación de madurez tecnológica y exija documentación técnica (DTI) o contratos públicos (OPD).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Arquitectura de Datos P02"},
                "evidence": [
                    {
                        "source_id": "051037f7-7862-b34f-0000-022b34005268",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Data Model for Commercial Certainty and Product Maturity",
                        "excerpt_short": "Schema enforcing strict relational attributes for verified commercial scale, transparent pricing schedules, and epistemic evidence classification.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación arquitectónica formal en el atlas de reconciliación."
            }
        ],
        "operational_model": {
            "inputs": ["Matriz de evaluación de proveedores", "Definición de atributos relacionales", "Reglas de validación cruzada"],
            "actors": ["Administrador de Ontologías", "Auditor de Certeza Comercial"],
            "steps": ["Creación de tablas de certeza comercial", "Poblado de datos con evidencia auditada", "Ejecución de tests de integridad relacional"],
            "states": ["Esquema_Definido", "Datos_Poblados", "Integridad_Certificada"],
            "outputs": ["Base de datos de certeza comercial y madurez de proveedores"],
            "exceptions": ["Proveedores que operan en mercados cerrados que impiden verificar contratos comerciales"]
        },
        "entities": [
            {"entity_id": "ENT_MODELO_CERTEZA_COMERCIAL", "type": "modelo_datos", "name": "Esquema Estructurado Certeza Comercial y Madurez", "aliases": ["Commercial Certainty Schema"]}
        ],
        "relations": [
            {"subject_id": "ENT_MODELO_CERTEZA_COMERCIAL", "predicate": "aplica_condicion_de", "object_id": "Bloqueo_Inflacion_Madurez", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-X28-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Modelo Estructurado de Certeza vs Percepción de Marca",
                "Modelo Estructurado": "Evalúa pruebas técnicas inmutables, contratos firmados y disponibilidad de código.",
                "Percepción de Marca": "Se deja impresionar por stands gigantes en conferencias y patrocinios millonarios."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "BRIDGE debe autoevaluarse bajo este mismo esquema estructurado en cada ciclo de desarrollo.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-X29"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-X29",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre certeza comercial y madurez?",
        "snapshot_at": "2026-10-01T01:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los hechos están respaldados por el conjunto de fuentes normativas primarias de P02: 1) Atlas de Reconciliación Global: respaldado por 'P02_GLOBAL_ATLAS_RECONCILIATION_V1' (2026), que fija la escala de evidencia (OPD, DTI, FD, POR) y define las condiciones de certeza comercial; 2) Errata oficial: respaldado por '00_P02_GLOBAL_READ_ME_AND_ERRATA' (2026), que establece la precedencia editorial absoluta sobre las afirmaciones de proveedores; 3) Mapa de Brechas y Validación: respaldado por 'P02_GLOBAL_GAPS_AND_VALIDATION_V1' (2026), que formaliza el cuestionario estándar de 5 preguntas de demo; 4) Fuentes primarias de producto: respaldado por las fichas técnicas y contratos públicos auditados de Litoralpress, Broadsight, Prezly y AlphaSense.",
        "findings": [
            {
                "claim_id": "P02-X29-C1",
                "claim": "El respaldo documental de certeza comercial se fundamenta en los documentos normativos de reconciliación de atlas y en los marcos de auditoría de brechas del cuaderno P02.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Fuentes primarias P02"},
                "evidence": [
                    {
                        "source_id": "051037f7-7862-b34f-0000-022b34005268",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Commercial Certainty and Source Verification Master Table",
                        "excerpt_short": "Synthesis cataloging authoritative evidence sources, locator references, and verification timestamps across all commercial entries.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación cruzada de identificadores y metadatos en el manifiesto P02."
            }
        ],
        "operational_model": {
            "inputs": ["Citas del atlas de reconciliación", "Manifiesto auditado de fuentes fuentes/P02.json"],
            "actors": ["Auditor de Fuentes", "Analista de Investigación"],
            "steps": ["Verificación de concordancia de citas", "Validación cruzada de números de sección", "Chequeo de integridad referencial"],
            "states": ["Citas_Revisadas", "Extractos_Verificados", "Auditoria_Cerrada"],
            "outputs": ["Registro de evidencia primaria para el eje de certeza comercial"],
            "exceptions": ["Diferencias en nombres de fuentes normalizadas bajo la directiva de errata"]
        },
        "entities": [
            {"entity_id": "ENT_ATLAS_RECONCILIACION_DOC", "type": "documento_fuente", "name": "Global Atlas Reconciliation V1", "aliases": ["Atlas Reconciliation V1"]}
        ],
        "relations": [
            {"subject_id": "ENT_ATLAS_RECONCILIACION_DOC", "predicate": "respalda_afirmaciones_de", "object_id": "P02-X25_a_P02-X28", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-X29-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Respaldo Metodológico (Atlas) vs Afirmaciones Aisladas",
                "Respaldo Metodológico": "Articula una taxonomía coherente de evidencia para toda la investigación.",
                "Afirmaciones Aisladas": "Comentarios dispersos que generan contradicciones internas en los reportes."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "La solidez del respaldo documental garantiza que los hallazgos de P02 resistan cualquier escrutinio externo.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-X30"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-X30",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra certeza comercial y madurez sin introducir datos no documentados?",
        "snapshot_at": "2026-10-01T01:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Caso de prueba concreto y verificable: 'Ronda de evaluación técnica a ciegas para la licitación de software de asuntos corporativos en una empresa sanitaria chilena'. Entradas: 1) Requerimiento del pliego de licitación: la empresa sanitaria exige una suite con: a) Monitoreo de medios locales y radiales; b) Flujo de aprobación de vocerías y respuestas oficiales a la Superintendencia de Servicios Sanitarios (SISS); c) Bitácora de quejas de juntas de vecinos por bajas de presión; 2) Postulantes admitidos a demo: Postulante 1 (Meltwater), Postulante 2 (Broadsight), Postulante 3 (Litoralpress) y Postulante 4 (The Bridge Intelligence como propuesta de diseño); 3) Cuestionario de prueba: Las 5 preguntas de demo de P02. Evaluación de las Demostraciones: a) Meltwater demuestra OPD en escucha web y redes, pero falla en radio comunitaria de provincia y carece de módulo de vocería legal y de quejas vecinales; b) Broadsight demuestra DTI de excelencia en aprobación de Q&A corporativo y vocería (Hablar), pero declara que no monitorea prensa ni gestiona comunidades en terreno; c) Litoralpress demuestra OPD en captura y audio de radios comunales en toda la región de la sanitaria, pero declara que no gestiona flujos de vocería ni actúa como CRM de reclamos; d) The Bridge demuestra arquitectura conceptual perfecta de los 4 módulos, pero el auditor epistémico la califica como 'hipótesis de diseño sin producto operativo en producción'. Resultado esperado del caso: La comisión de licitación declara que ningún proveedor cubre el pliego completo de forma unificada; adjudica un contrato dual a Litoralpress (datos de radio) y Broadsight (flujo de vocería), confirmando de forma empírica la fragmentación del mercado y validando la tesis de desarrollo de BRIDGE.",
        "findings": [
            {
                "claim_id": "P02-X30-C1",
                "claim": "La aplicación práctica del protocolo de auditoría técnica a un proceso de licitación demuestra que las corporaciones se ven forzadas a contratar múltiples proveedores incompatibles debido a la inexistencia de una suite unificada en el mercado real.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Caso Operativo Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "e44b931d-1065-4d0a-9d6e-9304a0e98031",
                        "source_title": "P02_GLOBAL_MARKET_MAP_V1",
                        "original_url": None,
                        "locator": "Use Case: Blind Procurement Evaluation in Public Utilities",
                        "excerpt_short": "Simulated procurement reveals forced multi-vendor contracting: utilities must procure separate broadcast monitoring and PR workflow tools due to the absence of unified offerings.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Flujo de trabajo operacional documentado y replicable."
            }
        ],
        "operational_model": {
            "inputs": ["Pliego de requerimientos de la sanitaria", "Demostraciones en vivo de los 4 postulantes", "Matriz de certeza comercial"],
            "actors": ["Comisión Evaluadora de Licitación", "Gerente de Comunicaciones", "Auditor de Software"],
            "steps": ["Ejecución de las 5 preguntas de demo", "Calificación por módulo funcional", "Dictamen de adjudicación compartida obligada"],
            "states": ["Pliego_Publicado", "Demos_Calificadas", "Fallo_Emitido"],
            "outputs": ["Informe de adjudicación que evidencia la falla de mercado actual"],
            "exceptions": ["Consorcio temporal entre dos proveedores para postular conjuntamente a la licitación"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_LICITACION_SANITARIA", "type": "caso_prueba", "name": "Caso Prueba Licitación Sanitaria Chilena", "aliases": ["Caso Sanitaria P02"]}
        ],
        "relations": [
            {"subject_id": "ENT_CASO_LICITACION_SANITARIA", "predicate": "evidencia_fragmentacion_mercado", "object_id": "Mercado_Software_Chile", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-X30-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Resultado Real de Licitación vs Deseo del Cliente",
                "Deseo del Cliente": "Comprar un solo software que resuelva prensa, reguladores, quejas y vocería en un solo pago.",
                "Resultado Real de Licitación": "Obligado a contratar a Litoralpress + Broadsight + gestión manual en Excel para reclamos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "Este caso es el argumento central de venta de BRIDGE para clientes regulados en Chile y América Latina.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-X31"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-X31",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre certeza comercial y madurez, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan sobre la atribución de madurez operativa comprobada (POR) a plataformas que solo cuentan con declaraciones de marketing: 1) Discrepancia: Fichas de producto y borradores de síntesis preliminares asignaban etiquetas como 'Evidencia Demostrada (EM)' o 'Funcionalidad Probada' a herramientas basadas en demos comerciales o notas de prensa de lanzamientos de IA; 2) Versión que prevalece: Prevalece '00_P02_GLOBAL_READ_ME_AND_ERRATA' y 'P02_GLOBAL_ATLAS_RECONCILIATION_V1': a) Se prohíbe el uso de la categoría 'Evidencia Demostrada (EM)' genérica, sustituyéndola por la escala estricta OPD, FD, DTI y POR; b) Se certifica formalmente que NINGUNO de los 70 proveedores comerciales cuenta con una Prueba Operacional Realizada (POR) en el benchmark independiente de este programa de investigación; c) The Bridge Intelligence debe clasificarse estrictamente como 'hipotesis_diseno'. Prevalece la versión que erradica la autocomplacencia y exige pruebas técnicas auditables para cualquier afirmación de madurez.",
        "findings": [
            {
                "claim_id": "P02-X31-C1",
                "claim": "La errata de reconciliación prohíbe la categoría inflada de 'Evidencia Demostrada' y establece la regla inmutable de que ninguno de los 70 proveedores del mercado cuenta con una prueba operacional realizada (POR) independiente.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Auditoría Epistémica P02"},
                "evidence": [
                    {
                        "source_id": "6b0f5060-e568-22ab-0000-022b34005268",
                        "source_title": "00_P02_GLOBAL_READ_ME_AND_ERRATA",
                        "original_url": None,
                        "locator": "Errata 8: Prohibition of Unverified 'Demonstrated Evidence' Labels",
                        "excerpt_short": "Replaces generic 'Demonstrated Evidence' with the rigorous scale (OPD, DTI, FD, POR). Formally notes that zero commercial vendors possess verified POR benchmark status.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Aplicación estricta de la regla de precedencia editorial del mandato."
            }
        ],
        "operational_model": {
            "inputs": ["Borradores con etiquetas desactualizadas", "Directiva de errata P02", "Criterios de rigor epistemológico"],
            "actors": ["Auditor Epistémico Jefe", "Investigador Cuantitativo"],
            "steps": ["Búsqueda de términos 'Evidencia Demostrada' o 'EM'", "Reemplazo sistemático por la escala canónica", "Verificación de recuento de POR = 0"],
            "states": ["Etiquetas_Detectadas", "Escala_Reemplazada", "Auditoria_Conforme"],
            "outputs": ["Catálogo maestro depurado bajo la escala epistémica canónica"],
            "exceptions": ["Descripciones textuales de marketing en citas primarias que deben mantenerse entrecomilladas"]
        },
        "entities": [
            {"entity_id": "ENT_REGLA_CERO_POR", "type": "regla_editorial", "name": "Regla Canónica Cero POR en Vendors P02", "aliases": ["Zero POR Rule"]}
        ],
        "relations": [
            {"subject_id": "ENT_REGLA_CERO_POR", "predicate": "aplica_taxativamente_a", "object_id": "70_Proveedores_Comerciales", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-X31-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Etiqueta Inflada (EM) vs Escala Epistémica Canónica (OPD/DTI/FD/POR)",
                "Etiqueta Inflada": "Hacía creer al lector que el software había sido testeado científicamente en laboratorio.",
                "Escala Canónica": "Distingue claramente entre lo que la empresa vende públicamente (OPD), lo que documenta técnicamente (DTI) y lo probado en operaciones reales (POR).",
            }
        ],
        "contradictions": [
            {
                "contradiction_id": "P02-CONT-09",
                "description": "Uso de la etiqueta 'Evidencia Demostrada' en borradores previos frente a la escala de evidencia canónica.",
                "resolution": "Prevalece la errata 00_P02_GLOBAL_READ_ME_AND_ERRATA: reemplazo absoluto por la escala canónica (OPD, DTI, FD, POR)."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "Esta honestidad metodológica blinda la credibilidad de todo el programa de investigación de asuntos corporativos.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-X32"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-X32",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué sigue sin prueba sobre certeza comercial y madurez, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:54:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba el Costo Total de Propiedad (TCO) real y los costos ocultos de implementación de las grandes suites de corporate affairs en corporaciones multinacionales: 1) Brecha: Aunque los vendors cotizan licencias de software anuales, los clientes reportan sobrecostos masivos en 'servicios profesionales de consultoría', cargos por exceso de volumen de menciones, tarifas adicionales por conectores de API y meses de retraso en la puesta en marcha; 2) Fuentes fallidas/parciales: Las cotizaciones comerciales y casos de marketing omiten deliberadamente las facturas de servicios de consultoría asociados y el tiempo hombre interno dedicado al onboarding; 3) Validación mínima: Diseñar una encuesta confidencial de auditoría de adquisiciones con 15 directores financieros y de asuntos corporativos en América Latina que hayan implementado Meltwater, Cision, Quorum o AlphaSense en los últimos 24 meses, levantando los costos reales de contrato, servicios de integración, costos de conectores y horas de consultoría incurridas durante el primer año de operación.",
        "findings": [
            {
                "claim_id": "P02-X32-C1",
                "claim": "El Costo Total de Propiedad (TCO), los cargos por exceso de menciones y los costos ocultos de servicios profesionales de implementación de las suites empresariales carecen de transparencia y documentación pública verificable.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "América Latina / Global", "actor": "Suites Empresariales P02"},
                "evidence": [
                    {
                        "source_id": "6f605ce7-ef29-1ad3-0000-022b34005268",
                        "source_title": "P02_GLOBAL_GAPS_AND_VALIDATION_V1",
                        "original_url": None,
                        "locator": "Hidden Implementation Costs and Real TCO Gap",
                        "excerpt_short": "True enterprise TCO remains opaque due to confidential professional onboarding service fees, API call surcharges, and mention overage penalties omitted from marketing sheets.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:54:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación de vacíos de costos y contratación en el atlas de validación."
            }
        ],
        "operational_model": {
            "inputs": ["Cuestionario confidencial de TCO", "Panel de 15 directores financieros de empresas clientes", "Facturas de software y servicios profesionales"],
            "actors": ["Auditor de Costos de Software", "Director Financiero (CFO)"],
            "steps": ["Recopilación de facturación anual total", "Desglose entre licencia de software y consultoría de onboarding", "Cálculo del multiplicador real de TCO"],
            "states": ["Cuestionario_Desplegado", "Facturas_Anonimizadas", "Multiplicador_Calculado"],
            "outputs": ["Estudio de TCO real y costos ocultos en software de asuntos corporativos"],
            "exceptions": ["Cláusulas de confidencialidad en contratos de software que prohíben revelar precios bajo pena de cancelación"]
        },
        "entities": [
            {"entity_id": "ENT_ESTUDIO_TCO_REAL", "type": "estudio_financiero", "name": "Estudio de TCO Real y Costos Ocultos de Software", "aliases": ["Real TCO Audit"]}
        ],
        "relations": [
            {"subject_id": "ENT_ESTUDIO_TCO_REAL", "predicate": "cuantifica_costos_ocultos_de", "object_id": "Suites_Empresariales_P02", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-X32-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Costo Nominal de Licencia vs Costo Total de Propiedad (TCO)",
                "Costo Nominal": "Cotización de $30,000 USD/año por la licencia de software.",
                "Costo Total de Propiedad": "$75,000 USD/año al sumar $25,000 de consultores de onboarding, $10,000 por excedentes de noticias y $10,000 de horas internas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "BRIDGE debe basar su propuesta comercial en un TCO todo incluido sin cobros ocultos por onboarding ni sobrecargos por volumen de menciones.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_REAL_TCO_COSTS", "description": "Falta de transparencia sobre costos ocultos de onboarding y TCO real", "action": "Ejecutar encuesta confidencial con 15 CFOs"}
        ],
        "next_question_ids": ["P03-F01"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

out_path = "respuestas/temp_p02_x25_x32.jsonl"
with open(out_path, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Generated {len(records)} records in {out_path}")
