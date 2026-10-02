<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Pilar P06: Cruce de conocimiento interno y señales externas

## Alcance
Este pilar forma parte del módulo **Saber** en el programa canónico BRIDGE.
Contiene 9 ejes de investigación temática y 72 preguntas atómicas ejecutadas bajo el Mandato de Asuntos Corporativos.
Su propósito es establecer la evidencia empírica, legal y procedimental para este ámbito directivo.

## Ejes
- [Eje 01-modelo-de-afirmacion-y-evidencia: Modelo de afirmación y evidencia](ejes/01-modelo-de-afirmacion-y-evidencia/EJE.md)
- [Eje 02-fuentes-internas-y-externas: Fuentes internas y externas](ejes/02-fuentes-internas-y-externas/EJE.md)
- [Eje 03-identidad-de-entidades-y-acontecimientos: Identidad de entidades y acontecimientos](ejes/03-identidad-de-entidades-y-acontecimientos/EJE.md)
- [Eje 04-temporalidad-y-versiones: Temporalidad y versiones](ejes/04-temporalidad-y-versiones/EJE.md)
- [Eje 05-arquitectura-de-procesamiento: Arquitectura de procesamiento](ejes/05-arquitectura-de-procesamiento/EJE.md)
- [Eje 06-tipos-de-discrepancia-y-respuesta: Tipos de discrepancia y respuesta](ejes/06-tipos-de-discrepancia-y-respuesta/EJE.md)
- [Eje 07-evaluacion-con-casos-de-referencia: Evaluación con casos de referencia](ejes/07-evaluacion-con-casos-de-referencia/EJE.md)
- [Eje 08-privacidad-y-limites-epistemicos: Privacidad y límites epistémicos](ejes/08-privacidad-y-limites-epistemicos/EJE.md)
- [Eje 09-grafo-de-afirmaciones: Profundización especializada](ejes/09-grafo-de-afirmaciones/EJE.md)
- [Eje 10-resolucion-de-contradicciones-complejas: Profundización especializada](ejes/10-resolucion-de-contradicciones-complejas/EJE.md)
- [Eje 11-seguridad-en-recuperacion-combinada: Profundización especializada](ejes/11-seguridad-en-recuperacion-combinada/EJE.md)
- [Eje 12-ablacion-y-valor-del-cruce: Profundización especializada](ejes/12-ablacion-y-valor-del-cruce/EJE.md)

## Fuentes rectoras y precedencia
> **Regla de precedencia:** Precedencia canónica estándar.

### Fuentes principales del pilar (38 fuentes registradas)
- **b78c4d97-51eb-4436-9dac-d03c896c69e6**: Calamai et al. (2025-2026) - Detecting Greenwashing Survey (Texto Completo HTML v2) (`texto_sustantivo`)
- **8efce53c-a1b5-4416-b399-3a615f36b2b5**: Zhu et al. (2026) - SABER: Trust or Abstain? (Texto Completo HTML v1) (`texto_sustantivo`)
- **c7b4a004-ddb4-48c4-9fa8-30961b581b5c**: Li et al. (2025) - T-GRAG: Dynamic GraphRAG (Texto Completo PDF) (`texto_sustantivo`)
- **589b1b7c-6049-4b3a-9f0d-1fa8990a7a1d**: CMF Chile - Sostenibilidad y Norma de Carácter General N° 461 (`texto_sustantivo`)
- **599d47e4-07ba-4ae2-9ec3-ae05a7cc4557**: Vinella et al. (2023-2024) - Language Models Greenwashing (Texto Completo HTML v2) (`texto_sustantivo`)

## Estado de verificación
Distribución de verificación para los 378 hallazgos del pilar:
- `no_verificada`: 28
- `en_proceso`: 0
- `no_verificable`: 0
- `verificada`: 1
- `refutada`: 0

## Vacíos abiertos
- **[P06-C02]** (alta): Inexistencia de datasets abiertos específicos para asuntos corporativos:** No existen benchmarks estandarizados que capturen la ambigüedad estratégica intencional, las declaraciones prospectivas (*safe harbor*) o las metas aspiracionales ESG a 2030/2
- **[P06-C02]** (alta): Invalidez de extrapolar benchmarks académicos:** Obtener un F1 \\(>90\%\\) en benchmarks sintéticos o de Wikipedia como FEVER, ARES o Ragas no prueba la capacidad del sistema para evaluar si una declaración del CEO contradice un pasivo laboral report
- **[P06-C04]** (alta): Fuentes Parciales, Fallidas o con Limitaciones Severas
- **[P06-C05]** (alta): Discrepancia Temporal en Acontecimientos (Desfase Temporal vs. Contradicción Factual)**
- **[P06-C05]** (alta): Versión que prevalece:** Prevalece la entidad canónica unificada mediante el algoritmo probabilístico Fellegi-Sunter (librería *Splink*) vinculado a nodos en grafos de conocimiento (*GraphRAG*), lo que permite asociar nombres de fantasía a su ID lega
- **[P06-C06]** (alta): Sin Prueba — Mapeo Ontológico Automático para Holdings en Latinoamérica:** No existe prueba de un enlace de entidades "cero-esfuerzo" para grupos económicos complejos en Chile y la región (holdings familiares y filiales en cascada) sin curaduría de r
- **[P06-C06]** (alta): Sin Prueba — Verificación de Imputaciones Informales:** Las acusaciones en redes sociales o prensa sin expediente judicial o resolución administrativa firme (ej. denuncias de accidentes no reportados en contratistas, caso CLM-05 [18]) se mantienen co
- **[P06-C08]** (alta): Lo que sigue sin prueba sobre temporalidad y versiones
- **[P06-C08]** (alta): Sin prueba (Falta de Benchmarks Corporativos):** No existe en la literatura un dataset de referencia abierto y estandarizado específico para asuntos corporativos que mida la "caducidad de la verdad" o la evolución temporal de compromisos plurianuales
- **[P06-C10]** (alta): Falsa equivalencia de rendimiento en benchmarks:** El **`P06_QUALITY_ADDENDUM` (Sección 3.2)** y **Zhu et al. (2026)** demuestran que obtener un F1 \\(> 90\%\\) en benchmarks de opción múltiple o verificación binaria no prueba que la arquitectura eva

## Cómo leer este pilar
La base de conocimiento está organizada en 5 niveles de granularidad:
- **Nivel L0 (Catálogo y Mandato):** Visión global en [kb/CATALOGO.json](../../CATALOGO.json) y el mandato rector.
- **Nivel L1 (Tarjeta de Pilar):** Este documento resumen con alcance, ejes y reglas de precedencia.
- **Nivel L2 (Fichas de Eje):** Síntesis de cada eje en sus respectivas rutas `ejes/<EJE_DIR>/EJE.md`.
- **Nivel L3 (Registros de Pregunta):** Respuestas atómicas en formato JSON (`<QID>.json`) con 20 atributos.
- **Nivel L4 (Fuentes Primarias):** Evidencias y metadatos documentales en `fuentes.jsonl` del pilar.
