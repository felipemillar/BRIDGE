<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 01-taxonomia-de-senales-externas: Taxonomía de señales externas

**Pilar:** [P03 — Monitoreo del entorno y acceso a fuentes](../../TARJETA.md)  
**Módulo:** Escuchar

---

## Preguntas del Eje (8)

### P03-C01: ¿Dónde discrepan fuentes originales y síntesis internas sobre taxonomía de señales externas, y qué versión prevalece según las correcciones?

> La discrepancia principal radicaba en que las síntesis internas iniciales equiparaban implícitamente la detección de patrones de coordinación temporal y presencia de bots con ataques maliciosos de desinformación. Prevalece de forma absoluta la rectificación formal de la P03_QUALITY_ADDENDUM (Sección

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C01.json](P03-C01.json)
### P03-C02: ¿Qué sigue sin prueba sobre taxonomía de señales externas, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba empírica la capacidad de una taxonomía algorítmica automatizada para predecir con exactitud si una señal débil de baja intensidad (ej. reclamo en junta de vecinos o publicación en foro comunal) escalará efectivamente a un conflicto regulatorio o paro operacional mayor: 1) Brecha: No

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C02.json](P03-C02.json)
### P03-F01: ¿Qué tipos de señales de prensa, redes, broadcast, reguladores y comunidades son relevantes?

> Para asuntos corporativos, las señales relevantes se dividen en 5 familias operativas: 1) Prensa estructurada y web abierta (artículos periodísticos, editoriales, columnas de opinión y blogs especializados con metadata de autor y medio); 2) Redes sociales y plataformas comunitarias (mensajería públi

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F01.json](P03-F01.json)
### P03-F02: ¿Qué metadatos mínimos permiten comparar noticias, publicaciones, alertas y documentos oficiales?

> El esquema canónico de metadatos mínimos para homologar señales heterogéneas consta de 8 atributos obligatorios: 1) `signal_id` (UUID único determinístico); 2) `timestamp_published` (marca temporal ISO-8601 con zona horaria UTC/local); 3) `source_type` (prensa, red_social, broadcast, regulador, comu

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F02.json](P03-F02.json)
### P03-F03: ¿Cómo se distingue una mención de marca de un cambio material para asuntos corporativos?

> La distinción se basa en tres filtros metodológicos acumulativos: 1) Umbral de materialidad regulatoria y financiera: una mención de marca es un evento meramente comunicacional (ej. auspicio deportivo, review de producto), mientras que un cambio material altera los derechos, obligaciones, gobernanza

- **Verificación:** verificada: 1
- **Registro:** [P03-F03.json](P03-F03.json)
### P03-F04: ¿Qué variables, categorías, relaciones y condiciones exige representar taxonomía de señales externas de forma estructurada?

> La representación estructurada de la taxonomía de señales exige: 1) Variables primarias: `severidad` (crítica, alta, media, baja), `alcance_geografico` (nacional, regional, comunal), `fase_regulatoria` (discusión_publica, proyecto_ley, tramite_legislativo, norma_vigente), `polarizacion_discursiva` y

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F04.json](P03-F04.json)
### P03-F05: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre taxonomía de señales externas?

> Los hechos de la taxonomía de señales externas están respaldados por: 1) Estándares de medición comunicacional: AMEC Barcelona Principles 3.0 (2020), que fundamenta el abandono de impresiones superficiales y exige medir outcomes organizacionales e institucionales; 2) Normalización de eventos noticio

- **Verificación:** verificada: 1
- **Registro:** [P03-F05.json](P03-F05.json)
### P03-F06: ¿Qué caso concreto, con entradas y resultado esperado, ilustra taxonomía de señales externas sin introducir datos no documentados?

> Caso: Monitoreo regulatorio y mediático ante un nuevo proyecto de ley de royalty a la minería en Chile. Entradas: 1) Boletín oficial de la Cámara de Diputadas y Diputados de Chile anunciando el ingreso del proyecto de ley (Señal Institucional/Regulatoria); 2) Nota de prensa en portal regional de Ant

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F06.json](P03-F06.json)

