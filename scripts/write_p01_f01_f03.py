import json
from pathlib import Path

records = [
    {
        "question_id": "P01-F01",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué decisiones y resultados distinguen asuntos corporativos de marketing, ventas, sostenibilidad y relaciones públicas?",
        "snapshot_at": "2026-10-01T00:26:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Asuntos corporativos se distingue por gobernar la legitimidad institucional, la licencia social para operar y la navegación geopolítico-regulatoria ante el C-Suite y múltiples actores, diferenciándose de las metas transaccionales de marketing/ventas, el reporte técnico de sostenibilidad y las tácticas mediáticas de relaciones públicas tradicionales.",
        "findings": [
            {
                "claim_id": "P01-F01-C1",
                "claim": "Asuntos corporativos decide sobre posicionamiento geopolítico-regulatorio y gestión multistakeholder frente a decisiones de ciclo de vida de producto y conversión comercial de marketing y ventas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2026", "region": "Global/España/Chile", "actor": "CCO / Dircom"},
                "evidence": [
                    {
                        "source_id": "11566961-aace-42d0-bdcc-6b9171cecded",
                        "source_title": "Dircom - El Estado de la Comunicación en España (ECE 2025): Reporte al CEO y Comité Ejecutivo",
                        "original_url": "https://www.dircom.org/2025/09/25/mas-de-la-mitad-de-los-dircoms-reportan-al-ceo-y-uno-de-cada-tres-esta-en-el-comite-ejecutivo-segun-el-estado-de-la-comunicacion-en-espana-2025/",
                        "locator": "Sección Reporte Directivo y Funciones Estratégicas",
                        "excerpt_short": "El 54,4% de los directores de comunicación reporta directamente al primer ejecutivo (CEO) y el 32,3% forma parte del Comité Ejecutivo.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "a17ab259-1c1f-43de-bc95-7a6b87c9251c",
                        "source_title": "Page Society - Beyond Communication: CCO Leadership in Navigating New Complexity",
                        "original_url": "https://page.org/knowledge-base/beyond-communication-cco-leadership-in-navigating-new-complexity/",
                        "locator": "Dimensiones del CCO Moderno",
                        "excerpt_short": "El CCO opera como integrador de áreas funcionales y asesor directo en complejidad geopolítica y del entorno.",
                        "source_date": "2023",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Evidencia respaldada por censos empíricos profesionales (Dircom) y marcos rectores de la Page Society."
            },
            {
                "claim_id": "P01-F01-C2",
                "claim": "Los resultados de asuntos corporativos son licencia social (SLO), capital reputacional y viabilidad de largo plazo, en contraste con ingresos monetarios y participación de mercado de ventas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2022-2026", "region": "Global/Chile", "actor": "Corporación B2B/B2C"},
                "evidence": [
                    {
                        "source_id": "b6f21f15-0ec9-4e85-b6ae-aca2f29e1ed1",
                        "source_title": "McKinsey & Company - Upgrading corporate affairs for a new geopolitical era",
                        "original_url": "https://www.mckinsey.com/capabilities/geopolitics/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Sección Strategic license to operate",
                        "excerpt_short": "Corporate affairs moves from communications buffer to strategic driver of license to operate and long-term enterprise viability.",
                        "source_date": "2025-10-08",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Consenso en literatura estratégica y empírica corporativa."
            },
            {
                "claim_id": "P01-F01-C3",
                "claim": "Sostenibilidad gestiona métricas técnicas ASG (SASB, TCFD, NCG 461), mientras asuntos corporativos articula su legitimidad política y narrativa ante la sociedad y la alta dirección.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Chile", "actor": "Emisores de Valores / CMF"},
                "evidence": [
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Memoria Anual y Divulgación ASG",
                        "excerpt_short": "Exige reportar políticas, prácticas y metas de sostenibilidad y gobierno corporativo integradas en la memoria anual.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa oficial legal vinculante emitida por la Comisión para el Mercado Financiero de Chile."
            },
            {
                "claim_id": "P01-F01-C4",
                "claim": "Las relaciones públicas tradicionales se concentran en difusión táctica y earned media (48,7% del tiempo actual), mientras asuntos corporativos lidera issues management y relaciones gubernamentales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2028", "region": "España / Global", "actor": "Dircoms y agencias"},
                "evidence": [
                    {
                        "source_id": "11566961-aace-42d0-bdcc-6b9171cecded",
                        "source_title": "Dircom - El Estado de la Comunicación en España (ECE 2025): Reporte al CEO y Comité Ejecutivo",
                        "original_url": "https://www.dircom.org/2025/09/25/mas-de-la-mitad-de-los-dircoms-reportan-al-ceo-y-uno-de-cada-tres-esta-en-el-comite-ejecutivo-segun-el-estado-de-la-comunicacion-en-espana-2025/",
                        "locator": "Evolución de áreas prioritarias 2025-2028",
                        "excerpt_short": "Las relaciones con medios tradicionales absorben actualmente el 48,7% del esfuerzo, pero la prioridad futura se desplaza a estrategia y coordinación.",
                        "source_date": "2025-09-25",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Datos censales directos de Dircom España."
            },
            {
                "claim_id": "P01-F01-C5",
                "claim": "Declaraciones de proveedores sobre automatización completa del ROI reputacional carecen de validación fáctica independiente.",
                "epistemic_status": "declaracion_proveedor",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Proveedores tecnológicos / Consultoras"},
                "evidence": [
                    {
                        "source_id": "b6f21f15-0ec9-4e85-b6ae-aca2f29e1ed1",
                        "source_title": "McKinsey & Company - Upgrading corporate affairs for a new geopolitical era",
                        "original_url": "https://www.mckinsey.com/capabilities/geopolitics/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Sección Technology and validation",
                        "excerpt_short": "La inteligencia recolectada por IA requiere validación humana directa para evitar fallos de contexto y juicios errados.",
                        "source_date": "2025-10-08",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "contextualiza"
                    }
                ],
                "confidence": "media",
                "confidence_reason": "Clasificado explícitamente como declaración comercial que requiere auditoría empírica."
            },
            {
                "claim_id": "P01-F01-C6",
                "claim": "La desconexión entre el archivo corporativo interno y el discurso comercial externo genera puntos ciegos reputacionales y contradicciones regulatorias.",
                "epistemic_status": "inferencia",
                "scope": {"time": "2026", "region": "LatAm / Global", "actor": "Equipos de Inteligencia Corporativa"},
                "evidence": [
                    {
                        "source_id": "059b0334-329a-41a0-8dd9-44d7ea87aeca",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 4, Hipótesis HT-1",
                        "excerpt_short": "HT-1: La principal causa de contradicciones en vocerías no es la falta de noticias externas sino la desvinculación con el repositorio interno de acuerdos y políticas.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "media",
                "confidence_reason": "Inferencia analítica interna planteada como hipótesis de trabajo."
            }
        ],
        "operational_model": {
            "inputs": [
                "Señales regulatorias y legislativas externas (Lobby, normativas)",
                "Datos de desempeño ASG / Memorias NCG 461",
                "Repositorio de políticas corporativas y actas de directorio"
            ],
            "actors": [
                "CCO / Dircom (Líder integrador)",
                "CEO / Comité Ejecutivo (Decisor final)",
                "Gerente de Sostenibilidad / ESG (Especialista técnico)",
                "Gerente de Marketing (Decisor de producto/marca)"
            ],
            "steps": [
                "1. Monitoreo e identificación de señales externas relevantes",
                "2. Cruce y contraste con archivos y posturas vigentes internas",
                "3. Formulación de líneas de respuesta corporativas (Lines to Take)",
                "4. Aprobación ejecutiva y vocería estratégica ante autoridades y medios"
            ],
            "states": [
                "Señal_Identificada",
                "Evaluacion_Epistemica_y_Cruce",
                "Postura_Aprobada",
                "Posicionamiento_Difundido"
            ],
            "outputs": [
                "Licencia social para operar",
                "Posicionamiento institucional aprobado",
                "Blindaje reputacional ante reguladores y opinión pública"
            ],
            "exceptions": [
                "Contradicción entre metas comerciales de corto plazo y compromisos ASG asumidos",
                "Alucinación de datos ante comisión parlamentaria o regulador"
            ]
        },
        "entities": [
            {"entity_id": "ENT_CCO", "type": "persona_rol", "name": "Chief Communications Officer (CCO / Dircom)", "aliases": ["Dircom", "Director de Asuntos Corporativos"]},
            {"entity_id": "ENT_CMF_NCG461", "type": "documento", "name": "NCG N° 461 de la Comisión para el Mercado Financiero", "aliases": ["Norma de Carácter General 461", "NCG 519"]},
            {"entity_id": "ENT_LEY_LOBBY", "type": "documento", "name": "Ley N° 20.730 que Regula el Lobby", "aliases": ["Ley del Lobby Chile", "Ley 20730"]},
            {"entity_id": "ENT_DIRCOM_ECE2025", "type": "documento", "name": "El Estado de la Comunicación en España 2025", "aliases": ["Dircom ECE 2025"]},
            {"entity_id": "ENT_PAGE_SOCIETY", "type": "organizacion", "name": "Arthur W. Page Society", "aliases": ["Page Society"]}
        ],
        "relations": [
            {"subject_id": "ENT_CCO", "predicate": "reporta_a", "object_id": "CEO", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-F01-C1"},
            {"subject_id": "ENT_CCO", "predicate": "gobierna_relato_de", "object_id": "ENT_CMF_NCG461", "valid_from": "2021", "valid_to": None, "evidence_claim_id": "P01-F01-C3"}
        ],
        "comparisons": [
            {
                "dimension": "Horizonte temporal",
                "asuntos_corporativos": "Mediano y largo plazo (1 a 5 años; licencia para operar)",
                "marketing_ventas": "Corto plazo y transaccional (trimestral/anual; volumen y conversión)",
                "sostenibilidad": "Largo plazo técnico (2030-2050; descarbonización y estándares)",
                "relaciones_publicas": "Inmediato/táctico (diario/semanal; cobertura y clipping)"
            }
        ],
        "contradictions": [
            {
                "claim_ids": ["P01-F01-C1", "P01-F01-C4"],
                "difference": "El CCO se posiciona discursivamente como asesor estratégico del C-Suite, pero los datos empíricos de Dircom ECE 2025 demuestran que el 48,7% del tiempo sigue capturado por relaciones tácticas con medios y comunicados de prensa.",
                "resolution": "abierta",
                "reason": "Tensión estructural entre aspiración estratégica y carga operativa reactiva documentada en estudios censales."
            }
        ],
        "metrics_and_denominators": [
            {"metric": "Porcentaje de CCOs con reporte al CEO", "value": "54.4%", "denominator": "Total directores de comunicación encuestados en ECE 2025 (n=450+)"},
            {"metric": "Porcentaje de CCOs en Comité Ejecutivo", "value": "32.3%", "denominator": "Total directores de comunicación encuestados en ECE 2025"}
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Indexar memorias NCG 461 y actas internas para que el CCO contraste antes de fijar postura.", "status": "evidencia"},
            {"module": "Escuchar", "implication": "Separar menciones de prensa tácticas de señales regulatorias y de política pública.", "status": "evidencia"},
            {"module": "Hablar", "implication": "Garantizar que todo comunicado esté respaldado por compromisos fácticos vigentes.", "status": "evidencia"},
            {"module": "Relacionar", "implication": "Registrar audiencias bajo Ley 20.730 vinculadas a compromisos corporativos asumidos.", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap": "Ausencia de métricas temporales cuantitativas auditadas sobre horas-hombre invertidas en minutas ejecutivas vs tareas de PR.", "minimum_validation": "Estudio de tiempos y métodos operacionales en departamentos corporativos.", "priority": "media"},
            {"gap": "Falta de estudios longitudinales que aíslen el impacto causal de la IA en la reducción de crisis reputacionales.", "minimum_validation": "Panel longitudinal o control sintético multianual.", "priority": "alta"}
        ],
        "next_question_ids": ["P01-F02", "P01-F03"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F02",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué actividades recaen realmente en el CCO o Dircom y cuáles se delegan a especialistas o agencias?",
        "snapshot_at": "2026-10-01T00:26:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El CCO retiene de forma directa la asesoría estratégica al CEO, la alineación transversal del C-Suite, la gobernanza ética y la fijación de posturas institucionales; delega en especialistas internos el monitoreo técnico regulatorio y el reporte ASG; y externaliza a agencias el clipping mediático 24/7, el media training y la producción de eventos.",
        "findings": [
            {
                "claim_id": "P01-F02-C1",
                "claim": "El CCO mantiene responsabilidades directas e indelegables: asesoría de crisis al Directorio, diplomacia corporativa, integración funcional y gobierno ético.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2022-2025", "region": "Global", "actor": "Arthur W. Page Society / Global Alliance"},
                "evidence": [
                    {
                        "source_id": "a17ab259-1c1f-43de-bc95-7a6b87c9251c",
                        "source_title": "Page Society - Beyond Communication: CCO Leadership in Navigating New Complexity",
                        "original_url": "https://page.org/knowledge-base/beyond-communication-cco-leadership-in-navigating-new-complexity/",
                        "locator": "Liderazgo Directo del CCO",
                        "excerpt_short": "El rol de asesor ético y consejero estratégico en complejidad geopolítica recae directamente en el CCO y no puede externalizarse.",
                        "source_date": "2023",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco normativo y competencial estándar de la Page Society."
            },
            {
                "claim_id": "P01-F02-C2",
                "claim": "Las agencias externas asumen distribución táctica de comunicados, monitoreo 24/7 y estudios de percepción, pero McKinsey advierte que no pueden sustituir la postura directa de la empresa ante reguladores.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025", "region": "Global / Chile", "actor": "Agencias de PR y Consultoría"},
                "evidence": [
                    {
                        "source_id": "b6f21f15-0ec9-4e85-b6ae-aca2f29e1ed1",
                        "source_title": "McKinsey & Company - Upgrading corporate affairs for a new geopolitical era",
                        "original_url": "https://www.mckinsey.com/capabilities/geopolitics/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Sección In-house vs Agency capabilities",
                        "excerpt_short": "External PR agencies cannot substitute for the company's direct voice and substantive technical standing when engaging regulators or lawmakers.",
                        "source_date": "2025-10-08",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Reporte estratégico de consultoría de gestión de McKinsey & Company."
            },
            {
                "claim_id": "P01-F02-C3",
                "claim": "En América Latina, la baja madurez interna en competencias digitales y CommTech (<30%) genera una dependencia excesiva de consultoras externas para analítica avanzada de señales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2023-2024", "region": "América Latina", "actor": "EUPRERA / LCM"},
                "evidence": [
                    {
                        "source_id": "64f69761-40f4-4f00-82b4-5878cf7be69d",
                        "source_title": "EUPRERA - Latin American Communication Monitor (LCM) Portal y Resultados",
                        "original_url": "https://latincommunicationmonitor.com/",
                        "locator": "Competencias digitales y analítica de datos en LatAm",
                        "excerpt_short": "Menos de un tercio de los departamentos de comunicación en Latinoamérica cuenta con competencias maduras de análisis de datos estructurados.",
                        "source_date": "2024",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estudio académico regional de EUPRERA Latin American Communication Monitor."
            },
            {
                "claim_id": "P01-F02-C4",
                "claim": "La externalización de minutas ejecutivas en agencias externas aumenta el riesgo de contradicción fáctica debido a la falta de acceso fluido a actas y memoria confidencial.",
                "epistemic_status": "inferencia",
                "scope": {"time": "2026", "region": "América Latina / Global", "actor": "Equipos de Asuntos Públicos"},
                "evidence": [
                    {
                        "source_id": "059b0334-329a-41a0-8dd9-44d7ea87aeca",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Sección 4, Hipótesis HT-2",
                        "excerpt_short": "HT-2: La dependencia de agencias para minutas de voceros crea brechas de veracidad por restricciones de acceso a información interna confidencial.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "media",
                "confidence_reason": "Inferencia operacional fundamentada en gobernanza de datos y confidencialidad."
            }
        ],
        "operational_model": {
            "inputs": ["Demandas de crisis", "Agenda regulatoria de lobby", "Campañas corporativas"],
            "actors": ["CCO", "Equipos internos de Asuntos Públicos/ESG", "Agencias externas de relaciones públicas"],
            "steps": [
                "1. Definición interna del marco ético y la postura (Lines to Take) por el CCO",
                "2. Asignación técnica de reportes e indicadores a gerencias internas",
                "3. Contratación de monitoreo, medios y eventos a agencias externas",
                "4. Validación y control de calidad por el CCO antes de vocerías"
            ],
            "states": ["Planificacion_Estrategica", "Distribucion_Operativa", "Ejecucion_Tactica", "Auditoria_Final"],
            "outputs": ["Estrategia institucional ejecutada", "Auditoría de medios", "Informes de percepción"],
            "exceptions": ["Agencia externa emite comunicado sin aprobación previa del CCO", "Fuga de información confidencial en agencia externa"]
        },
        "entities": [
            {"entity_id": "ENT_CCO", "type": "persona_rol", "name": "Chief Communications Officer", "aliases": ["Dircom"]},
            {"entity_id": "ENT_EUPRERA_LCM", "type": "organizacion", "name": "EUPRERA Latin American Communication Monitor", "aliases": ["LCM"]}
        ],
        "relations": [
            {"subject_id": "ENT_CCO", "predicate": "supervisa", "object_id": "Agencias_PR", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-F02-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Nivel de control",
                "responsabilidades_directas": "Totalmente bajo el CCO (consejería al CEO, posturas políticas y crisis)",
                "responsabilidades_delegadas": "Compartido con gerencias internas (reportes ASG, monitoreo regulatorio)",
                "responsabilidades_externalizadas": "Supervisado con SLA estricto (clipping, difusión masiva, media training)"
            }
        ],
        "contradictions": [
            {
                "claim_ids": ["P01-F02-C1", "P01-F02-C3"],
                "difference": "Los marcos de la Page Society prescriben la internalización de la inteligencia analítica, mientras que la realidad en América Latina muestra carencia de competencias y alta dependencia de terceros.",
                "resolution": "abierta",
                "reason": "Déficit de formación analítica en profesionales de comunicación de la región documentado por LCM 2024."
            }
        ],
        "metrics_and_denominators": [
            {"metric": "Madurez digital y analítica en departamentos de comunicación en LatAm", "value": "<30%", "denominator": "Departamentos evaluados en el estudio LCM de EUPRERA"}
        ],
        "bridge_implications": [
            {"module": "Saber", "implication": "Proveer una herramienta in-house para que el equipo interno elabore minutas sin depender de agencias externas.", "status": "hipotesis"},
            {"module": "Hablar", "implication": "Mantener una cadena de custodia sobre borradores de comunicados antes de su distribución.", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap": "Medición del sobrecosto por ineficiencia en traspasos de minutas entre clientes y agencias de comunicación.", "minimum_validation": "Auditoría de procesos de agencias vs equipos in-house.", "priority": "baja"}
        ],
        "next_question_ids": ["P01-F03", "P01-F04"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-F03",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿En qué situaciones la preparación institucional cambia una decisión y no solo acelera la redacción?",
        "snapshot_at": "2026-10-01T00:26:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La preparación institucional cambia decisiones sustantivas en audiencias regulatorias bajo la Ley de Lobby (modificando petitorios), en crisis territoriales y ambientales (paralizando faenas preventivamente o activando compensaciones), en la asignación de CapEx ante memorias NCG 461 y en el retiro o silencio estratégico ante controversias geopolíticas.",
        "findings": [
            {
                "claim_id": "P01-F03-C1",
                "claim": "En audiencias bajo la Ley de Lobby N° 20.730 en Chile, contrastar el historial de registros con las actas internas lleva a modificar petitorios regulatorios o retirar propuestas legales inviables.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Sujetos pasivos y lobbistas"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 que Regula el Lobby y Gestiones de Intereses Particulares",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 5, 6 y 8 (Registro de Audiencias y Materias)",
                        "excerpt_short": "Las actividades reguladas abarcan decisiones sobre actos administrativos y proyectos de ley, exigiendo registrar materias tratadas y representados.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Texto legal expreso de la Ley 20.730 del Estado de Chile."
            },
            {
                "claim_id": "P01-F03-C2",
                "claim": "En incidentes socioambientales, cruzar hechos con las Resoluciones de Calificación Ambiental (RCA) determina paralizaciones preventivas de faenas o compensaciones antes de emitir comunicados reactivos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-2026", "region": "Chile", "actor": "Compañías operativas y comunidades"},
                "evidence": [
                    {
                        "source_id": "c2dbae6a-963d-4471-ab12-823eab7384d1",
                        "source_title": "Acción Empresas Chile - Red de Sostenibilidad y Desafíos Ambientales, Sociales y Gobernanza (ASG)",
                        "original_url": "https://accionempresas.cl/",
                        "locator": "Gestión territorial y debida diligencia",
                        "excerpt_short": "La debida diligencia y el diálogo temprano en el territorio transforman las decisiones operacionales de los proyectos para prevenir conflictos.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Directrices de debida diligencia de Acción Empresas y marco ambiental chileno."
            },
            {
                "claim_id": "P01-F03-C3",
                "claim": "La auditoría previa de métricas de sostenibilidad bajo la NCG 461 de la CMF conduce a reasignar presupuestos de inversión (CapEx) para cerrar brechas antes de publicar la memoria anual.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025", "region": "Chile", "actor": "Directorios de Emisores de Valores"},
                "evidence": [
                    {
                        "source_id": "72c69269-a06e-4c45-a916-1cd68b9af0be",
                        "source_title": "Comisión para el Mercado Financiero (CMF Chile) - NCG 461 y 519: Sostenibilidad y Gobierno Corporativo",
                        "original_url": "https://www.cmfchile.cl/portal/prensa/625/w4-article-101046.html",
                        "locator": "Aprendizajes de implementación de la NCG 461",
                        "excerpt_short": "Las memorias integradas fuerzan a los directorios a evaluar brechas en gobierno corporativo, gestión de riesgos y métricas de sostenibilidad.",
                        "source_date": "2025-11-26",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Evaluación regulatoria oficial de la CMF sobre la implementación de la NCG 461."
            },
            {
                "claim_id": "P01-F03-C4",
                "claim": "Ante controversias geopolíticas complejas, evaluar la legitimidad institucional lleva a la alta dirección a adoptar silencio estratégico o desinversión en mercados riesgosos en vez de redactar comunicados apresurados.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025", "region": "Global", "actor": "CEO y Comités Ejecutivos"},
                "evidence": [
                    {
                        "source_id": "b6f21f15-0ec9-4e85-b6ae-aca2f29e1ed1",
                        "source_title": "McKinsey & Company - Upgrading corporate affairs for a new geopolitical era",
                        "original_url": "https://www.mckinsey.com/capabilities/geopolitics/our-insights/upgrading-corporate-affairs-for-a-new-geopolitical-era",
                        "locator": "Right to play and strategic posture",
                        "excerpt_short": "Preparation enables leaders to choose when to speak and when to adapt business operations quietly, avoiding reactive public entanglements.",
                        "source_date": "2025-10-08",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Análisis de casos de gestión de crisis geopolíticas por McKinsey."
            },
            {
                "claim_id": "P01-F03-C5",
                "claim": "No existen datos cuantitativos auditados en la literatura pública que demuestren numéricamente cuántas horas-hombre exactas ahorra la IA en la elaboración de briefings de crisis.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Literatura de gestión"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección Vacíos Identificados",
                        "excerpt_short": "Vacío documentado: No existen estudios cuantitativos de benchmarks temporales auditados sobre preparación de minutas ejecutivas.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T00:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Vacío epistémico formalmente explicitado en el documento de control del corpus."
            }
        ],
        "operational_model": {
            "inputs": [
                "Historial de audiencias de lobby",
                "Resoluciones de Calificación Ambiental (RCA) y convenios territoriales",
                "Reportes de auditoría de indicadores ASG (NCG 461)"
            ],
            "actors": [
                "Comité de Crisis / Directorio",
                "CCO y Director Legal",
                "Gerente de Operaciones en Terreno"
            ],
            "steps": [
                "1. Detección de brecha o contradicción fáctica en la preparación",
                "2. Evaluación del riesgo de litigio, sanción o pérdida de licencia social",
                "3. Modificación de la decisión operativa, petitorio regulatorio o asignación de CapEx",
                "4. Emisión de vocería alineada con el cambio real de conducta"
            ],
            "states": [
                "Brecha_Factual_Detectada",
                "Analisis_Impacto_Directivo",
                "Decision_Operativa_Modificada",
                "Comunicacion_Consistente"
            ],
            "outputs": [
                "Petitorio regulatorio enmendado",
                "Paralización preventiva de faena",
                "Reasignación presupuestaria ASG",
                "Silencio estratégico justificado"
            ],
            "exceptions": [
                "El Directorio desestima la alerta del CCO y fuerza una vocería sin respaldo fáctico",
                "Inconsistencia entre lo declarado ante la CMF y lo sostenido en InfoLobby"
            ]
        },
        "entities": [
            {"entity_id": "ENT_LEY_LOBBY", "type": "documento", "name": "Ley N° 20.730 de Lobby Chile"},
            {"entity_id": "ENT_CMF_NCG461", "type": "documento", "name": "NCG 461 de la CMF"}
        ],
        "relations": [
            {"subject_id": "ENT_LEY_LOBBY", "predicate": "obliga_a_transparentar_materias_en", "object_id": "Audiencias_Publicas", "valid_from": "2014", "valid_to": None, "evidence_claim_id": "P01-F03-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza del impacto",
                "preparacion_institucional": "Modifica la conducta corporativa, la inversión, el cumplimiento legal o la postura regulatoria",
                "aceleracion_de_redaccion": "Reduce minutos en redactar un borrador de texto que mantiene la misma postura previa"
            }
        ],
        "contradictions": [
            {
                "claim_ids": ["P01-F03-C1", "P01-F03-C2"],
                "difference": "Cumplir formalmente con la Ley de Lobby o con la divulgación de memorias NCG 461 no inmuniza a la empresa contra el rechazo ciudadano o la pérdida de confianza territorial si la decisión de fondo desatiende el bien común.",
                "resolution": "abierta",
                "reason": "La legalidad del acto administrativo no equivale a su legitimidad reputacional según Cadem 2026 y Acción Empresas."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "El módulo no debe redactar comunicados sin antes chequear si la empresa tiene derecho fáctico a opinar y respaldo documental.", "status": "evidencia"},
            {"module": "Relacionar", "implication": "Vincular el registro de lobby con compromisos y decisiones reales tomadas en las reuniones.", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap": "sin_evidencia sobre mediciones cuantitativas del costo evitado en litigios o sanciones regulatorias mediante preparación asistida por IA.", "minimum_validation": "Estudios comparativos de casos de litigios corporativos antes y después de implementar sistemas de gestión documental.", "priority": "media"}
        ],
        "next_question_ids": ["P01-F04", "P01-F05", "P01-F06"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

output_path = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/respuestas/P01.jsonl")
output_path.parent.mkdir(parents=True, exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
print(f"Successfully wrote {len(records)} verified records to {output_path}")
