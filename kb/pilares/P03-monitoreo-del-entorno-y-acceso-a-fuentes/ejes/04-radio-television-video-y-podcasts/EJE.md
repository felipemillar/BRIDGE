<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 04-radio-television-video-y-podcasts: Radio, televisión, video y podcasts

**Pilar:** [P03 — Monitoreo del entorno y acceso a fuentes](../../TARJETA.md)  
**Módulo:** Escuchar

---

## Preguntas del Eje (8)

### P03-C07: ¿Dónde discrepan fuentes originales y síntesis internas sobre radio, televisión, video y podcasts, y qué versión prevalece según las correcciones?

> La discrepancia principal radicaba en las promesas comerciales de 'alertas instantáneas en tiempo real al segundo en que se nombra una empresa en televisión o radio', recogidas acríticamente en notas iniciales de mercado. Prevalece la evidencia técnica de la P03_QUALITY_ADDENDUM y el mapa de evidenc

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C07.json](P03-C07.json)
### P03-C08: ¿Qué sigue sin prueba sobre radio, televisión, video y podcasts, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba empírica formal la precisión de reconocimiento de nombres de entidades corporativas y términos regulatorios en español chileno coloquial mediante modelos Whisper sin fine-tuning local: 1) Brecha: No existe un benchmark público publicado de Word Error Rate (WER) ni de extracción de e

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C08.json](P03-C08.json)
### P03-F19: ¿Qué opciones existen para transcribir, licenciar y consultar contenido audiovisual?

> Existen 3 arquitecturas principales para el tratamiento de contenido audiovisual: 1) Suites de monitoreo comercial de broadcast (TVEyes y CisionOne): capturan televisión lineal y radioemisoras 24/7 mediante sintonizadores dedicados, aplicando subtítulos cerrados y ASR propietario con latencias de 5

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F19.json](P03-F19.json)
### P03-F20: ¿Qué errores de transcripción, demoras y vacíos regionales afectan las alertas?

> Las alertas basadas en broadcast sufren 3 degradaciones técnicas documentadas: 1) Degradación por dialecto local y fonética chilena: mientras el WER en español estándar es de 5-8%, ante el habla coloquial chilena (aspiración sistemática de la /s/ implosiva, velocidad de elocución elevada, pérdida de

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F20.json](P03-F20.json)
### P03-F21: ¿Cuándo una noticia audiovisual debe tratarse como evidencia original y cuándo como resumen secundario?

> La distinción se rige por la trazabilidad del registro de voz y la intermediación editorial: 1) Evidencia original primaria: grabaciones de audio/video sin cortes donde se emiten declaraciones directas, conferencias de prensa oficiales, comisiones legislativas en vivo o entrevistas directas a vocero

- **Verificación:** verificada: 1
- **Registro:** [P03-F21.json](P03-F21.json)
### P03-F22: ¿Qué variables, categorías, relaciones y condiciones exige representar radio, televisión, video y podcasts de forma estructurada?

> La representación estructurada de contenidos audiovisuales exige: 1) Variables técnicas: `canal_emision` (tv_abierta, cable, radio_am, radio_fm, podcast_rss), `segmento_tiempo_inicio_fin` (timestamps precisos en segundos), `wer_estimado_transcripcion`, `locutor_detectado` (speaker diarization) y `fr

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F22.json](P03-F22.json)
### P03-F23: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre radio, televisión, video y podcasts?

> Los hechos están respaldados por: 1) APIs comerciales de broadcast: TVEyes API Partners Documentation (2026) y CisionOne API v2 (2026), que especifican la captura continua y licenciamiento de medios audiovisuales con latencias de 15 a 30 minutos; 2) Capacidades y límites de ASR neuronal: Radford et

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F23.json](P03-F23.json)
### P03-F24: ¿Qué caso concreto, con entradas y resultado esperado, ilustra radio, televisión, video y podcasts sin introducir datos no documentados?

> Caso: Detección y alerta de una entrevista radial de última hora a un dirigente gremial del sector energía en una emisora de Concepción. Entradas: 1) Stream de audio en vivo de Radio Bío-Bío Concepción segmentado en chunks de 30 segundos; 2) Transcripción continua ejecutada con Whisper donde la pala

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F24.json](P03-F24.json)

