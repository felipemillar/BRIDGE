<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 04-ciclo-de-vida-y-seguimiento: Ciclo de vida y seguimiento

**Pilar:** [P09 — Memoria de relaciones y gestión de compromisos](../../TARJETA.md)  
**Módulo:** Relacionar

---

## Preguntas del Eje (8)

### P09-C07: ¿Dónde discrepan fuentes originales y síntesis internas sobre ciclo de vida y seguimiento, y qué versión prevalece según las correcciones?

> Discrepancia Principal: En algunas síntesis iniciales se proponía una máquina de estados simplificada de 4 etapas (Pendiente, En Proceso, Cumplido, Cancelado), la cual permitía marcar un compromiso como 'Cumplido' directamente desde 'En Proceso' sin requerir una fase de validación ni verificar la su

- **Verificación:** no_verificada: 1
- **Registro:** [P09-C07.json](P09-C07.json)
### P09-C08: ¿Qué sigue sin prueba sobre ciclo de vida y seguimiento, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Brecha sin Prueba: El corpus no documenta la tasa de lectura y efectividad real de las alertas preventivas despachadas mediante mensajería instantánea (Slack, MS Teams, WhatsApp) frente al correo electrónico tradicional en personal de faena de terreno, existiendo incertidumbre sobre si las notificac

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P09-C08.json](P09-C08.json)
### P09-F19: ¿Qué estados y transiciones cubren propuesta, acuerdo, ejecución, verificación y cierre?

> El ciclo de vida del compromiso se gobierna mediante una máquina de estados finita con 8 estados y transiciones reglamentadas: 1) `PROPUESTO`: Iniciativa planteada en reunión o solicitud vecinal pendiente de análisis de viabilidad técnica y presupuestaria; 2) `APROBADO_ASIGNADO`: Compromiso formaliz

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F19.json](P09-F19.json)
### P09-F20: ¿Qué alertas anticipan incumplimiento o vencimiento sin duplicar tareas?

> El sistema implementa una arquitectura de alertas preventivas no intrusivas basadas en cadencias temporales y umbrales de riesgo, evitando la saturación por correos duplicados: 1) Alerta Temprana T-30: Notificación informativa al dueño del compromiso 30 días antes del vencimiento, recordando el hito

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F20.json](P09-F20.json)
### P09-F21: ¿Cómo se registra un cambio de alcance o renegociación sin borrar el compromiso original?

> La integridad de la memoria institucional y la defensa jurídica exigen un modelo de inmutabilidad append-only para los cambios de alcance: 1) Prohibición de Borrado o Sobrescritura: Queda taxativamente inhabilitada la edición destructiva de registros en base de datos; 2) Congelamiento de Versión Ori

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F21.json](P09-F21.json)
### P09-F22: ¿Qué variables, categorías, relaciones y condiciones exige representar ciclo de vida y seguimiento de forma estructurada?

> La representación estructurada del ciclo de vida y seguimiento exige: 1) Entidad de Hitos: `Entity_Milestone` con atributos (milestone_id, commitment_id, title, due_date, status, completion_percentage, evidence_id); 2) Entidad de Registro de Auditoría: `Entity_AuditTrail` con atributos (audit_id, en

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F22.json](P09-F22.json)
### P09-F23: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ciclo de vida y seguimiento?

> Los hechos relativos al ciclo de vida y seguimiento están fundamentados en: 1) Tractivity (2024, 'Stakeholder Commitment Tracking Guide'): Fija la máquina de estados, el protocolo de verificación probatoria previa y las reglas de escalamiento; 2) Simply Stakeholders (2024, 'Commitments Tracking Tool

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F23.json](P09-F23.json)
### P09-F24: ¿Qué caso concreto, con entradas y resultado esperado, ilustra ciclo de vida y seguimiento sin introducir datos no documentados?

> Caso Concreto Documentado: 'Gestión y Renegociación del Compromiso de Entrega de Agua Potable Rural (APR) en Quebrada Seca'. Entradas: 1) ID Original: COMP-2025-0045; 2) Promesa Inicial: 'Instalación de estanque de almacenamiento de 10.000 litros antes del 30 de agosto de 2025' asignado a Rodrigo Si

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F24.json](P09-F24.json)

