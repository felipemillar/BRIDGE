<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 09-grafo-de-afirmaciones: Profundización especializada

**Pilar:** [P06 — Cruce de conocimiento interno y señales externas](../../TARJETA.md)  
**Módulo:** Saber

---

## Preguntas del Eje (8)

### P06-X01: ¿Qué esquema mínimo relaciona afirmación, evidencia, organización, actor, compromiso y evento?

> El esquema ontológico mínimo para relacionar conocimiento en The Bridge Intelligence se estructura conforme a los principios de T-GRAG (Li et al., 2025; ArXiv 2508.01680), GraphRAG (Edge et al., 2024; ArXiv 2404.16130) y Palantir Foundry (Doc 'Why Ontology'): 1) Nodos Entidad: Organización (empresa

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X01.json](P06-X01.json)
### P06-X02: ¿Cómo expresar relación de apoyo, conflicto, modificación y caducidad sin perder procedencia?

> La expresión de relaciones dinámicas entre afirmaciones se implementa mediante bordes reificados y tipados en el grafo de conocimiento temporal (Li et al., 2025; Thorne et al., 2018): 1) Relación de Apoyo (SUPPORTS): Conecta dos afirmaciones o una evidencia con una afirmación cuando los hechos son c

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X02.json](P06-X02.json)
### P06-X03: ¿Qué consulta reconstruye por qué se emitió una alerta en una fecha concreta?

> La reconstrucción determinista de una alerta se ejecuta mediante una consulta de Linaje Causal en Grafo Temporal (T-GRAG / Palantir AIP; Li et al., 2025; Palantir 2024): La consulta recibe el `alert_id` y el timestamp $t_{alerta}$, ejecutando un recorrido retroactivo parametrizado: `MATCH (a:Alerta

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X03.json](P06-X03.json)
### P06-X04: ¿Qué variables, categorías, relaciones y condiciones exige representar grafo de afirmaciones de forma estructurada?

> La representación estructurada del grafo de afirmaciones exige un modelo de datos formal compuesto por: 1) Variables principales: `claim_id` (UUIDv4), `subject_entity_id`, `predicate`, `object_value_or_entity`, `epistemic_status` (hecho_documentado, declaración_corporativa, rumor_redes, inferencia),

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X04.json](P06-X04.json)
### P06-X05: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre grafo de afirmaciones?

> Los hechos, arquitecturas y esquemas sobre el grafo de afirmaciones se sustentan en las siguientes fuentes canónicas verificadas en el corpus: 1) Li et al. (2025, ArXiv:2508.01680; 'T-GRAG: Dynamic GraphRAG for Temporal Conflicts', Agosto 2025): Secciones 1, 3 y 4, demostrando el modelado de grafos

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X05.json](P06-X05.json)
### P06-X06: ¿Qué caso concreto, con entradas y resultado esperado, ilustra grafo de afirmaciones sin introducir datos no documentados?

> Caso Concreto CG-P06-101 (Evolución de Meta de Emisiones Corporativas): 1) Entradas: Documento Interno D1 ('Memoria Anual 2023', pág. 45, emitida el 15-03-2024): Afirmación 'Compromiso de reducir 30% emisiones alcance 1 para 2030'. Noticia Externa N1 ('Boletín Minero', 10-06-2025): Titular 'Compañía

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X06.json](P06-X06.json)
### P06-X07: ¿Dónde discrepan fuentes originales y síntesis internas sobre grafo de afirmaciones, y qué versión prevalece según las correcciones?

> Discrepancia y prevalencia en grafo de afirmaciones: 1) Discrepancia: El dossier preliminar P06_RESEARCH_DOSSIER proponía un grafo estático clásico tipo Neo4j donde las afirmaciones contrarias simplemente sobrescribían las anteriores o generaban un flag global de conflicto sin dimensión de tiempo, s

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X07.json](P06-X07.json)
### P06-X08: ¿Qué sigue sin prueba sobre grafo de afirmaciones, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba empírica formal la escalabilidad y latencia en tiempo real de consultas GraphRAG multi-salto sobre grafos con más de 1.000.000 de afirmaciones corporativas heterogéneas (P06_GAPS_AND_VALIDATION, Sección 3.1). Las fuentes del corpus (T-GRAG y GraphRAG) presentan pruebas experimentale

- **Verificación:** no_verificada: 1
- **Registro:** [P06-X08.json](P06-X08.json)

