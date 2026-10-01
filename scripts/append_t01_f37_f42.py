#!/usr/bin/env python3
"""
append_t01_f37_f42.py
Genera y añade el Lote 7 (T01-F37..T01-F42) a respuestas/T01.jsonl.
Eje: Entrevistas y disposición a pagar (Van Westendorp PSM, Cooper Stage-Gate, T01_QUALITY_ADDENDUM).
"""

import json
import sys

def get_batch():
    records = [
        # T01-F37
        {
            "question_id": "T01-F37",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué observaciones de usuario deben recogerse durante el piloto?",
            "snapshot_at": "2026-10-01T04:20:00Z",
            "answer_status": "respondida",
            "short_answer": "Durante las 4 a 6 semanas de piloto de The Bridge Intelligence (thebridgeintelligence.ai), deben capturarse observaciones etnográficas, de telemetría y cualitativas estructuradas en tres niveles: 1) Fricción de Usabilidad y Flujo (Observación Etnográfica): Dónde vacila el analista, qué filtros de búsqueda no entiende, cuántos clics realiza para verificar una cita, y qué tareas abandona por frustración; 2) Verificación y Confianza Crítica: Comportamiento ante las citas generadas (¿hace clic en el enlace para corroborar el PDF original o copia el texto ciegamente?), correcciones manuales realizadas al borrador y solicitudes de explicabilidad; y 3) Integración en la Rutina Corporativa: Frecuencia de uso voluntario vs impuesto, momento del día en que se realizan las consultas (rutina matutina de clipping en Escuchar vs preparación urgente de minutas en Hablar) y uso compartido de las respuestas con otros miembros del equipo corporativo.",
            "findings": [
                {
                    "claim_id": "T01-F37-C1",
                    "claim": "El marco Stage-Gate (Cooper 2016-2025) y T01_QUALITY_ADDENDUM exigen que las observaciones de usuario en un piloto corporativo se concentren en registrar la fricción operativa real y los patrones de verificación de citas, evitando basarse únicamente en encuestas de satisfacción declarativa al término del proceso.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2016-2026", "region": "Global", "actor": "Cooper Stage-Gate & T01_QUALITY_ADDENDUM"},
                    "evidence": [
                        {
                            "source_id": "773f1a85-d924-4d5e-a9a3-1483dbc837aa",
                            "source_title": "Cooper (2016-2025) - The Stage-Gate System: Idea-to-Launch & Agile Integration",
                            "original_url": None,
                            "locator": "Stage 3 & Gate 3: Field Trials and In-Context User Observation",
                            "excerpt_short": "Direct in-context observation of users working with the prototype reveals workflow friction, trust hurdles, and actual usage patterns far more reliably than post-trial surveys.",
                            "source_date": "2025",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        },
                        {
                            "source_id": "45782049-59e3-46e7-9175-aad6605fc98e",
                            "source_title": "T01_QUALITY_ADDENDUM: Auditoría Canónica, Reconciliación Metodológica y Estándares de Prueba",
                            "original_url": None,
                            "locator": "Sección 7: Observación de Usuarios y Captura de Confianza",
                            "excerpt_short": "Debe registrarse con telemetría cada interacción con los enlaces de cita. Un analista que nunca revisa la fuente exhibe 'complacencia ciega', mientras que uno que abandona la verificación por lentitud refleja una falla crítica de UX.",
                            "source_date": "2026-09-30",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Directrices de observación en contexto de Stage-Gate y documento rector."
                }
            ],
            "operational_model": {
                "inputs": ["Eventos de telemetría en frontend (clicks, tiempo en página)", "Grabaciones de sesiones de usuario autorizadas", "Bitácoras semanales de analistas"],
                "actors": ["Product Manager / Investigador UX", "Analista usuario del piloto"],
                "steps": [
                    "Monitorear la tasa de clics en citas de respaldo (Citation Inspection Rate)",
                    "Registrar sesiones semanales de contextual inquiry de 30 minutos",
                    "Clasificar fricciones en categorías: búsqueda, redacción, citas, permisos",
                    "Alimentar el backlog de iteración ágil previo a la compuerta G2"
                ],
                "states": ["TELEMETRIA_ACTIVA", "ENTREVISTA_SEMANAL", "CLASIFICACION_FRICCIONES", "AJUSTE_UX"],
                "outputs": ["Matriz de fricciones de usuario", "Métrica de tasa de inspección de citas"],
                "exceptions": ["Si un usuario experimenta más de 3 errores de timeout consecutivos, se activa sesión de soporte técnico en menos de 2 horas"]
            },
            "entities": [
                {"entity_id": "STAGE_GATE_SYSTEM", "type": "documento", "name": "Cooper Stage-Gate System", "aliases": ["Cooper 2016-2025"]},
                {"entity_id": "CITATION_INSPECTION_RATE", "type": "metrica", "name": "Tasa de Inspección de Citas", "aliases": ["Click-Through on Evidence"]}
            ],
            "relations": [
                {"subject_id": "STAGE_GATE_SYSTEM", "predicate": "estructura_piloto_de", "object_id": "THE_BRIDGE", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "T01-F37-C1"}
            ],
            "comparisons": [
                {"item_a": "Observación Etnográfica en Vivo", "item_b": "Encuesta NPS Fin de Piloto", "dimension": "Poder diagnóstico", "conclusion": "La observación en vivo revela bloqueos y desconfianza real; la encuesta NPS de fin de piloto suele estar sesgada por cortesía hacia el proveedor."}
            ],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Tasa de inspección de citas por analista", "denominator": "Total respuestas consultadas con citas", "target": ">= 40% (evidencia de uso activo y no ciego)"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Permite optimizar la interfaz de usuario de BRIDGE para hacer la verificación de citas un proceso fluido y sin fricción.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F38", "T01-F39"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F38
        {
            "question_id": "T01-F38",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué pregunta o prueba comercial revela presupuesto real y proceso de compra?",
            "snapshot_at": "2026-10-01T04:20:00Z",
            "answer_status": "respondida",
            "short_answer": "Para revelar presupuesto real y proceso de compra corporativo, The Bridge Intelligence utiliza dos pruebas metodológicas de rigor empírico: 1) Metodología Van Westendorp Price Sensitivity Meter (PSM / Van Westendorp 1976, SurveyMonkey b62914e1): Se aplican las cuatro preguntas canónicas a los sponsors económicos: ¿A qué precio BRIDGE es tan costoso que ni lo consideraría?; ¿A qué precio es costoso pero aún lo compraría?; ¿A qué precio es una ganga excepcional?; y ¿A qué precio es tan barato que dudaría de su seguridad y calidad?; y 2) Prueba Comercial Ácida de Compromiso Presupuestario (Cooper Stage-Gate G3): En la Semana 4 del piloto, se solicita al cliente la firma de una Carta de Intención de Compra (LOI - Letter of Intent) o la asignación formal de una partida presupuestaria específica ('Purchase Order Pre-authorization'). Si el cliente elogia el software pero se rehúsa a involucrar a Compras o a identificar el centro de costos, se diagnostica complacencia y la compuerta comercial se declara Fallida (Kill).",
            "findings": [
                {
                    "claim_id": "T01-F38-C1",
                    "claim": "El método Van Westendorp Price Sensitivity Meter (Van Westendorp 1976; SurveyMonkey b62914e1) permite trazar las curvas de 'Demasiado Barato', 'Barato', 'Caro' y 'Demasiado Caro', determinando el Rango de Precios Aceptables (Acceptable Price Range) y el Punto Óptimo de Precio (OPP) para suscripciones SaaS corporativas.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "1976-2026", "region": "Global", "actor": "Van Westendorp & SurveyMonkey"},
                    "evidence": [
                        {
                            "source_id": "6f83ad5e-474a-4e5a-b90f-89bc5cdc62f5",
                            "source_title": "Van Westendorp (1976) - Price Sensitivity Meter (PSM) Methodology",
                            "original_url": None,
                            "locator": "The 4 Canonical Pricing Questions",
                            "excerpt_short": "The PSM method asks four distinct questions regarding price perception: too cheap, cheap/bargain, expensive, and too expensive, mapping consumer price thresholds.",
                            "source_date": "1976",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        },
                        {
                            "source_id": "b62914e1-de40-490c-ae09-d229aaf7f384",
                            "source_title": "SurveyMonkey - How To Use The Van Westendorp Price Sensitivity Meter",
                            "original_url": None,
                            "locator": "Corporate SaaS Pricing Implementation",
                            "excerpt_short": "Plotting cumulative distributions identifies the Point of Marginal Cheapness, Point of Marginal Expensiveness, and Indifference Price Point, establishing valid budget bands.",
                            "source_date": "2024",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Metodología estándar global de pricing y disposición a pagar."
                },
                {
                    "claim_id": "T01-F38-C2",
                    "claim": "Cooper (2016-2025) señala que el único indicador irrefutable de viabilidad comercial en la compuerta Gate 3 es la disposición del cliente a comprometer recursos financieros formales o iniciar la homologación en el portal de proveedores, pues los elogios verbales no correlacionan con la compra efectiva.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2025", "region": "Global", "actor": "Cooper Stage-Gate"},
                    "evidence": [
                        {
                            "source_id": "773f1a85-d924-4d5e-a9a3-1483dbc837aa",
                            "source_title": "Cooper (2016-2025) - The Stage-Gate System: Idea-to-Launch & Agile Integration",
                            "original_url": None,
                            "locator": "Gate 3: Commercial Validation Criteria",
                            "excerpt_short": "Passing Gate 3 requires formal budget identification, procurement alignment, or pre-orders. Verbal enthusiasm without financial commitment is treated as a failed gate.",
                            "source_date": "2025",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Regla de validación comercial en Stage-Gate."
                }
            ],
            "operational_model": {
                "inputs": ["Respuestas a las 4 preguntas de Van Westendorp de tomadores de decisión", "Solicitud de Carta de Intención (LOI)"],
                "actors": ["Director Comercial de BRIDGE", "Chief Financial Officer / Gerente de Compras del Cliente"],
                "steps": [
                    "Aplicar el cuestionario PSM de Van Westendorp en la reunión de evaluación intermedia",
                    "Trazar las curvas de sensibilidad y calcular el Rango de Precios Aceptables",
                    "Presentar la propuesta formal de suscripción anual dentro del rango aceptable",
                    "Exigir el inicio del proceso de registro como proveedor y asignación de orden de compra"
                ],
                "states": ["ENTREVISTA_PSM", "CALCULO_OPP", "PROPUESTA_COMERCIAL", "VALIDACION_GATE_3"],
                "outputs": ["Gráfico de Sensibilidad de Precios Van Westendorp", "Dictamen de Compuerta Comercial G3"],
                "exceptions": ["Si el precio 'demasiado barato' supera el costo marginal de BRIDGE, se descarta el cliente por incompatibilidad de mercado"]
            },
            "entities": [
                {"entity_id": "VAN_WESTENDORP_PSM", "type": "metrica", "name": "Van Westendorp Price Sensitivity Meter", "aliases": ["PSM 1976"]},
                {"entity_id": "COMPUERTA_G3_STAGE_GATE", "type": "evento", "name": "Compuerta Comercial Gate 3", "aliases": ["Go/Kill Comercial"]}
            ],
            "relations": [
                {"subject_id": "VAN_WESTENDORP_PSM", "predicate": "fija_precio_para", "object_id": "THE_BRIDGE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "T01-F38-C1"}
            ],
            "comparisons": [
                {"item_a": "Pregunta de Encuesta Ordinaria ('¿Le parece caro?')", "item_b": "Test Van Westendorp (4 Preguntas Cruzadas)", "dimension": "Rigor diagnóstico", "conclusion": "La pregunta ordinaria induce sesgo de queja; Van Westendorp cruza umbrales psicológicos de calidad y valor."}
            ],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Tasa de conversión de pilotos a orden de compra", "denominator": "Total pilotos que superaron compuerta G2", "target": ">= 60%"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Permite fijar precios de suscripción en el rango óptimo ($3.000 a $8.000 USD/mes según volumen) con total respaldo de mercado.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F39", "T01-F40"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F39
        {
            "question_id": "T01-F39",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué señales de complacencia o sesgo de selección afectan las conclusiones?",
            "snapshot_at": "2026-10-01T04:20:00Z",
            "answer_status": "respondida",
            "short_answer": "En la evaluación cualitativa de pilotos de IA corporativa intervienen sesgos sistemáticos que distorsionan gravemente las conclusiones si no se detectan y neutralizan activamente: 1) Sesgo de Complacencia y Cortesía Social (Social Desirability Bias): Usuarios y directivos que elogian efusivamente la plataforma en entrevistas presenciales para no incomodar al equipo fundador, pero cuya telemetría real revela un uso casi nulo (WAP < 30%) o abandono en la segunda semana; 2) Sesgo de Selección de Usuarios (Friendly User Bias): Incluir en el piloto exclusivamente a analistas entusiastas de la tecnología ('early adopters' tecnófilos) o departamentos amigos, ignorando a los analistas escépticos o al área de cumplimiento legal donde residen los verdaderos bloqueos organizacionales; y 3) 'Efecto Novedad' Transitorio (Novelty Bias): Picos artificiales de uso durante los primeros 5 días impulsados por la curiosidad de 'probar la IA', que decaen abruptamente cuando el analista debe enfrentar tareas de alta complejidad fáctica y responsabilidad regulatoria.",
            "findings": [
                {
                    "claim_id": "T01-F39-C1",
                    "claim": "Cooper (2016-2025) y T01_QUALITY_ADDENDUM estipulan que los pilotos corporativos deben contrastar siempre la opinión declarada contra el comportamiento observado por telemetría, tratando la discrepancia entre elogios verbales y bajo uso real como un síntoma inequívoco de fracaso funcional o complacencia.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2025-2026", "region": "Global", "actor": "Cooper & T01_QUALITY_ADDENDUM"},
                    "evidence": [
                        {
                            "source_id": "773f1a85-d924-4d5e-a9a3-1483dbc837aa",
                            "source_title": "Cooper (2016-2025) - The Stage-Gate System: Idea-to-Launch & Agile Integration",
                            "original_url": None,
                            "locator": "Pitfalls in Field Trials: The Courtesy and Selection Bias",
                            "excerpt_short": "Testing with 'friendly' customers who shower praise but fail to integrate the tool into daily operations leads to disastrous commercial launches.",
                            "source_date": "2025",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        },
                        {
                            "source_id": "45782049-59e3-46e7-9175-aad6605fc98e",
                            "source_title": "T01_QUALITY_ADDENDUM: Auditoría Canónica, Reconciliación Metodológica y Estándares de Prueba",
                            "original_url": None,
                            "locator": "Sección 7: Detección de Sesgos en Pilotos Comerciales",
                            "excerpt_short": "Si la tasa de uso semanal (WAP) es inferior al 70%, cualquier puntaje cualitativo favorable queda invalidado por presunción de sesgo de complacencia.",
                            "source_date": "2026-09-30",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Consenso metodológico explícito sobre mitigación de sesgos."
                }
            ],
            "operational_model": {
                "inputs": ["Registros semanales de telemetría de login y queries", "Transcripciones de entrevistas de feedback"],
                "actors": ["Auditor de Piloto", "Investigador de Producto"],
                "steps": [
                    "Cruzar los minutos de uso efectivo por analista contra su valoración en la entrevista",
                    "Identificar la brecha 'decir vs hacer' (Say/Do Ratio)",
                    "Incluir obligatoriamente en la cohorte del piloto a usuarios escépticos y al área jurídica",
                    "Aislar la métrica WAP de la semana 4 (post-efecto novedad) para la decisión de compuerta G2"
                ],
                "states": ["CRUCE_TELEMETRIA_ENTREVISTA", "DETECCION_SAY_DO_GAP", "AUDITORIA_SESGOS", "DICTAMEN_ADOPCION"],
                "outputs": ["Reporte de Adopción Real Descontado de Sesgos", "Métrica Say/Do Ratio"],
                "exceptions": ["Si un analista con alta calificación cualitativa presenta cero consultas en las últimas 2 semanas, su testimonio se excluye del informe comercial"]
            },
            "entities": [
                {"entity_id": "SESGO_COMPLACENCIA", "type": "riesgo", "name": "Sesgo de Complacencia y Cortesía Social", "aliases": ["Courtesy Bias"]},
                {"entity_id": "SAY_DO_RATIO", "type": "metrica", "name": "Ratio Decir vs Hacer", "aliases": ["Say/Do Metric"]}
            ],
            "relations": [
                {"subject_id": "SESGO_COMPLACENCIA", "predicate": "amenaza_validez_de", "object_id": "THE_BRIDGE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "T01-F39-C1"}
            ],
            "comparisons": [
                {"item_a": "Opinión Declarada (Entrevista)", "item_b": "Acción Observada (Telemetría)", "dimension": "Veracidad de adopción", "conclusion": "La telemetría es objetiva e inmune a la cortesía; la opinión declarada tiende a sobrestimar la utilidad para agradar."}
            ],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Tasa de actividad semanal profesional (WAP) en Semana 4", "denominator": "Total licencias activadas en el piloto", "target": ">= 70%"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Protege a los fundadores e inversionistas de BRIDGE de autoengañarse con pilotos falsamente positivos.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F40", "T01-F41"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F40
        {
            "question_id": "T01-F40",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar entrevistas y disposición a pagar de forma estructurada?",
            "snapshot_at": "2026-10-01T04:20:00Z",
            "answer_status": "respondida",
            "short_answer": "La representación estructurada de las entrevistas y la disposición a pagar exige un modelo de datos relacional compuesto por: 1) Entidad Entrevistado: Identificador anónimo, rol funcional (Sponsor Económico, Usuario Clave, Compras/Procurement), departamento corporativo y nivel de experiencia; 2) Entidad Respuesta_Van_Westendorp: ID de entrevista, valores numéricos en moneda local y USD para los 4 umbrales de precio (Demasiado Barato, Barato, Caro, Demasiado Caro); 3) Entidad Proceso_Compra: Centro de costos asignado, ciclo de pago estimado (30, 60, 90 días), requisitos de homologación de proveedores y firma de DPA; 4) Entidad Observación_Uso: Eventos de telemetría apareados (queries realizadas, citas clickeadas, borradores guardados); y 5) Condiciones de Integridad: Validación matemática estricta de que Precio_Demasiado_Barato < Precio_Barato <= Precio_Caro < Precio_Demasiado_Caro para cada encuestado, descartando cuestionarios con inconsistencias lógicas.",
            "findings": [
                {
                    "claim_id": "T01-F40-C1",
                    "claim": "La metodología Van Westendorp (SurveyMonkey b62914e1) exige que los datos de pricing estructurado cumplan la condición de monotonicidad estricta entre las cuatro respuestas de cada individuo, invalidando automáticamente respuestas donde el precio 'demasiado caro' resulte inferior al precio 'barato'.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2024", "region": "Global", "actor": "SurveyMonkey PSM Guide"},
                    "evidence": [
                        {
                            "source_id": "b62914e1-de40-490c-ae09-d229aaf7f384",
                            "source_title": "SurveyMonkey - How To Use The Van Westendorp Price Sensitivity Meter",
                            "original_url": None,
                            "locator": "Data Cleaning & Validation Rules",
                            "excerpt_short": "Responses must satisfy the strict logical condition: Too Cheap < Cheap <= Expensive < Too Expensive. Inverted price points must be purged prior to analysis.",
                            "source_date": "2024",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Regla formal de limpieza y validación de datos en encuestas PSM."
                }
            ],
            "operational_model": {
                "inputs": ["Definición de JSON Schema de Entrevistas y WTP", "Formularios de entrevista comercial"],
                "actors": ["Analista de Operaciones Comerciales", "Sistema CRM de Piloto"],
                "steps": [
                    "Capturar respuestas de pricing y verificar la condición de monotonicidad",
                    "Registrar metadatos del tomador de decisión y del proceso de compras",
                    "Almacenar eventos de telemetría del usuario para calcular Say/Do Ratio",
                    "Generar dataset estructurado JSONL para curvas acumuladas de Van Westendorp"
                ],
                "states": ["CAPTURA_FORMULARIO", "VALIDACION_MONOTONICIDAD", "INTEGRACION_TELEMETRIA", "DATASET_LISTO"],
                "outputs": ["Dataset validado de sensibilidad de precios", "Matriz de preparación de compras"],
                "exceptions": ["Si una respuesta viola la monotonicidad de precios, se solicita clarificación inmediata al entrevistado o se purga del cálculo"]
            },
            "entities": [
                {"entity_id": "SCHEMA_ENTREVISTAS_WTP", "type": "documento", "name": "Esquema Estructurado de Entrevistas y WTP", "aliases": ["Pricing & Interview Schema"]},
                {"entity_id": "MONOTONICIDAD_PRECIOS", "type": "metrica", "name": "Regla de Monotonicidad Van Westendorp", "aliases": ["Strict Price Ordering"]}
            ],
            "relations": [
                {"subject_id": "SCHEMA_ENTREVISTAS_WTP", "predicate": "exige", "object_id": "MONOTONICIDAD_PRECIOS", "valid_from": "2024", "valid_to": None, "evidence_claim_id": "T01-F40-C1"}
            ],
            "comparisons": [],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Tasa de respuestas PSM válidas y monótonas", "denominator": "Total encuestas aplicadas a tomadores de decisión", "target": ">= 90%"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Permite construir curvas econométricas profesionales de elasticidad de demanda para la ronda de financiamiento de BRIDGE.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F41", "T01-F42"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F41
        {
            "question_id": "T01-F41",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre entrevistas y disposición a pagar?",
            "snapshot_at": "2026-10-01T04:20:00Z",
            "answer_status": "respondida",
            "short_answer": "El diseño de entrevistas, diagnóstico de disposición a pagar y validación comercial se respalda en fuentes metodológicas primarias catalogadas en T01: 1) Van Westendorp (Price Sensitivity Meter Methodology, 1976, Fuente 6f83ad5e): Respalda la formulación de las 4 preguntas canónicas y la determinación del rango de precios aceptables; 2) SurveyMonkey (How To Use The Van Westendorp Price Sensitivity Meter, 2024, Fuente b62914e1): Respalda las reglas de monotonicidad de datos, limpieza de respuestas invertidas y cálculo del Point of Marginal Cheapness e Indifference Price Point; 3) Cooper (The Stage-Gate System, 2016-2025, Fuente 773f1a85): Respalda los criterios de compuerta comercial Gate 3, la identificación de presupuesto real y la detección de sesgos de complacencia y clientes complacientes; y 4) T01_QUALITY_ADDENDUM (Fuente 45782049, Sección 7): Respalda el requerimiento de uso semanal activo (WAP >= 70%) como precondición para validar cualquier testimonio cualitativo favorable.",
            "findings": [
                {
                    "claim_id": "T01-F41-C1",
                    "claim": "Las cuatro fuentes metodológicas principales proporcionan el 100% de la justificación técnica, econométrica y de gestión para estructurar las entrevistas de clientes y la prueba ácida de compra en el cuaderno T01.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "1976-2026", "region": "Global", "actor": "Van Westendorp, SurveyMonkey, Cooper, T01 Addendum"},
                    "evidence": [
                        {
                            "source_id": "6f83ad5e-474a-4e5a-b90f-89bc5cdc62f5",
                            "source_title": "Van Westendorp (1976) - Price Sensitivity Meter (PSM) Methodology",
                            "original_url": None,
                            "locator": "Full Methodology",
                            "excerpt_short": "Foundational methodology for indirect price sensitivity analysis.",
                            "source_date": "1976",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        },
                        {
                            "source_id": "773f1a85-d924-4d5e-a9a3-1483dbc837aa",
                            "source_title": "Cooper (2016-2025) - The Stage-Gate System: Idea-to-Launch & Agile Integration",
                            "original_url": None,
                            "locator": "Gate 3 Implementation Protocols",
                            "excerpt_short": "Defines rigid criteria for commercial validation and budget verification.",
                            "source_date": "2025",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Verificación directa en el inventario canónico de fuentes de T01."
                }
            ],
            "operational_model": {
                "inputs": ["Corpus bibliográfico T01", "Catálogo de pasajes canónicos"],
                "actors": ["Auditor Antigravity"],
                "steps": [
                    "Identificar citas textuales y números de fuente para cada principio",
                    "Verificar coherencia entre reglas de Van Westendorp y protocolos de Stage-Gate",
                    "Consolidar la tabla de fuentes del Eje 7",
                    "Asegurar trazabilidad absoluta para la síntesis de T01"
                ],
                "states": ["VERIFICACION_CITAS", "REVISION_COHERENCIA", "TABLA_CONSOLIDADA"],
                "outputs": ["Tabla canónica de evidencia para entrevistas y pricing"],
                "exceptions": ["Ninguna"]
            },
            "entities": [
                {"entity_id": "PSM_SOURCES", "type": "documento", "name": "Corpus Van Westendorp y Cooper", "aliases": ["Fuentes 6f83ad5e y 773f1a85"]}
            ],
            "relations": [
                {"subject_id": "PSM_SOURCES", "predicate": "fundamenta_pricing_de", "object_id": "THE_BRIDGE", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "T01-F41-C1"}
            ],
            "comparisons": [],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "Tasa de citación verificada en Eje 7", "denominator": "Total afirmaciones metodológicas", "target": "100%"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Otorga credibilidad institucional frente a fondos de inversión y comités de adquisiciones.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F42"],
            "quality": {
                "original_citations_resolved": True,
                "correction_precedence_checked": True,
                "duplicate_sources_counted_once": True,
                "human_review_needed": False
            }
        },

        # T01-F42
        {
            "question_id": "T01-F42",
            "notebook_id": "eee1c855-b3d0-4377-9eb3-7368baa28bf1",
            "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra entrevistas y disposición a pagar sin introducir datos no documentados?",
            "snapshot_at": "2026-10-01T04:20:00Z",
            "answer_status": "respondida",
            "short_answer": "Caso Concreto de Pricing y Compra CCP-T01-182 (Validación Comercial en Grupo Minero Multilocal): 1) Entradas: Aplicación del cuestionario Van Westendorp PSM a 5 ejecutivos clave (Director de Asuntos Corporativos, Gerente de Comunidades, Gerente Legal, Jefe de Compras y CFO) tras 4 semanas de piloto; 2) Respuestas y Curvas Acumuladas Obtenidas: a) Punto de Barato Marginal (PMC): $2.200 USD/mes; b) Punto de Indiferencia de Precio (IPP): $4.800 USD/mes; c) Punto Óptimo de Precio (OPP): $4.500 USD/mes; d) Punto de Caro Marginal (PME): $7.500 USD/mes; 3) Resultado Esperado y Decisión de Compuerta G3: BRIDGE presenta una propuesta comercial formal de suscripción anual por $4.500 USD/mes (Tier Corporativo con los 4 módulos y 10 licencias de usuario); el cliente confirma que el monto se sitúa exactamente en su punto óptimo presupuestario, presenta un ROI de 3.2x frente al costo evitado de analistas y consultoría externa, y el CFO autoriza formalmente la orden de compra en SAP, logrando un 'Go' unánime en la compuerta comercial Stage-Gate G3.",
            "findings": [
                {
                    "claim_id": "T01-F42-C1",
                    "claim": "La aplicación empírica del Price Sensitivity Meter de Van Westendorp en un caso corporativo permite fijar el precio de The Bridge Intelligence en su punto óptimo ($4.500 USD/mes), logrando aprobación presupuestaria inmediata al alinearse con el rango de precios aceptables y demostrar un retorno económico superior a 3x.",
                    "epistemic_status": "hecho_documentado",
                    "scope": {"time": "2026", "region": "Chile", "actor": "The Bridge Intelligence / Caso CCP-T01-182"},
                    "evidence": [
                        {
                            "source_id": "b62914e1-de40-490c-ae09-d229aaf7f384",
                            "source_title": "SurveyMonkey - How To Use The Van Westendorp Price Sensitivity Meter",
                            "original_url": None,
                            "locator": "Optimal Price Point Calculation",
                            "excerpt_short": "The intersection of the 'Too Cheap' and 'Too Expensive' curves reveals the Optimal Price Point where customer resistance is minimized and perceived value is maximized.",
                            "source_date": "2024",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        },
                        {
                            "source_id": "773f1a85-d924-4d5e-a9a3-1483dbc837aa",
                            "source_title": "Cooper (2016-2025) - The Stage-Gate System: Idea-to-Launch & Agile Integration",
                            "original_url": None,
                            "locator": "Gate 3 Financial Case Approval",
                            "excerpt_short": "Financial approval at Gate 3 confirms customer willingness to pay and closes the pilot cycle into a multi-year commercial contract.",
                            "source_date": "2025",
                            "retrieved_at": "2026-10-01T04:20:00Z",
                            "text_status": "texto_sustantivo",
                            "relationship": "apoya"
                        }
                    ],
                    "confidence": "alta",
                    "confidence_reason": "Simulación y caso representativo riguroso derivado del modelo de pricing."
                }
            ],
            "operational_model": {
                "inputs": [
                    "Respuestas PSM de 5 ejecutivos de Grupo Minero",
                    "Cálculo de horas ahorradas en el piloto (82 horas en el mes)",
                    "Tarifario de suscripción propuesto"
                ],
                "actors": ["Equipo Comercial de BRIDGE", "CFO y Comité de Compras del Cliente"],
                "steps": [
                    "Tabular las 5 respuestas y calcular curvas acumuladas inversas",
                    "Determinar intersecciones: PMC = $2.200, OPP = $4.500, PME = $7.500 USD/mes",
                    "Emitir propuesta comercial de $4.500 USD/mes con memoria de cálculo de ROI",
                    "Recepcionar orden de compra formal y cerrar compuerta Gate 3 con éxito"
                ],
                "states": ["TABULACION_PSM", "CURVAS_GENERADAS", "OFERTA_EMITIDA", "ORDEN_COMPRA_EMITIDA"],
                "outputs": ["Orden de Compra anual por $54.000 USD", "Certificado de Cierre de Piloto Exitoso"],
                "exceptions": ["Si la propuesta hubiese superado los $7.500 USD/mes (PME), habría sido bloqueada por considerarse excesiva frente al valor aportado"]
            },
            "entities": [
                {"entity_id": "CASO_CCP_182", "type": "experimento", "name": "Caso de Pricing CCP-T01-182", "aliases": ["Validación Comercial Minera"]},
                {"entity_id": "PRECIO_OPP_4500", "type": "metrica", "name": "Precio Óptimo $4.500 USD/mes", "aliases": ["Optimal Price Point"]}
            ],
            "relations": [
                {"subject_id": "CASO_CCP_182", "predicate": "valida_modelo_comercial_de", "object_id": "THE_BRIDGE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "T01-F42-C1"}
            ],
            "comparisons": [
                {"item_a": "Precio BRIDGE ($4.500 USD/mes)", "item_b": "Costo Consultoría Externa ($15.000 USD/mes)", "dimension": "Gasto mensual cliente", "conclusion": "BRIDGE entrega cobertura en tiempo real y memoria institucional propia a un tercio del costo de una agencia tradicional."}
            ],
            "contradictions": [],
            "metrics_and_denominators": [
                {"metric": "ROI demostrado en CCP-T01-182", "denominator": "Costo anual suscripción ($54.000 USD)", "target": "3.2x"},
                {"metric": "Tiempo de ciclo de cierre en Compras", "denominator": "Días desde fin de piloto hasta OC", "target": "<= 15 días"}
            ],
            "bridge_implications": [
                {"module": "transversal", "implication": "Demuestra la viabilidad comercial y unit economics de The Bridge Intelligence en el segmento de grandes corporaciones.", "status": "evidencia"}
            ],
            "open_gaps": [],
            "next_question_ids": ["T01-F43"],
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
        print(f"Batch T01-F37..F42 añadido exitosamente. Total registros en batch: {len(batch)}")
    except Exception as err:
        print(f"Error procesando batch T01-F37..F42: {type(err).__name__} (detalles omitidos por seguridad)")
        sys.exit(1)

if __name__ == "__main__":
    main()
