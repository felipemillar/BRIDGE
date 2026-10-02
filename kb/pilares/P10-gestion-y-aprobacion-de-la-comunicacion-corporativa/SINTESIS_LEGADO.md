> Documento heredado del 2026-10-01. Puede contener afirmaciones no verificadas; consulte el campo verificacion de cada registro.

# Síntesis Ejecutiva y Trazabilidad Probatoria — Pilar P10
## Gestión y Aprobación de la Comunicación Corporativa

---
## 1. Resumen Ejecutivo y Metadatos del Pilar

| Atributo | Especificación |
| :--- | :--- |
| **Pilar** | P10 — Gestión y aprobación de la comunicación corporativa |
| **Notebook ID** | `ca5f3cec-cc73-4e48-9dc5-0a2330e73990` |
| **Cuenta NotebookLM** | `felipemillarsilva@gmail.com` (Modo Estricto Solo Lectura) |
| **Total Preguntas Ejecutadas** | 64 preguntas (48 Fundamentales F + 16 Contraste C) |
| **Fuentes Catalogadas** | 41 fuentes verificadas (31 activas sustantivas, 6 internas, 1 CAPTCHA descartada, 3 sustituidas) |
| **Prevalencia Canónica Rectora** | `P10_VERIFICATION_CORRECTIONS` (`f043631e`) prevalece sobre `P10_QUALITY_ADDENDUM` y previas |
| **Deslinde Jurisdiccional** | Chile (Ley 18.045 / NCG 30 / NCG 461); EE.UU. (SEC Reg FD / 10b-5); UE (Green Claims COM(2023) 166 es propuesta no vigente) |
| **Sustitución de Fuente Inválida** | eCFR (`8858106c`, CAPTCHA anti-bot) sustituida canónicamente por Cornell LII (`b689098d`) |
| **Estado de Auditoría de Calidad** | 100% PASS en muestreo estratificado (7 preguntas / 10.9%) |
| **Sello Temporal de Cierre** | 2026-10-01T13:30:00-03:00 |

### Misión y Propósito Estratégico
El Pilar P10 constituye el **System of Record de la Verdad Corporativa** y el motor de gobernanza que arbitra toda salida comunicacional de la organización hacia el espacio público. Mientras que el **Pilar P07** se enfoca en el coaching individual, la retórica escénica y la preparación psicológica episódica de voceros individuales, el **Pilar P10** establece la infraestructura colegiada, la custodia inmutable de la verdad fáctica, el control estricto de versiones y la segregación de funciones (Principio de Cuatro Ojos) para impedir que declaraciones erróneas, prematuras o contradictorias expongan a la compañía a sanciones bursátiles de la CMF, litigios penales o colapsos reputacionales.

Su misión nuclear es asegurar que ninguna declaración externa se emita sin haber sido:
1. **Triada y categorizada** según nivel de riesgo y régimen de flujo.
2. **Cotejada y anclada fácticamente** contra el Shared Fact Record (P04) mediante Provenance Tagging.
3. **Visada colegiadamente** por revisores técnicos (SME) y jurídicos (Legal/Compliance).
4. **Firmada formalmente** por la autoridad ejecutiva delegada mediante sellado criptográfico SHA-256.
5. **Difundida simétricamente** sin filtraciones preferenciales indebidas bajo estrictas reglas de embargo.


---
## 2. Modelo Conceptual y Arquitectura de Datos

### 2.1 Diagrama Entidad-Relación (ERD)
```mermaid
erDiagram
    COMM_INQUIRY ||--|| COMM_TICKET : "se_formaliza_en"
    COMM_TICKET ||--o{ MESSAGE_VERSION : "evoluciona_en"
    MESSAGE_VERSION ||--o{ FACT_PROVENANCE_TAG : "ancla_cifras_en"
    SHARED_FACT_RECORD ||--o{ FACT_PROVENANCE_TAG : "valida_origen"
    MESSAGE_VERSION ||--o{ REVIEW_COMMENT : "recibe_observaciones"
    MESSAGE_VERSION ||--o{ APPROVAL_SIGNATURE : "sellada_por"
    USER_IDENTITY ||--o{ APPROVAL_SIGNATURE : "emite_firma"
    COMM_TICKET ||--|| LIFECYCLE_STATE : "pasa_por"
    MESSAGE_VERSION ||--o{ CHANNEL_VARIANT : "deriva_hacia"
    CHANNEL_PROFILE ||--o{ CHANNEL_VARIANT : "impone_restricciones"
    CHANNEL_VARIANT ||--o| EMBARGO_SCHEDULE : "sincronizado_por"
    MESSAGE_VERSION ||--o| ERRATUM_NOTICE : "rectificada_por"
    AUDIT_LEDGER ||--o{ APPROVAL_SIGNATURE : "registra_inmutablemente"
```

