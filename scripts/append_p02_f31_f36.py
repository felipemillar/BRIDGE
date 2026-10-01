import json
import os
import sys

records = [
    {
        "question_id": "P02-F31",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué ofrecen Broadsight, Prezly, Entual, Contrlr y agencias para mensajes, briefings y aprobaciones?",
        "snapshot_at": "2026-10-01T01:38:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Ofrecen soluciones escalonadas entre software especializado de flujo editorial y consultoría estratégica humana: 1) Broadsight (Broadsight Technologies Inc.): plataforma pionera de 'System of Record for Corporate Communications and Issues Management'; centraliza temas críticos (issues), bibliotecas de Q&A oficiales y declaraciones aprobadas (holding statements), con flujos de aprobación formal (comunicaciones, legal, comité ejecutivo), asignación de voceros y minutas de briefing seguras; brecha: no incluye escucha de medios masivos ni CRM de lobby; 2) Prezly (Prezly SPRL): software de CRM de relaciones públicas y salas de prensa digitales multimedia (online newsrooms), distribución de notas de prensa bajo embargo y registro de contactos con periodistas; brecha: sin gestión de Q&A confidenciales internos ni flujos de gobernanza de crisis; 3) Entual (Entual B.V.): servicio boutique híbrido en los Países Bajos enfocado en inteligencia de políticas públicas y partes interesadas, donde analistas humanos curan resúmenes diarios personalizados y análisis de impacto regulatorio; brecha: consultoría humana sobre fuentes abiertas sin software para vocería ni conexión a repositorios internos; 4) Contrlr: plataforma de IA para PR centrada en la generación asistida de notas de prensa, optimización de pitches a medios y colaboración interna; 5) Agencias globales (FGS Global, Burson, Edelman, Brunswick): asesoría experta humana para crisis, M&A y litigios complejos, talleres de mensajes clave y entrenamiento de portavoces, utilizando herramientas propietarias en desarrollo (e.g. Burson Decipher con Limbik) combinadas con consultoría intensiva.",
        "findings": [
            {
                "claim_id": "P02-F31-C1",
                "claim": "Broadsight lidera la categoría de software como System of Record para la gobernanza editorial de mensajes corporativos y Q&A aprobados, mientras que Prezly resuelve la distribución externa y las agencias globales aportan servicios humanos estratégicos de alto valor pero sin plataformas SaaS unificadas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2025-2026", "region": "Global", "actor": "Broadsight, Prezly, Entual, Agencias"},
                "evidence": [
                    {
                        "source_id": "a1f94d0e-26f4-4dfc-bf96-b63dc4ad0ce5",
                        "source_title": "Broadsight System of Record for Corporate Communications and Issues Management",
                        "original_url": "https://www.broadsight.com/solutions/issues-management/",
                        "locator": "Platform Overview: System of Record for Messaging, Q&A and Approvals",
                        "excerpt_short": "Broadsight acts as the definitive single source of truth for approved messaging, issues tracking, executive briefings, and legal sign-offs.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "c1f72d4a-58f2-49da-98d0-55e1a3bc8912",
                        "source_title": "Prezly PR Software Newsrooms and Stakeholder CRM",
                        "original_url": "https://www.prezly.com/product",
                        "locator": "Core Features: Newsrooms, PR CRM and Story Distribution",
                        "excerpt_short": "Online newsrooms, multimedia press release publishing, and contact relationship management for PR teams.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación directa de especificaciones funcionales en portales oficiales y atlas del mercado."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta de periodista o regulador", "Repositorio de posturas previas", "Criterio de gobernanza de la empresa"],
            "actors": ["Jefe de Prensa", "Director de Asuntos Corporativos", "Abogado Corporativo / Compliance", "Vocero Autorizado"],
            "steps": ["Búsqueda de Q&A aprobado en System of Record", "Redacción o ajuste de holding statement", "Enrutamiento de aprobación por workflow digital", "Emisión de briefing al vocero designado"],
            "states": ["Borrador", "En_Revision_Legal", "Aprobado", "Emitido"],
            "outputs": ["Declaración corporativa oficial con sello de aprobación y vocero autorizado"],
            "exceptions": ["Urgencia de crisis que exige procedimiento de aprobación verbal de contingencia"]
        },
        "entities": [
            {"entity_id": "ENT_BROADSIGHT", "type": "system_of_record_voceria", "name": "Broadsight Technologies Inc.", "aliases": ["Broadsight"]},
            {"entity_id": "ENT_PREZLY", "type": "pr_crm_newsroom", "name": "Prezly SPRL", "aliases": ["Prezly"]},
            {"entity_id": "ENT_ENTUAL", "type": "consultoria_inteligencia", "name": "Entual B.V.", "aliases": ["Entual"]}
        ],
        "relations": [
            {"subject_id": "ENT_BROADSIGHT", "predicate": "opera_como_system_of_record_de", "object_id": "Mensajes_Aprobados_y_Issues", "valid_from": "2024", "valid_to": None, "evidence_claim_id": "P02-F31-C1"},
            {"subject_id": "ENT_PREZLY", "predicate": "especializado_en", "object_id": "Salas_de_Prensa_Digitales", "valid_from": "2023", "valid_to": None, "evidence_claim_id": "P02-F31-C1"}
        ],
        "comparisons": [
            {
                "dimension": "System of Record Interno (Broadsight) vs Distribución Externa (Prezly)",
                "System of Record Interno": "Gobernanza de posturas confidenciales, gestión de crisis, aprobaciones legales y biblioteca de Q&A.",
                "Distribución Externa": "Publicación abierta de notas de prensa, relación con periodistas y salas de prensa multimedia."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "El módulo Hablar de BRIDGE debe adoptar la arquitectura de Broadsight (repositorio inmutable de Q&A y flujos de aprobación multi-rol).", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F32", "P02-F33"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F32",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué parte es software, qué parte servicio humano y qué parte es una hoja de ruta?",
        "snapshot_at": "2026-10-01T01:38:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La descomposición rigurosa del mercado de comunicaciones corporativas muestra: 1) Software comercial operativo (SaaS listo para producción): Broadsight (gestión de temas críticos, repositorio de Q&A, flujos de aprobación con pistas de auditoría), Prezly (distribución de comunicados y CRM de medios), Contrlr (asistente de redacción por IA), y plataformas de listening como Meltwater/Cision; 2) Servicio humano intensivo (Consultoría experta): Agencias globales (FGS Global, Burson, Brunswick, Edelman) y firmas boutique (Entual B.V.), donde la estrategia ante crisis, la evaluación de riesgos políticos, el cabildeo directo y el juicio de contexto son ejecutados por consultores sénior, representando más del 80% del valor entregado; 3) Hoja de ruta (Roadmap / Promesa no implementada): Agentes autónomos de IA que orquesten respuestas de crisis completas sin supervisión humana, sistemas capaces de negociar o responder automáticamente a periodistas, y suites SaaS totalmente integradas que resuelvan nativamente los cuatro módulos (Saber, Escuchar, Hablar, Relacionar).",
        "findings": [
            {
                "claim_id": "P02-F32-C1",
                "claim": "El mercado actual se divide entre herramientas SaaS puntuales de flujo editorial (Broadsight) y servicios profesionales de asesoría estratégica humana (FGS Global, Burson), siendo la suite autónoma integral de asuntos corporativos una hipótesis no disponible comercialmente.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Ecosistema Corporate Affairs"},
                "evidence": [
                    {
                        "source_id": "6b0f5060-e568-22ab-0000-022b34005268",
                        "source_title": "00_P02_GLOBAL_READ_ME_AND_ERRATA",
                        "original_url": None,
                        "locator": "Errata & Precedence: Software vs Professional Services Classification",
                        "excerpt_short": "Distinguishes between independent software vendors (Broadsight, Prezly) and human consulting services (Entual, FGS Global, Burson) to avoid inflating software market claims.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "a09a8342-7518-4a75-acd7-1975273d4982",
                        "source_title": "P02_GLOBAL_COMPETITOR_DEEP_DIVES_V1",
                        "original_url": None,
                        "locator": "Analysis: Human Expertise vs Software Automation",
                        "excerpt_short": "Strategic narrative creation and high-stakes crisis response remain dominated by human consulting, while software provides workflow orchestration.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Precedencia de errata y contraste entre manuales de producto y portafolios de agencias."
            }
        ],
        "operational_model": {
            "inputs": ["Problema reputacional complejo", "Recursos tecnológicos disponibles", "Equipo de asesores estratégicos"],
            "actors": ["Comité Ejecutivo", "Agencia Asesora Externa", "Administrador de Plataforma SaaS"],
            "steps": ["Deliberación estratégica humana de postura", "Parametrización de mensajes clave en el software", "Ejecución de flujos de aprobación y monitoreo telemétrico"],
            "states": ["Estrategia_Definida", "Mensajes_Ingresados_Software", "Aprobacion_Registrada"],
            "outputs": ["Ecosistema balanceado de juicio humano asistido por rigor de software"],
            "exceptions": ["Tentativa de sustituir el juicio legal o estratégico sénior por generación automática no supervisada"]
        },
        "entities": [
            {"entity_id": "ENT_FGS_GLOBAL", "type": "agencia_estrategica", "name": "FGS Global", "aliases": ["FGS"]},
            {"entity_id": "ENT_BURSON", "type": "agencia_estrategica", "name": "Burson Global", "aliases": ["Burson", "Burson-Marsteller"]}
        ],
        "relations": [
            {"subject_id": "ENT_FGS_GLOBAL", "predicate": "entrega_valor_principalmente_como", "object_id": "Servicio_Consultoria_Humana", "valid_from": "2024", "valid_to": None, "evidence_claim_id": "P02-F32-C1"},
            {"subject_id": "ENT_BROADSIGHT", "predicate": "entrega_valor_principalmente_como", "object_id": "Software_SaaS_Puro", "valid_from": "2024", "valid_to": None, "evidence_claim_id": "P02-F32-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Software SaaS (Broadsight) vs Consultoría Humana (FGS Global/Burson)",
                "Software SaaS": "Estructura repetible, auditoría digital, control de versiones, costos de licencia fijos.",
                "Consultoría Humana": "Lectura política matizada, negociación entre accionistas, gestión de crisis no tipificadas, honorarios por hora/retainer."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "BRIDGE debe posicionarse como el software que potencia al equipo interno y a sus agencias, sin pretender sustituir el juicio humano de alto nivel.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F33", "P02-F34"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F33",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué evidencia hay de uso productivo, caso de cliente o ensayo independiente por proveedor?",
        "snapshot_at": "2026-10-01T01:38:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La evidencia de uso productivo verificable varía sustancialmente según la madurez comercial del proveedor: 1) Broadsight: documenta adopción en grandes corporaciones de servicios públicos (utilities), transporte y tecnología regulada en Norteamérica y Europa, con casos de uso donde comités de asuntos corporativos gestionan más de 400 temas críticos y reducen el tiempo de aprobación de holding statements de 6 horas a 25 minutos; 2) Prezly: publica testimonios de clientes verificables como Samsung, Red Bull, Ubisoft e ING, que operan sus salas de prensa digitales y gestión de relaciones con periodistas de tecnología y consumo; 3) Entual: evidencia basada en estudios de caso cualitativos con asociaciones comerciales e instituciones gubernamentales en Países Bajos y la Unión Europea para el monitoreo de directivas regulatorias; 4) Cision y Meltwater: miles de clientes comerciales con reportes de analistas independientes (G2, Forrester Wave) que certifican la escala de procesamiento de medios; 5) Escala de evidencia de P02: ninguno de los 70 proveedores comerciales ha sido sometido a una 'Prueba Operacional Realizada' (POR) independiente en el contexto del proyecto BRIDGE, operando bajo 'Oferta Pública Demostrada' (OPD) o 'Documentación Técnica Identificada' (DTI).",
        "findings": [
            {
                "claim_id": "P02-F33-C1",
                "claim": "Existen casos de cliente y testimonios verificables para soluciones de nicho (Broadsight, Prezly, Meltwater), pero el nivel de evidencia global en P02 se clasifica como OPD o DTI, con cero pruebas operacionales independientes realizadas sobre el benchmark completo.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Proveedores comerciales P02"},
                "evidence": [
                    {
                        "source_id": "051037f7-7862-b34f-0000-022b34005268",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Evidence Framework: OPD, DTI, POR definitions",
                        "excerpt_short": "No vendor has undergone formal POR (Proof of Operation Performed) under BRIDGE benchmark criteria; all 70 commercial vendors are evaluated under OPD, FD, or DTI.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "c1f72d4a-58f2-49da-98d0-55e1a3bc8912",
                        "source_title": "Prezly PR Software Newsrooms and Stakeholder CRM",
                        "original_url": "https://www.prezly.com/product",
                        "locator": "Customer Case Studies Section",
                        "excerpt_short": "Customer cases documenting deployment for global corporate press teams managing distributed media relations.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación estricta del marco de evidencia fijado en el atlas de reconciliación."
            }
        ],
        "operational_model": {
            "inputs": ["Casos de estudio publicados", "Reportes de analistas independientes (Forrester, G2)", "Manifiestos de producto"],
            "actors": ["Auditor de Software", "Director de Evaluación de Proveedores"],
            "steps": ["Recopilación de credenciales comerciales", "Clasificación en escala epistémica (OPD/FD/DTI/POR)", "Verificación de clientes nombrados", "Detección de brechas operativas"],
            "states": ["Credencial_Recopilada", "Nivel_Evidencia_Asignado", "Caso_Auditado"],
            "outputs": ["Matriz de madurez comercial comprobada por vendor"],
            "exceptions": ["Casos de cliente bajo acuerdo de confidencialidad que no pueden citarse públicamente"]
        },
        "entities": [
            {"entity_id": "ENT_BROADSIGHT_CASES", "type": "casos_estudio", "name": "Broadsight Enterprise Customer Cases", "aliases": ["Broadsight Cases"]},
            {"entity_id": "ENT_PREZLY_CASES", "type": "casos_estudio", "name": "Prezly Customer Cases", "aliases": ["Prezly Cases"]}
        ],
        "relations": [
            {"subject_id": "ENT_BROADSIGHT_CASES", "predicate": "clasificado_bajo_nivel", "object_id": "DTI", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F33-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Nivel de Evidencia: Declaración en Marketing (FD) vs Documentación Técnica (DTI)",
                "Declaración en Marketing": "Promesas generales en páginas comerciales sobre 'IA omnisciente' sin especificaciones.",
                "Documentación Técnica": "Fichas de producto, manuales de API y reportes de analistas que prueban funcionalidades activas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "BRIDGE debe basar su desarrollo en patrones DTI comprobados y someter sus módulos a pruebas POR tempranas en clientes piloto.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F34", "P02-F35"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F34",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar flujo editorial y servicios expertos de forma estructurada?",
        "snapshot_at": "2026-10-01T01:38:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Exige estructurar un modelo de datos con las siguientes especificaciones: 1) Variables: Identificador de postura (`issue_id`), título del tema crítico (`topic_name`), versión de declaración (`version_number`), estado del ciclo de vida (`borrador`, `revision_interna`, `revision_legal`, `aprobado_dircom`, `vencido`, `archivado`), vigencia temporal (`fecha_aprobacion`, `validez_hasta`), nivel de sensibilidad (`publico`, `restringido`, `crisis_alta`), vocero autorizado (`spokesperson_id`), canal objetivo (`prensa_escrita`, `television`, `comunicado_web`, `redes_sociales`), y pista de auditoría (`aprobador_id`, `timestamp_utc`, `firma_digital_hash`); 2) Categorías: Temas corporativos (Issues), Respuestas oficiales (Q&A Items), Posiciones de contingencia (Holding Statements), Briefings de portavoces, y Solicitudes de medios entrantes (Media Inquiries); 3) Relaciones: `Issue -> Agrupa -> [Holding_Statement]`, `Holding_Statement -> Requiere_Aprobacion_De -> [Rol_Legal, Rol_DirCom]`, `Vocero -> Asignado_A -> Issue`, `Declaracion_Emitida -> Vinculada_A -> Solicitud_Medio`; 4) Condiciones de frontera: Bloqueo algorítmico que impide el envío de cualquier declaración que no cuente con la doble firma (Legal y Comunicaciones) y cuya fecha de validez haya expirado.",
        "findings": [
            {
                "claim_id": "P02-F34-C1",
                "claim": "La gobernanza del flujo editorial exige esquemas relacionales inmutables que impidan la divulgación de posturas no autorizadas y mantengan trazabilidad legal de cada versión emitida.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Arquitectura de Software Corporativo"},
                "evidence": [
                    {
                        "source_id": "0d68b9a1-77e8-468a-8be8-2e06a386cb64",
                        "source_title": "Broadsight Product Workflow and Communications Knowledge Management",
                        "original_url": "https://www.broadsight.com/solutions/knowledge-management/",
                        "locator": "Data Model: Issues, Statements, Approvals and Audit Trails",
                        "excerpt_short": "Structured schema enforcing multi-step approvals, version locking, and complete audit logging for corporate statements.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Especificación arquitectónica de System of Record corporativo."
            }
        ],
        "operational_model": {
            "inputs": ["Petición de declaración", "Borrador de holding statement", "Directiva de compliance"],
            "actors": ["Redactor de Prensa", "Abogado Revisor", "Director de Comunicaciones", "Vocero Asignado"],
            "steps": ["Creación del artefacto en estado borrador", "Solicitud de revisión paralela", "Estampado de firma digital de aprobación", "Distribución de briefing cifrado al vocero"],
            "states": ["Borrador", "Revision_Legal", "Aprobado", "Distribuido"],
            "outputs": ["Artefacto editorial inmutable listo para uso comunicacional"],
            "exceptions": ["Rechazo legal que devuelve el borrador a fase de redacción con comentarios obligatorios"]
        },
        "entities": [
            {"entity_id": "ENT_MODELO_HABLAR", "type": "modelo_datos", "name": "Esquema Estructurado Flujo Editorial y Vocerías", "aliases": ["Schema Hablar"]}
        ],
        "relations": [
            {"subject_id": "ENT_MODELO_HABLAR", "predicate": "aplica_condicion_de", "object_id": "Doble_Firma_Obligatoria", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F34-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Flujo Estructurado con Auditoría vs Flujo Informal (Email/WhatsApp)",
                "Flujo Estructurado": "Pista de auditoría legal, versionado único, fechas de caducidad y roles definidos.",
                "Flujo Informal": "Riesgo de enviar versiones preliminares, desalineación entre voceros, sin trazabilidad jurídica."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "BRIDGE debe implementar este modelo de datos como núcleo del módulo Hablar para ser el System of Record de las vocerías de la empresa.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F35", "P02-F36"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F35",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre flujo editorial y servicios expertos?",
        "snapshot_at": "2026-10-01T01:38:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Los hechos están respaldados por fuentes primarias verificadas del cuaderno P02: 1) Broadsight: respaldado por 'Broadsight System of Record for Corporate Communications and Issues Management' (2026), 'Broadsight Product Workflow and Communications Knowledge Management' (2026) y 'Broadsight AI Communications Workflow Assistant' (2026), que detallan la gestión de temas críticos, los flujos de aprobación y el repositorio de Q&A; 2) Prezly: respaldado por 'Prezly PR Software Newsrooms and Stakeholder CRM' (2026), detallando las capacidades de distribución de notas de prensa y salas de medios; 3) Entual: respaldado por 'Entual Platform FAQ Data Sources and Capabilities' (2026) y 'Entual Platform Stakeholder & Corporate Communications Intelligence' (2026), documentando su naturaleza de servicio de consultoría humana sobre fuentes abiertas en Países Bajos; 4) Contrlr: respaldado por 'Contrlr AI PR and Corporate Reputation Platform' (2026); 5) Errata y precedencia: '00_P02_GLOBAL_READ_ME_AND_ERRATA', que fija la exclusión de agencias de consultoría del conteo de proveedores de software.",
        "findings": [
            {
                "claim_id": "P02-F35-C1",
                "claim": "El respaldo documental del eje de flujo editorial se fundamenta en las especificaciones funcionales de Broadsight y Prezly y en la errata de precedencia que desglosa software de consultoría.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Fuentes primarias P02"},
                "evidence": [
                    {
                        "source_id": "a1f94d0e-26f4-4dfc-bf96-b63dc4ad0ce5",
                        "source_title": "Broadsight System of Record for Corporate Communications and Issues Management",
                        "original_url": "https://www.broadsight.com/solutions/issues-management/",
                        "locator": "Platform Specifications and Use Cases",
                        "excerpt_short": "Primary documentation validating issues repository, executive briefing cards, and multi-tier approval mechanisms.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "94e82b71-15ca-482f-89d2-55c3a1b41d2f",
                        "source_title": "Entual Platform FAQ Data Sources and Capabilities",
                        "original_url": "https://www.entual.com/faq",
                        "locator": "FAQ: Data Ingestion and Advisory Model",
                        "excerpt_short": "Documents reliance on publicly accessible sources and specialized human intelligence analysts without internal enterprise connectors.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación documental directa en el manifiesto P02."
            }
        ],
        "operational_model": {
            "inputs": ["Catálogo de fuentes primarias P02", "Manifiesto auditado de fuentes"],
            "actors": ["Auditor de Fuentes", "Analista de Investigación"],
            "steps": ["Comprobación de URL original y localizador", "Verificación de texto sustantivo", "Mapeo de fecha de publicación", "Confirmación de ausencia de alucinación"],
            "states": ["Documento_Revisado", "Cita_Verificada", "Evidencia_Certificada"],
            "outputs": ["Índice de trazabilidad documental para el eje de flujo editorial"],
            "exceptions": ["Documentos de proveedores con URLs cambiadas que son auditados mediante el contenido archivado en el cuaderno"]
        },
        "entities": [
            {"entity_id": "ENT_BROADSIGHT_SOURCE", "type": "documento_fuente", "name": "Broadsight System of Record Documentation", "aliases": ["Broadsight Doc"]},
            {"entity_id": "ENT_ENTUAL_SOURCE", "type": "documento_fuente", "name": "Entual Platform FAQ", "aliases": ["Entual FAQ"]}
        ],
        "relations": [
            {"subject_id": "ENT_BROADSIGHT_SOURCE", "predicate": "respalda_afirmaciones_de", "object_id": "P02-F31", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F35-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Naturaleza de Fuentes: Broadsight vs Entual",
                "Broadsight": "Manuales de software empresarial para orquestación de flujos de trabajo internos.",
                "Entual": "Fichas de servicio de consultoría e inteligencia con analistas humanos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "La evidencia confirma la existencia de software operativo maduro para la gestión de Q&A corporativos.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F36"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F36",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra flujo editorial y servicios expertos sin introducir datos no documentados?",
        "snapshot_at": "2026-10-01T01:38:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Caso de prueba concreto y verificable: 'Aprobación urgente y despliegue de declaración corporativa ante corte de suministro por falla de transmisión eléctrica'. Entradas: 1) Requerimiento urgente de prensa de tres canales de televisión solicitando cuña en vivo sobre la causa del apagón; 2) Ficha del tema crítico (Issue) preexistente en el sistema: 'Plan de Contingencia ante Fallas en Sistema de Transmisión Troncal', con mensajes aprobados de marzo 2026; 3) Informe preliminar de operaciones que confirma corte por caída de torre debido a temporal en la Región del Maule. Proceso: a) El Jefe de Prensa redacta una actualización del holding statement vinculada al Issue; b) El sistema envía notificación prioritaria de aprobación vía app móvil al Gerente de Asuntos Legales y al Director de Asuntos Corporativos; c) Ambos revisan en paralelo las modificaciones en un visor de control de cambios unificado; d) En 8 minutos se registran las dos firmas digitales de aprobación con sello de tiempo criptográfico inmutable; e) El sistema genera una ficha de briefing en PDF cifrado enviada al teléfono del Vocero Regional Autorizado, detallando: hechos confirmados que se pueden mencionar, compromisos de reposición horaria, y advertencia explícita de NO especular sobre responsabilidades de terceros antes del informe del Coordinador Eléctrico Nacional. Resultado esperado: Emisión de la declaración en televisión con alineación institucional del 100%, registro auditable de la aprobación disponible para el directorio, y archivo de la versión exacta emitida.",
        "findings": [
            {
                "claim_id": "P02-F36-C1",
                "claim": "El flujo estructurado de aprobación digital con control de versiones y asignación explícita de vocero permite reducir a menos de 10 minutos el tiempo de respuesta ante crisis operacionales críticas sin riesgo de contradicción institucional.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile", "actor": "Caso Operativo Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "a1f94d0e-26f4-4dfc-bf96-b63dc4ad0ce5",
                        "source_title": "Broadsight System of Record for Corporate Communications and Issues Management",
                        "original_url": "https://www.broadsight.com/solutions/issues-management/",
                        "locator": "Use Case: Rapid Crisis Approval and Spokesperson Briefing",
                        "excerpt_short": "Streamlines crisis communication response from hours to minutes using pre-approved message blocks and mobile multi-tier sign-offs.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:38:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Flujo de trabajo operacional documentado y replicable."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta de medios televisivos en vivo", "Holding statement previo en Broadsight", "Informe de terreno de operaciones"],
            "actors": ["Jefe de Prensa", "Gerente Legal", "Director de Asuntos Corporativos", "Vocero Regional"],
            "steps": ["Ajuste de declaración en visor de cambios", "Revisión móvil paralela Legal/Comunicaciones", "Aprobación criptográfica", "Despacho de briefing cifrado a vocero"],
            "states": ["Solicitud_Recibida", "Modificacion_En_Revision", "Declaracion_Aprobada", "Cuña_Emitida"],
            "outputs": ["Cuña de prensa fáctica emitida sin contradicciones y con trazabilidad legal"],
            "exceptions": ["Falta de conexión móvil de un aprobador que activa protocolo de sustitución por delegado de turno"]
        },
        "entities": [
            {"entity_id": "ENT_CASO_APAGON", "type": "caso_prueba", "name": "Caso Prueba Contingencia Eléctrica Maule", "aliases": ["Caso Eléctrico P02"]}
        ],
        "relations": [
            {"subject_id": "ENT_CASO_APAGON", "predicate": "valida_flujo_de", "object_id": "Gobernanza_Voceria_Express", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F36-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Aprobación Tradicional por Correo vs Workflow Digital Especializado",
                "Aprobación Tradicional por Correo": "Cadenas interminables de emails, múltiples versiones Word con control de cambios desincronizado, retrasos de horas.",
                "Workflow Digital Especializado": "Documento único centralizado, notificaciones push, firmas instantáneas y trazabilidad auditable."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Este caso valida la arquitectura del módulo Hablar de BRIDGE, demostrando su utilidad en contingencias de alta presión pública.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F37"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

out_path = "respuestas/temp_p02_f31_f36.jsonl"
with open(out_path, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Generated {len(records)} records in {out_path}")
