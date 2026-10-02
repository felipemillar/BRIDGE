<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 02-separacion-entre-clientes: Separación entre clientes

**Pilar:** [P11 — Gobernanza de información y operación entre clientes](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### P11-C03: ¿Dónde discrepan fuentes originales y síntesis internas sobre separación entre clientes, y qué versión prevalece según las correcciones?

> La discrepancia principal sobre separación entre clientes estriba en el nivel de confianza otorgado al aislamiento en capas superiores versus el aislamiento en motor de datos: las versiones preliminares del dossier (`P11_RESEARCH_DOSSIER` y borradores de síntesis) postulaban que el aislamiento multi

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C03.json](P11-C03.json)
### P11-C04: ¿Qué sigue sin prueba sobre separación entre clientes, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> En la separación entre clientes: 1) Lo que sigue sin prueba empírica concluyente: La inmunidad del sistema ante ataques de inversión de embeddings (reconstrucción textual de fragmentos sensibles a partir de vectores numéricos) y la ausencia total de canales laterales (side-channel attacks basados en

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C04.json](P11-C04.json)
### P11-F07: ¿Qué frontera lógica y operativa impide que datos de un cliente aparezcan en otro?

> La separación entre clientes en BRIDGE se implementa mediante una arquitectura de defensa en profundidad multinivel que articula cuatro fronteras técnicas inquebrantables: 1) Capa de Base de Datos Relacional: PostgreSQL 18 con Row Level Security (RLS) mandatorio (`FORCE ROW LEVEL SECURITY`), donde c

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F07.json](P11-F07.json)
### P11-F08: ¿Cómo se prueba aislamiento en ingesta, índices, caché, conversación, exportación y respaldo?

> El aislamiento entre clientes se verifica empíricamente a través de un protocolo de auditoría continua en 6 planos técnicos: 1) Ingesta: Pruebas de inyección de documentos con metadatos cruzados, validando que el servicio de almacenamiento (S3/GCS) segregue rutas por prefijo restringido con política

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F08.json](P11-F08.json)
### P11-F09: ¿Qué fallos cruzados deben incluirse en pruebas adversariales?

> Las pruebas adversariales y ejercicios de Red Teaming en BRIDGE deben incluir de forma mandatoria 5 vectores de fallo cruzado de alta peligrosidad: 1) Suplantación de Cabeceras e Identidad de Tenant (Tenant ID Spoofing / Header Tampering): Manipulación de cabeceras HTTP (`X-Tenant-ID`) o parámetros

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F09.json](P11-F09.json)
### P11-F10: ¿Qué variables, categorías, relaciones y condiciones exige representar separación entre clientes de forma estructurada?

> La representación estructurada del aislamiento y separación entre clientes exige modelar: 1) Entidad TenantProfile (tenant_id, organization_name, isolation_mode: [POOLED_RLS, DEDICATED_SILO], kms_key_arn, vector_collection_name, redis_namespace_prefix, status: [ACTIVE, SUSPENDED, DELETED]); 2) Entid

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F10.json](P11-F10.json)
### P11-F11: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre separación entre clientes?

> Los hechos, mecanismos y requerimientos de separación entre clientes se fundamentan en fuentes primarias verificadas: 1) Arquitectura y Políticas de Aislamiento SaaS: AWS Whitepapers (2023-2025) 'SaaS Tenant Isolation Strategies', que formaliza los modelos Silo vs Pool y la propagación de contexto d

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F11.json](P11-F11.json)
### P11-F12: ¿Qué caso concreto, con entradas y resultado esperado, ilustra separación entre clientes sin introducir datos no documentados?

> Caso Concreto: Prevención de Fuga de Información Cruzada ante Consulta Idéntica entre Dos Faenas Mineras Competidoras (Minera Collahuasi vs Minera Escondida). Entradas: 1) Tenant Alpha (`COLLAHUASI-CORP`) sube a BRIDGE su borrador confidencial de negociación colectiva con el Sindicato N° 1 (D3 Confi

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F12.json](P11-F12.json)

