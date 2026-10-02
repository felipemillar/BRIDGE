<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 03-ficha-de-compromiso: Ficha de compromiso

**Pilar:** [P09 — Memoria de relaciones y gestión de compromisos](../../TARJETA.md)  
**Módulo:** Relacionar

---

## Preguntas del Eje (8)

### P09-C05: ¿Dónde discrepan fuentes originales y síntesis internas sobre ficha de compromiso, y qué versión prevalece según las correcciones?

> Discrepancia Principal: En síntesis preliminares se permitía consignar la titularidad del compromiso a entidades colectivas o departamentos corporativos (e.g., 'Responsable: Gerencia de Sustentabilidad' o 'Equipo de Faena'). La literatura de SRM (Boréalis, Tractivity) demuestra que las asignaciones

- **Verificación:** no_verificada: 1
- **Registro:** [P09-C05.json](P09-C05.json)
### P09-C06: ¿Qué sigue sin prueba sobre ficha de compromiso, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Brecha sin Prueba: El corpus no documenta el porcentaje de compromisos asumidos en el sector minero chileno que requieren renegociación formal por desfases de permisología ambiental estatal (e.g., demoras en permisos sectoriales de la DGA o Sernageomin ajenos al titular), existiendo incertidumbre so

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P09-C06.json](P09-C06.json)
### P09-F13: ¿Qué campos identifican promesa, responsable, beneficiario, plazo, evidencia y estado?

> La Ficha de Compromiso (Entity_Commitment) requiere 14 atributos nucleares estandarizados: 1) ID único inmutable (e.g., COMP-2025-089); 2) Título y descripción operativa SMART (específica, medible, alcanzable, relevante y temporal); 3) Tipología de compromiso (voluntario comunitario, exigencia de RC

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F13.json](P09-F13.json)
### P09-F14: ¿Cómo se enlaza el compromiso con acta, proyecto, autoridad y documentos internos?

> El enlace del compromiso opera a través de un grafo relacional de integridad referencial bidireccional: 1) Con el Acta/Interacción: Cada compromiso posee una clave foránea `origin_interaction_id` y `origin_minutes_document_id` que apunta al archivo probatorio (con hash SHA-256); 2) Con el Proyecto o

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F14.json](P09-F14.json)
### P09-F15: ¿Qué excepciones requieren aprobación, explicación pública o escalamiento?

> El sistema categoriza tres niveles de excepción que exigen protocolos rigurosos de gobernanza: 1) Modificación de Alcance o Presupuesto: Requiere aprobación formal del Gerente de Asuntos Corporativos y el Gerente de Operaciones, registrando el motivo técnico justificatorio en el audit trail inmutabl

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F15.json](P09-F15.json)
### P09-F16: ¿Qué variables, categorías, relaciones y condiciones exige representar ficha de compromiso de forma estructurada?

> La representación estructurada de la Ficha de Compromiso exige: 1) Identificadores y Metadatos: `commitment_id` (UUID), `code` (slug alfanumérico), `title`, `description_smart`, `category` (ambiental, social, laboral, infraestructura, lobby_acuerdo), `origin_type` (rca_legal, voluntary_dialogue, gri

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F16.json](P09-F16.json)
### P09-F17: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre ficha de compromiso?

> Los hechos normativos y metodológicos relativos a la Ficha de Compromiso están respaldados por: 1) Boréalis SRM (2024, 'The Proving Problem'): Documenta los atributos indispensables de una promesa auditable, la exigencia de dueño único y el bloqueo de cierre sin evidencia comprobatoria; 2) Tractivit

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F17.json](P09-F17.json)
### P09-F18: ¿Qué caso concreto, con entradas y resultado esperado, ilustra ficha de compromiso sin introducir datos no documentados?

> Caso Concreto Documentado: 'Compromiso de Pavimentación Participativa y Supresión de Polvo en Ruta G-25'. Entradas: 1) ID: COMP-2025-0104; 2) Título: 'Aplicación de supresor de polvo en tramo El Canelo - El Manzano'; 3) Tipo: Voluntario de relacionamiento comunitario derivado de mesa de trabajo; 4)

- **Verificación:** no_verificada: 1
- **Registro:** [P09-F18.json](P09-F18.json)

