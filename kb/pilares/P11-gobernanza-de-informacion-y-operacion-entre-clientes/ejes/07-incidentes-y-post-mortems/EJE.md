<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 07-incidentes-y-post-mortems: Incidentes y post-mortems

**Pilar:** [P11 — Gobernanza de información y operación entre clientes](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### P11-C13: ¿Dónde discrepan fuentes originales y síntesis internas sobre incidentes y post-mortems, y qué versión prevalece según las correcciones?

> La discrepancia esencial en incidentes y post-mortems se focaliza en los plazos legales de reporte y en el tratamiento de los datos del incidente: las versiones preliminares del dossier (`P11_RESEARCH_DOSSIER`) proponían un protocolo genérico de comunicación que fijaba plazos difusos como 'notificar

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C13.json](P11-C13.json)
### P11-C14: ¿Qué sigue sin prueba sobre incidentes y post-mortems, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> En la gestión de incidentes y post-mortems: 1) Lo que sigue sin prueba empírica: La capacidad técnica para detectar y neutralizar ataques avanzados de 'Exfiltración Esteganográfica en Salidas de LLMs' (In-Context Steganography), donde un prompt inyectado instruye al modelo a fugar información sensib

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C14.json](P11-C14.json)
### P11-F37: ¿Cómo detectar una cita a documento ajeno, un permiso desactualizado o un prompt malicioso?

> La detección de anomalías operacionales y brechas de seguridad en BRIDGE se implementa mediante tres subsistemas de inspección especializada en tiempo de ejecución: 1) Cita a Documento Ajeno (Cross-Tenant Citation Leak): El módulo post-generación 'CitationCrossTenantScrubber' intercepta la respuesta

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F37.json](P11-F37.json)
### P11-F38: ¿Qué secuencia de contención, comunicación y aprendizaje correspondería a cada fallo?

> Ante la materialización o detección de un fallo de seguridad, BRIDGE activa un Playbook de Respuesta a Incidentes estrictamente gobernado por el marco NIST SP 800-61 Rev. 3 y alineado con los plazos legales de Chile (Ley 21.663 de Ciberseguridad y Ley 21.719 de Protección de Datos Personales en vaca

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F38.json](P11-F38.json)
### P11-F39: ¿Cómo incorporar lecciones sin exponer datos del incidente en el sistema compartido?

> La incorporación de aprendizajes y lecciones aprendidas tras un incidente debe realizarse bajo el 'Protocolo de Descontaminación y Abstracción de Post-Mortems', garantizando que jamás se filtren datos confidenciales D3/D5 o datos personales D4 en repositorios comunes, tickets de soporte o modelos de

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F39.json](P11-F39.json)
### P11-F40: ¿Qué variables, categorías, relaciones y condiciones exige representar incidentes y post-mortems de forma estructurada?

> La representación estructurada de incidentes y post-mortems exige un modelo de datos formal de gestión de crisis y aseguramiento de calidad, estructurado en seis entidades principales: 1) `IncidentRecord`: Modela el evento anómalo (`incident_id`, `tenant_id` [o 'multi_tenant' si afecta la plataforma

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F40.json](P11-F40.json)
### P11-F41: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre incidentes y post-mortems?

> Los hechos, criterios y obligaciones operativas sobre gestión de incidentes y post-mortems están fundamentados en una sólida red de fuentes primarias vinculantes y estándares técnicos globales: 1) NIST SP 800-61 Rev. 3 (2024): Guía de referencia sobre el ciclo de vida de manejo de incidentes de cibe

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F41.json](P11-F41.json)
### P11-F42: ¿Qué caso concreto, con entradas y resultado esperado, ilustra incidentes y post-mortems sin introducir datos no documentados?

> El ciclo integral de incidentes y post-mortems se demuestra en el caso concreto 'Detección y Contención Automatizada de un Ataque de Prompt Injection Indirecto con Intento de Exfiltración Cross-Tenant'. En este caso: 1) Entradas: Un usuario legítimo de Tenant B ('Empresa Retail B', `tenant_id: retai

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F42.json](P11-F42.json)

