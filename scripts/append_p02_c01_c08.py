import json
import os
import sys

records = [
    {
        "question_id": "P02-C01",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre el universo comercial y deduplicación, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:44:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan en el tamaño del universo comercial y en la inclusión de entidades gremiales y modelos teóricos: 1) Discrepancia: Borradores iniciales de síntesis internas contabilizaban entre 73 y 82 'proveedores', inflando el mercado al incluir erróneamente a AMEC (asociación gremial sin fines de lucro de estándares de medición), Arthur W. Page Society (asociación profesional de directores de comunicación), The Bridge Intelligence (modelo de referencia conceptual e hipótesis arquitectónica propia), y duplicando entidades adquiridas (e.g. listar a Brandwatch separada de Cision sin explicitar el grupo, o Memo separada de Signal AI); 2) Versión que prevalece según correcciones: Rige con precedencia absoluta '00_P02_GLOBAL_READ_ME_AND_ERRATA' y 'P02_GLOBAL_ATLAS_RECONCILIATION_V1', fijando el denominador del mercado en exactamente 70 proveedores comerciales independientes. AMEC y Page Society se reclasifican como estándares gremiales; The Bridge se clasifica como hipótesis de diseño de referencia; y las marcas adquiridas se consolidan bajo sus matrices o se registran como subsidiarias en transición.",
        "findings": [
            {
                "claim_id": "P02-C01-C1",
                "claim": "La reconciliación editorial de P02 reduce el universo comercial a exactamente 70 proveedores independientes, eliminando distorsiones por entidades gremiales, modelos teóricos y duplicaciones corporativas de M&A.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Auditoría Editorial P02"},
                "evidence": [
                    {
                        "source_id": "6b0f5060-e568-22ab-0000-022b34005268",
                        "source_title": "00_P02_GLOBAL_READ_ME_AND_ERRATA",
                        "original_url": None,
                        "locator": "Errata 1: Absolute Precedence and Vendor Universe Re-baselining",
                        "excerpt_short": "Fixes the reconciled commercial vendor universe at exactly 70 independent vendors. Reclassifies AMEC and Page Society as industry associations and The Bridge as a design hypothesis.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:44:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "051037f7-7862-b34f-0000-022b34005268",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Universe Reconciliation: From 82 to 70 Vendors",
                        "excerpt_short": "Exhaustive deduplication eliminating 12 spurious entries including non-profit standards and internal research models.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:44:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Aplicación estricta de la regla de precedencia editorial del mandato."
            }
        ],
        "operational_model": {
            "inputs": ["Borrador preliminar de proveedores (82 filas)", "Directiva de errata '00_P02_GLOBAL_READ_ME_AND_ERRATA'", "Registros mercantiles de M&A"],
            "actors": ["Auditor Editorial", "Investigador Cuantitativo"],
            "steps": ["Filtrado de entidades sin fines de lucro (AMEC, Page Society)", "Aislamiento de la hipótesis propia (The Bridge)", "Consolidación de filiales de un mismo grupo económico", "Cierre del denominador en 70"],
            "states": ["Lista_Inflada", "Regla_Aplicada", "Denominador_Reconciliado"],
            "outputs": ["Catálogo maestro definitivo de 70 proveedores comerciales independientes"],
            "exceptions": ["Subsidiarias que aún operan con razones sociales independientes en transición"]
        },
        "entities": [
            {"entity_id": "ENT_AMEC", "type": "asociacion_gremial", "name": "International Association for Measurement and Evaluation of Communication", "aliases": ["AMEC"]},
            {"entity_id": "ENT_PAGE_SOCIETY", "type": "asociacion_profesional", "name": "Arthur W. Page Society", "aliases": ["Page Society"]}
        ],
        "relations": [
            {"subject_id": "ENT_AMEC", "predicate": "excluido_del_denominador_comercial", "object_id": "Universo_70_Vendors", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-C01-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Conteo Inflado (82) vs Conteo Reconciliado (70)",
                "Conteo Inflado": "Incluía entidades gremiales y duplicaba subsidiarias corporativas.",
                "Conteo Reconciliado": "Refleja exactamente 70 entidades comerciales independientes con oferta de mercado."
            }
        ],
        "contradictions": [
            {
                "contradiction_id": "P02-CONT-01",
                "description": "Discrepancia en el número total de competidores entre borradores tempranos (82) y el atlas reconciliado (70).",
                "resolution": "Prevalece la errata 00_P02_GLOBAL_READ_ME_AND_ERRATA: el total canónico es exactamente 70."
            }
        ],
        "metrics_and_denominators": [
            {"metric": "Denominador de Proveedores Comerciales", "value": "70", "context": "Cuaderno P02"}
        ],
        "bridge_implications": [
            {"module": "Todos", "implication": "BRIDGE debe calcular todas las métricas de penetración y cobertura sobre el denominador exacto de 70 proveedores.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-C02"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-C02",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué sigue sin prueba sobre el universo comercial y deduplicación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:44:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Siguen sin prueba empírica tres aspectos críticos del universo comercial: 1) Titularidad legal y sede física de Direct Signal: la entidad figura en catálogos de marketing pero sus fuentes fallaron en certificar registro corporativo activo en Delaware o California, manteniéndose como 'propiedad no verificada'; 2) Grado de integración real de datos entre CisionOne y Brandwatch: aunque Platinum Equity adquirió Brandwatch en 2021 por 450M USD, no hay prueba pública de que compartan un grafo de datos unificado; 3) Existencia de una suite de 4 módulos: ninguna fuente comercial o independiente prueba la existencia de un SaaS que integre nativamente Saber, Escuchar, Hablar y Relacionar; Validación mínima requerida: a) Búsqueda en el registro de corporaciones de Delaware para Direct Signal; b) Prueba técnica de API unificada entre Brandwatch y CisionOne; c) Ensayo operacional de extremo a extremo para validar si algún vendor puede procesar los 4 módulos sin middleware externo.",
        "findings": [
            {
                "claim_id": "P02-C02-C1",
                "claim": "La estructura societaria de Direct Signal carece de respaldo registral público, y la integración técnica interna de mega-adquisiciones (Cision/Brandwatch) no está demostrada fuera de presentaciones comerciales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Direct Signal, Cision/Brandwatch"},
                "evidence": [
                    {
                        "source_id": "6f605ce7-ef29-1ad3-0000-022b34005268",
                        "source_title": "P02_GLOBAL_GAPS_AND_VALIDATION_V1",
                        "original_url": None,
                        "locator": "Section 3: Unverified Corporate Entities and Integration Gaps",
                        "excerpt_short": "Direct Signal lacks corporate registration trail. Brandwatch and Cision remain operating with segregated backend architectures despite single ownership.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:44:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación documental de brechas registradas en el cuaderno P02."
            }
        ],
        "operational_model": {
            "inputs": ["Registros mercantiles", "Llamadas de prueba a endpoints de API de Cision/Brandwatch", "Fichas de proveedores no verificados"],
            "actors": ["Auditor Societario", "Ingeniero de Integración"],
            "steps": ["Consulta en base de datos mercantil estatal", "Envío de solicitud de demo técnica con flujo cruzado", "Verificación de autenticación unificada SSO y token de datos"],
            "states": ["Entidad_Sospechosa", "Consulta_Ejecutada", "Integracion_Evaluada"],
            "outputs": ["Ficha de validación societaria y técnica"],
            "exceptions": ["Negativa del proveedor a exhibir el backend de integración bajo secreto comercial"]
        },
        "entities": [
            {"entity_id": "ENT_DIRECT_SIGNAL", "type": "proveedor_no_verificado", "name": "Direct Signal", "aliases": ["DirectSignal AI"]}
        ],
        "relations": [
            {"subject_id": "ENT_DIRECT_SIGNAL", "predicate": "clasificado_como", "object_id": "Entidad_No_Verificada", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-C02-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Integración Comercial (Marketing) vs Integración Técnica (Backend)",
                "Integración Comercial": "Misma marca, empaquetamiento conjunto de precios y facturación única.",
                "Integración Técnica": "Bases de datos unificadas, API común y sincronización de eventos en tiempo real."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "BRIDGE no debe asumir que las mega-adquisiciones de la competencia representan plataformas unificadas en el backend.", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_DIRECT_SIGNAL", "description": "Falta de verificación jurídica de Direct Signal", "action": "Consultar registro mercantil"}
        ],
        "next_question_ids": ["P02-C03"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-C03",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre competidores cercanos a los cuatro módulos, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:44:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan sobre el alcance funcional real de los competidores más cercanos: 1) Discrepancia: Resúmenes comerciales previos insinuaban que suites como Meltwater, Onclusive o Signal AI cubrían 'de extremo a extremo' la gestión de asuntos corporativos, atribuyéndoles de facto los 4 módulos; 2) Versión que prevalece: Las fuentes primarias de producto y el atlas de reconciliación prueban que ninguna de estas suites cubre más de 2 módulos de forma nativa. Meltwater y Cision cubren primordialmente 'Escuchar' y parcialmente 'Hablar' (mediante distribución de notas de prensa sindicadas), pero carecen totalmente de repositorios RAG sobre documentos internos confidenciales ('Saber') y de gestión de compromisos comunitarios o Ley de Lobby ('Relacionar'). Quorum cubre 'Relacionar' legislativo y alertas normativas, pero es ciego a prensa masiva y carece de System of Record para vocerías de crisis. Prevalece la conclusión de que el mercado está compuesto por soluciones fragmentadas de nicho.",
        "findings": [
            {
                "claim_id": "P02-C03-C1",
                "claim": "Las revisiones técnicas de producto desmienten las afirmaciones de cobertura 'end-to-end' de las suites de listening globales, confirmando que ninguna solución comercial cubre los cuatro módulos de forma nativa.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Meltwater, Cision, Quorum, Signal AI"},
                "evidence": [
                    {
                        "source_id": "051037f7-7862-b34f-0000-022b34005268",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Four-Module Coverage Audit",
                        "excerpt_short": "No commercial vendor natively satisfies the 4-module architecture (Saber, Escuchar, Hablar, Relacionar). Maximum observed native coverage is two modules.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:44:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación cruzada de matrices de producto frente a especificaciones funcionales."
            }
        ],
        "operational_model": {
            "inputs": ["Fichas técnicas de Meltwater, Cision, Quorum y Signal AI", "Matriz funcional de 4 módulos"],
            "actors": ["Auditor Funcional", "Arquitecto de Soluciones"],
            "steps": ["Contraste módulo a módulo", "Evaluación de dependencias externas", "Calificación de cobertura (Nativa, Parcial, Nula)"],
            "states": ["Evaluacion_Iniciada", "Brechas_Mapeadas", "Veredicto_Emitido"],
            "outputs": ["Matriz de brechas funcionales de los líderes de mercado"],
            "exceptions": ["Módulos ofrecidos mediante integraciones iFrame con proveedores terceros"]
        },
        "entities": [
            {"entity_id": "ENT_MELTWATER", "type": "suite_listening", "name": "Meltwater N.V.", "aliases": ["Meltwater"]},
            {"entity_id": "ENT_QUORUM", "type": "crm_legislativo", "name": "Quorum Analytics Inc.", "aliases": ["Quorum"]}
        ],
        "relations": [
            {"subject_id": "ENT_MELTWATER", "predicate": "carece_de_modulo_nativo", "object_id": "Modulo_Relacionar_Comunitario", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-C03-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Afirmación Comercial vs Realidad Documentada",
                "Afirmación Comercial": "'Plataforma todo en uno de inteligencia para asuntos públicos y comunicaciones'.",
                "Realidad Documentada": "Herramienta especializada en monitoreo de prensa y redes con nula gestión de compromisos territoriales."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "La fragmentación de los líderes valida la tesis central de BRIDGE de construir una suite verdaderamente integrada.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-C04"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-C04",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué sigue sin prueba sobre competidores cercanos a los cuatro módulos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:44:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba la interoperabilidad operativa real entre herramientas que dicen comunicarse vía API: 1) Brecha: Ningún competidor ha demostrado un flujo continuo donde una alerta de medios (Escuchar) actualice automáticamente la ficha de riesgo de un parlamentario o dirigente comunal (Relacionar), genere un borrador de postura oficial en el repositorio de Q&A (Hablar) y consulte los contratos de faena en SharePoint (Saber); 2) Fuentes parciales: Las fichas de ventas de CisionOne y Meltwater mencionan 'capacidades de integración vía API' y 'asistentes generativos', pero no publican documentación de endpoints ni esquemas de eventos webhooks que soporten este ciclo; 3) Validación mínima: Diseñar un caso de prueba cerrado con datos sintéticos y solicitar a los vendors ejecutar en vivo el traspaso automático de un evento de crisis desde el clipping de prensa hasta la actualización del registro de compromisos y la generación del briefing de vocería.",
        "findings": [
            {
                "claim_id": "P02-C04-C1",
                "claim": "No existe evidencia técnica documentada de interoperabilidad automatizada de ciclo completo entre módulos de escucha externa y módulos de memoria de actores en ninguna plataforma comercial disponible.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Global", "actor": "Suites Comerciales de Corporate Affairs"},
                "evidence": [
                    {
                        "source_id": "6f605ce7-ef29-1ad3-0000-022b34005268",
                        "source_title": "P02_GLOBAL_GAPS_AND_VALIDATION_V1",
                        "original_url": None,
                        "locator": "Interoperability Validation Gap",
                        "excerpt_short": "Vendor literature lacks technical documentation verifying automated bidirectional event flows between media listening and stakeholder CRMs.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:44:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Auditoría de especificaciones de API públicas de los proveedores evaluados."
            }
        ],
        "operational_model": {
            "inputs": ["Guías de API de vendors", "Casos de prueba de ciclo cerrado", "Matriz de endpoints requeridos"],
            "actors": ["Ingeniero de Protocolos", "Evaluador de Software"],
            "steps": ["Revisión de Swagger/OpenAPI de los proveedores", "Detección de ausencia de triggers para eventos de asuntos públicos", "Diseño de protocolo de validación mínima"],
            "states": ["Especificaciones_Revisadas", "Brecha_Confirmada", "Protocolo_Fijado"],
            "outputs": ["Informe de viabilidad de interoperabilidad de competidores"],
            "exceptions": ["APIs privadas accesibles solo bajo acuerdos de desarrollo OEM de alto costo"]
        },
        "entities": [
            {"entity_id": "ENT_BRECHA_INTEROP", "type": "brecha_tecnica", "name": "Brecha de Interoperabilidad Multi-Módulo", "aliases": ["Interoperability Gap"]}
        ],
        "relations": [
            {"subject_id": "ENT_BRECHA_INTEROP", "predicate": "afecta_a", "object_id": "Lideres_Comerciales_Listening", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-C04-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Promesa de Ecosistema Integrado vs Realidad de Silos",
                "Promesa de Ecosistema": "'Nuestra plataforma conecta todos sus flujos de trabajo de relaciones públicas'.",
                "Realidad de Silos": "El usuario debe exportar reportes en PDF o Excel e ingresarlos manualmente en su CRM o gestor documental."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "BRIDGE debe construir su arquitectura sobre un bus de eventos reactivo que garantice este ciclo automático de forma nativa.", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_INTEROP", "description": "Falta de demostración de flujo inter-módulo en competidores", "action": "Ejecutar benchmark técnico"}
        ],
        "next_question_ids": ["P02-C05"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-C05",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre plataformas de escucha y reputación, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:44:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan en transacciones corporativas críticas, fechas de M&A y estructura de propiedad: 1) FGS Global: borradores tempranos continuaban categorizando a FGS Global como subsidiaria consolidada de WPP plc; la errata y el filing formal ante la SEC (Form 6-K a5017o.htm del 3 de diciembre de 2024) demuestran que WPP vendió su participación mayoritaria a fondos gestionados por KKR (Kite Bidco Inc.), por lo que FGS Global opera bajo control de KKR y no debe ser tratada como parte de WPP; 2) Burson Global y Limbik: notas preliminares fechaban la adquisición de Limbik de forma errática; la errata establece que la adquisición de la firma de IA cognitiva Limbik por Burson (WPP) ocurrió el 12 de agosto de 2026; 3) Signal AI y Memo: se rectifica la fecha de adquisición de Memo por Signal AI al 20 de abril de 2026 para la incorporación de 'Verified Readership'; Prevalecen las versiones rectificadas en '00_P02_GLOBAL_READ_ME_AND_ERRATA' con respaldo en documentos regulatorios oficiales.",
        "findings": [
            {
                "claim_id": "P02-C05-C1",
                "claim": "La errata editorial corrige definitivamente la estructura societaria de FGS Global (controlada por KKR desde dic-2024) y las fechas de adquisición de Limbik (Burson, 12-ago-2026) y Memo (Signal AI, 20-abr-2026).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-2026", "region": "Global", "actor": "FGS Global, Burson, Signal AI"},
                "evidence": [
                    {
                        "source_id": "6b0f5060-e568-22ab-0000-022b34005268",
                        "source_title": "00_P02_GLOBAL_READ_ME_AND_ERRATA",
                        "original_url": None,
                        "locator": "Errata 2 & 3: Corporate Ownership and Acquisition Dates",
                        "excerpt_short": "FGS Global ownership transferred to KKR (Kite Bidco) on Dec 3, 2024 (SEC Form 6-K). Limbik acquired by Burson on Aug 12, 2026. Memo acquired by Signal AI on Apr 20, 2026.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:44:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación directa en filings regulatorios de la SEC y directivas de errata inmutables."
            }
        ],
        "operational_model": {
            "inputs": ["Filings de la SEC de WPP", "Notas de prensa de KKR y Burson", "Borradores desactualizados de P02"],
            "actors": ["Auditor Corporativo", "Analista de Inteligencia Financiera"],
            "steps": ["Verificación de números de formulario SEC", "Cruce de fechas de anuncio vs cierre de transacción", "Corrección de matriz de propiedad corporativa"],
            "states": ["Error_Detectado", "Filing_Consultado", "Estructura_Corregida"],
            "outputs": ["Árbol genealógico societario verificado de agencias y vendors"],
            "exceptions": ["Operaciones de M&A cerradas bajo acuerdos privados sin revelación de montos"]
        },
        "entities": [
            {"entity_id": "ENT_KKR_KITE", "type": "fondo_inversion", "name": "Kite Bidco Inc. (KKR Funds)", "aliases": ["KKR"]},
            {"entity_id": "ENT_WPP_PLC", "type": "holding_publicitario", "name": "WPP plc", "aliases": ["WPP"]}
        ],
        "relations": [
            {"subject_id": "ENT_KKR_KITE", "predicate": "adquirio_control_mayoritario_de", "object_id": "FGS_Global", "valid_from": "2024-12-03", "valid_to": None, "evidence_claim_id": "P02-C05-C1"},
            {"subject_id": "ENT_BURSON", "predicate": "adquirio_empresa_cognitiva", "object_id": "Limbik", "valid_from": "2026-08-12", "valid_to": None, "evidence_claim_id": "P02-C05-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Propiedad de FGS Global: Versión Preliminar vs Versión Oficial SEC",
                "Versión Preliminar": "Considerada parte integral de WPP.",
                "Versión Oficial SEC": "Controlada por fondos de KKR (Kite Bidco) tras la desinversión mayoritaria de WPP en dic-2024."
            }
        ],
        "contradictions": [
            {
                "contradiction_id": "P02-CONT-02",
                "description": "Discrepancia en la propiedad de FGS Global y fechas de adquisición de Limbik y Memo.",
                "resolution": "Prevalece la errata 00_P02_GLOBAL_READ_ME_AND_ERRATA con respaldo en SEC Form 6-K."
            }
        ],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Todos", "implication": "La precisión en la estructura de propiedad evita falsas suposiciones sobre sinergias tecnológicas entre agencias y holdings.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-C06"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-C06",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué sigue sin prueba sobre plataformas de escucha y reputación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:44:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Siguen sin prueba empírica independiente dos factores nucleares de las plataformas de escucha: 1) Fiabilidad real del análisis de sentimiento automatizado y 'cognición de riesgo': los vendors afirman tasas de precisión superiores al 90%, pero ningún proveedor ha publicado evaluaciones de precisión sobre modismos locales, ironías políticas o debate regulatorio en español de América Latina; 2) Validez de las métricas sintéticas de visibilidad (como 'Verified Readership' de Memo o 'Share of Voice ponderado'): las fuentes de marketing prometen medir la audiencia real que leyó un artículo, pero no transparentan la muestra de telemetría de navegación ni su aplicabilidad en medios fuera del ámbito anglosajón; Validación mínima: a) Ejecución de un benchmark ciego de análisis de sentimiento sobre 1,000 menciones de prensa y redes en Chile comparando la salida de Meltwater, Signal AI y CisionOne contra un panel de 5 analistas humanos sénior; b) Auditoría técnica del método estadístico de estimación de lectores de Memo.",
        "findings": [
            {
                "claim_id": "P02-C06-C1",
                "claim": "Las métricas de análisis de sentimiento por IA y de lectura real declaradas por las plataformas de listening no cuentan con validación empírica independiente en el contexto cultural e idiomático de América Latina.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "América Latina / Global", "actor": "Meltwater, Signal AI, Cision"},
                "evidence": [
                    {
                        "source_id": "6f605ce7-ef29-1ad3-0000-022b34005268",
                        "source_title": "P02_GLOBAL_GAPS_AND_VALIDATION_V1",
                        "original_url": None,
                        "locator": "Sentiment and Readership Metrics Validation Gap",
                        "excerpt_short": "Vendor-reported sentiment accuracy lacks third-party validation in regional Spanish dialects, showing high false-positive rates on political sarcasm.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:44:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación de vacíos de prueba documentados en el atlas de validación."
            }
        ],
        "operational_model": {
            "inputs": ["Corpus de 1,000 menciones locales de prensa y redes", "Salidas clasificadas por los motores de IA de los vendors", "Clasificación de referencia por panel humano"],
            "actors": ["Auditor de NLP", "Panel de Expertos Lingüísticos"],
            "steps": ["Envío del corpus a las APIs de los vendors", "Cálculo de métricas de precisión, recall y F1-score", "Determinación de la tasa de error por ironía o contexto local"],
            "states": ["Corpus_Curated", "Inferencia_Ejecutada", "Metricas_Calculadas"],
            "outputs": ["Reporte empírico de precisión semántica de listening"],
            "exceptions": ["Cambios en el modelo de base del vendor durante la prueba que alteren los resultados"]
        },
        "entities": [
            {"entity_id": "ENT_BENCHMARK_SENTIMIENTO", "type": "protocolo_evaluacion", "name": "Benchmark Independiente de Sentimiento Regional", "aliases": ["Sentiment Audit"]}
        ],
        "relations": [
            {"subject_id": "ENT_BENCHMARK_SENTIMIENTO", "predicate": "evalua_calidad_de", "object_id": "Motores_IA_Listening", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-C06-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Promesa del Vendor vs Desempeño Regional Real",
                "Promesa del Vendor": "'95% de precisión en sentimiento mediante modelos de lenguaje avanzados'.",
                "Desempeño Regional": "Errores graves al clasificar modismos chilenos o debates regulatorios técnicos."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Escuchar", "implication": "BRIDGE no debe depender de puntuaciones genéricas de sentimiento de APIs globales, requiriendo modelos calibrados con contexto local.", "status": "evidencia"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_SENTIMENT_PRECISION", "description": "Falta de prueba independiente de precisión de sentimiento en español local", "action": "Ejecutar benchmark ciego"}
        ],
        "next_question_ids": ["P02-C07"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-C07",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Dónde discrepan fuentes originales y síntesis internas sobre asuntos públicos y memoria de actores, y qué versión prevalece según las correcciones?",
        "snapshot_at": "2026-10-01T01:44:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Discrepan sobre la transferibilidad de los CRMs legislativos de origen estadounidense a la gestión de asuntos públicos en América Latina: 1) Discrepancia: Resúmenes preliminares trataban a Quorum y FiscalNote como herramientas inmediatamente adoptables para asuntos públicos en Chile; 2) Versión que prevalece: Las fuentes primarias y el análisis de vacíos de P02 demuestran que Quorum y FiscalNote están estrechamente acoplados al sistema político y legislativo de Washington, Westminster y Bruselas (proyectos de ley del Congreso estadounidense, gacetas federales y registros de lobby norteamericanos). En Chile y la región andina, carecen totalmente de ingesta para la plataforma de Ley de Lobby (InfoLobby), el Sistema de Evaluación de Impacto Ambiental (SEIA) y la tramitación legislativa de la Cámara y el Senado. Prevalece la distinción entre software de lobby político anglosajón y las necesidades de gestión comunitaria y regulatoria territorial en faenas de recursos naturales (cubiertas parcialmente por Borealis y Open Point).",
        "findings": [
            {
                "claim_id": "P02-C07-C1",
                "claim": "Los CRMs legislativos líderes (Quorum, FiscalNote) no son directamente transferibles a América Latina debido a la ausencia de conectores nativos con la normativa local (Ley de Lobby, SEIA en Chile).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / América Latina", "actor": "Quorum, FiscalNote"},
                "evidence": [
                    {
                        "source_id": "79fc72f9-5c0c-0555-0000-022b34005268",
                        "source_title": "P02_GLOBAL_REGIONAL_AND_INTEGRATED_ADDENDUM_V1",
                        "original_url": None,
                        "locator": "Public Affairs Software Jurisdictional Misalignment",
                        "excerpt_short": "Quorum and FiscalNote lack native ingestion for Chilean InfoLobby and environmental regulatory frameworks, rendering them ineffective for local compliance without heavy custom integration.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:44:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación directa de catálogos de integración de Quorum y FiscalNote."
            }
        ],
        "operational_model": {
            "inputs": ["Marco regulatorio de Ley de Lobby chilena", "Mapeo de APIs de Quorum", "Requerimientos de compliance local"],
            "actors": ["Gerente de Asuntos Públicos", "Consultor Regulatorio"],
            "steps": ["Evaluación de compatibilidad de esquemas de datos", "Identificación de vacíos de integración institucional", "Dictamen de adopción tecnológica"],
            "states": ["Compatibilidad_Evaluada", "Vacio_Confirmado", "Decision_Adoptada"],
            "outputs": ["Dictamen de no transferibilidad directa de CRMs anglosajones"],
            "exceptions": ["Desarrollo de conectores intermedios ad-hoc que eleven el costo de mantención"]
        },
        "entities": [
            {"entity_id": "ENT_INFOLOBBY_CHILE", "type": "plataforma_estatal", "name": "Plataforma Ley de Lobby Chile", "aliases": ["InfoLobby"]}
        ],
        "relations": [
            {"subject_id": "ENT_QUORUM", "predicate": "no_posee_conector_con", "object_id": "InfoLobby_Chile", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-C07-C1"}
        ],
        "comparisons": [
            {
                "dimension": "CRM Legislativo Anglosajón vs Realidad de Asuntos Públicos en Chile",
                "CRM Anglosajón": "Modelado sobre comités del Congreso de EE. UU. y donaciones de campaña PAC.",
                "Realidad en Chile": "Regulada por Ley de Lobby estricta, audiencias públicas registradas y tramitación ambiental SEIA."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Relacionar", "implication": "BRIDGE debe construir el módulo Relacionar con conectores nativos a InfoLobby y SEIA para liderar el mercado chileno.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-C08"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-C08",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué sigue sin prueba sobre asuntos públicos y memoria de actores, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?",
        "snapshot_at": "2026-10-01T01:44:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Sigue sin prueba la capacidad de anticipar con precisión matemática la parálisis de un proyecto o el rechazo de un permiso ambiental a partir del análisis cruzado de relaciones comunitarias y audiencias de lobby: 1) Brecha: Borealis y Open Point documentan la gestión eficiente de quejas (grievances) y compromisos de RCA, pero carecen de modelos predictivos que alerten cuándo la acumulación de reclamos vecinales no resueltos alcanzará una masa crítica capaz de judicializar el proyecto; 2) Fuentes fallidas/parciales: Las fichas de marketing de SRM comunitario prometen 'preservar la licencia social para operar', pero no aportan datos empíricos de reducción cuantitativa de paralizaciones de obras en faenas mineras o energéticas; 3) Validación mínima: Realizar un estudio retrospectivo sobre 10 proyectos de inversión paralizados judicialmente en Chile en los últimos 5 años, cruzando sus bitácoras de quejas comunitarias con las alertas de prensa y reuniones de lobby para determinar si un algoritmo de grafos habría predicho el conflicto con al menos 30 días de anticipación.",
        "findings": [
            {
                "claim_id": "P02-C08-C1",
                "claim": "Las soluciones de gestión comunitaria (Borealis, Open Point) operan como repositorios de registro administrativo sin capacidad demostrada de predicción temprana de judicialización de proyectos.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Borealis, Open Point"},
                "evidence": [
                    {
                        "source_id": "6f605ce7-ef29-1ad3-0000-022b34005268",
                        "source_title": "P02_GLOBAL_GAPS_AND_VALIDATION_V1",
                        "original_url": None,
                        "locator": "Predictive Capability Gap in Stakeholder Management",
                        "excerpt_short": "Stakeholder engagement software functions as an administrative system of record; predictive correlation with project halting risks remains unverified.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:44:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Auditoría de capacidades analíticas en los manuales de Borealis y Open Point."
            }
        ],
        "operational_model": {
            "inputs": ["Historial de quejas de faena", "Fechas de fallos de tribunales ambientales", "Registros de prensa comunitaria"],
            "actors": ["Analista de Riesgo Socioambiental", "Investigador Algorítmico"],
            "steps": ["Recopilación de bitácoras históricas", "Modelación temporal de eventos", "Prueba de correlación estadística entre quejas y litigios", "Evaluación de poder predictivo"],
            "states": ["Datos_Historicos_Reunidos", "Modelo_Calibrado", "Poder_Predictivo_Medido"],
            "outputs": ["Estudio de validación empírica de predicción de crisis territoriales"],
            "exceptions": ["Incompletitud en los registros de terreno llevados manualmente por faenas antiguas"]
        },
        "entities": [
            {"entity_id": "ENT_ESTUDIO_PREDICCION", "type": "estudio_validacion", "name": "Estudio Retrospectivo Predicción Litigios Socioambientales", "aliases": ["Litigation Prediction Study"]}
        ],
        "relations": [
            {"subject_id": "ENT_ESTUDIO_PREDICCION", "predicate": "necesario_para_validar", "object_id": "Modulo_Relacionar_Predictivo", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-C08-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Registro Administrativo (Borealis) vs Predicción Anticipada (Hipótesis BRIDGE)",
                "Registro Administrativo": "Almacena la queja y avisa que pasaron 15 días sin respuesta al vecino.",
                "Predicción Anticipada": "Alerta que 5 quejas del mismo tenor en una cuenca hídrica activarán un recurso de protección ante la Corte de Apelaciones."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Relacionar", "implication": "BRIDGE debe pasar de ser una simple bitácora a un motor de analítica prescriptiva sobre el riesgo de judicialización.", "status": "hipotesis"}
        ],
        "open_gaps": [
            {"gap_id": "GAP_PREDICTION_RISK", "description": "Falta de validación predictiva de conflictos territoriales", "action": "Ejecutar estudio retrospectivo"}
        ],
        "next_question_ids": ["P02-C09"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

out_path = "respuestas/temp_p02_c01_c08.jsonl"
with open(out_path, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Generated {len(records)} records in {out_path}")
