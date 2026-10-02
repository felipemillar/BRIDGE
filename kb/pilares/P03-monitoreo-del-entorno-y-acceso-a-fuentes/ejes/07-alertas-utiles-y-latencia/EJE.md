<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 07-alertas-utiles-y-latencia: Alertas útiles y latencia

**Pilar:** [P03 — Monitoreo del entorno y acceso a fuentes](../../TARJETA.md)  
**Módulo:** Escuchar

---

## Preguntas del Eje (8)

### P03-C13: ¿Dónde discrepan fuentes originales y síntesis internas sobre alertas útiles y latencia, y qué versión prevalece según las correcciones?

> La discrepancia radicaba en la promesa comercial generalizada de las suites de monitoreo respecto a entregar 'alertas instantáneas omnicanal en tiempo real sobre cada mención sin riesgo de saturación'. Prevalece la evidencia técnica de AMEC y los principios de control de fatiga de P03_EVIDENCE_MAP:

- **Verificación:** no_verificada: 1
- **Registro:** [P03-C13.json](P03-C13.json)
### P03-C14: ¿Qué sigue sin prueba sobre alertas útiles y latencia, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba la tasa real de adopción, fatiga informativa y utilidad subjetiva de las alertas directivas cuando el sistema opera en condiciones de producción empresarial continua: 1) Brecha: Se carece de estudios longitudinales que midan el porcentaje de alertas que efectivamente desencadenaron

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C14.json](P03-C14.json)
### P03-F37: ¿Cómo se define relevancia de una alerta para cada rol y severidad?

> La relevancia de una alerta se define mediante una matriz bidimensional de rol corporativo y severidad de impacto: 1) Nivel Ejecutivo / Directorio (CEO, CCO, Directorio): Relevancia restringida exclusivamente a Severidad Crítica (alteración de continuidad operacional, Hecho Esencial en CMF/SEC, dema

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F37.json](P03-F37.json)
### P03-F38: ¿Qué umbrales minimizan fatiga de alertas sin ocultar eventos críticos?

> Para mitigar la fatiga de alertas (alert fatigue) sin arriesgar la omisión de eventos críticos se aplican 4 umbrales técnicos y algorítmicos: 1) Deduplicación estricta por evento madre: agrupar automáticamente las réplicas de una misma noticia en un único evento consolidado mediante algoritmos de ag

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F38.json](P03-F38.json)
### P03-F39: ¿Qué tiempos de detección y de verificación deben medirse por canal?

> El monitoreo riguroso exige descomponer la latencia total en dos métricas independientes medidas por canal: 1) Tiempo de Detección (Time-to-Detect - TTD): intervalo desde la emisión de la señal hasta su captura e indexación en el sistema: a) Redes federadas (AT Protocol Jetstream): <10 segundos; b)

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F39.json](P03-F39.json)
### P03-F40: ¿Qué variables, categorías, relaciones y condiciones exige representar alertas útiles y latencia de forma estructurada?

> La representación estructurada exige: 1) Variables técnicas y de telemetría: `alert_id` (UUID), `severity_level` (critica, alta, media, baja), `ttd_seconds`, `ttv_seconds`, `dispatch_channel` (push_app, email_digest, instant_messaging), `target_role` (c_suite, asuntos_publicos, analista), y `circuit

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F40.json](P03-F40.json)
### P03-F41: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre alertas útiles y latencia?

> Los respaldos documentales comprenden: 1) Principios de evaluación y focalización en audiencias: AMEC Barcelona Principles 3.0 (2020), que fundamenta la eliminación de métricas de vanidad superficiales y la entrega basada en gobernanza; 2) Agrupamiento de eventos y mitigación de fatiga: Event Regist

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F41.json](P03-F41.json)
### P03-F42: ¿Qué caso concreto, con entradas y resultado esperado, ilustra alertas útiles y latencia sin introducir datos no documentados?

> Caso: Manejo estructurado de una alerta sobre una paralización imprevista de transporte de carga en la Ruta 5 Norte que impacta los suministros de una faena minera. Entradas: 1) Publicación en Bluesky (Jetstream) de dirigente gremial camionero anunciando corte de ruta (TTD: 8 segundos); 2) Nota de r

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F42.json](P03-F42.json)

