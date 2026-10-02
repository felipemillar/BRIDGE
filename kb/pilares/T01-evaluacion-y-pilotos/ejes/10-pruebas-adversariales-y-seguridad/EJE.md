<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 10-pruebas-adversariales-y-seguridad: Profundización especializada

**Pilar:** [T01 — Evaluación y pilotos](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### T01-X09: ¿Qué casos incluyen prompt injection, documento vencido, fuente parcial y homónimo?

> La batería de pruebas adversariales de The Bridge Intelligence (thebridgeintelligence.ai) somete al sistema a cuatro escenarios críticos de estrés epistémico y de seguridad: 1) Inyección de Prompt (Directa e Indirecta): Ataques tipo jailbreak o instrucciones maliciosas incrustadas en documentos PDF

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X09.json](T01-X09.json)
### T01-X10: ¿Qué ataque intenta obtener datos de otro cliente o un mensaje no aprobado?

> Los dos ataques adversariales más destructivos en entornos SaaS corporativos multi-cliente son: 1) Ataque de Exfiltración y Fuga Cross-Tenant: Intentos estructurados de forzar al motor RAG a recuperar pasajes, vectores o citas pertenecientes a la partición de otro cliente (ej. un usuario del Cliente

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [T01-X10.json](T01-X10.json)
### T01-X11: ¿Qué criterio de fallo detiene inmediatamente un piloto con datos reales?

> En The Bridge Intelligence rige el 'Protocolo de Detención Inmediata de Emergencia' (Hard Kill Switch), el cual cancela y aborta de forma irrevocable un piloto en producción ante la ocurrencia de cualquiera de los siguientes tres eventos de fallo crítico: 1) Fuga o Exfiltración Cross-Tenant Confirma

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [T01-X11.json](T01-X11.json)
### T01-X12: ¿Qué variables, categorías, relaciones y condiciones exige representar pruebas adversariales y seguridad de forma estructurada?

> La representación estructurada de las pruebas adversariales y la seguridad exige un modelo de datos formal compuesto por: 1) Entidad Ataque_Adversarial: ID de vector de ataque, tipología (Prompt Injection, Cross-Tenant Exfiltration, Expired Document, Homonym Confusion, Privilege Escalation), payload

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X12.json](T01-X12.json)
### T01-X13: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre pruebas adversariales y seguridad?

> El marco de pruebas adversariales, guardrails y seguridad se sustenta en fuentes de texto completo y leyes oficiales verificadas en T01: 1) Inan et al. (Llama Guard, 2023-12-07, ArXiv d19f3dcf, p. 2-6): Respalda la clasificación de riesgos de seguridad, detección de prompt injection y auditoría de e

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X13.json](T01-X13.json)
### T01-X14: ¿Qué caso concreto, con entradas y resultado esperado, ilustra pruebas adversariales y seguridad sin introducir datos no documentados?

> Caso Concreto de Pentest Adversarial CPA-T01-280 (Ataque de Inyección Indirecta en Nota de Prensa y Tentativa de Fuga Cross-Tenant): 1) Entradas: Ingesta de un artículo de prensa externo aparentemente legítimo que contiene un ataque de prompt injection indirecto oculto en texto invisible de color bl

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X14.json](T01-X14.json)
### T01-X15: ¿Dónde discrepan fuentes originales y síntesis internas sobre pruebas adversariales y seguridad, y qué versión prevalece según las correcciones?

> Discrepancia y prevalencia en pruebas adversariales y seguridad: 1) Discrepancia: Las notas iniciales asumían que la seguridad del sistema quedaba suficientemente garantizada con las cláusulas contractuales de privacidad del proveedor del LLM (OpenAI/Microsoft) y que las pruebas adversariales eran o

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [T01-X15.json](T01-X15.json)
### T01-X16: ¿Qué sigue sin prueba sobre pruebas adversariales y seguridad, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba empírica formal la resistencia de The Bridge Intelligence ante ataques de envenenamiento de datos a largo plazo (Data Poisoning por goteo) en repositorios documentales colaborativos: 1) Vacío Identificado: Si un infiltrado o empleado descontento dentro de la empresa cliente sube gra

- **Verificación:** no_verificada: 1
- **Registro:** [T01-X16.json](T01-X16.json)

