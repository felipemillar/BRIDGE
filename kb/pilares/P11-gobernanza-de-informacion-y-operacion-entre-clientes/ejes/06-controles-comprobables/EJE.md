<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 06-controles-comprobables: Controles comprobables

**Pilar:** [P11 — Gobernanza de información y operación entre clientes](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### P11-C11: ¿Dónde discrepan fuentes originales y síntesis internas sobre controles comprobables, y qué versión prevalece según las correcciones?

> La discrepancia principal sobre controles comprobables radica en la suficiencia probatoria atribuida a informes estáticos versus pruebas dinámicas en código: las versiones exploratorias del dossier (`P11_RESEARCH_DOSSIER`) asumían que contar con una certificación ISO 27001 o un informe SOC 2 Type I

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C11.json](P11-C11.json)
### P11-C12: ¿Qué sigue sin prueba sobre controles comprobables, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> En el dominio de controles comprobables: 1) Lo que sigue sin prueba empírica: La verificación formal de controles de aislamiento en flujos multi-agente recursivos donde múltiples agentes autónomos encadenan invocaciones dinámicas de herramientas (tools), generando llamadas a sub-modelos o conectores

- **Verificación:** verificada: 1
- **Registro:** [P11-C12.json](P11-C12.json)
### P11-F31: ¿Qué pruebas muestran cifrado, segregación, registro, control de acceso y respuesta a incidentes?

> La arquitectura técnica de BRIDGE proporciona evidencias empíricas y verificables en los cinco dominios críticos de seguridad: 1) Cifrado: Envelope encryption demostrado mediante uso de Customer Managed Keys (CMK) independientes por tenant en AWS KMS / Cloud KMS (AES-256-GCM), cifrado en tránsito va

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F31.json](P11-F31.json)
### P11-F32: ¿Qué diferencia una afirmación de marketing de un control probado o certificación vigente?

> La distinción entre afirmaciones comerciales y garantías técnicas auditables es un pilar metodológico y epistémico de BRIDGE, ratificado canónicamente en las directrices rectoras `P11_VERIFICATION_CORRECTIONS` y `P11_2026_LAW_AND_PROVIDER_CORRECTION`: 1) Afirmación de Marketing: Es una declaración u

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F32.json](P11-F32.json)
### P11-F33: ¿Qué evidencia necesitaría un cliente para aceptar un piloto con sus documentos?

> Para autorizar la ingesta y procesamiento de sus documentos corporativos en un entorno de piloto productivo, un cliente enterprise (banca, minería, utilities, retail) exige un 'Paquete de Evidencia y Confianza Técnica' compuesto por seis artefactos formales indispensables: 1) Acuerdo de Procesamient

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F33.json](P11-F33.json)
### P11-F34: ¿Qué variables, categorías, relaciones y condiciones exige representar controles comprobables de forma estructurada?

> Representar controles de seguridad comprobables de forma estructurada exige un modelo de datos formal fundamentado en los catálogos estandarizados de NIST SP 800-53 Rev. 5, AICPA SOC 2 y Cloud Security Alliance (CCM v4), compuesto por seis entidades principales: 1) `ControlDef`: Define el control té

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F34.json](P11-F34.json)
### P11-F35: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre controles comprobables?

> Los hechos, criterios y requerimientos técnicos sobre controles comprobables están fundamentados en una matriz exhaustiva de fuentes originales primarias y síntesis canónicas rectoras: 1) AICPA SOC 2 Trust Services Criteria (2022/2024): Sustenta los criterios de evaluación de seguridad, disponibilid

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F35.json](P11-F35.json)
### P11-F36: ¿Qué caso concreto, con entradas y resultado esperado, ilustra controles comprobables sin introducir datos no documentados?

> El funcionamiento y verificación de controles comprobables se ilustra mediante el caso operacional concreto 'Auditoría Previa a Piloto de Banco Corporativo: Verificación de Aislamiento de Embeddings y Criptografía de Llaves'. En este escenario: 1) Entradas: Tenant A ('Banco Santander Chile', `tenant

- **Verificación:** verificada: 1
- **Registro:** [P11-F36.json](P11-F36.json)

