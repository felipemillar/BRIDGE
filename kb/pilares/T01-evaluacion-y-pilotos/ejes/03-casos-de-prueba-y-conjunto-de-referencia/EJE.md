<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 03-casos-de-prueba-y-conjunto-de-referencia: Casos de prueba y conjunto de referencia

**Pilar:** [T01 — Evaluación y pilotos](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### T01-C05: ¿Dónde discrepan fuentes originales y síntesis internas sobre casos de prueba y conjunto de referencia, y qué versión prevalece según las correcciones?

> Discrepancia y prevalencia en casos de prueba y golden dataset: 1) Discrepancia: El inventario original de fuentes contenía páginas breves de abstract (/abs/) de ArXiv que omitían detalles experimentales, metodologías de cálculo y anexos técnicos, lo cual inducía a síntesis incompletas; 2) Versión q

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [T01-C05.json](T01-C05.json)
### T01-C06: ¿Qué sigue sin prueba sobre casos de prueba y conjunto de referencia, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba empírica suficiente la robustez del Golden Benchmark de BRIDGE ante documentos corporativos históricos escaneados con bajo contraste, tablas complejas rotadas o marcas de agua invasivas: 1) Vacío Identificado: Los benchmarks ALCE (e1a0171b) y SABER (8663bbbe) fueron construidos sobr

- **Verificación:** no_verificada: 1
- **Registro:** [T01-C06.json](T01-C06.json)
### T01-F13: ¿Qué escenarios públicos y sintéticos cubren casos normales, ambiguos y críticos?

> Para evaluar integralmente los módulos de The Bridge Intelligence (thebridgeintelligence.ai), el conjunto de referencia (golden dataset) debe estratificarse en tres tipos de escenarios complementarios: 1) Escenarios Normales: Consultas fácticas estándar sobre hechos esenciales y memorias anuales cor

- **Verificación:** no_verificada: 2
- **Registro:** [T01-F13.json](T01-F13.json)
### T01-F14: ¿Cómo se rotulan afirmaciones, citas, conflictos y permisos de forma independiente?

> Para garantizar la máxima validez científica y evitar el sesgo de confirmación, la rotulación del conjunto de referencia debe desacoplarse en cuatro ejes independientes evaluados por jueces ciegos o modelos calibrados: 1) Rotulación de Afirmaciones Fácticas: Cada oración de la respuesta generada se

- **Verificación:** no_verificada: 2
- **Registro:** [T01-F14.json](T01-F14.json)
### T01-F15: ¿Qué separación entre diseño y evaluación evita contaminar el conjunto de prueba?

> Para prevenir la fuga de datos (data contamination) y el sobreajuste métrico en los pilotos de The Bridge Intelligence, debe aplicarse una estricta separación metodológica entre el equipo de diseño/desarrollo y el equipo de evaluación: 1) Aislamiento Estricto de Repositorios (Train/Dev vs Test): Los

- **Verificación:** no_verificada: 1, solo_sintesis_interna: 1
- **Registro:** [T01-F15.json](T01-F15.json)
### T01-F16: ¿Qué variables, categorías, relaciones y condiciones exige representar casos de prueba y conjunto de referencia de forma estructurada?

> La representación estructurada de los casos de prueba y el conjunto de referencia requiere modelar un esquema relacional estricto compuesto por: 1) Entidad Caso_Prueba: Identificador unívoco, escenario (normal, ambiguo, crítico), módulo destino (Saber, Escuchar, Hablar, Relacionar), consulta de entr

- **Verificación:** no_verificada: 1
- **Registro:** [T01-F16.json](T01-F16.json)
### T01-F17: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre casos de prueba y conjunto de referencia?

> El diseño, estructuración y control de conjuntos de referencia para la evaluación de The Bridge Intelligence se respaldan rigurosamente en la literatura científica de texto completo recuperada en T01: 1) Gao et al. (ALCE Benchmark, 2023-05-23, ArXiv e1a0171b, p. 3-6): Define la metodología de evalua

- **Verificación:** no_verificada: 1
- **Registro:** [T01-F17.json](T01-F17.json)
### T01-F18: ¿Qué caso concreto, con entradas y resultado esperado, ilustra casos de prueba y conjunto de referencia sin introducir datos no documentados?

> Caso de Prueba CP-T01-042 (Escenario de Conflicto de Fechas en Hecho Esencial CMF): 1) Entradas: Consulta del usuario: '¿Cuál fue la fecha formal de cierre de la transacción minera y el monto final acordado?'; Contexto disponible: Documento A (Nota de prensa, 15 de marzo de 2025: 'Transacción estima

- **Verificación:** no_verificada: 1
- **Registro:** [T01-F18.json](T01-F18.json)