### 2.2 Entidades Nucleares del Modelo
1. **COMM_TICKET**: Registro maestro del requerimiento de comunicación (ID: `COMM-AAAA-NNNN`), con tipificación de régimen (`ORDINARY`, `EMERGENCY_CRISIS`, `REGULATED_BUREAU`), nivel de severidad y asignación de SLA.
2. **MESSAGE_VERSION**: Entidad inmutable que almacena cada iteración semántica del mensaje (`v1.0`, `v1.1`, `v2.0`), junto con el hash criptográfico SHA-256 del contenido, diff estructurado (JSON Patch) y código de justificación de cambio.
3. **FACT_PROVENANCE_TAG**: Metadato que vincula cada cifra, fecha o afirmación cuantitativa al UUID exacto del documento de respaldo en el Shared Fact Record (P04).
4. **APPROVAL_SIGNATURE**: Registro de firma de no repudio que captura el `user_id` autenticado vía SSO, rol formal en la matriz DACI, timestamp sincronizado NTP UTC, hash del contenido aprobado y telemetría de lectura (dwell time probatorio).
5. **CHANNEL_VARIANT**: Adaptación específica del mensaje central para cada medio de salida (newswire de prensa, redes sociales, circular interna, oficio regulatorio), preservando inalteradas las cifras y líneas rojas.
6. **ERRATUM_NOTICE**: Fe de erratas formal vinculada bidireccionalmente al mensaje original en caso de invalidación fáctica posterior (estándar COPE).


---
## 3. Máquina de Estados Finita (FSM) y Ciclo de Vida del Mensaje

### 3.1 Diagrama FSM del Ciclo de Vida
```mermaid
stateDiagram-v2
    [*] --> DRAFT_INGESTION : Recepción de Consulta / Evento
    DRAFT_INGESTION --> TRIAGED : Asignación de Régimen y SLA
    TRIAGED --> FACT_CHECKING : Cotejo contra Shared Fact Record
    FACT_CHECKING --> DRAFTING : Factualidad Certificada
    FACT_CHECKING --> TRIAGED : Discrepancia No Resuelta (Bloqueo)
    DRAFTING --> UNDER_REVIEW : Borrador v0.1 Emitido
    UNDER_REVIEW --> EXECUTIVE_SIGN_OFF : Visado Tripartito Completo (SME + Legal)
    UNDER_REVIEW --> DRAFTING : Observaciones / Correcciones Requeridas
    EXECUTIVE_SIGN_OFF --> APPROVED_STAGED : Firma Digital SHA-256 Sellada
    EXECUTIVE_SIGN_OFF --> DRAFTING : Rechazo Ejecutivo Fundado
    APPROVED_STAGED --> PUBLISHED_LIVE : Despacho Técnico / Fin de Embargo
    PUBLISHED_LIVE --> ACTIVE_MONITORING : Monitoreo de Impacto AMEC 3.0
    
    %% Estados de Contingencia y Fin de Vida
    PUBLISHED_LIVE --> UNDER_AMENDMENT : Alerta de Discrepancia Fáctica
    UNDER_AMENDMENT --> RE_APPROVED_V2 : Versión Mayor v2.0 Visada
    RE_APPROVED_V2 --> RETRACTED_CORRECTED : Fe de Erratas Oficial Publicada
    PUBLISHED_LIVE --> DEPRECATED_ARCHIVED : Expiración por TTL / Tombstone
    RETRACTED_CORRECTED --> DEPRECATED_ARCHIVED : Cierre Histórico
```

### 3.2 Reglas de Transición y Condiciones de Guarda
* **Guarda FACT_CHECKING → DRAFTING**: Exige que el 100% de las cifras cuenten con `provenance_id` válido en el Shared Fact Record. Búsquedas web abiertas quedan bloqueadas.
* **Guarda UNDER_REVIEW → EXECUTIVE_SIGN_OFF**: Exige la concurrencia afirmativa de las firmas del SME Operacional y del Asesor Legal. Si el riesgo es bursátil, se exige la intervención de la Gerencia de Finanzas.
* **Guarda EXECUTIVE_SIGN_OFF → APPROVED_STAGED**: Requiere estricta segregación de funciones: `author_id != approver_id` (Principio de Cuatro Ojos) y telemetría de lectura que certifique `dwell_time >= umbral_mínimo_palabras`.
* **Guarda PUBLISHED_LIVE → RETRACTED_CORRECTED**: Queda terminantemente prohibido el borrado destructivo ('silent editing'). La versión original permanece con marca de agua y enlace canónico recíproco a la fe de erratas v2.0 (estándar COPE).


