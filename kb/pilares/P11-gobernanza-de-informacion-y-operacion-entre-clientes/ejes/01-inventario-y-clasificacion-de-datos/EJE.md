<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 01-inventario-y-clasificacion-de-datos: Inventario y clasificación de datos

**Pilar:** [P11 — Gobernanza de información y operación entre clientes](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### P11-C01: ¿Dónde discrepan fuentes originales y síntesis internas sobre inventario y clasificación de datos, y qué versión prevalece según las correcciones?

> La discrepancia principal entre las síntesis preliminares (P11_RESEARCH_DOSSIER) y las fuentes normativas originales radica en el estatus y exigibilidad de las categorías de datos: el dossier inicial articulaba una taxonomía homogénea D1 a D5 asumiendo que los estándares del GDPR europeo y de la Ley

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C01.json](P11-C01.json)
### P11-C02: ¿Qué sigue sin prueba sobre inventario y clasificación de datos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> En el dominio de taxonomía y gobierno de datos: 1) Lo que sigue sin prueba empírica: La fiabilidad y consistencia de la clasificación automática de documentos no estructurados (D1 a D5) ejecutada por modelos de lenguaje en tiempo de ingesta sin supervisión humana. No existen pruebas concluyentes de

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C02.json](P11-C02.json)
### P11-F01: ¿Qué datos son públicos, internos, confidenciales, personales o de terceros?

> La taxonomía de gobernanza de la información en BRIDGE clasifica exhaustivamente los activos de datos en 5 categorías formales: 1) Datos Públicos (D1): Información abierta y accesible al escrutinio general (comunicados oficiales emitidos, leyes de la BCN, resoluciones públicas de la SMA, registros d

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F01.json](P11-F01.json)
### P11-F02: ¿Quién es dueño y responsable de cada conjunto de documentos y señales?

> La gobernanza de datos en BRIDGE estructura la responsabilidad bajo el principio de 'Dueño Único Identificable' (Single Point of Accountability), deslindando tres roles jerárquicos: 1) Dueño del Dato (Data Owner): La persona natural corporativa (con cargo, nombre y correo) titular del proceso de neg

- **Verificación:** verificada: 1
- **Registro:** [P11-F02.json](P11-F02.json)
### P11-F03: ¿Qué regla decide si una fuente puede incluirse en búsqueda y respuesta?

> La admisibilidad de una fuente en el motor de búsqueda semántica y RAG de BRIDGE se rige por la 'Regla de las 4 Compuertas Copulativas': 1) Legitimidad y Procedencia Verificada: La fuente debe haber ingresado por un canal corporativo acreditado con hash de procedencia, prohibiendo datos extraídos de

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F03.json](P11-F03.json)
### P11-F04: ¿Qué variables, categorías, relaciones y condiciones exige representar inventario y clasificación de datos de forma estructurada?

> La representación estructurada del inventario y clasificación de datos exige modelar: 1) Entidad DataAsset (asset_id, tenant_id, asset_name, asset_type: [UNSTRUCTURED_DOC, STRUCTURED_TABLE, TRANSCRIPT, API_STREAM], source_origin_hash, created_at, storage_location_s3_uri); 2) Entidad ClassificationTi

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F04.json](P11-F04.json)
### P11-F05: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre inventario y clasificación de datos?

> Los hechos, taxonomías y requisitos sobre inventario y clasificación se sustentan en un cuerpo riguroso de fuentes normativas y técnicas primarias: 1) Legislación Chilena de Protección de Datos y Ciberseguridad: BCN Ley N° 21.719 (promulgada 2024, vacatio legis vigente diferida a fines de 2026), que

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F05.json](P11-F05.json)
### P11-F06: ¿Qué caso concreto, con entradas y resultado esperado, ilustra inventario y clasificación de datos sin introducir datos no documentados?

> Caso Concreto: Ingesta, Clasificación y Enrutamiento Seguro de Carpeta de Antecedentes de Expansión Minera (Faena Pelambres). Entradas: 1) Paquete de 3 documentos subido por el Gerente de Proyectos: A) Resumen Ejecutivo de la RCA pública aprobada por el SEA (D1 Público); B) Minuta interna de cronogr

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F06.json](P11-F06.json)

