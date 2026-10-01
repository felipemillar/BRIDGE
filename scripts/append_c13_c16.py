import json
import os
import sys

# Script to generate P01-C13, P01-C14, P01-C15, P01-C16 with full 20 keys schema

records = [
    {
        "question_id": "P01-C13",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre usuarios de asuntos corporativos en Chile y Latinoamérica, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:17:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan en la representación del perfil del usuario: las fuentes globales (Page Society, McKinsey, Dircom España ECE 2025) asumen un CCO con asiento garantizado en el C-Suite enfocado puramente en narrativa estratégica y consultoría directiva. Por el contrario, las síntesis internas (P01_EVIDENCE_MAP, P01_RESEARCH_DOSSIER) y los datos de LCM EUPRERA evidencian una severa brecha táctica en Latinoamérica, donde más del 60% del tiempo se consume en tareas operativas reactivas y de baja escala analítica. Además, las síntesis internas contextualizan el perfil del usuario chileno bajo tres restricciones obligatorias ausentes en modelos anglosajones: 1) Ley N° 20.730 de Lobby (transparencia y registro obligatorio de audiencias); 2) CMF NCG 461 (reporte mandatorio ASG/ESG en Memoria Anual); y 3) Exigencias de relacionamiento territorial directo y licencia social (Acción Empresas e ICARE). Prevalece la versión de las síntesis internas por su ajuste estricto al marco normativo y operativo real de Chile.",
        "findings": [
            {
                "claim_id": "P01-C13-C1",
                "claim": "Frente a la visión anglosajona idealizada del CCO exclusivamente abocado al consejo directivo, la evidencia empírica regional (LCM EUPRERA) y las síntesis internas demuestran que en América Latina existe una brecha digital y operativa: menos del 30% cuenta con herramientas CommTech maduras y más del 60% del tiempo se absorbe en redacción manual de comunicados y gestión reactiva.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-2026", "region": "América Latina", "actor": "Equipos de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "80d4fcba-ae0d-4a1d-a36c-2f3b925b4fa2",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Tensión 1 y Paradoja Territorial de Asuntos Corporativos",
                        "excerpt_short": "En LatAm más del 60% del tiempo se gasta en labores operativas y reactivas.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "18092a4f-ba3b-4861-ba1b-b72e59df957a",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Taxonomía de 6 roles en Chile y Latinoamérica",
                        "excerpt_short": "Estructuración de seis roles interconectados y subordinados a exigencias legales locales.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Convergencia entre encuestas empíricas latinoamericanas y marco legal vinculante chileno."
            },
            {
                "claim_id": "P01-C13-C2",
                "claim": "En Chile, el rol del usuario de asuntos corporativos está determinado por la Ley N° 20.730 de Lobby y la NCG 461 de la CMF, las cuales convierten cualquier declaración corporativa o reunión con autoridades en un acto de responsabilidad legal pública inmediata.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2014-2026", "region": "Chile", "actor": "Reguladores y Emisores CMF"},
                "evidence": [
                    {
                        "source_id": "87978287-38ec-4b0f-bd60-e724e02362aa",
                        "source_title": "Biblioteca del Congreso Nacional de Chile - Ley N° 20.730 de Lobby",
                        "original_url": "https://www.bcn.cl/leychile/navegar?idNorma=1060115",
                        "locator": "Artículos 5 y 8: Sujetos pasivos y registro público de audiencias",
                        "excerpt_short": "Obligatoriedad de transparentar reuniones, gestores y materias tratadas ante autoridades.",
                        "source_date": "2026-04-02",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "f5108429-197e-4009-b684-2a6c1e95cfc9",
                        "source_title": "Comisión para el Mercado Financiero - Norma de Carácter General N° 461",
                        "original_url": "https://www.cmfchile.cl/normativa/ncg_461_2021.pdf",
                        "locator": "Sección: Memoria Anual Integrada y Divulgación ASG",
                        "excerpt_short": "Exigencia de reporte de riesgos de sostenibilidad y gobierno corporativo para emisores públicos.",
                        "source_date": "2021-11-12",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Normativa legal vinculante en el ordenamiento chileno."
            }
        ],
        "operational_model": {
            "inputs": ["Agendas regulatorias chilenas", "Requerimientos de lobby", "Demandas territoriales de comunidades"],
            "actors": ["CCO", "Gerente de Asuntos Públicos", "Gerente de Sostenibilidad", "Comunidades Locales", "Sujeto Pasivo"],
            "steps": ["Detección de evento territorial o regulatorio", "Cotejo de antecedentes legales (CMF/Lobby)", "Preparación de minuta alineada", "Audiencia o mesa de diálogo", "Registro en plataformas públicas"],
            "states": ["Evento_Detectado", "Alineamiento_Normativo", "Interaccion_Ejecutada", "Cumplimiento_Registrado"],
            "outputs": ["Declaración corporativa validada y acta fidedigna de interacción"],
            "exceptions": ["Descalce entre compromiso territorial local y reporte ASG enviado a la CMF"]
        },
        "entities": [
            {"entity_id": "ENT_USUARIO_CHILENO", "type": "perfil_profesional", "name": "Usuario de Asuntos Corporativos en Chile", "aliases": ["Dircom Regulado en Chile"]}
        ],
        "relations": [
            {"subject_id": "ENT_USUARIO_CHILENO", "predicate": "sujeto_a_normativa", "object_id": "Ley_20730_y_NCG461", "valid_from": "2021", "valid_to": None, "evidence_claim_id": "P01-C13-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Modelo Anglosajón de CCO vs Realidad Operativa Chilena",
                "Modelo Anglosajón (Page/McKinsey)": "Foco en relaciones públicas voluntarias, activismo corporativo y narrativa ESG global.",
                "Realidad Chilena (Síntesis Prevaleciente)": "Foco en Ley del Lobby, NCG 461 de la CMF y mesas de diálogo con comunidades territoriales."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Relacionar", "implication": "Configurar la solución BRIDGE integrando conectores con la plataforma de Ley de Lobby e indicadores CMF NCG 461.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-C14", "P01-C15"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C14",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué sigue sin prueba sobre usuarios de asuntos corporativos en Chile y Latinoamérica, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:17:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba: 1) métricas temporales auditadas sobre horas-hombre en preparación de minutas ejecutivas en Chile (la meta 'de 4h a 15 min' es la hipótesis HT-2); 2) estudios longitudinales revisados por pares sobre el impacto de la IA en la preservación de la licencia social para operar; 3) auditorías de consistencia fáctica entre minutas preparatorias y transcripciones de audiencias de lobby. Fuentes fallidas: Gartner (Future of Communications y Gartner for Communications), Global Alliance GCF Release, Gregory & Willis 2019, Page Society (Pacesetter y Corporate Character), OECD Corporate Governance (todas por bloqueo técnico/paywall). Fuentes parciales: Asociaciones profesionales globales (ignoran el poder de veto de CISO/Legal) y consultoras comerciales (promesas no auditadas de AI Lighthouses). Validación mínima: Fase 1 (15 entrevistas cualitativas con Dircoms de sectores regulados en Chile) y Fase 2 (shadowing cronometrado durante preparación de comités de crisis o audiencias de lobby).",
        "findings": [
            {
                "claim_id": "P01-C14-C1",
                "claim": "Las fuentes originales internacionales sobre usuarios y adopción tecnológica sufren de parcialidad analítica al centrarse exclusivamente en la figura del comunicador, omitiendo los requerimientos técnicos y de seguridad que imponen las áreas de ciberseguridad (CISO) y cumplimiento legal en grandes corporaciones de Chile y la región.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "América Latina", "actor": "Comités de Ciberseguridad y Compliance"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Evaluación de Fuentes Parciales y Vacíos de Gobernanza B2B",
                        "excerpt_short": "Las fuentes tradicionales omiten los criterios de veto de CISO y Legal/Compliance.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Evaluación metodológica de vacíos de investigación en el cuaderno P01."
            },
            {
                "claim_id": "P01-C14-C2",
                "claim": "Para cerrar los vacíos sobre tiempos reales y fricciones del usuario chileno, se requiere ejecutar la Fase 1 (15 entrevistas cualitativas exploratorias con CCOs de minería, energía, retail y banca) y la Fase 2 (shadowing con cronómetro en tiempo real de un comité de crisis o preparación de audiencia).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Equipo Investigador BRIDGE"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Fase 1 y Fase 2 del Protocolo de Validación en Terreno",
                        "excerpt_short": "Fase 1: 15 entrevistas con CCOs; Fase 2: shadowing cronometrado durante preparación de comités.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Protocolo de campo estructurado en los entregables de investigación."
            }
        ],
        "operational_model": {
            "inputs": ["Muestra intencional de 15 empresas chilenas", "Pauta de entrevista semiestructurada", "Herramienta de cronometraje"],
            "actors": ["Investigador de Campo", "CCO Entrevistado", "Jefe de Prensa"],
            "steps": ["Contacto y firma de NDA", "Entrevista en profundidad sobre flujos diarios", "Observación de preparación de minuta", "Codificación de transcripciones"],
            "states": ["Contacto_Iniciado", "Entrevista_Realizada", "Flujo_Observado", "Datos_Codificados"],
            "outputs": ["Informe de Hallazgos Empíricos de Usuarios en Chile"],
            "exceptions": ["Negativa de participar en el estudio por políticas de secreto corporativo"]
        },
        "entities": [
            {"entity_id": "ENT_ESTUDIO_USUARIOS_CHILE", "type": "estudio_empirico", "name": "Estudio Empírico de Usuarios de Asuntos Corporativos en Chile", "aliases": ["Validación de Campo Fase 1 y 2"]}
        ],
        "relations": [
            {"subject_id": "ENT_ESTUDIO_USUARIOS_CHILE", "predicate": "valida_necesidades_de", "object_id": "ENT_USUARIO_CHILENO", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-C14-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Literatura Teórica vs Protocolo de Investigación Empírica",
                "Literatura Disponible": "Monitores globales de percepción sin trazabilidad a flujos de trabajo de software.",
                "Protocolo de Investigación": "Medición empírica in situ de tiempos, herramientas y repositorios consultados por usuarios reales."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Ajustar las interfaces y el lenguaje de BRIDGE al léxico institucional chileno (Lobby, RCA, CMF, audiencias) en lugar de terminología genérica anglosajona.", "status": "evidencia"}
        ],
        "open_gaps": [
            "Medición cuantitativa auditada de horas de trabajo invertidas por equipos chilenos en responder oficios de la CMF y requerimientos territoriales.",
            "Estudios comparativos de daño reputacional entre empresas con preparación manual y empresas asistidas por software de inteligencia."
        ],
        "next_question_ids": ["P01-C15", "P01-C16"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C15",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre descubrimiento y validación de usuarios, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:17:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan en la concepción del proceso de descubrimiento: las fuentes comerciales de software y consultoría (McKinsey 2025) asumen un proceso de descubrimiento lineal centrado únicamente en el usuario final (el CCO o equipo de prensa que necesita minutas rápidas), presuponiendo que satisfacer al usuario garantiza la adopción comercial. En contraste, las síntesis internas (P01_RESEARCH_DOSSIER, P01_EVIDENCE_MAP) demuestran que en asuntos corporativos de alta complejidad la validación B2B requiere abordar la Tríada de Personas: 1) El Usuario (busca rapidez y cero alucinaciones); 2) El Comprador (CEO/VP, busca blindaje y justificación de presupuesto); y 3) El Aprobador (CISO y Fiscal Legal, quienes exigen aislamiento criptográfico y poseen poder de veto vinculante si los datos se exponen a modelos públicos). Prevalece la versión de las síntesis internas: la aprobación de seguridad y cumplimiento legal es una condición previa no negociable para cualquier adopción corporativa.",
        "findings": [
            {
                "claim_id": "P01-C15-C1",
                "claim": "Frente al enfoque de venta lineal de software que se enfoca solo en resolver las tareas del usuario operativo, las síntesis internas de P01 estructuran la adopción institucional mediante la Tríada B2B: el Usuario Final (User Persona), el Comprador Presupuestario (Buyer Persona) y el Aprobador de Ciberseguridad y Compliance (Approver Persona), este último con capacidad de veto absoluto sobre la compra.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global / Chile", "actor": "Comités de Compras B2B y CISOs"},
                "evidence": [
                    {
                        "source_id": "18092a4f-ba3b-4861-ba1b-b72e59df957a",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Sección: Mapa de Actores del Ecosistema B2B (Usuario, Comprador, Aprobador)",
                        "excerpt_short": "El CISO y el Fiscal Legal ejercen poder de veto si se exponen documentos reservados a modelos públicos.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "80d4fcba-ae0d-4a1d-a36c-2f3b925b4fa2",
                        "source_title": "P01_EVIDENCE_MAP",
                        "original_url": None,
                        "locator": "Matriz de Aprobación B2B e Hipótesis HT-3",
                        "excerpt_short": "La viabilidad del producto depende de la arquitectura de seguridad antes que de la venta de características funcionales.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Estructura metodológica validada en los dossiers de investigación de P01."
            },
            {
                "claim_id": "P01-C15-C2",
                "claim": "Las síntesis internas corrigen la categorización de los Jobs-to-be-Done (JTBD), dividiéndolos en tres niveles: Funcionales (cruzar conocimiento interno con señales externas), Emocionales (reducir la ansiedad directiva ante preguntas difíciles) y Sociales (proteger la legitimidad pública de la compañía).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Marco Teórico JTBD en BRIDGE"},
                "evidence": [
                    {
                        "source_id": "18092a4f-ba3b-4861-ba1b-b72e59df957a",
                        "source_title": "P01_RESEARCH_DOSSIER",
                        "original_url": None,
                        "locator": "Estructuración de JTBD Funcionales, Emocionales y Sociales",
                        "excerpt_short": "Clasificación rigurosa de las tres capas de dolor que justifican la adopción de tecnología.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Marco conceptual de ingeniería de producto de P01."
            }
        ],
        "operational_model": {
            "inputs": ["Casos de uso del usuario operativo", "Políticas de ciberseguridad corporativa", "Presupuesto anual C-Suite"],
            "actors": ["Dircom (Usuario)", "CEO (Comprador)", "CISO (Aprobador)", "Fiscal Legal (Aprobador)"],
            "steps": ["Identificación de dolor en el equipo operativo", "Demostración de propuesta de valor al Comprador", "Evaluación de arquitectura de datos por CISO/Legal", "Dictamen de aprobación o veto vinculante"],
            "states": ["Descubrimiento_Usuario", "Interes_Comprador", "Evaluacion_Seguridad", "Aprobacion_Corporativa"],
            "outputs": ["Contrato de Adopción Corporativa B2B"],
            "exceptions": ["Veto de CISO por riesgo de fuga de información corporativa sensible"]
        },
        "entities": [
            {"entity_id": "ENT_TRIADA_B2B", "type": "modelo_adopcion", "name": "Tríada B2B de Asuntos Corporativos (Usuario, Comprador, Aprobador)", "aliases": ["Ecosistema B2B de Decisión"]}
        ],
        "relations": [
            {"subject_id": "ENT_TRIADA_B2B", "predicate": "determina_exito_adopcion_de", "object_id": "Software_Inteligencia_Ejecutiva", "valid_from": "2025", "valid_to": None, "evidence_claim_id": "P01-C15-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Descubrimiento de Usuario Tradicional vs Tríada B2B Corporativa",
                "Enfoque Tradicional": "Validar si al analista de comunicaciones le gusta la interfaz y redacta comunicados más rápido.",
                "Enfoque Tríada B2B (Prevaleciente)": "Validar simultáneamente utilidad operativa, retorno directivo y cumplimiento estricto de seguridad con el CISO."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Estructurar los materiales comerciales y técnicos de BRIDGE diferenciando argumentos de velocidad para el usuario y garantías de cifrado/VPC para el CISO y Fiscal.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P01-C16"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P01-C16",
        "notebook_id": "21152990-b13f-4cda-bd6c-0286ca855ff9",
        "question_text": "¿Qué sigue sin prueba sobre descubrimiento y validación de usuarios, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:17:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba: 1) los protocolos exactos y condiciones de seguridad bajo las cuales los CISOs del IPSA autorizarían la ingesta de documentos confidenciales en un motor de inteligencia; 2) la localización real de los repositorios corporativos en Chile (fragmentados entre SharePoint, Google Drive y correos privados); 3) la disposición a pagar (WTP) del C-Suite por herramientas de inteligencia ejecutiva; y 4) el marco de atribución legal por eventuales alucinaciones reproducidas por un vocero ante un regulador. Fuentes fallidas: Gartner (for Communications Leaders) y ResearchGate (Gregory & Willis). Fuentes parciales: monitores globales de opinión (Edelman, EUPRERA, PAC), útiles para tendencias macro pero ciegos a flujos de trabajo de software. Validación mínima: Plan en tres fases: Fase 1 (15 entrevistas cualitativas con CCOs), Fase 2 (shadowing cronometrado de preparación de comités), y Fase 3 (PoC trilateral con CCO, CISO y Fiscal Legal sobre arquitectura VPC para validar viabilidad técnica y adopción).",
        "findings": [
            {
                "claim_id": "P01-C16-C1",
                "claim": "Existe un vacío crítico de investigación respecto a los requerimientos de encriptación y aislamiento criptográfico que exigen los CISOs de grandes corporaciones para autorizar el procesamiento de minutas reservadas de directorio, así como sobre la disposición a pagar (WTP) del C-Suite por soluciones de blindaje reputacional.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / América Latina", "actor": "CISOs y Fiscalías Corporativas"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección: Vacíos de Prueba en Descubrimiento y Validación B2B",
                        "excerpt_short": "Falta de especificación estandarizada sobre las exigencias técnicas que imponen los CISOs para ingesta de datos sensibles.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación del mapa de vacíos e incertidumbres críticas del cuaderno P01."
            },
            {
                "claim_id": "P01-C16-C2",
                "claim": "El plan de validación de P01 resuelve integralmente la incertidumbre mediante un protocolo de investigación empírica en tres fases: Fase 1 de entrevistas exploratorias (semanas 1-4), Fase 2 de shadowing cronometrado (semanas 5-8) y Fase 3 de prueba de concepto con el panel evaluador tripartito CCO, CISO y Fiscal Legal (semanas 9-12).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Equipo Investigador BRIDGE"},
                "evidence": [
                    {
                        "source_id": "882b1e52-412f-4505-ae57-212def190031",
                        "source_title": "P01_GAPS_AND_VALIDATION",
                        "original_url": None,
                        "locator": "Sección: Cronograma y Fases del Plan de Validación Mínima",
                        "excerpt_short": "Estructuración secuencial del plan de validación en 3 fases durante 12 semanas.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:17:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Plan experimental estructurado en los documentos de gobernanza del proyecto."
            }
        ],
        "operational_model": {
            "inputs": ["Pauta de 15 entrevistas", "Cronómetro de shadowing", "Demo en VPC aislada"],
            "actors": ["Equipo BRIDGE", "CCO", "CISO", "Fiscal Legal"],
            "steps": ["Ejecución de Fase 1 (Entrevistas)", "Ejecución de Fase 2 (Shadowing en crisis)", "Ejecución de Fase 3 (PoC de seguridad)", "Consolidación de matriz de viabilidad"],
            "states": ["Fase1_Iniciada", "Fase2_Completada", "Fase3_Evaluada", "Incertidumbre_Cerrada"],
            "outputs": ["Matriz Validada de Adopción, Tiempos Reales y Aprobación B2B"],
            "exceptions": ["Rechazo de CISOs a validar despliegues en nube sin homologación ISO 27001 formal previa"]
        },
        "entities": [
            {"entity_id": "ENT_PLAN_3_FASES", "type": "plan_investigacion", "name": "Plan de Validación Empírica en Tres Fases (12 Semanas)", "aliases": ["Roadmap de Validación de Campo BRIDGE"]}
        ],
        "relations": [
            {"subject_id": "ENT_PLAN_3_FASES", "predicate": "despeja_incertidumbre_de", "object_id": "Viabilidad_Comercial_BRIDGE", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P01-C16-C2"}
        ],
        "comparisons": [
            {
                "dimension": "Validación Teórica de Escritorio vs Plan de Validación en 3 Fases",
                "Validación de Escritorio": "Asumir que las afirmaciones de consultoras sobre IA son aplicables de inmediato al CCO chileno.",
                "Plan de Validación BRIDGE": "Comprobar empíricamente tiempos con cronómetro y someter la arquitectura al escrutinio formal de CISO y Legal."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Ejecutar el protocolo de las tres fases como condición habilitante previa al desarrollo final del producto BRIDGE.", "status": "hipotesis"}
        ],
        "open_gaps": [
            "Protocolos técnicos de homologación de seguridad de proveedores SaaS en el sector bancario y minero de Chile.",
            "Jurisprudencia o marco legal aplicable sobre atribución de responsabilidad por errores fácticos generados por IA en declaraciones corporativas."
        ],
        "next_question_ids": ["P02-F01"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

with open("respuestas/temp_c13_c16.jsonl", "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print("Generated 4 records in respuestas/temp_c13_c16.jsonl")