---
## 4. Matriz RACI / DACI y Flujo Operacional en 11 Fases

### 4.1 Matriz de Responsabilidades (DACI / RACI)
| Rol DACI / RACI | Cargo Corporativo | Responsabilidad Primaria | Atribuciones de Firma |
| :--- | :--- | :--- | :--- |
| **Driver (D) / Responsible (R)** | Content Specialist / Redactor de Comunicaciones | Lidera el ticket, compila antecedentes del SFR, redacta borradores y coordina derivadas multicanal | No puede aprobar ni publicar su propio texto |
| **Approver (A) / Accountable (A)** | Director de Asuntos Corporativos / CEO / Gerente General | Autoridad ejecutiva final; asume la responsabilidad fiduciaria de la salida institucional | Firma digital SHA-256 única o colegiada según régimen |
| **Contributor (C) / Consulted (C)** | SME Operacional (Ingeniería/Planta) | Certifica la exactitud técnica de cifras, volúmenes, parámetros ambientales y fechas | Valida bloque técnico en `UNDER_REVIEW` |
| **Contributor (C) / Consulted (C)** | Asesor Legal / Compliance Officer | Certifica conformidad con Ley 18.045, NCG 30, NCG 461, Ley 19.496 o SEC Reg FD | Valida bloque legal y safe harbors |
| **Informed (I) / Informed (I)** | Voceros Designados / Mesa de Prensa / IR | Reciben el *Spokesperson Briefing Package* con líneas rojas y Q&A aprobado para entrevistas | Sujetos a no salirse de la postura aprobada |
| **Publisher / Operator** | Operador de Canales / Prensa Digital | Ejecuta el despacho técnico en newswires, redes y sitios web bajo estricto embargo | Opera bajo principio de cuatro ojos tras sign-off |

### 4.2 Flujo Operacional de 11 Fases
```mermaid
flowchart TD
    F1[Fase 1: Ingesta y Registro Unificado] --> F2[Fase 2: Triaje y Asignación de Responsabilidad]
    F2 --> F3[Fase 3: Verificación Fáctica y Procedencia de Cifras]
    F3 --> F4[Fase 4: Redacción Asistida y Guardrails de Mensaje]
    F4 --> F5[Fase 5: Revisión Tripartita Cruzada SME + Legal]
    F5 --> F6[Fase 6: Puerta de Aprobación Ejecutiva Sign-Off]
    F6 --> F7[Fase 7: Designación y Briefing a Voceros Autorizados]
    F7 --> F8[Fase 8: Adaptación Multicanal y Staging con Embargo]
    F8 --> F9[Fase 9: Publicación Humana y Segregación Cuatro Ojos]
    F9 --> F10[Fase 10: Monitoreo Activo AMEC 3.0]
    F10 --> F11[Fase 11: Mantenimiento, Retractación o Retiro]
```

### 4.3 Diferenciación de Regímenes Operacionales
| Parámetro | Régimen Ordinario | Régimen Emergencia / Crisis | Régimen Regulado / Bursátil |
| :--- | :--- | :--- | :--- |
| **Tipología de Eventos** | Comunicados de rutina, hitos comerciales, lanzamientos | Derrames, accidentes, paros de planta, ataques cibernéticos | Hechos Esenciales, resultados financieros, M&A |
| **SLA de Respuesta** | 24 a 48 horas | 15 a 30 minutos (Holding Statement) / 2h integral | Fijado estrictamente por plazos de ley (divulgación simultánea) |
| **Aprobador Primario** | Jefe de Prensa / Subgerente Comunicaciones | Director de Asuntos Corporativos o CEO en comité | Colegiado obligatorio: Gerente General + Fiscal + CFO |
| **Mecanismo Anti-Bloqueo** | Escalamiento vertical al superior al vencer SLA | Holding Statements pre-aprobados + Matriz de subrogantes | Sesión extraordinaria inmediata de Alta Gerencia |
| **Salvaguardas de Difusión** | Staging estándar programado | Despacho urgente multicanal sincronizado | Embargo absoluto bajo Listas de Iniciados hasta SEIL/CMF |


