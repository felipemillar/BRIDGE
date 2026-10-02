<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 07-busqueda-y-respuesta-fundada: Búsqueda y respuesta fundada

**Pilar:** [P04 — Conocimiento documentado de la corporación](../../TARJETA.md)  
**Módulo:** Saber

---

## Preguntas del Eje (8)

### P04-C13: ¿Dónde discrepan fuentes originales y síntesis internas sobre búsqueda y respuesta fundada, y qué versión prevalece según las correcciones?

> Discrepancia Principal: Soluciones comerciales de RAG afirman que 'incluir la instrucción "cite sus fuentes" en el prompt del sistema es suficiente para obtener respuestas trazables y confiables'. En agudo contraste, la investigación científica de Google Research (Bohnet et al., 2022, Attributed QA)

- **Verificación:** no_verificada: 1
- **Registro:** [P04-C13.json](P04-C13.json)
### P04-C14: ¿Qué sigue sin prueba sobre búsqueda y respuesta fundada, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Vacío e Incertidumbre: Sigue sin prueba empírica comparativa el balance óptimo entre latencia de respuesta y completitud analítica al contrastar Búsqueda Híbrida (ColBERT) vs GraphRAG sobre corpus de memorias anuales corporativas en español. GraphRAG requiere pre-computación de resúmenes de comunida

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-C14.json](P04-C14.json)
### P04-F37: ¿Qué preguntas debe resolver la búsqueda exacta, semántica o híbrida?

> La arquitectura de recuperación distribuye las consultas según su tipología lingüística y estructural: 1) Búsqueda Exacta / Léxica (BM25): resuelve consultas puntuales con identificadores unívocos, códigos de compromiso (e.g. 'COM-ENV-2023-089'), números de resolución ambiental (e.g. 'RCA N° 124/201

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F37.json](P04-F37.json)
### P04-F38: ¿Cómo se seleccionan citas suficientes para respaldar cifras, fechas y compromisos?

> La selección de citas suficientes se fundamenta en la metodología de Atribución Factual a Nivel de Oración (Sentence-Level Attribution; Bohnet et al., 2022; Yue et al., 2023): 1) Descomposición Atómica: la respuesta generada se fragmenta en proposiciones atómicas individuales (cada una con un sujeto

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F38.json](P04-F38.json)
### P04-F39: ¿Cuándo debe abstenerse el sistema por conflicto, vencimiento o falta de evidencia?

> El sistema debe activar el protocolo de 'Abstención Activa Segura' (Self-RAG / CRAG; Asai et al., 2023; Yan et al., 2024) en tres circunstancias operacionales estrictas: 1) Falta de Evidencia Documentada: cuando la recuperación arroja una confianza de relevancia insuficiente (`[IsRel] = False`) o cu

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F39.json](P04-F39.json)
### P04-F40: ¿Qué variables, categorías, relaciones y condiciones exige representar búsqueda y respuesta fundada de forma estructurada?

> Representar de forma estructurada la búsqueda y respuesta fundada exige: 1) Variables de respuesta (`response_id`, `query_text`, `generated_text`, `epistemic_status`: 'fact_supported', 'inference_supported', 'abstention_no_evidence'; `groundedness_score`, `citation_precision_score`); 2) Estructura d

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-F40.json](P04-F40.json)
### P04-F41: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre búsqueda y respuesta fundada?

> Los hechos relativos a la búsqueda y respuesta fundada se sustentan en cuatro fuentes académicas fundacionales: 1) Khattab & Zaharia (abril 2020, ColBERT, arXiv:2004.12832), que demuestra la superioridad de la interacción tardía para consultas con identificadores exactos y terminología especializada

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F41.json](P04-F41.json)
### P04-F42: ¿Qué caso concreto, con entradas y resultado esperado, ilustra búsqueda y respuesta fundada sin introducir datos no documentados?

> Caso Canónico: Consulta de prensa sobre compromisos de diversidad de género en cargos directivos. Entradas documentadas: 1) Pregunta recibida: '¿Cuál es la meta de participación femenina en el Directorio y cuánto se avanzó en 2025?'; 2) Documento en base: Memoria Integrada 2025 (pág. 54, Capítulo Go

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F42.json](P04-F42.json)

