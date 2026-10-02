<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 05-estados-versiones-y-auditoria: Estados, versiones y auditoría

**Pilar:** [P10 — Gestión y aprobación de la comunicación corporativa](../../TARJETA.md)  
**Módulo:** Hablar

---

## Preguntas del Eje (8)

### P10-C09: ¿Dónde discrepan fuentes originales y síntesis internas sobre estados, versiones y auditoría, y qué versión prevalece según las correcciones?

> La discrepancia esencial se centraba en el tratamiento de errores publicados: Síntesis internas preliminares asumían la práctica informal de 'edición silenciosa' (stealth editing), corrigiendo la errata directamente en la página web institucional sin dejar constancia visible; por el contrario, los e

- **Verificación:** no_verificada: 1
- **Registro:** [P10-C09.json](P10-C09.json)
### P10-C10: ¿Qué sigue sin prueba sobre estados, versiones y auditoría, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> 1) Lo que sigue sin prueba empírica suficiente es la preservación de integridad de auditoría y no repudio sobre activos multimedia generados por IA (videos explicativos sintéticos, audios clonados) a lo largo de ciclos de archivo de más de 10 años frente a la obsolescencia criptográfica; 2) Fuentes

- **Verificación:** no_verificada: 1
- **Registro:** [P10-C10.json](P10-C10.json)
### P10-F25: ¿Qué estados debe recorrer un mensaje desde borrador hasta retiro o corrección?

> El ciclo de vida del mensaje institucional en un System of Record se modela mediante una Máquina de Estados Finita (FSM) rigurosa que recorre 9 estados principales y 4 estados de contingencia: 1) DRAFT_INGESTION (recepción de la solicitud y creación de ticket); 2) TRIAGED (clasificación de régimen,

- **Verificación:** no_verificada: 1
- **Registro:** [P10-F25.json](P10-F25.json)
### P10-F26: ¿Cómo se conservan versiones, motivos de cambio y firmas de aprobación?

> La conservación y auditabilidad de versiones se rige por un esquema de libro mayor inmutable (append-only ledger) y control semántico de cambios: 1) Numeración Semántica de Versiones: Se dividen en Versiones Menores (v1.x: ajustes estilísticos, ortografía, formato de canal; aprobables por Jefe de Pr

- **Verificación:** no_verificada: 1
- **Registro:** [P10-F26.json](P10-F26.json)
### P10-F27: ¿Qué ocurre cuando nueva evidencia invalida un mensaje ya publicado?

> Cuando surge nueva evidencia técnica, operacional o pericial que invalida las afirmaciones de un mensaje en estado PUBLISHED_LIVE, el protocolo corporativo prohíbe terminantemente la 'eliminación silenciosa' (silent deletion/stealth editing) y activa el flujo formal de rectificación en 5 pasos: 1) M

- **Verificación:** no_verificada: 1
- **Registro:** [P10-F27.json](P10-F27.json)
### P10-F28: ¿Qué variables, categorías, relaciones y condiciones exige representar estados, versiones y auditoría de forma estructurada?

> La representación estructurada del ciclo de vida, versionado y auditoría requiere un esquema de datos relacional y temporal riguroso: 1) Entidad MessageLifecycleState (state_id, state_name, state_type: [ACTIVE, STAGED, PUBLISHED, RETRACTED, ARCHIVED], entered_at, exited_at, triggered_by_user_id); 2)

- **Verificación:** no_verificada: 1
- **Registro:** [P10-F28.json](P10-F28.json)
### P10-F29: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre estados, versiones y auditoría?

> Los preceptos técnicos, éticos y operacionales sobre estados, versionado y auditoría se fundamentan en fuentes primarias verificadas: 1) Estándares éticos internacionales de corrección y retractación: COPE (Committee on Publication Ethics, 2021) 'Retraction Guidelines', que fija el mandato de no bor

- **Verificación:** no_verificada: 1
- **Registro:** [P10-F29.json](P10-F29.json)
### P10-F30: ¿Qué caso concreto, con entradas y resultado esperado, ilustra estados, versiones y auditoría sin introducir datos no documentados?

> Caso Concreto: Detección y Rectificación de Error en Cifra de Emisiones en Comunicado de Sostenibilidad. Entradas: 1) Comunicado v1.0 publicado hace 48 horas anunciando 'Reducción del 35% en emisiones de alcance 1 en Faena Centinela'; 2) Hallazgo de auditoría técnica interna: La cifra auditada certi

- **Verificación:** no_verificada: 1
- **Registro:** [P10-F30.json](P10-F30.json)