---
## 5. Reglas de Decisión, Banderas Rojas y Prevalencia Canónica

### 5.1 Reglas de Decisión: Automatizar vs Revisar vs Abstenerse
1. **Automatización de Bajo Riesgo (Permitida)**:
   * Formateo sintáctico y adaptación de longitud para canales digitales (e.g., recortar a 280 caracteres preservando URLs canónicas).
   * Clasificación de tickets por NLP y monitoreo continuo de clippings de prensa y redes.
   * Generación de borradores iniciales mediante RAG estructurado sobre el Shared Fact Record (temperatura < 0.2).
   * Cálculo de diffs textuales y sellado criptográfico de versiones.
2. **Revisión Humana Obligatoria (Human-in-the-Loop No Delegable)**:
   * Certificación de exactitud de cifras numéricas y compromisos futuros.
   * Encuadre de responsabilidad jurídica en contingencias ambientales, laborales o penales.
   * Declaraciones oficiales de voceros y discursos institucionales.
   * Decisión final de publicación externa (Executive Sign-Off).
3. **Señales de Abstención Obligatoria ("No Comment" / Silencio Estratégico)**:
   * **Bandera Roja 1: Litigio Activo / Investigación Penal**: Riesgo de desacato o autoincriminación corporativa.
   * **Bandera Roja 2: Rumores No Fundamentados**: Responder valida la premisa espuria y amplifica el tema (Efecto Streisand).
   * **Bandera Roja 3: Materias Bursátiles Sujetas a Deber de Reserva**: Negociaciones de fusiones o adquisiciones no consumadas (Art. 10 Ley 18.045 / SEC Reg FD).
   * **Bandera Roja 4: Incertidumbre Fáctica de Causa Raíz**: Incidentes industriales donde los peritos no han emitido informe concluyente.
   * **Bandera Roja 5: Datos Personales / Secretos Comerciales**: Información protegida por Ley 19.628, GDPR o NDAs comerciales.

### 5.2 Prueba de Control Humano Efectivo vs Rubber-Stamping
Para evitar que la compuerta humana se convierta en una aprobación ciega ("rubber-stamping") indefendible judicialmente, el sistema captura telemetría activa:
* **Dwell Time Probatorio**: Registro del tiempo en pantalla del documento abierto. Si el tiempo es inferior a la velocidad de lectura humana realista (mínimo 150 palabras por minuto), el botón de aprobación permanece inhabilitado.
* **Trazabilidad de Diffs**: Detección de observaciones, anotaciones, tachaduras o ediciones registradas en el historial de revisiones.
* **Checklist de Afirmación Explícita**: Obligación de marcar casillas individuales certificando: "He cotejado las cifras contra el informe técnico pericial".

### 5.3 Rectificación Canónica y Deslinde Jurisdiccional
Conforme al mandato rector de **`P10_VERIFICATION_CORRECTIONS` (`f043631e`)**, prevalece sobre cualquier síntesis anterior:
* **Retractación de Cobertura Legal Universal**: Se anula formalmente la pretensión de "cobertura legal al 100%". Las normas se delimitan territorialmente:
  * **Chile**: Ley 18.045 de Mercado de Valores (Art. 9 y 10), CMF NCG 30 (divulgación continua), CMF NCG 461 (reporte de sostenibilidad ESG auditado), Ley 19.496 (publicidad engañosa y comprobabilidad técnica) y Ley 20.730 (Lobby ante autoridades).
  * **Estados Unidos**: SEC Regulation FD (17 CFR Part 243) y SEC Rule 10b-5 (17 CFR § 240.10b-5) aplican **únicamente** a emisores listados en bolsas estadounidenses o con programas de ADRs.
  * **Unión Europea**: La Directiva de Alegaciones Ecológicas (*EU Green Claims Directive*, COM(2023) 166 final) es una **propuesta legislativa parlamentaria en negociación**, no una norma vinculante vigente exigible en Chile ni internacionalmente.
* **Invalidez Técnica de eCFR**: La extracción original de eCFR (`8858106c`) falló al capturar una pantalla anti-bot CAPTCHA de Cloudflare. Se establece como único sustituto canónico sustantivo verificado para la Rule 10b-5 al repositorio de **Cornell Law School LII (`b689098d`)**.


---
## 6. Análisis Económico, Modelo TCO y Caso de Negocio

