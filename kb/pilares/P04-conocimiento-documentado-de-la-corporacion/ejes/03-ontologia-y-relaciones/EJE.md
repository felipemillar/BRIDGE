<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 03-ontologia-y-relaciones: Ontología y relaciones

**Pilar:** [P04 — Conocimiento documentado de la corporación](../../TARJETA.md)  
**Módulo:** Saber

---

## Preguntas del Eje (8)

### P04-C05: ¿Dónde discrepan fuentes originales y síntesis internas sobre ontología y relaciones, y qué versión prevalece según las correcciones?

> Discrepancia Principal: Soluciones comerciales de bases de datos de grafos para empresas promueven la extracción automática de entidades y relaciones mediante LLMs ('Zero-shot Open Information Extraction') insertando todas las tripletas resultantes en el grafo como verdades homogéneas. En agudo cont

- **Verificación:** no_verificada: 1
- **Registro:** [P04-C05.json](P04-C05.json)
### P04-C06: ¿Qué sigue sin prueba sobre ontología y relaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Vacío e Incertidumbre: Falta una ontología de dominio abierta y validada empíricamente para el ecosistema societario y regulatorio chileno, que interopere nativamente entre el RUT corporativo de la CMF, las Resoluciones de Calificación Ambiental (RCA) del SEIA/SMA y los registros de concesiones mine

- **Verificación:** no_verificada: 1
- **Registro:** [P04-C06.json](P04-C06.json)
### P04-F13: ¿Qué entidades y relaciones son necesarias para representar la memoria corporativa?

> Representar la memoria corporativa exige un Grafo de Conocimiento (Knowledge Graph) compuesto por 7 clases maestras de entidades y sus relaciones dirigidas: 1) `org:Organization` (matriz, filiales, subsidiarias con RUT/LEI); 2) `corp:FacilityProject` (faenas operacionales, plantas industriales o pro

- **Verificación:** verificada: 1
- **Registro:** [P04-F13.json](P04-F13.json)
### P04-F14: ¿Qué casos exigen separar matriz, filial, proyecto, instalación y vocero?

> La separación estricta entre matriz, filial, proyecto, instalación y vocero es mandatoria en tres casos operacionales críticos: 1) Controversias Regulatorias y Ambientales: los permisos (e.g. Resoluciones de Calificación Ambiental - RCA en Chile ante la SMA o el SEIA) y los cargos por incumplimiento

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F14.json](P04-F14.json)
### P04-F15: ¿Cómo se evita que un grafo convierta una relación inferida en hecho comprobado?

> Para evitar que un grafo de conocimiento promueva una relación inferida (inducida por algoritmos o modelos de lenguaje) al estatus de hecho comprobado, se aplican tres salvaguardas arquitectónicas estrictas: 1) Tipificación Epistémica de Aristas (Edge Properties / Named Graphs): toda arista en el gr

- **Verificación:** no_verificada: 1
- **Registro:** [P04-F15.json](P04-F15.json)
### P04-F16: ¿Qué variables, categorías, relaciones y condiciones exige representar ontología y relaciones de forma estructurada?

> La representación estructurada de la ontología corporativa y sus relaciones exige: 1) Variables de nodo (`node_id`, `node_type`, `canonical_name`, `jurisdiction_rut_lei`, `valid_period`); 2) Propiedades de arista (`edge_id`, `predicate`, `source_node`, `target_node`, `epistemic_status`, `confidence_

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-F16.json](P04-F16.json)
### P04-F17: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ontología y relaciones?

> Los fundamentos sobre ontología y relaciones corporativas descansan en cuatro fuentes primarias del corpus: 1) EDM Council Financial Industry Business Ontology (FIBO, edición marzo 2024), módulos Corporate Governance y Business Entities, que tipifican personas jurídicas, filiales y titularidad forma

- **Verificación:** verificada: 1
- **Registro:** [P04-F17.json](P04-F17.json)
### P04-F18: ¿Qué caso concreto, con entradas y resultado esperado, ilustra ontología y relaciones sin introducir datos no documentados?

> Caso Canónico: Desambiguación y trazado de responsabilidad ante una contingencia operacional en una división minera. Entradas documentadas: 1) Entidad Matriz: 'Holding Minero del Norte S.A.' (RUT matriz consolidada); 2) Entidad Filial Titular: 'Minera Cordillera Andina S.A.' (RUT filial con 100% de

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P04-F18.json](P04-F18.json)

