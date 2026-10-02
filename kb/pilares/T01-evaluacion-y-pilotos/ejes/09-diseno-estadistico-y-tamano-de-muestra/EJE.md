<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 09-diseno-estadistico-y-tamano-de-muestra: Profundización especializada

**Pilar:** [T01 — Evaluación y pilotos](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### T01-X01: ¿Qué unidad de análisis y tamaño de muestra necesita cada experimento?

> Para asegurar significancia estadística y poder analítico (1 - beta >= 0.80 con alfa = 0.05), The Bridge Intelligence define unidades de análisis y tamaños de muestra desacoplados según el tipo de experimento: 1) Experimento de Fidelidad y Citación RAG (Unidad: Proposición Atómica / Claim fáctico):

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X01.json](T01-X01.json)
### T01-X02: ¿Qué incertidumbre debe reportarse para precisión de citas y detección de contradicciones?

> En The Bridge Intelligence está terminantemente prohibido reportar estimaciones puntuales aisladas sin su correspondiente medida de incertidumbre estadística: 1) Intervalos de Confianza al 95% (95% CI): Para la Precisión de Citación (Citation Precision) y la Exhaustividad (Citation Recall), se debe

- **Verificación:** verificada: 1
- **Registro:** [T01-X02.json](T01-X02.json)
### T01-X03: ¿Cómo evitar seleccionar solo casos fáciles o provenientes de un único sector?

> Para prevenir el sesgo de selección y evitar la trampa de evaluar a The Bridge Intelligence únicamente en casos triviales o monopolizados por una sola industria, se aplica una Matriz de Estratificación Cruzada Bidimensional (conforme a ALCE / Gao et al. 2023, SummEval / Fabbri et al. 2021 y T01_QUAL

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X03.json](T01-X03.json)
### T01-X04: ¿Qué variables, categorías, relaciones y condiciones exige representar diseño estadístico y tamaño de muestra de forma estructurada?

> La representación estructurada del diseño estadístico exige un modelo de datos formal compuesto por: 1) Entidad Experimento_Estadistico: ID unívoco, hipótesis nula y alternativa formalizadas matemáticamente, nivel alfa (0.05), potencia estadística (1 - beta = 0.80), y tamaño de efecto mínimo detecta

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X04.json](T01-X04.json)
### T01-X05: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre diseño estadístico y tamaño de muestra?

> El diseño estadístico, cálculo de muestras y reporte de incertidumbre se respaldan en textos completos primarios verificados en T01: 1) Saad-Falcon et al. (ARES, 2023-11-16, ArXiv bff33bd6, p. 3-6): Respalda la teoría de Prediction-Powered Inference (PPI) y el dimensionamiento de muestras híbridas (

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X05.json](T01-X05.json)
### T01-X06: ¿Qué caso concreto, con entradas y resultado esperado, ilustra diseño estadístico y tamaño de muestra sin introducir datos no documentados?

> Caso Concreto de Auditoría Estadística CAE-T01-255 (Certificación de Citation Precision en el Módulo Saber ante Comité de Riesgos de Banco Multinacional): 1) Entradas: Testset de N = 200 consultas corporativas financieras estratificadas en 4 sectores; Descomposición en n = 640 afirmaciones fácticas

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X06.json](T01-X06.json)
### T01-X07: ¿Dónde discrepan fuentes originales y síntesis internas sobre diseño estadístico y tamaño de muestra, y qué versión prevalece según las correcciones?

> Discrepancia y prevalencia en diseño estadístico: 1) Discrepancia: Las notas iniciales sugerían que un muestreo informal de 20 consultas seleccionadas ad-hoc por el equipo comercial bastaba para 'validar el funcionamiento' de la plataforma antes del lanzamiento; 2) Versión que Prevalece: Según ARES

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [T01-X07.json](T01-X07.json)
### T01-X08: ¿Qué sigue sin prueba sobre diseño estadístico y tamaño de muestra, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba empírica formal el cálculo de la correlación intra-clúster (ICC - Intra-Cluster Correlation) en respuestas generadas para un mismo cliente corporativo: 1) Vacío Identificado: Cuando se evalúan múltiples claims generados para una misma empresa minera que comparte un repositorio común

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X08.json](T01-X08.json)

