<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 06-desambiguacion-y-analisis-de-senales: Desambiguación y análisis de señales

**Pilar:** [P03 — Monitoreo del entorno y acceso a fuentes](../../TARJETA.md)  
**Módulo:** Escuchar

---

## Preguntas del Eje (8)

### P03-C11: ¿Dónde discrepan fuentes originales y síntesis internas sobre desambiguación y análisis de señales, y qué versión prevalece según las correcciones?

> La discrepancia principal radicaba en que las síntesis preliminares afirmaban que el modelo fundacional en español BETO (Cañete et al. 2020) resolvía de forma nativa la comprensión del dialecto chileno, la ironía política y la postura en controversias regulatorias complejas. Prevalece la rigurosa ca

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C11.json](P03-C11.json)
### P03-C12: ¿Qué sigue sin prueba sobre desambiguación y análisis de señales, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba la exactitud del análisis de postura (stance analysis) y clasificación de riesgo reputacional en el debate regulatorio y corporativo chileno: 1) Brecha: Ausencia absoluta de un conjunto de datos de evaluación (benchmark) estandarizado y público anotado con lenguaje y coyunturas de p

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C12.json](P03-C12.json)
### P03-F31: ¿Cómo se distinguen homónimos, filiales, productos y personas con nombres similares?

> La desambiguación precisa de homónimos, filiales, marcas comerciales y ejecutivos se resuelve mediante una arquitectura de Entity Linking de dos etapas (Wu et al. 2020 - BLINK): 1) Recuperación densa de candidatos (Bi-Encoder): el contexto textual de la mención y las descripciones canónicas de la ba

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F31.json](P03-F31.json)
### P03-F32: ¿Qué método permite detectar temas emergentes aun cuando no mencionan a la empresa?

> El método estándar es el Modelado de Tópicos Neuronal Dinámico no supervisado mediante BERTopic (Grootendorst 2022): 1) Generación de embeddings: se transforman los documentos noticiosos y publicaciones del entorno en representaciones vectoriales densas de oraciones (Sentence Transformers o BETO); 2

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F32.json](P03-F32.json)
### P03-F33: ¿Qué límites tienen sentimiento automático, clasificación narrativa y detección de desinformación?

> El análisis automático presenta 3 limitaciones metodológicas y técnicas infranqueables sin supervisión humana: 1) Fracaso del sentimiento tripolar genérico (Positivo/Negativo/Neutro): no detecta ironía ni sarcasmo, confunde el tono crítico de una investigación seria con un ataque reputacional, e ign

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F33.json](P03-F33.json)
### P03-F34: ¿Qué variables, categorías, relaciones y condiciones exige representar desambiguación y análisis de señales de forma estructurada?

> La representación estructurada exige: 1) Variables técnicas de NLP: `confidence_score_linking` (0.0 a 1.0), `candidate_entity_id`, `topic_cluster_id` (HDBSCAN label), `topic_coherence_score`, `stance_direction` (favor, contra, neutral, ambivalente) y `disarm_ttp_code` (ej. T0015); 2) Categorías de s

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F34.json](P03-F34.json)
### P03-F35: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre desambiguación y análisis de señales?

> Los hechos de este eje están respaldados por: 1) Arquitectura de desambiguación densa: Wu et al. (2020, 'Scalable Zero-shot Entity Linking with Dense Entity Retrieval' - BLINK paper, arXiv:1911.03814); 2) Modelado neuronal de tópicos no supervisado: Grootendorst (2022, 'BERTopic: Neural Topic Modeli

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F35.json](P03-F35.json)
### P03-F36: ¿Qué caso concreto, con entradas y resultado esperado, ilustra desambiguación y análisis de señales sin introducir datos no documentados?

> Caso: Detección y desambiguación de una polémica sobre el uso de salmueras en el Salar de Atacama que involucra a una filial y a un competidor. Entradas: 1) Nota de prensa que menciona 'la empresa minera SQM Salar' y a su ejecutivo 'Patricio Contesse'; 2) Modelo BLINK procesando la mención: el bi-en

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F36.json](P03-F36.json)

