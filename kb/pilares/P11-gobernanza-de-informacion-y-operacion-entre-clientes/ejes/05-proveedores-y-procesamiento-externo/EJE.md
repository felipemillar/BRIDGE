<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 05-proveedores-y-procesamiento-externo: Proveedores y procesamiento externo

**Pilar:** [P11 — Gobernanza de información y operación entre clientes](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### P11-C09: ¿Dónde discrepan fuentes originales y síntesis internas sobre proveedores y procesamiento externo, y qué versión prevalece según las correcciones?

> La discrepancia fundamental sobre proveedores externos estriba en la naturaleza de sus garantías de privacidad y en los documentos contractuales vigentes: el dossier inicial (`P11_RESEARCH_DOSSIER`) y síntesis preliminares (`P11_PENDING_SOURCES_RESOLUTION`) asumían que las declaraciones públicas de

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C09.json](P11-C09.json)
### P11-C10: ¿Qué sigue sin prueba sobre proveedores y procesamiento externo, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> En el procesamiento externo con proveedores cloud: 1) Lo que sigue sin prueba empírica: El cumplimiento efectivo y continuo de la política de 'Zero Retention' en la memoria volátil y cachés intermedias de inferencia de los proveedores de LLMs (ej. AWS Bedrock, Azure OpenAI, Vertex AI) durante contin

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C10.json](P11-C10.json)
### P11-F25: ¿Qué datos recibe cada proveedor de IA, búsqueda, monitoreo y almacenamiento?

> La arquitectura de BRIDGE aplica un principio estricto de minimización de datos (Data Minimization) que delimita con precisión el payload que recibe cada categoría de proveedor externo: 1) Proveedores de Inferencia de IA (AWS Bedrock, Azure OpenAI Service, Google Cloud Vertex AI, Anthropic Commercia

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F25.json](P11-F25.json)
### P11-F26: ¿Qué cláusulas, regiones de procesamiento y condiciones de entrenamiento aparecen en términos directos?

> Los contratos de servicios y acuerdos de procesamiento de datos de los proveedores enterprise directos estipulan con claridad: 1) Cláusula de No Entrenamiento (No-Training Commitment): OpenAI Services Agreement (Sección 4.2, versión 01-01-2026 oficial en PDF) establece textualmente que OpenAI no uti

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F26.json](P11-F26.json)
### P11-F27: ¿Qué respuesta de debida diligencia sigue pendiente de confirmación contractual?

> En los procesos de debida diligencia de ciberseguridad y contratación de proveedores de IA de frontera, existen 3 puntos críticos que permanecen como preguntas abiertas o pendientes de confirmación contractual exhaustiva: 1) SLA Específico para Notificación de Brechas de Seguridad: Proveedores como

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F27.json](P11-F27.json)
### P11-F28: ¿Qué variables, categorías, relaciones y condiciones exige representar proveedores y procesamiento externo de forma estructurada?

> El modelamiento estructurado de proveedores externos y transferencias de datos exige representar: 1) Entidad CloudProvider (provider_id, provider_name: [AWS_BEDROCK, AZURE_OPENAI, VERTEX_AI, ANTHROPIC, OPENAI_API, QDRANT_CLOUD], contract_tier: [ENTERPRISE_B2B, STANDARD], dpa_signed: boolean, no_trai

- **Verificación:** verificada: 1
- **Registro:** [P11-F28.json](P11-F28.json)
### P11-F29: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre proveedores y procesamiento externo?

> Los hechos, términos contractuales y compromisos sobre proveedores de IA y procesamiento externo se sustentan en fuentes primarias verificadas: 1) Contratos Oficiales de Proveedores de IA (Versiones Vigentes 2026 en PDF): OpenAI Services Agreement (Sección 4.2 en PDF oficial `8d9a7ceb`) y OpenAI Dat

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F29.json](P11-F29.json)
### P11-F30: ¿Qué caso concreto, con entradas y resultado esperado, ilustra proveedores y procesamiento externo sin introducir datos no documentados?

> Caso Concreto: Generación de Resumen Ejecutivo Asistido por IA mediante API Enterprise de AWS Bedrock para Minera Candelaria. Entradas: 1) Activo documental: 'Informe de Diagnóstico Social y Relaciones Laborales de Faena Candelaria' clasificado como D2 Interno por el Gerente de Recursos Humanos; 2)

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F30.json](P11-F30.json)

