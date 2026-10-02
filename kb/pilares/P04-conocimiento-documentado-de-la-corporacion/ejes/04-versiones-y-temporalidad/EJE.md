<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 04-versiones-y-temporalidad: Versiones y temporalidad

**Pilar:** [P04 — Conocimiento documentado de la corporación](../../TARJETA.md)  
**Módulo:** Saber

---

## Preguntas del Eje (8)

### P04-C07: ¿Dónde discrepan fuentes originales y síntesis internas sobre versiones y temporalidad, y qué versión prevalece según las correcciones?

> Discrepancia Principal: La práctica de ingeniería de software documental convencional recurre con frecuencia a la 'reindexación por sobreescritura' (batch overwrite nocturno) o al borrado de documentos superados para ahorrar costos de almacenamiento en bases vectoriales. En fuerte contradicción, los

- **Verificación:** no_verificada: 1
- **Registro:** [P04-C07.json](P04-C07.json)
### P04-C08: ¿Qué sigue sin prueba sobre versiones y temporalidad, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Vacío e Incertidumbre: Sigue sin prueba empírica formal la resolución algorítmica de 'reexpresiones implícitas o silenciosas de líneas base' cuando una empresa altera una cifra histórica en una tabla comparativa sin añadir una nota técnica explícita al pie de página ni emitir una fe de erratas. Fuen

- **Verificación:** no_verificada: 1
- **Registro:** [P04-C08.json](P04-C08.json)
### P04-F19: ¿Qué diferencia hay entre fecha del hecho, fecha de publicación y fecha de incorporación al sistema?

> La gestión rigurosa de memoria corporativa desacopla tres dimensiones temporales independientes: 1) Fecha del Hecho (Event Time / Valid Time): momento físico en que ocurrió el suceso, se ejecutó la medición o rigió el ejercicio contable (e.g. año operativo 2024 o fecha exacta de un incidente operaci

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F19.json](P04-F19.json)
### P04-F20: ¿Cómo debe responderse una pregunta sobre lo que la empresa sabía o decía en una fecha histórica?

> Una consulta sobre el conocimiento o postura corporativa en una fecha histórica (Point-in-Time / As-of Query) debe responderse ejecutando un corte temporal retrospectivo estricto sobre el Grafo y el índice de recuperación. El protocolo exige: 1) Fijar como filtro de consulta que `transaction_time <=

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-F20.json](P04-F20.json)
### P04-F21: ¿Qué regla prevalece cuando un documento fue corregido, retirado o reemplazado?

> La regla que prevalece se rige por el Principio de No-Destrucción Histórica y Prevalencia de Superación Normativa (W3C DCAT-3 y PROV-O): 1) Regla de Inmutabilidad: el documento original nunca se elimina ni se sobreescribe físicamente; su hash SHA-256 se preserva para auditoría y peritaje legal; 2) R

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F21.json](P04-F21.json)
### P04-F22: ¿Qué variables, categorías, relaciones y condiciones exige representar versiones y temporalidad de forma estructurada?

> Representar versiones y temporalidad estructuradas exige: 1) Variables de marca temporal (`event_date_start`, `event_date_end`, `publication_date`, `system_ingestion_timestamp`); 2) Propiedades de versión (`version_number` semántico, `version_status`: Activo, Superado, Retirado, Borrador; `reexpress

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F22.json](P04-F22.json)
### P04-F23: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre versiones y temporalidad?

> Los hechos relativos a versiones y temporalidad corporativa se sustentan en cuatro fuentes primarias del corpus: 1) W3C DCAT-3 Data Catalog Vocabulary (mayo 2024), que define las propiedades de versionado y sustitución documental (`dcterms:replaces`, `dcterms:isReplacedBy`); 2) W3C PROV-O (abril 201

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F23.json](P04-F23.json)
### P04-F24: ¿Qué caso concreto, con entradas y resultado esperado, ilustra versiones y temporalidad sin introducir datos no documentados?

> Caso Canónico: Reexpresión de línea base de emisiones de Gases de Efecto Invernadero (GEI) tras la venta de un activo industrial. Entradas documentadas: 1) Meta original en Memoria 2022: Reducción del 30% en emisiones Alcance 1 al 2030, con línea base 2020 de 500.000 tCO2e; 2) Evento societario en 2

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F24.json](P04-F24.json)

