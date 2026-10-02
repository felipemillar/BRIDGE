<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 08-derechos-costos-y-calidad-de-ingesta: Derechos, costos y calidad de ingesta

**Pilar:** [P03 — Monitoreo del entorno y acceso a fuentes](../../TARJETA.md)  
**Módulo:** Escuchar

---

## Preguntas del Eje (8)

### P03-C15: ¿Dónde discrepan fuentes originales y síntesis internas sobre derechos, costos y calidad de ingesta, y qué versión prevalece según las correcciones?

> La discrepancia principal radicaba en suponer que la minería de textos y datos (TDM) sobre la prensa abierta goza de una cobertura legal general en Chile similar al marco europeo. Prevalece la rigurosa distinción jurídica de la P03_QUALITY_ADDENDUM (Sección 2.4): 1) En la Unión Europea, el Artículo

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C15.json](P03-C15.json)
### P03-C16: ¿Qué sigue sin prueba sobre derechos, costos y calidad de ingesta, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba pública el Costo Total de Propiedad (TCO) real y los cargos ocultos en la contratación de suites de monitoreo comercial de medios (Factiva, Meltwater, Cision, TVEyes) para empresas con operaciones en Chile: 1) Brecha: Los contratos comerciales operan bajo estrictas cláusulas de conf

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C16.json](P03-C16.json)
### P03-F43: ¿Qué derechos de uso, retención, redistribución y entrenamiento están documentados por tipo de fuente?

> Los derechos de uso se estructuran en 4 regímenes jurídicos diferenciados: 1) Datos Públicos Gubernamentales (CMF, ChileCompra, SEC EDGAR, Diario Oficial): derecho pleno de consulta, indexación, retención indefinida y derivación analítica interna, con redistribución autorizada citando la fuente ofic

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F43.json](P03-F43.json)
### P03-F44: ¿Qué costos y dependencias contractuales son observables y cuáles requieren cotización?

> Los costos y dependencias contractuales se dividen en observables y opacos: 1) Costos observables públicamente: a) Bluesky (AT Protocol Jetstream): $0 USD (abierto y libre); b) APIs Estatales (ChileCompra, CMF, SEC EDGAR, Diario Oficial): $0 USD de costo de licencia (consumo de datos abiertos sujeto

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F44.json](P03-F44.json)
### P03-F45: ¿Cómo evaluar precisión, cobertura, duplicados y fallos de captura con denominadores correctos?

> La evaluación rigurosa de la calidad de ingesta exige definir matemáticamente 4 métricas con denominadores formalmente auditados: 1) Precisión de Señal (Precision): `Señales_Pertinentes_para_Asuntos_Corporativos / Total_de_Señales_Ingeridas` (evita inflar métricas con ruido comercial u homónimos); 2

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F45.json](P03-F45.json)
### P03-F46: ¿Qué variables, categorías, relaciones y condiciones exige representar derechos, costos y calidad de ingesta de forma estructurada?

> La representación estructurada exige: 1) Variables técnicas y comerciales: `regimen_licencia` (publico_abierto, comercial_sindicado, api_restringida, scraping_condicionado), `costo_licencia_anual_usd`, `limite_consultas_minuto`, `permite_entrenamiento_ia` (booleano), `precision_auditada` (0.0 a 1.0)

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F46.json](P03-F46.json)
### P03-F47: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre derechos, costos y calidad de ingesta?

> Los hechos de este eje están respaldados por: 1) Normativa de propiedad intelectual en Chile: Ley 17.336 (BCN, texto refundido 2026, Art. 38 y 71, derecho de cita y ausencia de excepción TDM general); 2) Derecho europeo de minería de datos: Directiva (UE) 2019/790 (Art. 3 y 4, excepciones de TDM y r

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F47.json](P03-F47.json)
### P03-F48: ¿Qué caso concreto, con entradas y resultado esperado, ilustra derechos, costos y calidad de ingesta sin introducir datos no documentados?

> Caso: Auditoría de cumplimiento jurídico y calidad métrica de un pipeline de ingesta para una empresa forestal en el sur de Chile. Entradas: 1) Captura de 1.000 artículos de prensa regional mediante RSS y scraping de portales abiertos; 2) Verificación automática de directivas `robots.txt` y metaetiq

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F48.json](P03-F48.json)

