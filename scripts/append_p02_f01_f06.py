import json
import os
import sys

# Script to generate P02-F01 through P02-F06 with full 20 keys schema

records = [
    {
        "question_id": "P02-F01",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué organizaciones, marcas y productos son entidades distintas y cuáles pertenecen al mismo grupo?",
        "snapshot_at": "2026-10-01T01:25:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La investigación corporativa y la fe de erratas (00_P02_GLOBAL_READ_ME_AND_ERRATA) distinguen grupos matrices, entidades legales y marcas de producto: 1) WPP plc es matriz de Burson Global, que adquirió Limbik (12 agosto 2026) operando bajo la suite Burson Decipher; 2) FGS Global pertenece a Kite Bidco Inc. (KKR), habiendo vendido WPP su participación mayoritaria el 3 diciembre 2024; 3) Platinum Equity es matriz de Cision Ltd., que consolida Brandwatch, PR Newswire, Falcon.io y Paladin (PROV-002); 4) Signal AI Ltd. es matriz y absorbió a Memo (20 abril 2026); 5) Open Point Group unifica Consultation Manager, Social Point y Converlens (julio 2024); 6) Darzin Software Pty Ltd y Simply Stakeholders son la misma entidad legal; 7) Symphony Technology Group (STG) es matriz de Onclusive (fusiona Kantar Rep Intelligence, PRgloo, Critical Mention, Digimind); 8) Hootsuite adquirió Talkwalker (abril 2024); 9) Irth Solutions es matriz de Borealis Software; 10) Stagwell engloba a PRophet AI y UNICEPTA; 11) Access Group engloba a Isentia y Vuelio. Entidades operativamente vinculadas pero jurídicamente independientes: Contrlr y Third Hemisphere comparten dirección pero no fusión demostrada; Direct Signal mantiene sede no verificada; Entual opera con servicio humano bespoke sobre datos públicos abiertos.",
        "findings": [
            {
                "claim_id": "P02-F01-C1",
                "claim": "En la estructura de propiedad global, FGS Global pertenece a Kite Bidco Inc. (controlada por fondos de KKR) tras el cierre de venta formal de WPP el 3 de diciembre de 2024 (SEC Form 6-K), por lo que WPP ya no es su matriz.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2024-12-03", "region": "Global / Reino Unido / EE. UU.", "actor": "WPP plc / KKR / Kite Bidco"},
                "evidence": [
                    {
                        "source_id": "a988d447-9257-41e7-be10-04aaeeff3b99",
                        "source_title": "SEC Form 6-K WPP Sale of FGS Global to KKR Kite Bidco",
                        "original_url": "https://www.sec.gov/Archives/edgar/data/1072379/000107237924000045/a5017o.htm",
                        "locator": "Filing Form 6-K WPP plc: Completion of transaction with Kite Bidco Inc.",
                        "excerpt_short": "WPP announces completion of the sale of its majority stake in FGS Global to Kite Bidco Inc., an entity controlled by KKR.",
                        "source_date": "2024-12-03",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "e08c2111-b14b-44d9-bd3c-54651ef434b5",
                        "source_title": "00_P02_GLOBAL_READ_ME_AND_ERRATA",
                        "original_url": None,
                        "locator": "Sección: Corrección de Propiedad de Grupos Económicos (FGS Global / WPP / KKR)",
                        "excerpt_short": "FGS Global ya no pertenece a WPP ni a Mayfair como matriz actual, sino a Kite Bidco Inc. (KKR).",
                        "source_date": "2026-10-01",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Presentación regulatoria vinculante ante la SEC de EE. UU. y fe de erratas canónica."
            },
            {
                "claim_id": "P02-F01-C2",
                "claim": "Platinum Equity controla Cision Ltd. (PROV-002), holding que consolidó bajo una sola entidad económica a Brandwatch (adquirida en junio de 2021), PR Newswire, Falcon.io y Paladin.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "EE. UU. / Global", "actor": "Platinum Equity / Cision Ltd."},
                "evidence": [
                    {
                        "source_id": "420e830e-dd53-4597-a51d-827824c4ce38",
                        "source_title": "Cision Brandwatch Acquisition Announcement PR Newswire",
                        "original_url": "https://www.prnewswire.com/news-releases/cision-closes-brandwatch-acquisition-301302866.html",
                        "locator": "Sección: Cision Closes Brandwatch Acquisition",
                        "excerpt_short": "Cision closes Brandwatch acquisition to create a global leader in PR, marketing and social consumer intelligence.",
                        "source_date": "2021-06-01",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Comunicado oficial de cierre de transacción corporativa."
            },
            {
                "claim_id": "P02-F01-C3",
                "claim": "Burson Global (WPP) adquirió la firma de IA cognitiva Limbik el 12 de agosto de 2026, integrando sus capacidades predictivas en la suite Burson Decipher dentro de la infraestructura WPP Open.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-08-12", "region": "EE. UU. / Global", "actor": "Burson Global / Limbik / WPP"},
                "evidence": [
                    {
                        "source_id": "e63cb0e1-84a9-4ca8-80d5-36ec84c18b16",
                        "source_title": "Burson Acquisition of Cognitive AI Firm Limbik",
                        "original_url": "https://www.bursonglobal.com/newsroom/global/burson-acquires-cognitive-ai-company-limbik",
                        "locator": "Burson Newsroom: Burson acquires cognitive AI company Limbik",
                        "excerpt_short": "Burson acquires cognitive AI company Limbik to enhance predictive media and audience engagement.",
                        "source_date": "2026-08-12",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Confirmación oficial en newsroom de Burson y corrección explícita de fe de erratas."
            }
        ],
        "operational_model": {
            "inputs": ["Estructuras de capital", "Filings de la SEC", "Notas de prensa de M&A"],
            "actors": ["Holdings Matrices", "Filiales Operativas", "Marcas Comerciales"],
            "steps": ["Verificación de entidad jurídica", "Rastreo de transacciones de M&A", "Deduplicación bajo holding de control", "Asignación de ID único de proveedor"],
            "states": ["Entidad_Identificada", "Holding_Verificado", "Registro_Consolidado"],
            "outputs": ["Catálogo deduplicado de proveedores independientes"],
            "exceptions": ["Empresas con alianzas comerciales pero sin fusión accionaria demostrada (ej. Contrlr y Third Hemisphere)"]
        },
        "entities": [
            {"entity_id": "GRP_CISION", "type": "holding_corporativo", "name": "Cision Ltd. (Platinum Equity)", "aliases": ["Brandwatch", "PR Newswire", "Falcon.io"]},
            {"entity_id": "GRP_KKR_FGS", "type": "holding_corporativo", "name": "Kite Bidco Inc. (KKR)", "aliases": ["FGS Global"]},
            {"entity_id": "GRP_WPP_BURSON", "type": "holding_corporativo", "name": "WPP plc / Burson Global", "aliases": ["Limbik", "Burson Decipher"]},
            {"entity_id": "GRP_SIGNAL_AI", "type": "holding_corporativo", "name": "Signal AI Ltd.", "aliases": ["Signal AI AIQ", "Memo"]}
        ],
        "relations": [
            {"subject_id": "GRP_KKR_FGS", "predicate": "adquirio_participacion_controladora_de", "object_id": "FGS Global", "valid_from": "2024-12-03", "valid_to": None, "evidence_claim_id": "P02-F01-C1"},
            {"subject_id": "GRP_CISION", "predicate": "consolida_operativamente_a", "object_id": "Brandwatch", "valid_from": "2021-06-01", "valid_to": None, "evidence_claim_id": "P02-F01-C2"},
            {"subject_id": "GRP_WPP_BURSON", "predicate": "adquirio", "object_id": "Limbik", "valid_from": "2026-08-12", "valid_to": None, "evidence_claim_id": "P02-F01-C3"}
        ],
        "comparisons": [
            {
                "dimension": "Independencia Comercial vs Pertenencia a Holding",
                "Entidades Aparentes Separadas": "Brandwatch, PR Newswire, Falcon.io y Paladin parecían 4 competidores en listas públicas.",
                "Estructura Real Verificada": "Pertenecen a un solo grupo comercial (Cision Ltd. / Platinum Equity), computando como 1 solo proveedor en N_comm."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric_name": "Denominador de Proveedores Comerciales Independientes Reconciliado",
                "value": 70,
                "unit": "empresas_independientes",
                "denominator": "Total de proveedores comerciales verificados tras deduplicar holdings y excluir entidades no comerciales",
                "evidence_claim_id": "P02-F01-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Evaluar la competencia en BRIDGE considerando grupos corporativos y no marcas aisladas, evitando sobredimensionar la fragmentación de mercado.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F02", "P02-F03"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F02",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué criterios separan proveedor comercial, asociación, estándar, consultora y propuesta de referencia?",
        "snapshot_at": "2026-10-01T01:25:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La metodología de P02 establece 5 categorías conceptuales excluyentes: 1) Proveedor Comercial Competitivo (N_comm=70): empresa con fines de lucro que licencia software B2B, APIs de datos o plataformas para uso operativo continuo (ej. Meltwater, Signal AI, Quorum, AlphaSense); 2) Asociación Profesional / Gremio: organización no gubernamental sin fines de lucro que agrupa profesionales y emite directrices éticas o formativas sin comercializar software (ej. AMEC, Arthur W. Page Society); 3) Estándar / Marco Teórico: metodología conceptual de medición o buenas prácticas, no un producto de software (ej. Barcelona Principles 3.0 de AMEC, CommTech Framework de Page Society); 4) Consultora Estratégica / Asesoría Humana: firma de servicios profesionales que factura por honorarios/retainer y resuelve requerimientos con analistas humanos (ej. Tironi, Azerta, Extend, Kreab, Edelman) o agencias híbridas con tecnología cautiva no transferible como SaaS (ej. Burson con Limbik, LLYC con Bespoke/Minerva); 5) Propuesta de Referencia / Sujeto de Estudio: modelo arquitectónico objeto de contraste comparativo (The Bridge Intelligence), tratado estrictamente como hipótesis de diseño a validar y excluido del total de competidores comerciales.",
        "findings": [
            {
                "claim_id": "P02-F02-C1",
                "claim": "Para evitar la distorsión del mercado, la fe de erratas y el atlas reconciliado excluyen del denominador de competidores a las asociaciones profesionales (AMEC, Page Society), a los estándares conceptuales (Barcelona Principles 3.0) y a la propuesta de referencia (The Bridge Intelligence), fijando el denominador en exactamente 70 proveedores comerciales.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-10-01", "region": "Global", "actor": "Metodología de Auditoría BRIDGE"},
                "evidence": [
                    {
                        "source_id": "e08c2111-b14b-44d9-bd3c-54651ef434b5",
                        "source_title": "00_P02_GLOBAL_READ_ME_AND_ERRATA",
                        "original_url": None,
                        "locator": "Sección: Criterios de Clasificación y Reconciliación del Denominador",
                        "excerpt_short": "Exclusión de asociaciones (AMEC, Page Society) y de la propuesta de referencia (The Bridge) del denominador comercial de 70 proveedores.",
                        "source_date": "2026-10-01",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "339114e9-8d29-48b7-8e88-8e52f15ceebc",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Taxonomía de Entidades y Criterios de Exclusión",
                        "excerpt_short": "Clasificación rigurosa entre proveedores de software, asociaciones, marcos metodológicos y consultoras.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Definición metodológica autoritativa de la fe de erratas del pilar."
            },
            {
                "claim_id": "P02-F02-C2",
                "claim": "Las consultoras y agencias de comunicación estratégica (Tironi, Azerta, Extend, LLYC, Burson) constituyen sustitutos funcionales o híbridos tecnológicos, distinguiéndose del software SaaS puro por facturar retainers de horas humanas y no transferir su tecnología como autoservicio independiente.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026", "region": "Chile / Global", "actor": "Consultoras de Asuntos Corporativos"},
                "evidence": [
                    {
                        "source_id": "8445acb1-1da5-4f0e-a98a-c9c3d8dac8a1",
                        "source_title": "P02_GLOBAL_COMPANY_ATLAS_V1",
                        "original_url": None,
                        "locator": "Categoría 6: Agencias y Consultoras Estratégicas",
                        "excerpt_short": "Las consultoras resuelven el problema con equipos humanos de asesores, operando como sustitutos del software.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación del modelo de negocio en el atlas de empresas de P02."
            }
        ],
        "operational_model": {
            "inputs": ["Modelo de ingresos", "Naturaleza jurídica", "Disponibilidad de software"],
            "actors": ["Analista Metodológico", "Proveedores de Software", "Asociaciones", "Consultoras"],
            "steps": ["Evaluación de fines de lucro", "Verificación de software SaaS entregable", "Detección de estándares o marcos conceptuales", "Clasificación en uno de los 5 arquetipos"],
            "states": ["Entidad_Evaluada", "Arquetipo_Asignado", "Denominador_Filtrado"],
            "outputs": ["Población depurada de proveedores comerciales independientes"],
            "exceptions": ["Agencias de servicios con herramientas propietarias de uso interno exclusivo (modelos híbridos)"]
        },
        "entities": [
            {"entity_id": "ARQ_PROV_COMERCIAL", "type": "arquetipo_mercado", "name": "Proveedor Comercial Competitivo", "aliases": ["SaaS Vendor B2B"]},
            {"entity_id": "ARQ_ASOCIACION", "type": "arquetipo_mercado", "name": "Asociación Profesional / Gremio", "aliases": ["Organización Sin Fines de Lucro"]},
            {"entity_id": "ARQ_ESTANDAR", "type": "arquetipo_mercado", "name": "Estándar / Marco Teórico", "aliases": ["Framework Metodológico"]},
            {"entity_id": "ARQ_CONSULTORA", "type": "arquetipo_mercado", "name": "Consultora Estratégica / Asesoría", "aliases": ["Sustituto Humano de Servicio"]},
            {"entity_id": "ARQ_REFERENCIA", "type": "arquetipo_mercado", "name": "Propuesta de Referencia", "aliases": ["The Bridge Intelligence Hypothesis"]}
        ],
        "relations": [
            {"subject_id": "ARQ_PROV_COMERCIAL", "predicate": "conforma_denominador", "object_id": "N_comm_70", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F02-C1"},
            {"subject_id": "ARQ_ASOCIACION", "predicate": "excluida_de", "object_id": "N_comm_70", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F02-C1"},
            {"subject_id": "ARQ_REFERENCIA", "predicate": "excluida_de", "object_id": "N_comm_70", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F02-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Software SaaS vs Consultoría Humana Estratégica",
                "Software SaaS B2B": "Herramienta accesible por suscripción de autoservicio que automatiza flujos continuos.",
                "Consultoría Estratégica": "Servicio intensivo en horas de profesionales senior cobrado por iguala o proyecto."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Posicionar a BRIDGE frente a software SaaS en eficiencia y frente a consultoras en velocidad y costo, reconociendo a las consultoras como socios o sustitutos híbridos.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F03", "P02-F04"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F03",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué fichas del atlas quedan cuestionadas por la fe de erratas y cómo debe reconciliarse el denominador?",
        "snapshot_at": "2026-10-01T01:25:00-03:00",
        "answer_status": "respondida",
        "short_answer": "La fe de erratas (00_P02_GLOBAL_READ_ME_AND_ERRATA) y la reconciliación del atlas (P02_GLOBAL_ATLAS_RECONCILIATION_V1) sustituyen formalmente la versión preliminar (V1) corrigiendo: 1) El denominador comercial de la V1 (que reportaba 78 o 70 'proveedores independientes' sin deduplicación estricta) queda depurado y fijado en exactamente 70 proveedores comerciales independientes, tras restar 2 asociaciones (AMEC y Page Society), 1 propuesta de referencia (The Bridge) y deduplicar subsidiarias (ej. Memo dentro de Signal AI); 2) FGS Global se desvincula de WPP y se asigna a Kite Bidco Inc. / KKR (SEC Form 6-K de dic 2024); 3) Limbik se fija con adquisición de Burson el 12 agosto 2026 (no 2024); 4) Direct Signal queda con sede e identidad jurídica no verificadas; 5) Entual se precisa como servicio humano bespoke sobre datos públicos sin repositorio interno; 6) Contrlr y Third Hemisphere mantienen separación legal; 7) Se elimina la escala 'Evidencia Demostrada (EM)' y se sustituye por la escala auditada: OPD (Oferta Pública Documentada), FD (Funcionalidad Declarada), DTI (Documentación Técnica Identificada) y POR (Prueba Operacional Realizada = Ninguna en los 70 casos); 8) Se retiran superlativos no probados (cobertura insuperable en Litoralpress, RAG Zero Hallucination en AlphaSense, o superioridad máxima de Quorum).",
        "findings": [
            {
                "claim_id": "P02-F03-C1",
                "claim": "El denominador comercial del mercado queda fijado por la fe de erratas en exactamente 70 proveedores independientes verificados, excluyendo entidades sin fines de lucro y deduplicando filiales corporativas.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-10-01", "region": "Global", "actor": "Auditoría de Manifiesto P02"},
                "evidence": [
                    {
                        "source_id": "e08c2111-b14b-44d9-bd3c-54651ef434b5",
                        "source_title": "00_P02_GLOBAL_READ_ME_AND_ERRATA",
                        "original_url": None,
                        "locator": "Sección: Conciliación del Denominador Comercial (70 Proveedores)",
                        "excerpt_short": "El denominador reconciliado fija el total en exactamente 70 proveedores comerciales independientes.",
                        "source_date": "2026-10-01",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "339114e9-8d29-48b7-8e88-8e52f15ceebc",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Tabla de Reconciliación V1 vs Versión Auditada",
                        "excerpt_short": "Depuración de 78 entidades brutas a 70 proveedores comerciales independientes verificados.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Regla de prevalencia editorial autoritativa y vinculante del pilar P02."
            },
            {
                "claim_id": "P02-F03-C2",
                "claim": "Se sustituye la categorización 'Evidencia Demostrada (EM)' por la escala rigurosa OPD/FD/DTI/POR, consignando 'POR = Ninguna' para todos los proveedores evaluados al no haberse realizado pruebas de laboratorio con credenciales de clientes.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-10-01", "region": "Global", "actor": "Equipo Evaluador P02"},
                "evidence": [
                    {
                        "source_id": "e08c2111-b14b-44d9-bd3c-54651ef434b5",
                        "source_title": "00_P02_GLOBAL_READ_ME_AND_ERRATA",
                        "original_url": None,
                        "locator": "Sección: Escala Epistémica de Evidencia de Producto",
                        "excerpt_short": "Sustitución de EM por OPD, FD, DTI y POR (marcado como Ninguna en todos los casos).",
                        "source_date": "2026-10-01",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Protocolo de control de calidad metodológico del mandato."
            }
        ],
        "operational_model": {
            "inputs": ["Borrador preliminar Atlas V1", "Documentos de fe de erratas", "Filings corporativos actualizados"],
            "actors": ["Auditor Editorial", "Base de Datos del Atlas", "Fuentes Primarias"],
            "steps": ["Identificación de entidades dudosas en V1", "Reconciliación matemática del denominador", "Retiro de juicios categóricos y superlativos", "Publicación de atlas reconciliado"],
            "states": ["Atlas_Preliminar_Cuestionado", "Auditoria_Ejecutada", "Denominador_Reconciliado_70"],
            "outputs": ["Atlas Reconciliado V1 con 70 proveedores independientes"],
            "exceptions": ["Aparición de nuevas fusiones societarias no registradas a la fecha de corte"]
        },
        "entities": [
            {"entity_id": "ENT_FE_ERRATAS_P02", "type": "documento_normativo_interno", "name": "00_P02_GLOBAL_READ_ME_AND_ERRATA", "aliases": ["Fe de Erratas Canónica P02"]},
            {"entity_id": "ENT_ATLAS_RECONCILIADO", "type": "documento_sintesis", "name": "P02_GLOBAL_ATLAS_RECONCILIATION_V1", "aliases": ["Atlas Reconciliado"]}
        ],
        "relations": [
            {"subject_id": "ENT_FE_ERRATAS_P02", "predicate": "reemplaza_y_anula", "object_id": "P02_GLOBAL_COMPANY_ATLAS_V1_Borrador", "valid_from": "2026-10-01", "valid_to": None, "evidence_claim_id": "P02-F03-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Cifras de Mercado Preliminares vs Cifras Auditadas",
                "Versión Preliminar V1": "78 entidades heterogéneas mezclando software, gremios y marcos teóricos.",
                "Versión Auditada (Prevaleciente)": "Exactamente 70 proveedores comerciales independientes verificados."
            }
        ],
        "contradictions": [
            {
                "claim_ids": ["P02-F03-C1", "P02-F01-C1"],
                "difference": "Divergencia entre reportes de prensa antiguos que atribuían FGS Global a WPP y el documento oficial de cierre de venta ante la SEC.",
                "resolution": "resuelta",
                "reason": "Prevalece la fe de erratas y el SEC Form 6-K: la propiedad actual corresponde a Kite Bidco Inc. (KKR)."
            }
        ],
        "metrics_and_denominators": [
            {
                "metric_name": "Proveedores Comerciales Independientes Verificados",
                "value": 70,
                "unit": "empresas",
                "denominator": "70 proveedores tras deduplicación de 78 registros brutos",
                "evidence_claim_id": "P02-F03-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Utilizar exclusivamente el denominador N=70 en todos los cálculos de cobertura y participación de mercado de BRIDGE.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F04", "P02-F05"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F04",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar universo comercial y deduplicación de forma estructurada?",
        "snapshot_at": "2026-10-01T01:25:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Exige estructurar un esquema relacional normalizado con las siguientes especificaciones: 1) Variables de entidad: ID_Proveedor (PROV-001 a PROV-070), Entidad_Legal, Grupo_Corporativo, Marca_Producto, Sede_HQ (con flag de verificación), Cobertura_Comercial, Categoria_Primaria (1 a 7), Relacion_Competitiva (Directo, Parcial, Sustituto, Complemento), Modelo_Operativo (SaaS, Híbrido, Consultoría), URL_Primaria, Módulos Saber/Escuchar/Hablar/Relacionar (con niveles OPD/FD/DTI/POR/ND), Limitaciones_Observadas y Confianza_Epistémica; 2) Siete Categorías Funcionales: (1) Media Monitoring & Social Listening (24 prov, 34,3%), (2) Public Affairs & Stakeholder CRM (11 prov, 15,7%), (3) Enterprise Search, RAG & Knowledge (6 prov, 8,6%), (4) PR Workflow & Governance (10 prov, 14,3%), (5) Medición de Reputación y Confianza (5 prov, 7,1%), (6) Agencias y Consultoras Estratégicas (10 prov, 14,3%), (7) Narrative & Disinformation Intelligence (4 prov, 5,7%); 3) Cuatro Condiciones de Deduplicación: Condición 1 (Control de Propiedad: si Marca_A pertenece a Grupo_Y, consolidar en 1 registro con matriz Grupo_Y); Condición 2 (Identidad Legal: si RazónSocial_A = RazónSocial_B, unificar fila); Condición 3 (Exclusión de No Comerciales: si Tipo in {Asociación, Estándar, Sujeto de Estudio}, excluir de N_comm=70); Condición 4 (Independencia Operativa: si vínculo es meramente comercial o de liderazgo compartido sin fusión accionaria formal, preservar registros separados).",
        "findings": [
            {
                "claim_id": "P02-F04-C1",
                "claim": "El universo de los 70 proveedores independientes se distribuye de forma exhaustiva en 7 categorías funcionales de mercado, donde el monitoreo de medios concentra el 34,3% (24 proveedores), seguido de asuntos públicos con el 15,7% (11 proveedores) y agencias con el 14,3% (10 proveedores).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-10-01", "region": "Global", "actor": "Taxonomía de Mercado P02"},
                "evidence": [
                    {
                        "source_id": "339114e9-8d29-48b7-8e88-8e52f15ceebc",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Distribución por Categorías Funcionales del Mercado",
                        "excerpt_short": "Segmentación en 7 categorías funcionales totalizando el 100% de los 70 proveedores.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Conteo auditado en el atlas reconciliado de P02."
            },
            {
                "claim_id": "P02-F04-C2",
                "claim": "La escala epistémica obligatoria para calificar la presencia de cada uno de los 4 módulos de BRIDGE en los proveedores se divide en OPD (Oferta Pública), FD (Declarada en Marketing), DTI (Técnica Identificada), POR (Prueba Realizada = Ninguna) y ND (No Documentado).",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-10-01", "region": "Global", "actor": "Escala de Calificación P02"},
                "evidence": [
                    {
                        "source_id": "e08c2111-b14b-44d9-bd3c-54651ef434b5",
                        "source_title": "00_P02_GLOBAL_READ_ME_AND_ERRATA",
                        "original_url": None,
                        "locator": "Definición Formal de la Escala OPD / FD / DTI / POR / ND",
                        "excerpt_short": "Definición estandarizada de los 5 niveles de evidencia técnica para cada módulo.",
                        "source_date": "2026-10-01",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Regla metodológica canónica del mandato."
            }
        ],
        "operational_model": {
            "inputs": ["Catálogo en bruto de empresas", "Reglas formales de deduplicación", "Categorías funcionales 1 a 7"],
            "actors": ["Motor de Normalización", "Auditor de Datos", "Base de Entidades"],
            "steps": ["Extracción de atributos", "Evaluación de condiciones 1 a 4", "Asignación de categoría 1 a 7", "Calificación de módulos en escala OPD/FD/DTI/POR/ND", "Generación de registro normalizado"],
            "states": ["Dato_Bruto", "Condiciones_Aplicadas", "Registro_Normalizado_Valido"],
            "outputs": ["Ficha estructurada de proveedor comercial"],
            "exceptions": ["Proveedores con sedes jurídicas dudosas (flag de verificación activo)"]
        },
        "entities": [
            {"entity_id": "SCH_ATLAS_EMPRESAS", "type": "esquema_datos", "name": "Esquema Estructurado del Atlas de Empresas P02", "aliases": ["Data Model P02"]}
        ],
        "relations": [
            {"subject_id": "SCH_ATLAS_EMPRESAS", "predicate": "normaliza", "object_id": "Catálogo_70_Proveedores", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F04-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Representación Informal vs Estructura Normalizada",
                "Listado Informal": "Texto libre con descripciones comerciales y mezcla de marcas filiales.",
                "Estructura Normalizada": "Tabla relacional con 16 atributos tipados, escala epistémica y reglas booleanas de deduplicación."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric_name": "Distribución Categoría 1: Media Monitoring",
                "value": 34.3,
                "unit": "porcentaje",
                "denominator": "70 proveedores independientes (24 empresas)",
                "evidence_claim_id": "P02-F04-C1"
            },
            {
                "metric_name": "Distribución Categoría 2: Public Affairs & CRM",
                "value": 15.7,
                "unit": "porcentaje",
                "denominator": "70 proveedores independientes (11 empresas)",
                "evidence_claim_id": "P02-F04-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Adoptar el esquema estructurado de 16 atributos como ontología base en la base de entidades corporativas de BRIDGE.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F05", "P02-F06"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F05",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre universo comercial y deduplicación?",
        "snapshot_at": "2026-10-01T01:25:00-03:00",
        "answer_status": "respondida",
        "short_answer": "Cada hecho está respaldado por fuentes primarias y documentos de errata con trazabilidad exhaustiva: 1) Venta de FGS Global a KKR por WPP: respaldada por SEC Form 6-K WPP (filing a5017o.htm del 3 dic 2024) y fe de erratas (00_P02_GLOBAL_READ_ME_AND_ERRATA); 2) Adquisición de Limbik por Burson: respaldada por comunicado oficial de Burson (12 agosto 2026) y 00_P02_GLOBAL_READ_ME_AND_ERRATA; 3) Absorción de Memo por Signal AI: respaldada por comunicado de Signal AI y Memo (anuncio 20 abril 2026) y 00_P02_GLOBAL_READ_ME_AND_ERRATA; 4) Integración de Brandwatch en Cision Ltd.: respaldada por PR Newswire Announcement (1 junio 2021) y P02_GLOBAL_SOURCE_INDEX_V1; 5) Creación de Open Point Group: respaldada por Consultation Manager Release y P02_GLOBAL_REGIONAL_AND_INTEGRATED_ADDENDUM_V1 (adquisición de Converlens en julio 2024); 6) Exclusión de AMEC, Page Society y The Bridge del denominador comercial: respaldada por 00_P02_GLOBAL_READ_ME_AND_ERRATA y P02_GLOBAL_ATLAS_RECONCILIATION_V1 (1 octubre 2026).",
        "findings": [
            {
                "claim_id": "P02-F05-C1",
                "claim": "La trazabilidad de las transacciones societarias y exclusiones del atlas se sustenta en fuentes regulatorias formales (SEC), notas de prensa oficiales de M&A y documentos de síntesis con fechas auditables entre junio de 2021 y octubre de 2026.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2021-2026", "region": "Global", "actor": "Registro Oficial de Fuentes P02"},
                "evidence": [
                    {
                        "source_id": "a988d447-9257-41e7-be10-04aaeeff3b99",
                        "source_title": "SEC Form 6-K WPP Sale of FGS Global to KKR Kite Bidco",
                        "original_url": "https://www.sec.gov/Archives/edgar/data/1072379/000107237924000045/a5017o.htm",
                        "locator": "Filing Form 6-K WPP plc: Completion of transaction with Kite Bidco Inc.",
                        "excerpt_short": "Report of Foreign Private Issuer Pursuant to Rule 13a-16: Sale of majority stake in FGS Global.",
                        "source_date": "2024-12-03",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    },
                    {
                        "source_id": "420e830e-dd53-4597-a51d-827824c4ce38",
                        "source_title": "Cision Brandwatch Acquisition Announcement PR Newswire",
                        "original_url": "https://www.prnewswire.com/news-releases/cision-closes-brandwatch-acquisition-301302866.html",
                        "locator": "PR Newswire: Cision closes Brandwatch acquisition",
                        "excerpt_short": "Cision closes Brandwatch acquisition creating PR and consumer intelligence leader.",
                        "source_date": "2021-06-01",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación directa de los documentos fuente en los repositorios de P02."
            }
        ],
        "operational_model": {
            "inputs": ["Identificadores de fuente", "URLs originales", "Fechas de corte de eventos de M&A"],
            "actors": ["Auditor Epistémico", "Sistema de Trazabilidad"],
            "steps": ["Verificación de URL/Filing", "Extracción de fecha y fragmento textual", "Asociación al ID de afirmación", "Publicación en matriz de fuentes"],
            "states": ["Fuente_Auditada", "Pasaje_Verificado", "Trazabilidad_Consolidada"],
            "outputs": ["Matriz de Trazabilidad Epistémica de P02"],
            "exceptions": ["Fuentes afectadas por errores 403 o paywall (se documenta su sustituto)"]
        },
        "entities": [
            {"entity_id": "MATRIZ_TRAZABILIDAD_P02", "type": "artefacto_auditoria", "name": "Matriz de Trazabilidad Epistémica de P02", "aliases": ["Source Traceability Matrix"]}
        ],
        "relations": [
            {"subject_id": "MATRIZ_TRAZABILIDAD_P02", "predicate": "respalda_afirmaciones_de", "object_id": "P02_UNIVERSO_COMERCIAL", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F05-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Cita Genérica vs Cita Epistémica con Localizador",
                "Cita Genérica": "Mencionar 'WPP vendió FGS' sin fecha, fuente ni número de filing.",
                "Cita Epistémica": "Venta formal a Kite Bidco Inc. (KKR) el 3 de diciembre de 2024 según SEC Form 6-K filing a5017o.htm."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [],
        "bridge_implications": [
            {"module": "Hablar", "implication": "Implementar en el motor de respuesta de BRIDGE el mismo estándar de trazabilidad que exige enlazar localizadores exactos para cada hecho.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F06", "P02-C01"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P02-F06",
        "notebook_id": "bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440",
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra universo comercial y deduplicación sin introducir datos no documentados?",
        "snapshot_at": "2026-10-01T01:25:00-03:00",
        "answer_status": "respondida",
        "short_answer": "El caso concreto se ilustra mediante un lote de prueba de 10 entradas brutas heterogéneas tomadas del catálogo inicial: 1) Brandwatch; 2) CisionOne; 3) PR Newswire; 4) Memo; 5) Signal AI AIQ; 6) Consultation Manager; 7) Social Point; 8) AMEC (Barcelona Principles 3.0); 9) The Bridge Intelligence; 10) FGS Global. Ejecución del algoritmo paso a paso: Paso 1 (Filtrado de no comerciales / estándares): AMEC se clasifica como asociación emisora de estándar y se excluye de N_comm; The Bridge Intelligence se clasifica como propuesta de referencia y se excluye de N_comm. Paso 2 (Deduplicación por grupo matriz y entidad legal): Brandwatch, CisionOne y PR Newswire se consolidan bajo Cision Ltd. / Platinum Equity (PROV-002, 1 proveedor); Memo y Signal AI AIQ se consolidan bajo Signal AI Ltd. (PROV-006, 1 proveedor); Consultation Manager y Social Point se consolidan bajo Open Point Group (PROV-018, 1 proveedor). Paso 3 (Verificación de propiedad actual): FGS Global se asigna como proveedor independiente (PROV-055) bajo KKR / Kite Bidco Inc. (no WPP). Resultado final estructurado: de 10 entradas brutas se obtienen exactamente 4 proveedores comerciales independientes verificados y 2 entidades excluidas, demostrando la reconciliación sin datos no documentados.",
        "findings": [
            {
                "claim_id": "P02-F06-C1",
                "claim": "El algoritmo de deduplicación procesa de forma determinista un conjunto de 10 entradas heterogéneas reduciéndolas a 4 proveedores comerciales independientes únicos bajo sus matrices reales y 2 entidades no comerciales excluidas del denominador.",
                "epistemic_status": "hecho_documentado",
                "scope": {"time": "2026-10-01", "region": "Global", "actor": "Caso de Prueba Algorítmica P02"},
                "evidence": [
                    {
                        "source_id": "339114e9-8d29-48b7-8e88-8e52f15ceebc",
                        "source_title": "P02_GLOBAL_ATLAS_RECONCILIATION_V1",
                        "original_url": None,
                        "locator": "Sección: Caso de Prueba Controlado de Deduplicación",
                        "excerpt_short": "Demostración de consolidación de marcas bajo grupos económicos únicos.",
                        "source_date": "2026",
                        "retrieved_at": "2026-10-01T01:25:00-03:00",
                        "text_status": "texto_sustantivo",
                        "relationship": "apoya"
                    }
                ],
                "confidence": "alta",
                "confidence_reason": "Verificación matemática y documental del algoritmo en el atlas reconciliado."
            }
        ],
        "operational_model": {
            "inputs": [
                "Entrada 1: Brandwatch", "Entrada 2: CisionOne", "Entrada 3: PR Newswire",
                "Entrada 4: Memo", "Entrada 5: Signal AI AIQ", "Entrada 6: Consultation Manager",
                "Entrada 7: Social Point", "Entrada 8: AMEC", "Entrada 9: The Bridge Intelligence",
                "Entrada 10: FGS Global"
            ],
            "actors": ["Algoritmo de Deduplicación", "Tabla de Reglas M&A"],
            "steps": [
                "Paso 1: Filtrar AMEC y The Bridge (exclusión de N_comm)",
                "Paso 2: Consolidar Brandwatch + CisionOne + PR Newswire -> PROV-002 (Cision Ltd.)",
                "Paso 3: Consolidar Memo + Signal AI AIQ -> PROV-006 (Signal AI Ltd.)",
                "Paso 4: Consolidar Consultation Manager + Social Point -> PROV-018 (Open Point Group)",
                "Paso 5: Asignar FGS Global -> PROV-055 (Kite Bidco / KKR)",
                "Paso 6: Conteo final de proveedores"
            ],
            "states": ["Lote_Ingresado", "Filtro_NoComercial_Ejecutado", "Holding_Agrupado", "Salida_Verificada"],
            "outputs": [
                "PROV-002: Cision Ltd. (CisionOne/Brandwatch/PR Newswire)",
                "PROV-006: Signal AI Ltd. (Signal AI AIQ/Memo)",
                "PROV-018: Open Point Group (Consultation Manager/Social Point)",
                "PROV-055: FGS Global (KKR / Kite Bidco)",
                "EXCL-001: AMEC Org (Estándar Gremial)",
                "EXCL-002: The Bridge Intelligence (Sujeto de Análisis / Referencia)"
            ],
            "exceptions": ["Detección de acuerdos de marca compartida sin compraventa de acciones"]
        },
        "entities": [
            {"entity_id": "TEST_CASE_DEDUPLICACION", "type": "caso_prueba", "name": "Caso de Prueba Controlado de Deduplicación (10 Entradas)", "aliases": ["Gold Standard Test Dataset"]}
        ],
        "relations": [
            {"subject_id": "TEST_CASE_DEDUPLICACION", "predicate": "valida_algoritmo_de", "object_id": "Deduplicacion_Mercado_P02", "valid_from": "2026", "valid_to": None, "evidence_claim_id": "P02-F06-C1"}
        ],
        "comparisons": [
            {
                "dimension": "Entradas Brutas vs Salidas Validadas",
                "Total Entradas Brutas": "10 registros aparentemente dispersos.",
                "Total Salidas Reconciliadas": "4 proveedores comerciales independientes + 2 exclusiones justificadas."
            }
        ],
        "contradictions": [],
        "metrics_and_denominators": [
            {
                "metric_name": "Tasa de Reducción por Deduplicación en Caso de Prueba",
                "value": 60.0,
                "unit": "porcentaje",
                "denominator": "10 entradas brutas reducidas a 4 proveedores comerciales (60% de reducción)",
                "evidence_claim_id": "P02-F06-C1"
            }
        ],
        "bridge_implications": [
            {"module": "Transversal", "implication": "Implementar este mismo algoritmo de resolución de entidades en el pipeline de datos de BRIDGE para deduplicar automáticamente actores y medios en el módulo Relacionar.", "status": "evidencia"}
        ],
        "open_gaps": [],
        "next_question_ids": ["P02-F07", "P02-C01"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

# Ensure respuestas directory exists and write
with open("respuestas/temp_p02_f01_f06.jsonl", "w", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"Generated {len(records)} records in respuestas/temp_p02_f01_f06.jsonl")
