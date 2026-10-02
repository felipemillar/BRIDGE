<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 11-seguridad-en-recuperacion-combinada: Profundización especializada

**Pilar:** [P06 — Cruce de conocimiento interno y señales externas](../../TARJETA.md)  
**Módulo:** Saber

---

## Preguntas del Eje (8)

### P06-X17: ¿Qué ocurre cuando una noticia pública activa una búsqueda sobre documentos internos restringidos?

> Cuando una señal o noticia pública gatilla una recuperación automática que intersecta documentos internos clasificados, la arquitectura de The Bridge Intelligence activa el protocolo de Aislamiento Contextual y Control de Acceso Basado en Atributos (ABAC) con Row-Level Security (Palantir AIP; P11 Mu

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X17.json](P06-X17.json)
### P06-X18: ¿Cómo ofrecer una alerta útil sin revelar la existencia o contenido de un documento protegido?

> Ofrecer una alerta útil preservando la confidencialidad absoluta de documentos protegidos se resuelve mediante el patrón de 'Notificación Ciega de Escalabilidad' (*Blind Escalation Token*) implementado en sistemas de alta seguridad (Palantir AIP; P06_QUALITY_ADDENDUM, Sección 4.2): 1) Detección en S

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X18.json](P06-X18.json)
### P06-X19: ¿Qué pruebas muestran ausencia de contaminación entre clientes y usuarios?

> La ausencia de contaminación cross-tenant y cross-user se certifica mediante una batería de pruebas de regresión adversarial automatizadas en el pipeline de CI/CD (P11 Multi-Tenant Governance; Palantir AIP; P06_QUALITY_ADDENDUM, Sección 4.3): 1) Pruebas de Penetración de Inyección Cruzada (Cross-Ten

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X19.json](P06-X19.json)
### P06-X20: ¿Qué variables, categorías, relaciones y condiciones exige representar seguridad en recuperación combinada de forma estructurada?

> La representación estructurada de la seguridad en recuperación combinada exige modelar: 1) Variables de control de acceso: `user_id`, `tenant_id`, `security_clearance` (D1_Publico, D2_Uso_Interno, D3_Confidencial, D4_Restringido_CMF, D5_Secreto_Industrial), `active_roles` (Viewer, Analyst, CCO, Lega

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X20.json](P06-X20.json)
### P06-X21: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre seguridad en recuperación combinada?

> La seguridad en recuperación combinada se sustenta en las siguientes fuentes verificadas del corpus: 1) Palantir Technologies (2024; 'Palantir AIP: Architecture Overview & Context Engineering', Junio 2024): Documentación oficial de arquitectura industrial, Secciones sobre Context Engineering, Granul

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X21.json](P06-X21.json)
### P06-X22: ¿Qué caso concreto, con entradas y resultado esperado, ilustra seguridad en recuperación combinada sin introducir datos no documentados?

> Caso Concreto CSR-P06-303 (Consulta de Analista Junior ante Rumor de Adquisición): 1) Entradas: Señal Externa ('Portal Financiero', 18-08-2025): 'Rumores indican que Grupo Industrial A negocia la compra de Competidor B por 400M USD'. Documento Interno Protegido ('Acta Extraordinaria de Directorio D4

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X22.json](P06-X22.json)
### P06-X23: ¿Dónde discrepan fuentes originales y síntesis internas sobre seguridad en recuperación combinada, y qué versión prevalece según las correcciones?

> Discrepancia y prevalencia en seguridad de recuperación combinada: 1) Discrepancia: El dossier preliminar P06_RESEARCH_DOSSIER asumía que bastaba con incluir instrucciones en el system prompt del LLM (ej. 'si el usuario no tiene permiso, no menciones el documento reservado X'), confiando en la adher

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X23.json](P06-X23.json)
### P06-X24: ¿Qué sigue sin prueba sobre seguridad en recuperación combinada, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba empírica formal la resistencia de la plataforma ante ataques de inferencia por canales laterales basados en latencia de respuesta o tamaño de respuesta (Side-Channel Timing Attacks) en despliegues compartidos en la nube (P06_GAPS_AND_VALIDATION, Sección 3.4). Las fuentes analizadas

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P06-X24.json](P06-X24.json)

