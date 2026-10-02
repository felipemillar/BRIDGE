<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 01-universo-comercial-y-deduplicacion: Universo comercial y deduplicación

**Pilar:** [P02 — Empresas y soluciones existentes](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### P02-C01: ¿Dónde discrepan fuentes originales y síntesis internas sobre universo comercial y deduplicación, y qué versión prevalece según las correcciones?

> Discrepan en el tamaño del universo comercial y en la inclusión de entidades gremiales y modelos teóricos: 1) Discrepancia: Borradores iniciales de síntesis internas contabilizaban entre 73 y 82 'proveedores', inflando el mercado al incluir erróneamente a AMEC (asociación gremial sin fines de lucro

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P02-C01.json](P02-C01.json)
### P02-C02: ¿Qué sigue sin prueba sobre universo comercial y deduplicación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Siguen sin prueba empírica tres aspectos críticos del universo comercial: 1) Titularidad legal y sede física de Direct Signal: la entidad figura en catálogos de marketing pero sus fuentes fallaron en certificar registro corporativo activo en Delaware o California, manteniéndose como 'propiedad no ve

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P02-C02.json](P02-C02.json)
### P02-F01: ¿Qué organizaciones, marcas y productos son entidades distintas y cuáles pertenecen al mismo grupo?

> La investigación corporativa y la fe de erratas (00_P02_GLOBAL_READ_ME_AND_ERRATA) distinguen grupos matrices, entidades legales y marcas de producto: 1) WPP plc es matriz de Burson Global, que adquirió Limbik (12 agosto 2026) operando bajo la suite Burson Decipher; 2) FGS Global pertenece a Kite Bi

- **Verificación:** no_verificada: 3
- **Registro:** [P02-F01.json](P02-F01.json)
### P02-F02: ¿Qué criterios separan proveedor comercial, asociación, estándar, consultora y propuesta de referencia?

> La metodología de P02 establece 5 categorías conceptuales excluyentes: 1) Proveedor Comercial Competitivo (N_comm=70): empresa con fines de lucro que licencia software B2B, APIs de datos o plataformas para uso operativo continuo (ej. Meltwater, Signal AI, Quorum, AlphaSense); 2) Asociación Profesion

- **Verificación:** solo_sintesis_interna: 2
- **Registro:** [P02-F02.json](P02-F02.json)
### P02-F03: ¿Qué fichas del atlas quedan cuestionadas por la fe de erratas y cómo debe reconciliarse el denominador?

> La fe de erratas (00_P02_GLOBAL_READ_ME_AND_ERRATA) y la reconciliación del atlas (P02_GLOBAL_ATLAS_RECONCILIATION_V1) sustituyen formalmente la versión preliminar (V1) corrigiendo: 1) El denominador comercial de la V1 (que reportaba 78 o 70 'proveedores independientes' sin deduplicación estricta) q

- **Verificación:** solo_sintesis_interna: 2
- **Registro:** [P02-F03.json](P02-F03.json)
### P02-F04: ¿Qué variables, categorías, relaciones y condiciones exige representar universo comercial y deduplicación de forma estructurada?

> Exige estructurar un esquema relacional normalizado con las siguientes especificaciones: 1) Variables de entidad: ID_Proveedor (PROV-001 a PROV-070), Entidad_Legal, Grupo_Corporativo, Marca_Producto, Sede_HQ (con flag de verificación), Cobertura_Comercial, Categoria_Primaria (1 a 7), Relacion_Compet

- **Verificación:** solo_sintesis_interna: 2
- **Registro:** [P02-F04.json](P02-F04.json)
### P02-F05: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre universo comercial y deduplicación?

> Cada hecho está respaldado por fuentes primarias y documentos de errata con trazabilidad exhaustiva: 1) Venta de FGS Global a KKR por WPP: respaldada por SEC Form 6-K WPP (filing a5017o.htm del 3 dic 2024) y fe de erratas (00_P02_GLOBAL_READ_ME_AND_ERRATA); 2) Adquisición de Limbik por Burson: respa

- **Verificación:** no_verificada: 1
- **Registro:** [P02-F05.json](P02-F05.json)
### P02-F06: ¿Qué caso concreto, con entradas y resultado esperado, ilustra universo comercial y deduplicación sin introducir datos no documentados?

> El caso concreto se ilustra mediante un lote de prueba de 10 entradas brutas heterogéneas tomadas del catálogo inicial: 1) Brandwatch; 2) CisionOne; 3) PR Newswire; 4) Memo; 5) Signal AI AIQ; 6) Consultation Manager; 7) Social Point; 8) AMEC (Barcelona Principles 3.0); 9) The Bridge Intelligence; 10

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P02-F06.json](P02-F06.json)

