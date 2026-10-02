<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 04-ciclo-de-vida-y-retencion: Ciclo de vida y retención

**Pilar:** [P11 — Gobernanza de información y operación entre clientes](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### P11-C07: ¿Dónde discrepan fuentes originales y síntesis internas sobre ciclo de vida y retención, y qué versión prevalece según las correcciones?

> La discrepancia principal sobre ciclo de vida y retención radica en la rigidez de los plazos y en la viabilidad técnica del borrado en IA: las síntesis preliminares del dossier (`P11_RESEARCH_DOSSIER`) proponían plazos estáticos arbitrarios de retención (ej. 'retener 5 años todo documento de cliente

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C07.json](P11-C07.json)
### P11-C08: ¿Qué sigue sin prueba sobre ciclo de vida y retención, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> En el ciclo de vida y retención: 1) Lo que sigue sin prueba empírica: La certeza forense de que la invocación del comando de borrado de vectores (`delete_points` o borrado de colección) en motores de bases de datos vectoriales como Qdrant elimine físicamente los datos de la memoria persistente de fo

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C08.json](P11-C08.json)
### P11-F19: ¿Cómo se ingesta, versiona, archiva, corrige y elimina información según su tipo?

> El ciclo de vida de la información en BRIDGE se modula dinámicamente según la clasificación del activo (D1 a D5): 1) Ingesta: D1 y D2 ingresan por pipelines estándar de texto/metadatos; D3 exige cifrado en tránsito TLS 1.3 y sellado con clave KMS dedicada; D4 pasa por escaneo y tokenización de PII;

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F19.json](P11-F19.json)
### P11-F20: ¿Qué períodos de retención son políticas propuestas y cuáles obligaciones verificadas?

> La gobernanza de retención deslinda con rigor las obligaciones legales verificadas de las políticas propuestas de diseño operativo: 1) Obligaciones Legales Verificadas en Chile: A) Ley N° 20.730 de Lobby: Conservación pública permanente de los registros de audiencias, viajes y donativos de sujetos p

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F20.json](P11-F20.json)
### P11-F21: ¿Cómo se ejecuta una revocación sin dejar copias en resultados o registros?

> La revocación o supresión de un documento (o el ejercicio del 'derecho al olvido' / supresión bajo Ley 21.719 / GDPR Art. 17) sin dejar copias residuales en resultados o memorias de IA se ejecuta mediante un protocolo de purga coordinada en 5 pasos síncronos: 1) Destrucción de la Clave de Cifrado de

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F21.json](P11-F21.json)
### P11-F22: ¿Qué variables, categorías, relaciones y condiciones exige representar ciclo de vida y retención de forma estructurada?

> La representación estructurada del ciclo de vida, retención y sanitización exige modelar: 1) Entidad RetentionSchedule (schedule_id, data_classification: [D1, D2, D3, D4, D5], retention_period_months, retention_type: [STATUTORY_MANDATORY, OPERATIONAL_PROPOSED], legal_authority_source: [LEY_20730, CO

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F22.json](P11-F22.json)
### P11-F23: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ciclo de vida y retención?

> Los hechos, métodos de sanitización y períodos de retención se fundamentan en fuentes normativas y técnicas verificadas: 1) Estándar Federal de Sanitización de Medios: NIST SP 800-88 Rev. 2 (2014) 'Guidelines for Media Sanitization', que define los métodos Clear, Purge, Destroy y valida formalmente

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F23.json](P11-F23.json)
### P11-F24: ¿Qué caso concreto, con entradas y resultado esperado, ilustra ciclo de vida y retención sin introducir datos no documentados?

> Caso Concreto: Ejercicio del Derecho de Supresión de Datos Personales por Ex-Dirigente Vecinal tras Término de Mesa de Diálogo (Comunidad Los Vilos). Entradas: 1) Solicitud formal de ejercicio de derecho de cancelación (supresión) enviada por don Carlos Henríquez, ex-presidente de la Junta de Vecino

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F24.json](P11-F24.json)

