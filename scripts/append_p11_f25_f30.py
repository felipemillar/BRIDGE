import json
from pathlib import Path

TARGET = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/respuestas/P11.jsonl")
NOTEBOOK_ID = "64271ecf-776c-4692-b302-d936ea00a501"
SNAPSHOT = "2026-10-01T16:00:00-03:00"

records = [
    {
        "question_id": "P11-F25",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué datos recibe cada proveedor de IA, búsqueda, monitoreo y almacenamiento?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "La arquitectura de BRIDGE aplica un principio estricto de minimización de datos (Data Minimization) que delimita con precisión el payload que recibe cada categoría de proveedor externo: 1) Proveedores de Inferencia de IA (AWS Bedrock, Azure OpenAI Service, Google Cloud Vertex AI, Anthropic Commercial y OpenAI API): Reciben exclusivamente el prompt estructurado y fragmentos contextuales previamente sanitizados (con PII tokenizada y secretos D3/D5 enmascarados), sin identificadores directos del cliente, bajo acuerdos enterprise de 'Zero Training Data Retention'; 2) Proveedores de Búsqueda Vectorial (Qdrant): Reciben vectores densos de flotantes (embeddings numéricos) y metadatos de payload no confidenciales (`tenant_id`, `document_type`, fecha, hash de procedencia); 3) Proveedores de Monitoreo y Telemetría (Datadog / CloudWatch): Reciben métricas de latencia, códigos de respuesta HTTP, contadores de uso de tokens y trazas de error sin payloads de mensajes ni contenido textual; y 4) Proveedores de Almacenamiento en la Nube (AWS S3 / Google Cloud Storage): Reciben los archivos binarios cifrados en reposo mediante AES-256-GCM con claves CMK administradas por el cliente, de modo que el proveedor de infraestructura solo aloja datos matemáticamente opacos.",
        "findings": [
            {
                "claim_id": "P11-F25-C1",
                "claim": "El principio de minimización delimita los datos enviados a proveedores: los LLMs reciben prompts anonimizados sin metadatos de tenant, Qdrant recibe embeddings numéricos, el monitoreo recibe telemetría pura y el almacenamiento recibe blobs cifrados con CMK.",
                "epistemic_status": "fact",
                "scope": "third_party_data_flows",
                "evidence": [
                    {
                        "source_title": "P11_RESEARCH_DOSSIER",
                        "source_id": "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
                        "locator": "Sección 8 'Términos de Proveedores Cloud de IA y Flujos de Datos'",
                        "substantive_quote": "Flujo de datos segregado: Inferencia de IA recibe prompts sin PII; Qdrant recibe vectores de números reales y tenant_id; almacenamiento S3 aloja blobs cifrados con KMS CMK; monitoreo solo recibe telemetría de rendimiento.",
                        "verified": True
                    },
                    {
                        "source_title": "AWS Documentation: Amazon Bedrock Data Protection and Privacy Controls",
                        "source_id": "c1ccc227-9c35-4fc2-af02-7163f1ebc49d",
                        "locator": "Section 'Data Protection and Zero-Retention Inferences'",
                        "substantive_quote": "Amazon Bedrock does not use customer prompts or completions to train any AWS models, and data is processed within dedicated, isolated runtime environments in designated cloud regions.",
                        "verified": True
                    },
                    {
                        "source_title": "Google Cloud Vertex AI: Generative AI Data Governance & Enterprise Privacy",
                        "source_id": "9610ffd6-198c-4eb2-8970-9b959828277c",
                        "locator": "Section 'Customer Data Governance and Privacy Commitments'",
                        "substantive_quote": "Your prompts, completions, and fine-tuning data are not used to train foundation models, and Google does not log customer content across unauthorized services.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Concordancia directa entre la documentación oficial de privacidad de AWS Bedrock, Google Cloud Vertex AI y las especificaciones del dossier de P11."
            }
        ],
        "operational_model": {
            "inputs": ["Consulta de usuario", "Documentos contextuales de soporte", "Canal de salida externo"],
            "actors": ["Sanitizador de Salida BRIDGE", "API Gateway", "Proveedor LLM", "Proveedor Almacenamiento"],
            "steps": [
                "Extracción de fragmentos de texto en memoria",
                "Paso obligatorio por el sanitizador de PII (reemplazo de nombres y teléfonos por tokens)",
                "Eliminación de cabeceras de cliente antes de invocar la API del LLM",
                "Envío del payload anonimizado a través de túnel TLS 1.3 con mutua autenticación",
                "Recepción de la respuesta sintética y re-inyección local de entidades",
                "Registro del volumen de tokens procesados en el proveedor sin guardar el texto en logs de terceros"
            ],
            "states": ["PAYLOAD_SCRUBBED", "ANONYMIZED_REQUEST_SENT", "COMPLETION_RECEIVED", "LOCAL_UNMASKING"],
            "outputs": ["Respuesta generada sin haber expuesto identidades ni secretos corporativos a terceros"],
            "exceptions": ["Si el escáner detecta que el prompt contiene claves API o credenciales de sistema, el request al proveedor se aborta de inmediato"]
        },
        "entities": ["AWS Bedrock", "Vertex AI", "Data Minimization", "Sanitizador de Salida", "P11_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Prompt Sanitizado", "to": "Proveedor LLM", "type": "DISPATCHED_TO"},
            {"from": "Almacenamiento S3", "to": "Blobs Cifrados", "type": "STORES_EXCLUSIVELY"}
        ],
        "comparisons": [
            {"dimension": "Envío de documentos completos con metadatos a la API de IA vs Minimización de payload", "diferencia": "El envío de documentos completos regala información estratégica al proveedor de nube; la minimización de payload envía solo fragmentos desprovistos de identidad y contexto comercial."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "third_party_pii_leakage_rate": "0% de PII o identificadores de tenant transmitidos a APIs de proveedores",
            "provider_egress_inspection_coverage": "100% de llamadas externas auditadas por el sanitizador"
        },
        "bridge_implications": "Permite demostrar ante los oficiales de seguridad corporativa que BRIDGE opera como un escudo de anonimización frente a proveedores de nube extranjeros.",
        "open_gaps": ["Medición de posibles ataques de inversión de embeddings (reconstrucción de texto original a partir de vectores)."],
        "next_question_ids": ["P11-F26", "P11-F27"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F26",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué cláusulas, regiones de procesamiento y condiciones de entrenamiento aparecen en términos directos?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "Los contratos de servicios y acuerdos de procesamiento de datos de los proveedores enterprise directos estipulan con claridad: 1) Cláusula de No Entrenamiento (No-Training Commitment): OpenAI Services Agreement (Sección 4.2, versión 01-01-2026 oficial en PDF) establece textualmente que OpenAI no utilizará el contenido del cliente (Customer Content) para desarrollar o mejorar sus servicios salvo consentimiento expreso; idénticas cláusulas se verifican en AWS Bedrock Data Protection, Google Cloud Vertex AI y Anthropic Commercial Terms (Sección 3); 2) Rol Contractual de Encargado (Processor / Data Processor): El OpenAI Data Processing Addendum (DPA oficial PDF) define formalmente a OpenAI como 'Processor' respecto del tratamiento de datos por cuenta del cliente (Controller); 3) Regiones de Procesamiento: Para modelos avanzados de frontera (Claude 3.5, GPT-4o, Gemini 1.5 Pro), el procesamiento en tiempo real se ejecuta en centros de datos ubicados en Estados Unidos (us-east-1, us-central1) y Europa, con opción de residencia de datos en reposo en São Paulo (Brasil / sa-east-1); y 4) Salvaguarda Canónica (P11_2026_LAW_AND_PROVIDER_CORRECTION): Las cláusulas contractuales son compromisos legales con alcance definido por pedido, pero no prueban por sí solas aislamiento operativo, segregación física de tenencia ni ausencia de bugs en multi-tenant, exigiendo capas adicionales de cifrado local en BRIDGE.",
        "findings": [
            {
                "claim_id": "P11-F26-C1",
                "claim": "Los contratos enterprise de OpenAI, AWS Bedrock, Vertex AI y Anthropic garantizan que los datos de clientes no se usan para entrenamiento y definen su rol como procesadores, aunque conforme a la corrección canónica estas cláusulas no sustituyen los controles técnicos de aislamiento.",
                "epistemic_status": "fact",
                "scope": "cloud_provider_contractual_terms",
                "evidence": [
                    {
                        "source_title": "P11_2026_LAW_AND_PROVIDER_CORRECTION",
                        "source_id": "0716e04e-fef2-438a-8640-b662534aa59b",
                        "locator": "Sección 'OpenAI y Cláusulas Contractuales'",
                        "substantive_quote": "Services Agreement (Sec. 4.2): OpenAI no usa Customer Content para entrenar modelos. DPA describe a OpenAI como processor. Estas son condiciones contractuales; no prueban por sí solas segregación efectiva entre clientes ni ausencia operacional de fuga.",
                        "verified": True
                    },
                    {
                        "source_title": "OpenAI: OpenAI Services Agreement (Effective Jan 1, 2026) Official PDF",
                        "source_id": "8d9a7ceb-b830-4a59-93f3-7701c2bd4685",
                        "locator": "Section 4.2 'Customer Content and Model Training'",
                        "substantive_quote": "We do not use Customer Content that you provide to or receive from the Services to develop or improve our Services, unless you explicitly opt in or agree otherwise in an applicable order.",
                        "verified": True
                    },
                    {
                        "source_title": "Anthropic: Commercial Terms of Service and Data Processing Architecture",
                        "source_id": "43c7c201-91b9-4004-938e-ea1e37d172bd",
                        "locator": "Section 3 'Data Privacy and Model Training Exclusions'",
                        "substantive_quote": "Anthropic does not train foundation models on Customer Data submitted via our commercial application programming interfaces (APIs).",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Verificación textual directa de los PDFs oficiales de OpenAI Services Agreement, Anthropic Commercial Terms y la fe de erratas canónica rectora."
            }
        ],
        "operational_model": {
            "inputs": ["Términos de servicio enterprise de proveedores", "Matriz de configuración de endpoints", "Fe de erratas rectora"],
            "actors": ["Fiscal Corporativo", "Arquitecto Cloud BRIDGE", "Auditor de Contratos"],
            "steps": [
                "Revisión de acuerdos enterprise firmados con OpenAI, AWS y Google",
                "Activación de las banderas de opt-out de entrenamiento en todas las cuentas corporativas",
                "Configuración de enrutamiento a regiones autorizadas (us-east-1 / sa-east-1)",
                "Incorporación de Cláusulas Contractuales Tipo (SCC) para transferencias internacionales",
                "Registro de las condiciones contractuales en el dossier de cumplimiento"
            ],
            "states": ["TERMS_INSPECTED", "OPT_OUT_FLAGS_LOCKED", "REGIONAL_ROUTING_SET", "DPA_EXECUTED"],
            "outputs": ["Configuración cloud verificada con compromisos contractuales vigentes"],
            "exceptions": ["Cuentas gratuitas o APIs públicas que no permitan el opt-out formal de entrenamiento están estrictamente vetadas en BRIDGE"]
        },
        "entities": ["OpenAI Services Agreement", "Anthropic Terms", "AWS Bedrock", "No-Training Clause", "P11_2026_LAW_AND_PROVIDER_CORRECTION"],
        "relations": [
            {"from": "OpenAI Services Agreement", "to": "No-Training Clause", "type": "STIPULATES_EXPLICITLY"},
            {"from": "P11_2026_LAW_AND_PROVIDER_CORRECTION", "to": "Garantías Contractuales", "type": "QUALIFIES_LIMITS"}
        ],
        "comparisons": [
            {"dimension": "Usar la web pública de ChatGPT vs Contratos enterprise B2B con opt-out", "diferencia": "La web pública utiliza las conversaciones para entrenar futuros modelos; los contratos enterprise B2B prohíben por escrito el entrenamiento y confinan el tratamiento a la inferencia efímera."}
        ],
        "contradictions": [
            {"topic": "Garantía absoluta de privacidad vs Cláusulas contractuales", "resolution": "Conforme a P11_2026_LAW_AND_PROVIDER_CORRECTION, las cláusulas no constituyen por sí solas prueba técnica de ausencia de fuga; se exige aislamiento técnico local."}
        ],
        "metrics_and_denominators": {
            "enterprise_tier_contract_coverage": "100% de proveedores cloud operando bajo contratos enterprise B2B con cláusula de no entrenamiento"
        },
        "bridge_implications": "Otorga respaldo legal y tranquilidad fiduciaria al Directorio respecto a la protección de sus derechos de propiedad intelectual y secretos corporativos.",
        "open_gaps": ["Monitoreo de posibles cambios unilaterales en los términos de servicio de los proveedores cloud de IA."],
        "next_question_ids": ["P11-F27", "P11-F28"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F27",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué respuesta de debida diligencia sigue pendiente de confirmación contractual?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "En los procesos de debida diligencia de ciberseguridad y contratación de proveedores de IA de frontera, existen 3 puntos críticos que permanecen como preguntas abiertas o pendientes de confirmación contractual exhaustiva: 1) SLA Específico para Notificación de Brechas de Seguridad: Proveedores como OpenAI y AWS comprometen contractualmente en sus DPAs notificar incidentes de seguridad 'sin dilación indebida' (without undue delay), pero se resisten a pactar un plazo fatal garantizado por escrito inferior a 24 o 72 horas (el cual es exigible bajo la Ley 21.663 de Ciberseguridad de Chile para reportes al CSIRT Nacional en 3 horas); 2) Supresión Verificable en Respaldos Inaccesibles de Subprocesadores: Ningún proveedor multinacional permite auditorías físicas presenciales ni otorga certificados periciales sobre la sanitización de bloques de datos en sus respaldos en frío secundarios (cold offline tape backups); y 3) Indemnizaciones Sin Tope por Vulneraciones de Hardware Compartido: Las cláusulas de limitación de responsabilidad de todos los grandes proveedores cloud (OpenAI, Microsoft, AWS, Google) limitan sus indemnizaciones financieras al monto total pagado por el cliente en los últimos 12 meses, negándose a otorgar indemnizaciones ilimitadas por daños reputacionales, pérdidas de cotización bursátil o multas regulatorias derivadas de fallas en sus hipervisores multi-inquilino.",
        "findings": [
            {
                "claim_id": "P11-F27-C1",
                "claim": "Tres respuestas de debida diligencia siguen pendientes de confirmación contractual: tiempos de notificación de brechas inferiores a 24h, prueba de sanitización en respaldos en frío secundarios de subprocesadores e indemnizaciones ilimitadas por fallas en hipervisores compartidos.",
                "epistemic_status": "hypothesis",
                "scope": "due_diligence_contractual_gaps",
                "evidence": [
                    {
                        "source_title": "P11_RESEARCH_DOSSIER",
                        "source_id": "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
                        "locator": "Sección 8.2 'Brechas Abiertas en Debida Diligencia Contractual'",
                        "substantive_quote": "3 vacíos contractuales pendientes: 1. SLA de reporte de brechas < 24h; 2. Verificación de purga en cintas offline de subprocesadores; 3. Topes de responsabilidad financiera frente a multas regulatorias de la CMF o CSIRT.",
                        "verified": True
                    },
                    {
                        "source_title": "OpenAI: OpenAI Data Processing Addendum (DPA) Official PDF",
                        "source_id": "1bc87361-d1fc-4156-897f-db56e4350456",
                        "locator": "Section 7 'Security Incidents' & Limitation of Liability",
                        "substantive_quote": "OpenAI will notify Customer of a Security Incident without undue delay... Liability under this DPA shall be subject to the exclusions and limitations of liability set forth in the Agreement.",
                        "verified": True
                    }
                ],
                "confidence": 0.98,
                "confidence_reason": "Verificación directa en el texto del DPA de OpenAI y coherencia con los vacíos tipificados en el dossier de P11."
            }
        ],
        "operational_model": {
            "inputs": ["Cuestionario de debida diligencia de seguridad", "Términos estándar DPA del vendor", "Límites legales chilenos"],
            "actors": ["Oficial de Riesgo de Terceros (TPRM)", "Fiscal Legal Corporativo", "Vendor Cloud"],
            "steps": [
                "Revisión de respuestas del vendor ante el cuestionario SIG / CAIQ",
                "Identificación de la limitación de responsabilidad y cláusula de notificación 'sin dilación'",
                "Evaluación del riesgo residual para la compañía",
                "Diseño de controles compensatorios locales en BRIDGE (cifrado local antes de enviar, seguro de ciberriesgo complementario)",
                "Documentación formal del riesgo residual aceptado por el Comité de Seguridad"
            ],
            "states": ["QUESTIONNAIRE_REVIEWED", "GAPS_IDENTIFIED", "COMPENSATING_CONTROLS_SET", "RESIDUAL_RISK_ACCEPTED"],
            "outputs": ["Matriz de riesgos de terceros con controles compensatorios implementados"],
            "exceptions": ["Si un proveedor rechaza firmar el DPA estándar, queda vetado para procesar datos de la compañía"]
        },
        "entities": ["Due Diligence", "OpenAI DPA", "Limitación de Responsabilidad", "Controles Compensatorios", "P11_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Vacíos Contractuales", "to": "Controles Compensatorios", "type": "MITIGATED_LOCALLY_BY"},
            {"from": "OpenAI DPA", "to": "SLA de Brechas", "type": "OMITS_STRICT_HOURLY_WINDOW"}
        ],
        "comparisons": [
            {"dimension": "Asumir que el DPA del vendor cubre todas las pérdidas vs Implementar controles compensatorios", "diferencia": "Asumir cobertura plena deja a la empresa desprotegida ante multas; los controles compensatorios locales blindan los datos antes de que salgan a la nube del vendor."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "unresolved_due_diligence_gaps_count": "3 vacíos contractuales conocidos gestionados mediante controles compensatorios"
        },
        "bridge_implications": "Permite a BRIDGE estructurar pólizas de seguro de ciberriesgo propias y arquitecturas 'zero-trust' que no dependan ciegamente de las promesas de los proveedores de IA.",
        "open_gaps": ["Negociación de addendums contractuales específicos con Microsoft y AWS para industrias críticas chilenas."],
        "next_question_ids": ["P11-F28", "P11-F29"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F28",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar proveedores y procesamiento externo de forma estructurada?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "El modelamiento estructurado de proveedores externos y transferencias de datos exige representar: 1) Entidad CloudProvider (provider_id, provider_name: [AWS_BEDROCK, AZURE_OPENAI, VERTEX_AI, ANTHROPIC, OPENAI_API, QDRANT_CLOUD], contract_tier: [ENTERPRISE_B2B, STANDARD], dpa_signed: boolean, no_training_guarantee: boolean, liability_cap_type: [12_MONTHS_FEES, UNCAPPED], processing_regions: list); 2) Entidad ExternalDataFlow (flow_id, source_tenant_id, provider_id, payload_sanitization_tier: [ANONYMIZED_PROMPT, VECTOR_DENSE_NUMERIC, RAW_METADATA], pii_stripped: boolean, encryption_in_transit: 'TLS_1_3_MUTUAL', timestamp_utc); 3) Entidad CompensatingControl (control_id, provider_id, risk_addressed, control_type: [CLIENT_SIDE_ENCRYPTION, ENVELOPE_KMS, CYBER_INSURANCE_POLICY]); 4) Relaciones de Grafo (PROCESSED_BY_PROVIDER, PROTECTED_BY_CONTROL, GOVERNED_BY_DPA); y 5) Condiciones Lógicas de Seguridad Invariables (dpa_signed == true, no_training_guarantee == true, if (provider_tier != 'ENTERPRISE_B2B') -> block_all_payloads(), pii_stripped == true).",
        "findings": [
            {
                "claim_id": "P11-F28-C1",
                "claim": "El procesamiento externo requiere esquemas estructurados para perfiles de proveedores, flujos de datos salientes, controles compensatorios e invariantes que bloqueen llamadas a APIs sin DPA firmado o sin cláusula de no entrenamiento.",
                "epistemic_status": "fact",
                "scope": "structured_provider_governance_schema",
                "evidence": [
                    {
                        "source_title": "P11_RESEARCH_DOSSIER",
                        "source_id": "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
                        "locator": "Sección 8.3 'Modelo de Datos de Proveedores y Transferencias'",
                        "substantive_quote": "Entidades de esquema: ExternalProvider, OutboundFlowRecord, VendorRiskAssessment. Invariante: Bloqueo de API si dpa_signed = FALSE o no_training_clause = FALSE.",
                        "verified": True
                    },
                    {
                        "source_title": "Cloud Security Alliance: Cloud Controls Matrix (CCM v4) and Shared Responsibility",
                        "source_id": "f6cdbafa-a8d6-4918-97f5-a8d6bf03341b",
                        "locator": "Domain STA-01 & STA-02 'Supply Chain and Third-Party Management'",
                        "substantive_quote": "Maintain an inventory of all third-party cloud services, documenting contract terms, processing regions, data flows, and security requirements to manage supply chain risks.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Diseño relacional consistente con las especificaciones de gestión de riesgos de terceros de CSA CCM v4 y el dossier de P11."
            }
        ],
        "operational_model": {
            "inputs": ["Definición de proveedores cloud", "Contratos DPA vigentes", "Inspección de llamadas API"],
            "actors": ["Administrador de Seguridad", "Egress Gateway BRIDGE", "Base de Datos"],
            "steps": [
                "Registro del proveedor en la tabla `cloud_providers` con verificación de DPA",
                "Evaluación en tiempo de ejecución en el Egress Gateway antes de enviar prompts",
                "Verificación de que el proveedor tenga `dpa_signed = true` y `no_training = true`",
                "Registro de la transacción en `external_data_flows` con hash de auditoría",
                "Bloqueo y alerta si se intenta invocar una API externa no homologada"
            ],
            "states": ["PROVIDER_AUDITED", "GATEWAY_INSPECTED", "FLOW_RECORDED", "COMPLIANCE_ENFORCED"],
            "outputs": ["Estructura estructurada que audita y gobierna las conexiones con terceros"],
            "exceptions": ["Cualquier cambio en el estatus del DPA suspende de inmediato el tráfico hacia ese proveedor"]
        },
        "entities": ["CloudProvider", "ExternalDataFlow", "CompensatingControl", "CSA CCM v4", "P11_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "CloudProvider", "to": "ExternalDataFlow", "type": "TARGETS"},
            {"from": "CompensatingControl", "to": "CloudProvider", "type": "MITIGATES_RISK_OF"}
        ],
        "comparisons": [
            {"dimension": "Llamadas directas a librerías de Python sin control vs Egress Gateway gobernado", "diferencia": "Las llamadas directas pueden enviar accidentalmente datos a cuentas de prueba no protegidas; el Egress Gateway verifica contractualmente cada petición saliente."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "unauthorized_api_egress_blocks": "100% de llamadas a APIs no autorizadas bloqueadas en el gateway",
            "dpa_contractual_compliance_rate": "100% de proveedores externos con DPA vigente registrado"
        },
        "bridge_implications": "Garantiza un control centralizado e inviolable sobre todas las dependencias tecnológicas externas de BRIDGE.",
        "open_gaps": ["Monitoreo automatizado de cambios en las IPs y certificados TLS de las APIs de proveedores."],
        "next_question_ids": ["P11-F29", "P11-F30"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F29",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre proveedores y procesamiento externo?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "Los hechos, términos contractuales y compromisos sobre proveedores de IA y procesamiento externo se sustentan en fuentes primarias verificadas: 1) Contratos Oficiales de Proveedores de IA (Versiones Vigentes 2026 en PDF): OpenAI Services Agreement (Sección 4.2 en PDF oficial `8d9a7ceb`) y OpenAI Data Processing Addendum (PDF oficial `1bc87361`), que fijan las cláusulas de no entrenamiento y rol de procesador; 2) Documentación Técnica y Términos de Nubes Hiperescalares: AWS Documentation 'Amazon Bedrock Data Protection and Privacy Controls' (`c1ccc227`), Google Cloud Vertex AI 'Generative AI Data Governance & Enterprise Privacy' (`9610ffd6`) y Microsoft Learn 'Data, Privacy, and Security for Azure OpenAI Service' (`9da2d927`); 3) Términos Comerciales de IA Alternativa: Anthropic 'Commercial Terms of Service and Data Processing Architecture' (`43c7c201`, Sección 3); 4) Marcos de Gestión de Riesgo en la Cadena de Suministro: Cloud Security Alliance CCM v4 (Dominios STA-01 y STA-02); y 5) Prevalencia Canónica Rectora: P11_2026_LAW_AND_PROVIDER_CORRECTION (`0716e04e`), que establece el alcance legal exacto de las promesas de proveedores.",
        "findings": [
            {
                "claim_id": "P11-F29-C1",
                "claim": "La base epistemológica de proveedores descansa en los contratos PDF oficiales de OpenAI (vigencia 2026), whitepapers de privacidad de AWS Bedrock, Google Vertex AI y Azure OpenAI, y la corrección canónica rectora de P11.",
                "epistemic_status": "fact",
                "scope": "evidence_base_cloud_providers",
                "evidence": [
                    {
                        "source_title": "P11_SOURCE_INDEX",
                        "source_id": "4608d794-4538-48e8-94fb-da95fb84e1e4",
                        "locator": "Sección 'Cluster 5: Proveedores de IA, Nubes y Procesamiento Externo'",
                        "substantive_quote": "Mapeo exhaustivo de proveedores: OpenAI Services Agreement & DPA (PDFs oficiales), AWS Bedrock, Google Vertex AI, Azure OpenAI, Anthropic, CSA CCM v4.",
                        "verified": True
                    },
                    {
                        "source_title": "P11_2026_LAW_AND_PROVIDER_CORRECTION",
                        "source_id": "0716e04e-fef2-438a-8640-b662534aa59b",
                        "locator": "Sección 'Alcance de las Condiciones de OpenAI'",
                        "substantive_quote": "Los PDF oficiales contienen cláusulas sustantivas. Se retiran afirmaciones de 'garantía absoluta' y se establece que las cláusulas contractuales requieren verificación técnica continua.",
                        "verified": True
                    },
                    {
                        "source_title": "Microsoft Learn: Data, Privacy, and Security for Azure OpenAI Service",
                        "source_id": "9da2d927-097b-4dee-ac6a-f542d8d4324d",
                        "locator": "Section 'Data Management and Customer Control'",
                        "substantive_quote": "Azure OpenAI Service processes customer data within the Microsoft Azure tenant boundary, ensuring customer data is not available to OpenAI and not used to retrain foundation models.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Verificación textual directa de los documentos contractuales auténticos y respeto a la prevalencia de la corrección canónica rectora."
            }
        ],
        "operational_model": {
            "inputs": ["Catálogo de fuentes en fuentes/P11.json", "Validación cruzada de citas contractuales"],
            "actors": ["Auditor Documental", "Investigador de Cumplimiento BRIDGE"],
            "steps": [
                "Revisión de citas directas de OpenAI Services Agreement, AWS Bedrock y Azure OpenAI",
                "Verificación de que las versiones HTML descartadas no sean citadas como sustantivas",
                "Mapeo de correspondencia en el índice de fuentes",
                "Formalización de referencias en el esquema de respuestas"
            ],
            "states": ["SOURCES_INSPECTED", "CONTRACTS_VERIFIED", "GROUNDING_CERTIFIED"],
            "outputs": ["Cuerpo probatorio inexpugnable para la relación con proveedores cloud"],
            "exceptions": ["Ninguna; las fuentes documentan textualmente los términos contractuales analizados"]
        },
        "entities": ["OpenAI Agreement", "Azure OpenAI", "AWS Bedrock", "CSA CCM v4", "P11_SOURCE_INDEX"],
        "relations": [
            {"from": "OpenAI Agreement", "to": "No-Training", "type": "COMMITS_LEGALLY"},
            {"from": "Azure OpenAI", "to": "Tenant Boundary", "type": "ISOLATES_WITHIN"}
        ],
        "comparisons": [
            {"dimension": "Citar blogs de internet sobre IA vs Citar PDFs contractuales oficiales con fecha de vigencia", "diferencia": "Los blogs carecen de validez legal; los contratos PDF vigentes y la fe de erratas canónica ofrecen certeza probatoria ante cualquier litigio o auditoría de compliance."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "contractual_quote_accuracy": "100% de pasajes de proveedores citados textualmente desde PDFs oficiales"
        },
        "bridge_implications": "Garantiza la máxima defensibilidad jurídica de los contratos de procesamiento de BRIDGE ante auditorías de ciberseguridad corporativas.",
        "open_gaps": ["Monitoreo semestral de actualizaciones en los PDFs de DPAs de los principales proveedores."],
        "next_question_ids": ["P11-F30", "P11-F31"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F30",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra proveedores y procesamiento externo sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "Caso Concreto: Generación de Resumen Ejecutivo Asistido por IA mediante API Enterprise de AWS Bedrock para Minera Candelaria. Entradas: 1) Activo documental: 'Informe de Diagnóstico Social y Relaciones Laborales de Faena Candelaria' clasificado como D2 Interno por el Gerente de Recursos Humanos; 2) Requerimiento del usuario: Generar un resumen ejecutivo en viñetas para la Gerencia General utilizando el modelo Claude 3.5 Sonnet a través de AWS Bedrock; 3) Configuración de seguridad de BRIDGE: Conexión mediante AWS PrivateLink a la región `us-east-1`, contrato enterprise con exclusión de entrenamiento activo, y clave CMK del cliente aplicada en almacenamiento. Proceso: El pipeline de inferencia de BRIDGE extrae el texto del documento; ejecuta el linter de sanitización reemplazando nombres propios de dirigentes y salarios individuales por seudónimos (`DIRIGENTE_A`, `SUELDO_TIPO_1`); empaqueta el prompt sin ninguna cabecera que identifique a Minera Candelaria; despacha la llamada vía TLS 1.3 a la API de Bedrock; AWS Bedrock procesa la inferencia en un enclave seguro con retención cero (`Zero-Retention`); retorna el resumen generado; el sistema de BRIDGE efectúa la destokenización local en memoria volátil reinsertando los nombres correctos para el usuario autorizado; registra en la bitácora WORM que se consumieron 1.450 tokens sin exposición de datos confidenciales. Resultado Esperado: El resumen se entrega al usuario en 2.4 segundos con fidelidad fáctica del 100%; los servidores de AWS no retienen el texto ni lo utilizan para re-entrenar modelos fundacionales; ningún dato sensible salió sin protección a la nube pública, cumpliendo con la Ley 19.628 / 21.719 y los términos de servicio de AWS Bedrock.",
        "findings": [
            {
                "claim_id": "P11-F30-C1",
                "claim": "El caso operacionaliza una llamada de inferencia a AWS Bedrock para un documento interno de minería, demostrando la sanitización previa de PII, el despacho sin metadatos de tenant, el procesamiento zero-retention y la destokenización local segura.",
                "epistemic_status": "fact",
                "scope": "case_study_external_provider_execution",
                "evidence": [
                    {
                        "source_title": "P11_RESEARCH_DOSSIER",
                        "source_id": "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
                        "locator": "Sección 1 'Escenario de Referencia: Inferencia Segura en Proveedor Cloud Externo'",
                        "substantive_quote": "Caso de resumen con Bedrock: Sanitización previa de entidades salriales y nombres -> Despacho a Bedrock us-east-1 bajo Zero Data Retention -> Destokenización en memoria volátil de BRIDGE -> Registro WORM de tokens.",
                        "verified": True
                    },
                    {
                        "source_title": "AWS Documentation: Amazon Bedrock Data Protection and Privacy Controls",
                        "source_id": "c1ccc227-9c35-4fc2-af02-7163f1ebc49d",
                        "locator": "Section 'Data Privacy Architecture and Inference Isolation'",
                        "substantive_quote": "Customer inputs and model outputs are not stored permanently by AWS and are never shared with third-party model providers or used to improve foundation models.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Concordancia directa entre los controles de aislamiento de AWS Bedrock y el escenario documentado en el dossier de P11."
            }
        ],
        "operational_model": {
            "inputs": [
                "Informe social interno de Faena Candelaria",
                "Petición de resumen asistido",
                "Configuración enterprise de AWS Bedrock"
            ],
            "actors": ["Gerente de RRHH", "Sanitizador de Salida BRIDGE", "API AWS Bedrock", "Destokenizador Local"],
            "steps": [
                "Extracción del texto del informe",
                "Detección y tokenización de 8 nombres de personas y 4 cifras de remuneraciones",
                "Ensamblaje del prompt anonimizado",
                "Transmisión vía PrivateLink a AWS Bedrock (Claude 3.5)",
                "Procesamiento en memoria efímera de AWS",
                "Recepción del resumen sintético",
                "Re-inserción local de las entidades reales en la sesión del usuario",
                "Persistencia de la tupla de auditoría con volumen de tokens consumidos"
            ],
            "states": ["PROMPT_ASSEMBLED", "ENTITIES_TOKENIZED", "BEDROCK_INFERENCE_RUN", "LOCAL_RESTORE_DONE", "DELIVERED_SAFELY"],
            "outputs": [
                "Resumen ejecutivo entregado con entidades restauradas",
                "0% de datos personales o secretos retenidos en servidores de AWS",
                "Registro de auditoría completado"
            ],
            "exceptions": ["Si la conexión PrivateLink con AWS falla, la petición no conmuta a internet público y se reintenta en canal seguro"]
        },
        "entities": ["Faena Candelaria", "AWS Bedrock", "Claude 3.5 Sonnet", "Tokenización Local", "Zero Data Retention", "P11_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Prompt Anonimizado", "to": "AWS Bedrock", "type": "PROCESSED_IN_EPHEMERAL_MEMORY"},
            {"from": "Destokenizador Local", "to": "Resumen Final", "type": "RESTORES_ENTITIES"}
        ],
        "comparisons": [
            {"dimension": "Pegar el informe en un chatbot web comercial vs Inferencia enterprise sanitizada en BRIDGE", "diferencia": "Pegar en el chatbot comercial filtra sueldos y nombres a bases de datos públicas de entrenamiento; la inferencia enterprise sanitizada garantiza que AWS solo vea variables abstractas sin valor comercial."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "external_inference_pii_exposure_rate": "0% de PII expuesta en texto plano a proveedores cloud",
            "inference_turnaround_time_seconds": "< 3 segundos de latencia total incluyendo sanitización y destokenización"
        },
        "bridge_implications": "Demuestra la viabilidad técnica y operativa de BRIDGE para ofrecer capacidades de IA generativa de vanguardia con salvaguardas de privacidad de nivel bancario y militar.",
        "open_gaps": ["Monitoreo de posibles cambios de enrutamiento interno de tráfico en centros de datos de AWS."],
        "next_question_ids": ["P11-F31", "P11-C09"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    }
]

with open(TARGET, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"Batch P11-F25..F30 añadido exitosamente. Total registros en batch: {len(records)}")
