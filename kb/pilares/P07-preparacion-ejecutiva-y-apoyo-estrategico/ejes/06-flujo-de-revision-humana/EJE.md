<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 06-flujo-de-revision-humana: Flujo de revisión humana

**Pilar:** [P07 — Preparación ejecutiva y apoyo estratégico](../../TARJETA.md)  
**Módulo:** Hablar

---

## Preguntas del Eje (8)

### P07-C11: ¿Dónde discrepan fuentes originales y síntesis internas sobre flujo de revisión humana, y qué versión prevalece según las correcciones?

> Discrepan en la naturaleza del ahorro temporal: la publicidad de vendors comerciales promete una 'automatización total de extremo a extremo' que libera al equipo de comunicaciones de cualquier carga de trabajo; mientras que las síntesis internas (P07_EVIDENCE_MAP, P07_GAPS_AND_VALIDATION) y los estu

- **Verificación:** no_verificada: 1
- **Registro:** [P07-C11.json](P07-C11.json)
### P07-C12: ¿Qué sigue sin prueba sobre flujo de revisión humana, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba empírica la cuantificación del sesgo de complacencia algorítmica (automation bias) en directores corporativos tras meses de uso continuo (si el CCO o asesor legal termina aprobando acríticamente los briefs al constatar una alta tasa de acierto inicial, pasando por alto una alucinaci

- **Verificación:** no_verificada: 1
- **Registro:** [P07-C12.json](P07-C12.json)
### P07-F31: ¿Quién valida cifras, interpretación, lenguaje y autorización antes de usar un brief?

> La validación se ejecuta mediante una cadena colegiada de cuatro roles con responsabilidades indelegables: 1) Cifras duras y parámetros operacionales: Validadas por el Dueño Técnico del Dato (Gerencia de Operaciones, Medio Ambiente o Finanzas); 2) Interpretación estratégica y encuadre narrativo: Val

- **Verificación:** no_verificada: 1
- **Registro:** [P07-F31.json](P07-F31.json)
### P07-F32: ¿Cómo se registran cambios y razones de aprobación o rechazo?

> Se registran mediante una pista de auditoría inmutable basada en Event Sourcing y control de versiones semántico: 1) Cada edición de texto genera un diff estructurado (redlining) que almacena el valor anterior, el valor modificado, el identificador del usuario, el rol y el timestamp UTC; 2) En caso

- **Verificación:** verificada: 1
- **Registro:** [P07-F32.json](P07-F32.json)
### P07-F33: ¿Qué latencia de revisión es aceptable en operación normal y en crisis?

> Los acuerdos de nivel de servicio (SLA) de latencia se definen según el régimen operativo: 1) En Operación Normal (Briefing matinal de directorio, preparación de reunión de lobby programada o entrevista acordada): La latencia aceptable para la revisión colegiada es de 2 a 4 horas (la IA genera el bo

- **Verificación:** no_verificada: 1
- **Registro:** [P07-F33.json](P07-F33.json)
### P07-F34: ¿Qué variables, categorías, relaciones y condiciones exige representar flujo de revisión humana de forma estructurada?

> Exige estructurar un schema de flujo de revisión humana (Human_Review_Workflow_Schema) compuesto por: 1) Metadatos de proceso (Workflow_Id, Document_Ref_Id, Regime_Mode [ROUTINE / CRISIS_EXPRESS]); 2) Cadena secuencial de revisores (Reviewer_Chain: Step_Index, Assigned_User_Id, Assigned_Role, Step_S

- **Verificación:** no_verificada: 1
- **Registro:** [P07-F34.json](P07-F34.json)
### P07-F35: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre flujo de revisión humana?

> Se respaldan en cinco fuentes canónicas del corpus: 1) Marcos de Supervisión y Rendición de Cuentas de IA: NIST AI RMF 1.0 (2023, funciones GOVERN 1.2 y MANAGE 2.4) y NIST Generative AI Profile (NIST AI 600-1, 2024) sobre arquitectura Human-in-the-Loop; 2) Estándares Éticos y Deontológicos: PR Counc

- **Verificación:** no_verificada: 1
- **Registro:** [P07-F35.json](P07-F35.json)
### P07-F36: ¿Qué caso concreto, con entradas y resultado esperado, ilustra flujo de revisión humana sin introducir datos no documentados?

> El caso documentado en la Plantilla 1 del Dossier P07 ilustra el flujo de revisión colegiada del Briefing Matinal para el Directorio y Comité Ejecutivo de Minera Los Salares S.A. ante la detección de un video viral en redes sociales (1.200 menciones, 62% sentimiento negativo) sobre turbiedad en la c

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P07-F36.json](P07-F36.json)

