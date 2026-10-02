<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 02-afirmaciones-y-compromisos: Afirmaciones y compromisos

**Pilar:** [P04 — Conocimiento documentado de la corporación](../../TARJETA.md)  
**Módulo:** Saber

---

## Preguntas del Eje (8)

### P04-C03: ¿Dónde discrepan fuentes originales y síntesis internas sobre afirmaciones y compromisos, y qué versión prevalece según las correcciones?

> Discrepancia Principal: La industria de software corporativo y soluciones de IA generativa proclama que 'un LLM puede identificar automáticamente promesas y logros corporativos usando un prompt de clasificación'. Sin embargo, la literatura académica especializada en procesamiento de lenguaje natural

- **Verificación:** no_verificada: 1
- **Registro:** [P04-C03.json](P04-C03.json)
### P04-C04: ¿Qué sigue sin prueba sobre afirmaciones y compromisos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Vacío e Incertidumbre: Permanece sin resolver empíricamente la detección automatizada del 'abandono silencioso de compromisos' (drift o meta abandonada). Ocurre cuando una empresa publica una meta ambiciosa en un año (e.g. Memoria 2021) y en los reportes subsiguientes (2023-2025) deja de mencionarla

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-C04.json](P04-C04.json)
### P04-F07: ¿Cómo se registra una afirmación corporativa con cifra, fecha, alcance, fuente y responsable?

> Una afirmación corporativa con valor cuantitativo se registra mediante la 'Ficha Canónica de Compromiso Corporativo' (Corporate Commitment Data Sheet) estructurada en JSON-Schema. El registro captura obligatoriamente: 1) Cifra y unidad métrica en un objeto `baseline` o `target` con valor numérico fl

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-F07.json](P04-F07.json)
### P04-F08: ¿Qué campos distinguen promesa, meta, avance, incumplimiento y rectificación?

> La diferenciación entre los estados de un compromiso corporativo se rige por campos específicos en el modelo de datos: 1) Promesa / Declaración de Intención: tipificada como `corp:Statement`, caracterizada por `has_quantitative_target: false`, ausencia de `baseline_year` y horizonte indefinido; 2) M

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F08.json](P04-F08.json)
### P04-F09: ¿Cómo se enlazan afirmaciones y compromisos con documentos, actores y decisiones posteriores?

> El enlace relacional entre afirmaciones, compromisos, documentos y decisiones se implementa mediante un Grafo de Conocimiento fundamentado en el estándar W3C PROV-O y el vocabulario FIBO (Financial Industry Business Ontology). Se configuran cuatro aristas direccionales tipadas: 1) Linaje Documental

- **Verificación:** verificada: 1
- **Registro:** [P04-F09.json](P04-F09.json)
### P04-F10: ¿Qué variables, categorías, relaciones y condiciones exige representar afirmaciones y compromisos de forma estructurada?

> La representación estructurada de afirmaciones y compromisos exige: 1) Variables métricas e identitarias (`commitment_id`, `title`, `description`, `baseline_value`, `target_value`, `unit`, `metric_type`); 2) Categorías temáticas normalizadas (`category`: Ambiental/Clima, Social/Comunidad, Gobierno C

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-F10.json](P04-F10.json)
### P04-F11: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre afirmaciones y compromisos?

> Los hechos relativos al modelado de afirmaciones y compromisos se sustentan en cuatro pilares normativos y ontológicos: 1) IFRS S2 Climate-related Disclosures (junio 2023, párrs. 33-36), que exige la divulgación de metas absolutas/intensidad, años base, hitos intermedios y revisiones metodológicas;

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F11.json](P04-F11.json)
### P04-F12: ¿Qué caso concreto, con entradas y resultado esperado, ilustra afirmaciones y compromisos sin introducir datos no documentados?

> Caso Canónico: Seguimiento del compromiso ambiental 'Reducción de extracción de agua continental en operaciones mineras' (ID: COM-ENV-2023-089). Entradas documentadas: 1) Declaración original en Memoria 2023: Reducción del 40% al 2030 respecto a la línea base 2021 (1.250 l/s), meta objetivo 750 l/s,

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-F12.json](P04-F12.json)