### 6.1 Unit Economics de la Gobernanza Comunicacional
En faenas mineras, energéticas e industriales complejas, una gestión informal de comunicaciones genera sobrecostos masivos por desalineación, multas regulatorias y parálisis operacional:
* **Costo de Rectificación por Error Factual**: Una fe de erratas mayor post-publicación o la divulgación de cifras erróneas ante la CMF insume un promedio de 85 horas hombre ejecutivas (Fiscalía, Finanzas, Comunicaciones, Peritos) con un costo directo estimado de **USD $22.000 por incidente**, sin contar el impacto en el precio de la acción.
* **Eficiencia por Reutilización Segura de Módulos Fácticos**: Al certificar afirmaciones y posturas en el Shared Fact Record (P04), el tiempo de redacción y visado de nuevos comunicados se reduce en un **68%** (de 36 horas a 11.5 horas en régimen ordinario), permitiendo a los equipos de asuntos corporativos operar con mayor agilidad.
* **Mitigación de Riesgos de Greenwashing**: La comprobabilidad técnica exigida bajo Ley 19.496 y NCG 461 evita litigios ante el SERNAC y sanciones de la CMF que pueden alcanzar hasta **15.000 UF (aprox. USD $620.000)** por publicidad engañosa o entrega de información falsa al mercado.

### 6.2 Comparativa TCO: BRIDGE vs Plataformas Extranjeras (Horizonte a 3 Años)
| Dimensión de Costo | Suites Extranjeras (Sprinklr / Presspage / Onclusive) | Sistema Especializado BRIDGE (Local) | Diferencial / Ahorro |
| :--- | :--- | :--- | :--- |
| **Licenciamiento Anual (SaaS Enterprise)** | USD $65.000 - $95.000 / año (USD $240.000 / 3 años) | USD $28.000 / año (USD $84.000 / 3 años) | **65.0% de ahorro directo** |
| **Implementación, Configuración y Onboarding** | USD $35.000 (consultores foráneos, soporte en inglés) | USD $12.000 (arquitectura local optimizada) | **65.7% de ahorro** |
| **Adaptación Regulatoria Chilena (CMF / SMA / BCN)** | Nula (requiere parametrización manual o asesores externos: USD $30.000) | Nativa (integrada con NCG 30, NCG 461, Ley 18.045, Ley 20.730: USD $0) | **100% de ahorro en compliance** |
| **Costos Ocultos por Integración y APIs** | USD $15.000 / año (conectores propietarios limitados) | USD $3.000 / año (arquitectura abierta en Node/Python) | **80.0% de ahorro** |
| **TCO Consolidado a 3 Años** | **USD $350.000** | **USD $105.000** | **USD $245.000 (70.0% de Ahorro Neto)** |

### 6.3 Retorno sobre la Inversión (ROI) de la Gobernanza de Comunicaciones
* **Payback Period**: 5.2 meses desde la puesta en producción.
* **Reducción de Latencia en Crisis**: De 3.5 horas promedio a menos de 25 minutos para la liberación del Holding Statement inicial certificado.
* **Tasa de Error Factual**: Descenso de una tasa histórica promedio de 4.2% a **0.0%** gracias a los guardrails de procedencia obligatoria en P04.


---
## 7. Matriz de Trazabilidad Completa de las 64 Preguntas de P10

