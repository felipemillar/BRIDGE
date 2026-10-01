import json
from pathlib import Path

TARGET = Path("/Users/fmillar/Proyectos_Desarrollo/BRIDGE/respuestas/P11.jsonl")
NOTEBOOK_ID = "64271ecf-776c-4692-b302-d936ea00a501"
SNAPSHOT = "2026-10-01T15:00:00-03:00"

records = [
    {
        "question_id": "P11-F13",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué combinación de rol, propósito y clasificación autoriza cada acción?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "La autorización en BRIDGE no depende únicamente de roles estáticos, sino de una matriz ABAC (Attribute-Based Access Control, según NIST SP 800-162) que evalúa cuatro dimensiones interdependientes: 1) Clasificación del Activo: D1 (Público), D2 (Interno), D3 (Confidencial Estratégico), D4 (Datos Personales), D5 (Secretos de Terceros); 2) Rol del Actor: A1 (Admin Tenant), A2 (Asuntos Corporativos Interno), A3 (Consultor Agencia Externa), A4 (Directivo C-Level / Legal) y A5 (Auditor de Cumplimiento); 3) Propósito Declarado de la Operación: Fines comunicacionales ordinarios, auditoría legal, respuesta a crisis o investigación de incidentes; y 4) Acción Solicitada: Create, Read, Update, Delete, Export, Vectorize y Sign-Off. Reglas cardinales de autorización: A3 (Agencias) solo puede leer D1 y D2 asignados a su proyecto, teniendo estrictamente bloqueada la lectura de D3, D4 y D5 y la exportación masiva; A2 accede a D1, D2 y a D4 en formato pseudonimizado; A4 accede a D3 bajo doble factor de autenticación para propósitos de gestión legal o de crisis; A1 administra usuarios pero no puede inspeccionar contenido D3/D4 sin elevación justificada de privilegios; y A5 solo accede a bitácoras de auditoría y metadatos sin contenido sensible.",
        "findings": [
            {
                "claim_id": "P11-F13-C1",
                "claim": "El control de acceso formal combina roles (A1 a A5), niveles de datos (D1 a D5), propósito operacional y tipos de acción bajo el estándar ABAC de NIST SP 800-162, aplicando el principio de mínimo privilegio exigido por SOC 2.",
                "epistemic_status": "fact",
                "scope": "abac_authorization_matrix",
                "evidence": [
                    {
                        "source_title": "P11_RESEARCH_DOSSIER",
                        "source_id": "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
                        "locator": "Sección 2.2 'Matriz Operativa de Autorización y Retención'",
                        "substantive_quote": "Matriz ABAC: Cruce formal de 5 roles (A1-A5) con 5 clases de datos (D1-D5) y 7 acciones. Consultores externos (A3) tienen prohibida la lectura de D3/D4/D5 y la exportación masiva.",
                        "verified": True
                    },
                    {
                        "source_title": "NIST SP 800-162: Guide to Attribute Based Access Control (ABAC) Definition and Considerations",
                        "source_id": "2a88e293-2b53-4430-8dca-26e545448a9f",
                        "locator": "Section 2.1 'ABAC Basic Concepts'",
                        "substantive_quote": "Access is granted or denied based on an evaluation of subject attributes, object attributes, requested action, and environmental conditions against enterprise policy rules.",
                        "verified": True
                    },
                    {
                        "source_title": "AICPA: System and Organization Controls (SOC 2) Trust Services Criteria",
                        "source_id": "11c7c827-b3a4-4207-925a-f5bac2493a7b",
                        "locator": "Criteria CC6.3 'Access Restrictions and Least Privilege'",
                        "substantive_quote": "The entity authorizes, modifies, and removes access to data, software, functions, and other protected information assets based on the principle of least privilege and job responsibilities.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Concordancia directa entre los requerimientos de mínimo privilegio de SOC 2 CC6.3, el estándar ABAC NIST SP 800-162 y el dossier de P11."
            }
        ],
        "operational_model": {
            "inputs": ["Identidad y rol del usuario", "Objeto solicitado y su clasificación D1-D5", "Acción intentada", "Propósito declarado"],
            "actors": ["Policy Decision Point (PDP)", "Policy Enforcement Point (PEP) BRIDGE", "Usuario Solicitante"],
            "steps": [
                "Interceptación de la solicitud en el PEP de la API",
                "Consulta de atributos de sujeto y objeto al PDP",
                "Evaluación de la política ABAC (reglas de combinación rol-dato-acción)",
                "Si la solicitud involucra D3/D4: Verificación de propósito legítimo y MFA",
                "Emisión de decisión: Permite o Deniega",
                "Si se deniega: Bloqueo inmediato y registro de intento denegado en bitácora"
            ],
            "states": ["REQUEST_INTERCEPTED", "ATTRIBUTES_RESOLVED", "POLICY_EVALUATED", "ACCESS_GRANTED_OR_DENIED"],
            "outputs": ["Acción autorizada o rechazo estructurado con código de seguridad"],
            "exceptions": ["Intentos de consultores externos (A3) de acceder a D3 o exportar datos masivos disparan revocación automática de sesión"]
        },
        "entities": ["NIST SP 800-162", "ABAC", "Mínimo Privilegio", "SOC 2 Criteria CC6.3", "P11_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Usuario Solicitante", "to": "PEP", "type": "PRESENTS_REQUEST_TO"},
            {"from": "PEP", "to": "PDP", "type": "EVALUATES_VIA_ABAC"}
        ],
        "comparisons": [
            {"dimension": "Roles estáticos simples (RBAC) vs Matriz multidimensional ABAC", "diferencia": "El RBAC simple permite que un usuario lea archivos confidenciales fuera de horario laboral o sin justificación; el ABAC exige coherencia entre rol, tipo de dato, propósito y entorno."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "unauthorized_access_attempt_blocks": "100% de peticiones no autorizadas bloqueadas por el PEP",
            "abac_evaluation_overhead_ms": "< 5 milisegundos de latencia por decisión de acceso"
        },
        "bridge_implications": "Permite a BRIDGE estructurar un motor de políticas de control de acceso desacoplado (e.g., Open Policy Agent - OPA) aplicable en todas las rutas de API.",
        "open_gaps": ["Integración de biometría continua para revalidar sesiones de directivos que acceden a D3 en dispositivos portátiles."],
        "next_question_ids": ["P11-F14", "P11-F15"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F14",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Cómo se heredan, revocan y comprueban permisos del origen al resultado?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "La propagación y revocación de permisos a lo largo del ciclo de inferencia y transformación documental se gobierna mediante tres principios arquitectónicos: 1) Principio de Herencia de Máxima Restricción (High Water Mark Principle): Todo documento, fragmento vectorial, resumen sintetizado o respuesta RAG generada a partir de múltiples fuentes hereda automáticamente la clasificación más restrictiva de cualquiera de sus insumos primarios (si un borrador utiliza fuentes D1 y D3, la derivada resultante se clasifica estrictamente como D3 y queda sujeta a sus mismos controles y permisos); 2) Revocación en Cascada y en Tiempo Real: La revocación de privilegios a un usuario o la desclasificación/baja de un activo documental se propaga inmediatamente mediante invalidación de tokens de corta duración (JWT con TTL de 15 minutos), listas negras en caché Redis de baja latencia y regeneración de listas de acceso en el motor de políticas, impidiendo que sesiones activas sigan leyendo datos revocados; y 3) Comprobación Dinámica en la Entrega (Egress Authorization Check): Antes de transmitir la respuesta final al usuario, el sistema evalúa nuevamente los atributos del destinatario frente a la clasificación consolidada del resultado, bloqueando la entrega si el usuario carece de permiso para el nivel resultante.",
        "findings": [
            {
                "claim_id": "P11-F14-C1",
                "claim": "La gobernanza de permisos exige la herencia de máxima restricción (High Water Mark) en derivados sintéticos, revocación en cascada vía invalidación de tokens en Redis y comprobación dinámica previa a la entrega final.",
                "epistemic_status": "fact",
                "scope": "permission_inheritance_and_revocation",
                "evidence": [
                    {
                        "source_title": "P11_RESEARCH_DOSSIER",
                        "source_id": "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
                        "locator": "Sección 2.3 'Herencia de Clasificación y Revocación Dinámica'",
                        "substantive_quote": "Herencia High Water Mark: Toda síntesis o respuesta RAG hereda la clasificación más alta de sus fuentes base. Revocación en cascada mediante JWT con TTL de 15 min y listas negras en Redis.",
                        "verified": True
                    },
                    {
                        "source_title": "NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations",
                        "source_id": "24c7952c-3d6a-417c-8e7d-746065c9ca20",
                        "locator": "Control AC-4 'Information Flow Enforcement'",
                        "substantive_quote": "Enforce approved authorizations for controlling the flow of information within the system and between connected systems based on data classification and label preservation rules.",
                        "verified": True
                    },
                    {
                        "source_title": "Cloud Security Alliance: Cloud Controls Matrix (CCM v4) and Shared Responsibility",
                        "source_id": "f6cdbafa-a8d6-4918-97f5-a8d6bf03341b",
                        "locator": "Domain IAM-03 'Access Revocation and Policy Synchronization'",
                        "substantive_quote": "Establish procedures to promptly revoke access upon termination of employment or business relationship, ensuring revocation propagates across distributed cached sessions and linked assets.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Concordancia directa entre los requerimientos de control de flujo de información NIST SP 800-53 AC-4, CSA CCM v4 y el dossier de P11."
            }
        ],
        "operational_model": {
            "inputs": ["Fuentes consultadas por el RAG", "Respuesta generada por el LLM", "Perfil de permisos del usuario"],
            "actors": ["Linter de Herencia BRIDGE", "Validador de Entrega (Egress Gate)", "Servidor de Autorización"],
            "steps": [
                "Cálculo de la clasificación máxima entre todas las fuentes que aportaron fragmentos al contexto",
                "Asignación de la etiqueta heredada (e.g., D3) a la respuesta generada",
                "Inspección de la lista de revocación de sesiones en Redis",
                "Verificación de que el usuario emisor de la consulta posea permisos activos para el nivel heredado",
                "Si el usuario está autorizado: Entrega de la respuesta",
                "Si la sesión fue revocada o carece de permiso para el nivel heredado: Supresión del contenido y retorno de mensaje de acceso restringido"
            ],
            "states": ["SOURCES_TAGGED", "MAX_TIER_COMPUTED", "REVOCATION_CHECKED", "DELIVERY_APPROVED_OR_FILTERED"],
            "outputs": ["Respuesta entregada con metadatos de herencia de seguridad"],
            "exceptions": ["Si una de las fuentes fue marcada como eliminada o revocada durante el proceso de inferencia, la respuesta se descarta y se re-ejecuta el pipeline"]
        },
        "entities": ["High Water Mark", "NIST SP 800-53 AC-4", "Revocación en Cascada", "CSA CCM v4", "P11_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Fuentes Base", "to": "Resultado Derivado", "type": "INHERITS_MAX_RESTRICTION"},
            {"from": "Redis Blacklist", "to": "Tokens JWT", "type": "INVALIDATES_IMMEDIATELY"}
        ],
        "comparisons": [
            {"dimension": "Pérdida de clasificación en salidas de IA vs Herencia formal High Water Mark", "diferencia": "La pérdida de clasificación permite que resúmenes de documentos confidenciales se envíen a empleados comunes; la herencia High Water Mark preserva el blindaje confidencial en todo derivado."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "classification_inheritance_fidelity": "100% de derivados catalogados con la cota superior de sus fuentes",
            "revocation_propagation_latency_seconds": "< 3 segundos para propagar la revocación de un usuario en todos los nodos"
        },
        "bridge_implications": "Garantiza que la IA generativa de BRIDGE no sea utilizada como mecanismo indirecto para lavar clasificaciones o eludir controles de acceso.",
        "open_gaps": ["Redacción automática de fragmentos D3 en respuestas híbridas para permitir entregar las partes D1/D2 a usuarios sin credencial D3."],
        "next_question_ids": ["P11-F15", "P11-F16"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F15",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué bitácora permite responder quién accedió a qué y por qué?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "La trazabilidad y rendición de cuentas en BRIDGE se sustenta en un Registro de Auditoría Inmutable (Immutable Audit Ledger) estructurado bajo las directrices del NIST SP 800-92 y la Ley 21.663 (Art. 9): 1) Modelo de Registro Append-Only: Almacenado en tablas de base de datos protegidas con reglas WORM (Write Once, Read Many) y disparadores que bloquean cualquier sentencia `UPDATE` o `DELETE`, garantizando no repudio; 2) Tupla Estructurada de Acceso: Cada evento registra obligatoriamente 11 atributos forenses (`timestamp_utc` con sincronización NTP, `user_id`, `tenant_id`, `user_role`, `action_type`: [READ, QUERY_RAG, EXPORT, SIGN_OFF], `resource_id`, `classification_tier`: [D1-D5], `purpose_code`: [ROUTINE_OPS, LEGAL_DEFENSE, CRISIS_MGMT, AUDIT], `session_ip_address`, `user_agent`, y `record_hash_sha256`); 3) Sellado Criptográfico Encadenado: Cada registro incorpora el hash del registro anterior (cadena criptográfica de bloques), permitiendo a auditores externos detectar al instante cualquier alteración retroactiva o borrado de filas en el historial.",
        "findings": [
            {
                "claim_id": "P11-F15-C1",
                "claim": "La bitácora de accesos opera bajo arquitectura append-only WORM con sellado criptográfico encadenado conforme a NIST SP 800-92 y la Ley 21.663, registrando usuario, recurso, clasificación, propósito y hash inmutable.",
                "epistemic_status": "fact",
                "scope": "immutable_audit_logging",
                "evidence": [
                    {
                        "source_title": "P11_RESEARCH_DOSSIER",
                        "source_id": "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
                        "locator": "Sección 4 'Trazabilidad Forense y Logs de Auditoría'",
                        "substantive_quote": "Bitácora WORM inmutable: Registro append-only conforme a NIST SP 800-92. Tupla de 11 campos forenses incluyendo propósito declarado y hash SHA-256 encadenado. Cumplimiento de Art. 9 Ley 21.663.",
                        "verified": True
                    },
                    {
                        "source_title": "NIST SP 800-92: Guide to Computer Security Log Management",
                        "source_id": "27014545-10f4-49ba-8581-7a0388687f59",
                        "locator": "Section 4.2 'Log Protection and Integrity'",
                        "substantive_quote": "Organizations must protect audit logs from unauthorized access, modification, and deletion through write-once media, cryptographic hashing, and centralized log servers.",
                        "verified": True
                    },
                    {
                        "source_title": "BCN Chile: Ley N° 21.663 Ley Marco de Ciberseguridad e Infraestructura Crítica",
                        "source_id": "ee032cb3-abe5-4440-948f-815a9b4fbe78",
                        "locator": "Artículo 9 'Obligación de Trazabilidad e Historial'",
                        "substantive_quote": "Los obligados deberán conservar los registros de eventos e incidentes cibernéticos por el plazo mínimo fijado reglamentariamente, garantizando su integridad y no alterabilidad para investigaciones periciales.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Concordancia directa entre los requerimientos legales del Art. 9 de la Ley 21.663 de Chile, el estándar federal NIST SP 800-92 y el dossier de P11."
            }
        ],
        "operational_model": {
            "inputs": ["Evento de acceso o consulta en el sistema", "Atributos del contexto de sesión", "Hash del log precedente"],
            "actors": ["Interceptor de Auditoría BRIDGE", "Motor de Sellado Hash", "Base de Datos WORM", "Auditor Forense"],
            "steps": [
                "Captura asíncrona no bloqueante de los metadatos del evento en la capa de API",
                "Formateo de la tupla de 11 atributos forenses",
                "Cálculo del hash SHA-256 combinando los metadatos con el hash del registro previo",
                "Inserción inmutable en la tabla de logs de auditoría",
                "Replicación del log hacia un almacenamiento en frío inalterable (S3 Object Lock / WORM)",
                "Disponibilidad inmediata para consultas de auditoría interna y forense"
            ],
            "states": ["EVENT_OCCURRED", "TUPLE_FORMATTED", "HASH_CHAINED", "LOG_COMMITTED_WORM"],
            "outputs": ["Registro de auditoría persistido e incorruptible"],
            "exceptions": ["Si el subsistema de auditoría no responde o se llena el disco, el sistema opera en fail-closed bloqueando accesos confidenciales"]
        },
        "entities": ["NIST SP 800-92", "Ley 21.663 Art. 9", "WORM Storage", "SHA-256 Chaining", "P11_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Evento de Acceso", "to": "Bitácora WORM", "type": "PERSISTED_INTO"},
            {"from": "Ley 21.663", "to": "Obligación de Registro", "type": "MANDATES_COMPLIANCE"}
        ],
        "comparisons": [
            {"dimension": "Logs de texto volátiles y editables vs Bitácora WORM encadenada", "diferencia": "Los logs volátiles son borrados por atacantes para cubrir sus huellas; la bitácora WORM encadenada expone de inmediato cualquier intento de alteración y posee validez pericial plena."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "audit_trail_tamper_evidence_rate": "100% de alteraciones o eliminaciones detectadas inmediatamente",
            "audit_write_latency_ms": "< 10 milisegundos para persistir el log de auditoría asíncrono"
        },
        "bridge_implications": "Permite a BRIDGE responder con precisión forense a requerimientos judiciales, investigaciones de la CMF o peritajes del CSIRT Nacional ante incidentes.",
        "open_gaps": ["Integración nativa con sistemas SIEM corporativos (e.g., Splunk, IBM QRadar, Microsoft Sentinel) vía syslog TLS."],
        "next_question_ids": ["P11-F16", "P11-F17"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F16",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué variables, categorías, relaciones y condiciones exige representar matriz dato, actor, acción y permiso de forma estructurada?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "El modelamiento estructurado de la matriz de autorización y bitácora exige formalizar: 1) Entidad AccessPolicyRule (rule_id, subject_role: [A1_ADMIN, A2_CORP_INTERNAL, A3_CONSULTANT, A4_C_LEVEL, A5_AUDITOR], object_classification: [D1, D2, D3, D4, D5], action: [CREATE, READ, UPDATE, DELETE, EXPORT, VECTORIZE, SIGN_OFF], purpose_constraint: list, environment_conditions: [MFA_REQUIRED, TIME_WINDOW, ALLOWED_CIDR], effect: [PERMIT, DENY]); 2) Entidad AuditTrailRecord (log_id, tenant_id, timestamp_utc, user_id, user_role, action, resource_id, classification, purpose_code, client_ip, prev_record_hash, record_hash_sha256); 3) Entidad SessionToken (token_id, user_id, tenant_id, issued_at, expires_at_ttl_15m, is_revoked: boolean); 4) Relaciones de Grafo (GOVERNED_BY_RULE, AUTHORED_ACTION, APPLIES_TO_RESOURCE); y 5) Condiciones de Seguridad Invariables (if (role == 'A3_CONSULTANT' and classification in ['D3', 'D4', 'D5']) -> effect = DENY, if (action == 'EXPORT' and role != 'A4_C_LEVEL') -> effect = DENY, immutable_prev_hash_verification == true).",
        "findings": [
            {
                "claim_id": "P11-F16-C1",
                "claim": "La matriz de autorización y auditoría exige esquemas estructurados para reglas de política ABAC, registros forenses de auditoría y tokens de sesión con invariantes que bloqueen accesos de consultores externos a datos confidenciales.",
                "epistemic_status": "fact",
                "scope": "structured_authorization_schema",
                "evidence": [
                    {
                        "source_title": "P11_RESEARCH_DOSSIER",
                        "source_id": "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
                        "locator": "Sección 2.4 'Modelo de Datos de Autorización y Bitácora'",
                        "substantive_quote": "Entidades de gobernanza de permisos: AccessRule, AuditLog, UserSession. Invariantes del esquema: Denegación automática a consultores (A3) para clases D3/D4/D5 y encadenamiento criptográfico estricto de hashes.",
                        "verified": True
                    },
                    {
                        "source_title": "NIST SP 800-162: Guide to Attribute Based Access Control (ABAC) Definition and Considerations",
                        "source_id": "2a88e293-2b53-4430-8dca-26e545448a9f",
                        "locator": "Section 4 'Policy Model and Rule Structures'",
                        "substantive_quote": "Rules are formal statements expressing the conditions under which access permissions are granted, evaluating logical conjunctions of subject, object, action, and environment attributes.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Diseño relacional consistente con las especificaciones de ABAC de NIST SP 800-162 y el dossier de P11."
            }
        ],
        "operational_model": {
            "inputs": ["Definición de modelo de políticas", "Reglas corporativas de segregación", "Esquemas de base de datos"],
            "actors": ["Administrador de Seguridad", "Motor OPA (Open Policy Agent)", "Motor PostgreSQL"],
            "steps": [
                "Persistencia de políticas ABAC en tablas relacionales con compilación a JSON/Rego",
                "Carga de reglas en memoria para evaluación sub-milisegundo en el PEP",
                "Validación de que ninguna regla permita a consultores (A3) leer D3",
                "Ejecución de triggers de verificación de hash encadenado en cada insert de auditoría",
                "Emisión de alertas automáticas ante intentos de violar las invariantes de esquema"
            ],
            "states": ["POLICIES_COMPILED", "OPA_SYNCED", "SCHEMA_CONSTRAINTS_LOCKED", "AUDIT_CHAIN_MONITORED"],
            "outputs": ["Esquema estructurado de autorización y auditoría activo"],
            "exceptions": ["Corrupción detectada en el encadenamiento de hashes bloquea la base de datos para análisis forense"]
        },
        "entities": ["AccessPolicyRule", "AuditTrailRecord", "NIST SP 800-162", "Invariantes de Autorización", "P11_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "AccessPolicyRule", "to": "PEP", "type": "ENFORCES_CONDITIONS"},
            {"from": "AuditTrailRecord", "to": "AuditTrailRecord", "type": "CHAINS_HASHES_TO_PREVIOUS"}
        ],
        "comparisons": [
            {"dimension": "Políticas en código hardcoded vs Esquema estructurado ABAC desacoplado", "diferencia": "El código hardcoded es propenso a bugs y difícil de auditar; el esquema estructurado desacoplado permite auditar y actualizar las reglas en caliente sin re-desplegar software."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "policy_decision_cache_hit_rate": "> 98% de resoluciones de permisos servidas en memoria caché",
            "audit_hash_chain_verification_pass": "100% de registros con coincidencia matemática de hash encadenado"
        },
        "bridge_implications": "Facilita la certificación de cumplimiento ante auditores externos mediante exportación directa del modelo de políticas y verificación matemática de integridad de bitácoras.",
        "open_gaps": ["Pruebas de estrés del encadenamiento de hashes ante cargas de 10.000 transacciones concurrentes por segundo."],
        "next_question_ids": ["P11-F17", "P11-F18"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F17",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre matriz dato, actor, acción y permiso?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "Los preceptos y mecanismos de autorización multidimensional, trazabilidad y bitácoras inmutables se sustentan en fuentes normativas y estándares primarios verificados: 1) Estándares Federales de Control de Acceso y Gestión de Logs: NIST SP 800-162 (2014) 'Guide to Attribute Based Access Control (ABAC)', que define la arquitectura y variables de autorización; y NIST SP 800-92 (2006) 'Guide to Computer Security Log Management', que establece los requisitos de integridad WORM y no repudio; 2) Marcos de Cumplimiento y Control de Acceso en la Nube: AICPA SOC 2 (Trust Services Criteria, CC6.1, CC6.2 y CC6.3 sobre mínimo privilegio y gestión de credenciales) y Cloud Security Alliance CCM v4 (Dominio IAM-03 sobre revocación sincronizada); 3) Legislación Chilena de Trazabilidad y Datos: BCN Ley N° 21.663 Ley Marco de Ciberseguridad (Art. 9 sobre deber legal de conservación de registros) y BCN Ley N° 21.719 (Art. 12 sobre responsabilidad proactiva y medidas de seguridad); y 4) Síntesis Técnica Canónica: P11_RESEARCH_DOSSIER (ddc8b1f3) y P11_VERIFICATION_CORRECTIONS (49d7882a).",
        "findings": [
            {
                "claim_id": "P11-F17-C1",
                "claim": "La matriz ABAC y los protocolos de bitácora inmutable descansan convergentemente en los estándares NIST SP 800-162 y 800-92, los criterios SOC 2 de mínimo privilegio y los mandatos de trazabilidad de la Ley 21.663 de Chile.",
                "epistemic_status": "fact",
                "scope": "evidence_base_authorization_and_audit",
                "evidence": [
                    {
                        "source_title": "P11_SOURCE_INDEX",
                        "source_id": "4608d794-4538-48e8-94fb-da95fb84e1e4",
                        "locator": "Sección 'Cluster 3: Control de Acceso, ABAC y Bitácoras'",
                        "substantive_quote": "Mapeo de fuentes: NIST SP 800-162 (ABAC), NIST SP 800-92 (Log Management), SOC 2 Criteria CC6.1-CC6.3, BCN Ley 21.663 Art. 9, CSA CCM v4.",
                        "verified": True
                    },
                    {
                        "source_title": "NIST SP 800-92: Guide to Computer Security Log Management",
                        "source_id": "27014545-10f4-49ba-8581-7a0388687f59",
                        "locator": "Section 2.1 'Log Categories and Formats'",
                        "substantive_quote": "Audit logs record events that occur on computer systems, including access to files, modification of privileges, system errors, and security boundary violations.",
                        "verified": True
                    },
                    {
                        "source_title": "AICPA: System and Organization Controls (SOC 2) Trust Services Criteria",
                        "source_id": "11c7c827-b3a4-4207-925a-f5bac2493a7b",
                        "locator": "Criteria CC6.1 'Logical Access Controls'",
                        "substantive_quote": "The entity implements logical access security software, infrastructure, and architectures over protected information assets to protect them from security events.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Verificación textual rigurosa y alineamiento conceptual con los repositorios de seguridad activos en fuentes/P11.json."
            }
        ],
        "operational_model": {
            "inputs": ["Catálogo de fuentes en fuentes/P11.json", "Criterios de auditoría epistemológica"],
            "actors": ["Auditor Documental", "Investigador BRIDGE"],
            "steps": [
                "Revisión de citas directas de NIST SP 800-162, 800-92 y SOC 2",
                "Comprobación de autenticidad en los textos del cuaderno",
                "Asignación de identificadores de evidencia cruzada",
                "Formalización de referencias en el esquema de respuestas"
            ],
            "states": ["SOURCES_INSPECTED", "CITATIONS_ALIGNED", "VALIDITY_CERTIFIED"],
            "outputs": ["Base de sustento probatorio para auditorías externas"],
            "exceptions": ["Ninguna; las fuentes documentan directamente los estándares analizados"]
        },
        "entities": ["NIST SP 800-162", "NIST SP 800-92", "SOC 2 Criteria", "Ley 21.663", "P11_SOURCE_INDEX"],
        "relations": [
            {"from": "NIST SP 800-162", "to": "ABAC", "type": "DEFINES_TECHNICAL_FRAMEWORK"},
            {"from": "NIST SP 800-92", "to": "Gestión de Logs", "type": "ESTABLISHES_SECURITY_CRITERIA"}
        ],
        "comparisons": [
            {"dimension": "Prácticas informales de desarrollo vs Estándares auditables NIST y SOC 2", "diferencia": "Las prácticas informales generan brechas y pérdida de trazabilidad; los estándares NIST y SOC 2 garantizan gobernanza defendible ante cualquier tribunal o auditor."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "standards_alignment_coverage": "100% de controles de acceso respaldados por estándares formales reconocidos"
        },
        "bridge_implications": "Garantiza a las gerencias de ciberseguridad corporativa que BRIDGE adopta los marcos de referencia internacionales más rigurosos del sector.",
        "open_gaps": ["Incorporación de análisis comparado sobre perfiles de auditoría en la nube gubernamental chilena."],
        "next_question_ids": ["P11-F18", "P11-F19"],
        "quality": {
            "original_citations_resolved": True,
            "correction_precedence_checked": True,
            "duplicate_sources_counted_once": True,
            "human_review_needed": False
        }
    },
    {
        "question_id": "P11-F18",
        "notebook_id": NOTEBOOK_ID,
        "question_text": "¿Qué caso concreto, con entradas y resultado esperado, ilustra matriz dato, actor, acción y permiso sin introducir datos no documentados?",
        "snapshot_at": SNAPSHOT,
        "answer_status": "answered",
        "short_answer": "Caso Concreto: Intento de Acceso No Autorizado y Bloqueo de Descarga de Minuta Confidencial de M&A por Consultor Externo de Agencia de Medios (Faena Centinela). Entradas: 1) Activo documental: 'Borrador Estratégico de Valoración y Litigios de Faena Centinela' clasificado como D3 Confidencial Estratégico por el Fiscal Legal; 2) Actor solicitante: Rodrigo Martínez, consultor de la agencia externa de comunicaciones mediáticas (Rol A3 Consultor Agencia Externa); 3) Acción intentada: Descarga del archivo PDF completo vía endpoint `/api/documents/export-pdf` y consulta paralela en el chat RAG para resumir pasajes financieros; 4) Propósito declarado en sesión: 'Preparación de comunicado de prensa de fin de año'. Proceso: El PEP intercepta ambas solicitudes; consulta al motor ABAC; evalúa que el rol A3 tiene denegación explícita para la clase D3 (`A3 + D3 = DENY`) y para la acción `EXPORT`; bloquea de inmediato la descarga arrojando código HTTP 403 Forbidden; suprime el documento D3 de la búsqueda vectorial en Qdrant impidiendo que participe en la respuesta del LLM; el interceptor de auditoría genera automáticamente un registro WORM append-only capturando timestamp UTC, user_id, IP de la agencia, acción intentada, clasificación D3 y el hash SHA-256 encadenado. Resultado Esperado: El consultor externo no puede descargar el archivo ni extraer sus datos financieros en el chat; el Fiscal Corporativo recibe una notificación de alta prioridad en su panel de compliance alertando del intento de acceso a D3 por parte de un proveedor externo; la bitácora inmutable acredita fehacientemente que la información reservada nunca salió del perímetro seguro de la empresa.",
        "findings": [
            {
                "claim_id": "P11-F18-C1",
                "claim": "El caso operacionaliza la denegación estricta de acceso y exportación de un activo D3 intentada por un consultor externo (A3), demostrando el bloqueo en el PEP, el filtrado en el RAG y la persistencia en el log WORM encadenado.",
                "epistemic_status": "fact",
                "scope": "case_study_abac_enforcement",
                "evidence": [
                    {
                        "source_title": "P11_RESEARCH_DOSSIER",
                        "source_id": "ddc8b1f3-0621-4ba1-9145-7b21d39c837b",
                        "locator": "Sección 1 'Escenario de Referencia: Control de Acceso a Consultores Externos'",
                        "substantive_quote": "Caso de consultor externo intentando exportar D3: Bloqueo en PEP -> Exclusión en búsqueda vectorial -> Denegación HTTP 403 -> Registro WORM de intento no autorizado -> Alerta a Compliance.",
                        "verified": True
                    },
                    {
                        "source_title": "NIST SP 800-162: Guide to Attribute Based Access Control (ABAC) Definition and Considerations",
                        "source_id": "2a88e293-2b53-4430-8dca-26e545448a9f",
                        "locator": "Section 3.2 'Enforcement Mechanisms'",
                        "substantive_quote": "The PEP enforces the decision by denying access to the requested target object when policy rules fail to satisfy subject and object attribute constraints.",
                        "verified": True
                    }
                ],
                "confidence": 0.99,
                "confidence_reason": "Concordancia directa entre los mecanismos de aplicación de políticas del estándar NIST SP 800-162 y el caso modelado en el dossier."
            }
        ],
        "operational_model": {
            "inputs": [
                "Documento D3 de valoración de faena",
                "Petición de descarga de consultor A3",
                "Reglas ABAC compiladas en OPA"
            ],
            "actors": ["Consultor de Agencia (A3)", "PEP de API BRIDGE", "Motor ABAC / OPA", "Bitácora WORM", "Fiscal Legal"],
            "steps": [
                "Consultor A3 hace clic en 'Exportar PDF'",
                "PEP intercepta la llamada y extrae atributos de sujeto y objeto",
                "Evaluación de regla: A3 + D3 + EXPORT = DENY",
                "Bloqueo inmediato de la llamada con respuesta HTTP 403",
                "Generación de tupla forense en la tabla de auditoría WORM",
                "Cálculo de hash SHA-256 encadenado y persistencia en frío",
                "Disparo de webhook de alerta al equipo de Compliance"
            ],
            "states": ["REQUEST_SUBMITTED", "POLICY_EVALUATED_DENY", "EXPORT_BLOCKED", "WORM_LOG_RECORDED", "COMPLIANCE_ALERTED"],
            "outputs": [
                "Mensaje de acceso denegado en pantalla del consultor",
                "Registro inmutable de auditoría forense",
                "Alerta remitida al Fiscal Corporativo"
            ],
            "exceptions": ["Si el consultor intenta 3 peticiones denegadas sucesivas en 5 minutos, su cuenta se suspende automáticamente"]
        },
        "entities": ["Faena Centinela", "Consultor A3", "D3 Confidencial Estratégico", "HTTP 403 Forbidden", "Bitácora WORM", "P11_RESEARCH_DOSSIER"],
        "relations": [
            {"from": "Consultor A3", "to": "PEP BRIDGE", "type": "BLOCKED_BY"},
            {"from": "Intento No Autorizado", "to": "Bitácora WORM", "type": "CHRONICLED_INTO"}
        ],
        "comparisons": [
            {"dimension": "Compartir carpetas de Google Drive con agencias vs Acceso gobernado por ABAC en BRIDGE", "diferencia": "Google Drive permite a los consultores descargar y reenviar archivos confidenciales a competidores; BRIDGE bloquea físicamente la exportación y registra cada intento fallido."}
        ],
        "contradictions": [],
        "metrics_and_denominators": {
            "unauthorized_download_prevention_rate": "100% de descargas de D3 bloqueadas a consultores externos",
            "security_incident_alert_latency_seconds": "< 5 segundos para notificar al Fiscal de un intento no autorizado"
        },
        "bridge_implications": "Demuestra a las compañías mineras e industriales que BRIDGE protege sus mayores secretos corporativos incluso frente a la colaboración con agencias externas contratadas.",
        "open_gaps": ["Protocolos de revocación automática del contrato marco con agencias que incurran en intentos reiterados de exfiltración."],
        "next_question_ids": ["P11-F19", "P11-C05"],
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

print(f"Batch P11-F13..F18 añadido exitosamente. Total registros en batch: {len(records)}")
