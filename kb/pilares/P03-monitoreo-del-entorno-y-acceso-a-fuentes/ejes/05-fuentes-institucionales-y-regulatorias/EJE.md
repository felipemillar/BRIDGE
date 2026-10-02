<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 05-fuentes-institucionales-y-regulatorias: Fuentes institucionales y regulatorias

**Pilar:** [P03 — Monitoreo del entorno y acceso a fuentes](../../TARJETA.md)  
**Módulo:** Escuchar

---

## Preguntas del Eje (8)

### P03-C09: ¿Dónde discrepan fuentes originales y síntesis internas sobre fuentes institucionales y regulatorias, y qué versión prevalece según las correcciones?

> La discrepancia principal radicaba en que las notas preliminares agrupaban acríticamente herramientas de investigación académica (Meta Content Library y TikTok Research API) junto con APIs oficiales gubernamentales (SEC EDGAR, CMF y ChileCompra), como si fueran fuentes utilizables indistintamente en

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C09.json](P03-C09.json)
### P03-C10: ¿Qué sigue sin prueba sobre fuentes institucionales y regulatorias, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba la capacidad de ingesta automatizada continua sobre ordenanzas, resoluciones alcaldicias y actas de concejos municipales en los 345 municipios de Chile: 1) Brecha: Mientras las instituciones centrales (CMF, Diario Oficial, Congreso) poseen portales consolidados, la regulación comuna

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C10.json](P03-C10.json)
### P03-F25: ¿Qué registros, organismos y boletines son prioritarios para Chile y para un despliegue multinacional?

> Los registros y boletines prioritarios se dividen en dos niveles operativos: 1) Nivel Nacional (Chile): a) Comisión para el Mercado Financiero (CMF): hechos esenciales, sanciones y circulares normativas de emisores de valores; b) Diario Oficial de la República de Chile: decretos supremos, leyes prom

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F25.json](P03-F25.json)
### P03-F26: ¿Cómo se detectan cambios normativos y de actores sin confundir propuesta, trámite y norma vigente?

> Para evitar falsas alarmas y errores de apreciación jurídica, la detección se estructura mediante una Máquina de Estados Finitos (FSM) que clasifica cada documento en 5 estados ontológicos mutuamente excluyentes: 1) `Propuesta_o_Minuta`: ideas prelegislativas, declaraciones de prensa o mociones no i

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F26.json](P03-F26.json)
### P03-F27: ¿Qué frecuencia, formatos y trazabilidad ofrecen las fuentes oficiales revisadas?

> La frecuencia, formatos y trazabilidad técnica presentan las siguientes especificaciones verificadas: 1) CMF Chile: Divulgación en tiempo casi real continua (polling cada 5 minutos recomendado); formato HTML semiestructurado y archivos PDF descargables; trazabilidad mediante código único de ingreso

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F27.json](P03-F27.json)
### P03-F28: ¿Qué variables, categorías, relaciones y condiciones exige representar fuentes institucionales y regulatorias de forma estructurada?

> La representación estructurada de fuentes oficiales exige: 1) Variables técnicas y jurídicas: `organismo_emisor` (CMF, SEC, SII, SEIA, Congreso), `tipo_documento` (hecho_esencial, decreto_supremo, resolucion_exenta, form_8k, licitacion_ocds), `numero_expediente_o_boletin`, `estado_juridico` (propues

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F28.json](P03-F28.json)
### P03-F29: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre fuentes institucionales y regulatorias?

> Los hechos de este eje están respaldados por: 1) Normativa y divulgación de hechos esenciales en Chile: CMF Chile Portal de Consulta y Ley 18.045 de Mercado de Valores (Art. 9 y 10, definición de hecho esencial y divulgación continua); 2) Datos abiertos de contratación pública: ChileCompra API Docum

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F29.json](P03-F29.json)
### P03-F30: ¿Qué caso concreto, con entradas y resultado esperado, ilustra fuentes institucionales y regulatorias sin introducir datos no documentados?

> Caso: Detección anticipada de riesgo regulatorio hídrico que no menciona a la compañía afectada. Entradas: 1) Publicación en el Diario Oficial de Chile de una Resolución Exenta de la Dirección General de Aguas (DGA) declarando 'Zona de Escasez Hídrica' en una cuenca del Valle del Huasco; 2) Acta de

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F30.json](P03-F30.json)