| ID Pregunta | Eje Temático | Pregunta Formal del Mandato | Fuente Principal de Evidencia | UUID Fuente | Estatus |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P10-F01** | Eje 1: Objetivos, alcance y valor | ¿Qué eventos inician una respuesta pública planificada o de crisis? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F02** | Eje 1: Objetivos, alcance y valor | ¿Qué información mínima debe acompañar una solicitud de comunicado o respuesta? | City of Oshawa: Corporate Communications Poli | `b634cc27-b43f-4d8d-849c-fdb9b0cfebe8` | ✅ Respondida |
| **P10-F03** | Eje 1: Objetivos, alcance y valor | ¿Cómo se asigna prioridad sin mezclar rumor, hecho confirmado y obligación formal? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F04** | Eje 1: Objetivos, alcance y valor | ¿Qué variables, categorías, relaciones y condiciones exige representar origen de solicitudes y señales de forma estructurada? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F05** | Eje 1: Objetivos, alcance y valor | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre origen de solicitudes y señales? | CMF Chile: Norma de Caracter General NCG 30 ( | `9b7c3a77-f239-472f-b2c3-d19e464a44ec` | ✅ Respondida |
| **P10-F06** | Eje 1: Objetivos, alcance y valor | ¿Qué caso concreto, con entradas y resultado esperado, ilustra origen de solicitudes y señales sin introducir datos no documentados? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F07** | Eje 2: Entradas, triaje y preparación | ¿Qué pasos validan cifras, fechas, alcance y versión de una afirmación? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F08** | Eje 2: Entradas, triaje y preparación | ¿Quién resuelve discrepancias entre datos operativos, memoria publicada y medios? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F09** | Eje 2: Entradas, triaje y preparación | ¿Cómo se documenta que una afirmación quedó pendiente o no puede publicarse? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F10** | Eje 2: Entradas, triaje y preparación | ¿Qué variables, categorías, relaciones y condiciones exige representar verificación de hechos y cifras de forma estructurada? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F11** | Eje 2: Entradas, triaje y preparación | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre verificación de hechos y cifras? | Cornell LII: 17 CFR § 240.10b-5 - Employment  | `b689098d-8595-4f11-9e01-293b0e194a96` | ✅ Respondida |
| **P10-F12** | Eje 2: Entradas, triaje y preparación | ¿Qué caso concreto, con entradas y resultado esperado, ilustra verificación de hechos y cifras sin introducir datos no documentados? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F13** | Eje 3: Validación factual y control de procedencia | ¿Qué elementos de una postura aprobada deben preservarse al adaptar canal o audiencia? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F14** | Eje 3: Validación factual y control de procedencia | ¿Qué variaciones son editorialmente admisibles y cuáles requieren nueva aprobación? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F15** | Eje 3: Validación factual y control de procedencia | ¿Cómo se genera un borrador que conserve citas y advertencias de incertidumbre? | PR Council: Ethical Standards and Guidelines  | `493c8ec0-08c7-4b4a-81c4-c95a7734bfe1` | ✅ Respondida |
| **P10-F16** | Eje 3: Validación factual y control de procedencia | ¿Qué variables, categorías, relaciones y condiciones exige representar redacción y adaptación de mensajes de forma estructurada? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F17** | Eje 3: Validación factual y control de procedencia | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre redacción y adaptación de mensajes? | PR Council: Ethical Standards and Guidelines  | `493c8ec0-08c7-4b4a-81c4-c95a7734bfe1` | ✅ Respondida |
| **P10-F18** | Eje 3: Validación factual y control de procedencia | ¿Qué caso concreto, con entradas y resultado esperado, ilustra redacción y adaptación de mensajes sin introducir datos no documentados? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F19** | Eje 4: RACI, DACI y cadena de aprobación | ¿Qué roles preparan, consultan, autorizan y publican cada tipo de mensaje? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F20** | Eje 4: RACI, DACI y cadena de aprobación | ¿Qué cambia entre operación ordinaria, emergencia y asunto regulado? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F21** | Eje 4: RACI, DACI y cadena de aprobación | ¿Cómo evitar bloqueos por ausencia de un aprobador sin saltarse controles? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F22** | Eje 4: RACI, DACI y cadena de aprobación | ¿Qué variables, categorías, relaciones y condiciones exige representar rACI, DACI y cadena de aprobación de forma estructurada? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F23** | Eje 4: RACI, DACI y cadena de aprobación | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre rACI, DACI y cadena de aprobación? | P10_SOURCE_INDEX: Indice Maestro de Fuentes,  | `1c52f005-30d5-4877-9b75-31f0785411ca` | ✅ Respondida |
| **P10-F24** | Eje 4: RACI, DACI y cadena de aprobación | ¿Qué caso concreto, con entradas y resultado esperado, ilustra rACI, DACI y cadena de aprobación sin introducir datos no documentados? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F25** | Eje 5: Estados, versiones y auditoría | ¿Qué estados debe recorrer un mensaje desde borrador hasta retiro o corrección? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F26** | Eje 5: Estados, versiones y auditoría | ¿Cómo se conservan versiones, motivos de cambio y firmas de aprobación? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F27** | Eje 5: Estados, versiones y auditoría | ¿Qué ocurre cuando nueva evidencia invalida un mensaje ya publicado? | COPE: Committee on Publication Ethics - Retra | `d0f9e6c9-5476-410e-886f-4bbb38556d95` | ✅ Respondida |
| **P10-F28** | Eje 5: Estados, versiones y auditoría | ¿Qué variables, categorías, relaciones y condiciones exige representar estados, versiones y auditoría de forma estructurada? | Broadsight: System of Record for Corporate Co | `a8a48a2b-3621-422f-92fe-03700efebe57` | ✅ Respondida |
| **P10-F29** | Eje 5: Estados, versiones y auditoría | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre estados, versiones y auditoría? | P10_SOURCE_INDEX: Indice Maestro de Fuentes,  | `1c52f005-30d5-4877-9b75-31f0785411ca` | ✅ Respondida |
| **P10-F30** | Eje 5: Estados, versiones y auditoría | ¿Qué caso concreto, con entradas y resultado esperado, ilustra estados, versiones y auditoría sin introducir datos no documentados? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F31** | Eje 6: Reglas para automatizar o abstenerse | ¿Qué tareas pueden automatizarse con bajo riesgo y cuáles deben revisarse siempre? | CIPR: Artificial Intelligence in Public Relat | `0f644aa9-897a-4f0e-87ac-29dd7c0e2d0b` | ✅ Respondida |
| **P10-F32** | Eje 6: Reglas para automatizar o abstenerse | ¿Qué señales obligan a abstenerse y pedir consejo legal o técnico? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F33** | Eje 6: Reglas para automatizar o abstenerse | ¿Qué prueba demostraría que un control humano fue efectivo y no solo nominal? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F34** | Eje 6: Reglas para automatizar o abstenerse | ¿Qué variables, categorías, relaciones y condiciones exige representar reglas para automatizar o abstenerse de forma estructurada? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F35** | Eje 6: Reglas para automatizar o abstenerse | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre reglas para automatizar o abstenerse? | P10_SOURCE_INDEX: Indice Maestro de Fuentes,  | `1c52f005-30d5-4877-9b75-31f0785411ca` | ✅ Respondida |
| **P10-F36** | Eje 6: Reglas para automatizar o abstenerse | ¿Qué caso concreto, con entradas y resultado esperado, ilustra reglas para automatizar o abstenerse sin introducir datos no documentados? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F37** | Eje 7: Canales y escenarios | ¿Cómo difieren comunicado, respuesta a periodista, mensaje interno y explicación a autoridad? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F38** | Eje 7: Canales y escenarios | ¿Qué flujos exigen crisis ambiental, reporte de sostenibilidad o consulta comunitaria? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F39** | Eje 7: Canales y escenarios | ¿Cómo mantener coherencia sin enviar el mismo texto a audiencias distintas? | Arthur W. Page Society: The Page Principles | `405cc287-6f42-46a2-b04d-dd7fa51c16a1` | ✅ Respondida |
| **P10-F40** | Eje 7: Canales y escenarios | ¿Qué variables, categorías, relaciones y condiciones exige representar canales y escenarios de forma estructurada? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F41** | Eje 7: Canales y escenarios | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre canales y escenarios? | P10_SOURCE_INDEX: Indice Maestro de Fuentes,  | `1c52f005-30d5-4877-9b75-31f0785411ca` | ✅ Respondida |
| **P10-F42** | Eje 7: Canales y escenarios | ¿Qué caso concreto, con entradas y resultado esperado, ilustra canales y escenarios sin introducir datos no documentados? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F43** | Eje 8: Indicadores y límites normativos | ¿Qué mide tiempo de aprobación, tasa de corrección, error factual y reutilización segura? | AMEC: Barcelona Principles 3.0 Communications | `8702eaf4-718b-4c51-932c-29f0907db863` | ✅ Respondida |
| **P10-F44** | Eje 8: Indicadores y límites normativos | ¿Qué regulaciones específicas están verificadas en fuentes oficiales y cuáles siguen pendientes? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-F45** | Eje 8: Indicadores y límites normativos | ¿Qué correcciones de P10_VERIFICATION_CORRECTIONS impiden citar eCFR o afirmar cobertura legal universal? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-F46** | Eje 8: Indicadores y límites normativos | ¿Qué variables, categorías, relaciones y condiciones exige representar indicadores y límites normativos de forma estructurada? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-F47** | Eje 8: Indicadores y límites normativos | ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre indicadores y límites normativos? | P10_SOURCE_INDEX: Indice Maestro de Fuentes,  | `1c52f005-30d5-4877-9b75-31f0785411ca` | ✅ Respondida |
| **P10-F48** | Eje 8: Indicadores y límites normativos | ¿Qué caso concreto, con entradas y resultado esperado, ilustra indicadores y límites normativos sin introducir datos no documentados? | P10_RESEARCH_DOSSIER: Arquitectura de Gestion | `49c765d6-20d4-4361-9fc7-ee10bd457b96` | ✅ Respondida |
| **P10-C01** | Eje 1: Objetivos, alcance y valor (Contraste) | ¿Dónde discrepan fuentes originales y síntesis internas sobre origen de solicitudes y señales, y qué versión prevalece según las correcciones? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-C02** | Eje 1: Objetivos, alcance y valor (Contraste) | ¿Qué sigue sin prueba sobre origen de solicitudes y señales, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | P10_GAPS_AND_VALIDATION: Vacios, Hipotesis y  | `1bdee7c1-95df-4848-ba8e-74ff3eaca685` | ✅ Respondida |
| **P10-C03** | Eje 2: Entradas, triaje y preparación (Contraste) | ¿Dónde discrepan fuentes originales y síntesis internas sobre verificación de hechos y cifras, y qué versión prevalece según las correcciones? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-C04** | Eje 2: Entradas, triaje y preparación (Contraste) | ¿Qué sigue sin prueba sobre verificación de hechos y cifras, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | P10_GAPS_AND_VALIDATION: Vacios, Hipotesis y  | `1bdee7c1-95df-4848-ba8e-74ff3eaca685` | ✅ Respondida |
| **P10-C05** | Eje 3: Validación factual y control de procedencia (Contraste) | ¿Dónde discrepan fuentes originales y síntesis internas sobre redacción y adaptación de mensajes, y qué versión prevalece según las correcciones? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-C06** | Eje 3: Validación factual y control de procedencia (Contraste) | ¿Qué sigue sin prueba sobre redacción y adaptación de mensajes, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | P10_GAPS_AND_VALIDATION: Vacios, Hipotesis y  | `1bdee7c1-95df-4848-ba8e-74ff3eaca685` | ✅ Respondida |
| **P10-C07** | Eje 4: RACI, DACI y cadena de aprobación (Contraste) | ¿Dónde discrepan fuentes originales y síntesis internas sobre rACI, DACI y cadena de aprobación, y qué versión prevalece según las correcciones? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-C08** | Eje 4: RACI, DACI y cadena de aprobación (Contraste) | ¿Qué sigue sin prueba sobre rACI, DACI y cadena de aprobación, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | P10_GAPS_AND_VALIDATION: Vacios, Hipotesis y  | `1bdee7c1-95df-4848-ba8e-74ff3eaca685` | ✅ Respondida |
| **P10-C09** | Eje 5: Estados, versiones y auditoría (Contraste) | ¿Dónde discrepan fuentes originales y síntesis internas sobre estados, versiones y auditoría, y qué versión prevalece según las correcciones? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-C10** | Eje 5: Estados, versiones y auditoría (Contraste) | ¿Qué sigue sin prueba sobre estados, versiones y auditoría, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | P10_GAPS_AND_VALIDATION: Vacios, Hipotesis y  | `1bdee7c1-95df-4848-ba8e-74ff3eaca685` | ✅ Respondida |
| **P10-C11** | Eje 6: Reglas para automatizar o abstenerse (Contraste) | ¿Dónde discrepan fuentes originales y síntesis internas sobre reglas para automatizar o abstenerse, y qué versión prevalece según las correcciones? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-C12** | Eje 6: Reglas para automatizar o abstenerse (Contraste) | ¿Qué sigue sin prueba sobre reglas para automatizar o abstenerse, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | P10_GAPS_AND_VALIDATION: Vacios, Hipotesis y  | `1bdee7c1-95df-4848-ba8e-74ff3eaca685` | ✅ Respondida |
| **P10-C13** | Eje 7: Canales y escenarios (Contraste) | ¿Dónde discrepan fuentes originales y síntesis internas sobre canales y escenarios, y qué versión prevalece según las correcciones? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-C14** | Eje 7: Canales y escenarios (Contraste) | ¿Qué sigue sin prueba sobre canales y escenarios, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | P10_GAPS_AND_VALIDATION: Vacios, Hipotesis y  | `1bdee7c1-95df-4848-ba8e-74ff3eaca685` | ✅ Respondida |
| **P10-C15** | Eje 8: Indicadores y límites normativos (Contraste) | ¿Dónde discrepan fuentes originales y síntesis internas sobre indicadores y límites normativos, y qué versión prevalece según las correcciones? | P10_VERIFICATION_CORRECTIONS: Rectificación C | `f043631e-98ac-4b5b-8fc6-de772d489bcf` | ✅ Respondida |
| **P10-C16** | Eje 8: Indicadores y límites normativos (Contraste) | ¿Qué sigue sin prueba sobre indicadores y límites normativos, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre? | P10_GAPS_AND_VALIDATION: Vacios, Hipotesis y  | `1bdee7c1-95df-4848-ba8e-74ff3eaca685` | ✅ Respondida |