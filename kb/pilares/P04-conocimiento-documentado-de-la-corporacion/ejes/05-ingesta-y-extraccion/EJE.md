<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 05-ingesta-y-extraccion: Ingesta y extracción

**Pilar:** [P04 — Conocimiento documentado de la corporación](../../TARJETA.md)  
**Módulo:** Saber

---

## Preguntas del Eje (8)

### P04-C09: ¿Dónde discrepan fuentes originales y síntesis internas sobre ingesta y extracción, y qué versión prevalece según las correcciones?

> Discrepancia Principal: La mayoría de tutoriales y frameworks de desarrollo rápido de RAG recomiendan segmentación por longitud fija (e.g. 500 tokens con overlap de 50) como receta universal. Por el contrario, la investigación especializada de Gao et al. (2023) y la síntesis P04_EVIDENCE_MAP demuest

- **Verificación:** no_verificada: 1
- **Registro:** [P04-C09.json](P04-C09.json)
### P04-C10: ¿Qué sigue sin prueba sobre ingesta y extracción, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Vacío e Incertidumbre: Permanece sin prueba empírica la extracción completamente desatendida de tablas multipágina con celdas fusionadas asimétricas y notas al pie en memorias de empresas chilenas, donde frecuentemente se combinan formatos contables IFRS con narrativas de sostenibilidad CMF. Fuente

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-C10.json](P04-C10.json)
### P04-F25: ¿Qué pasos permiten extraer tablas, anexos, cifras y notas de PDF, web y archivos ofimáticos?

> La extracción de tablas, anexos, cifras y notas en memorias corporativas complejas se ejecuta mediante un pipeline en 4 pasos especializados: 1) Análisis de Maquetación Sensible al Layout (Layout-Aware Document Parsing): identificación de bloques mediante detección de objetos visuales (títulos, colu

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F25.json](P04-F25.json)
### P04-F26: ¿Qué unidades de fragmentación preservan contexto y citas sin mezclar versiones?

> La arquitectura óptima de fragmentación es el 'Chunking Jerárquico de Dos Niveles' (Parent Document Retrieval): 1) Fragmentos Hijo (Child Chunks, 128 a 256 tokens): segmentos atómicos altamente enfocados en proposiciones individuales, métricas o filas de tabla, optimizados para coincidencia densa ve

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F26.json](P04-F26.json)
### P04-F27: ¿Cómo detectar errores de OCR, tablas incompletas y referencias cruzadas rotas?

> La detección de anomalías e inconsistencias en la ingesta se realiza mediante una triple batería de validadores algorítmicos: 1) Auditor de Paridad Tabular (Table Structure Auditor): comprueba que cada fila de una tabla contenga exactamente el mismo número de celdas que la fila de encabezados y que

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F27.json](P04-F27.json)
### P04-F28: ¿Qué variables, categorías, relaciones y condiciones exige representar ingesta y extracción de forma estructurada?

> Representar de forma estructurada el proceso de ingesta y extracción exige: 1) Variables de fragmento (`chunk_id`, `parent_chunk_id`, `chunk_index`, `page_number`, `bounding_box_coordinates`, `token_count`, `hash_sha256`); 2) Categorías de contenido (`chunk_type`: Párrafo_Narrativo, Tabla_Financiera

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-F28.json](P04-F28.json)
### P04-F29: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ingesta y extracción?

> Los hechos sobre ingesta y extracción de memorias corporativas se fundamentan en tres fuentes académicas y técnicas principales: 1) Gao et al. (diciembre 2023, arXiv:2312.10997), que sistematiza las limitaciones del chunking tradicional y demuestra las ventajas del pre-retrieval jerárquico y estruct

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F29.json](P04-F29.json)
### P04-F30: ¿Qué caso concreto, con entradas y resultado esperado, ilustra ingesta y extracción sin introducir datos no documentados?

> Caso Canónico: Ingesta de la 'Tabla de Emisiones de GEI y Consumo Energético' (pág. 92 de la Memoria Integrada 2025). Entradas documentadas: PDF con tabla compleja que abarca dos páginas, con columnas para 'Alcance 1 (tCO2e)', 'Alcance 2 (tCO2e)', 'Intensidad Energética (GJ/ton)' para los años 2023,

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-F30.json](P04-F30.json)

