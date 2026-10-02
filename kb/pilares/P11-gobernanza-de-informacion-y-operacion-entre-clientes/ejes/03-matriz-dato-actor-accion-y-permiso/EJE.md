<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 03-matriz-dato-actor-accion-y-permiso: Matriz dato, actor, acción y permiso

**Pilar:** [P11 — Gobernanza de información y operación entre clientes](../../TARJETA.md)  
**Módulo:** transversal

---

## Preguntas del Eje (8)

### P11-C05: ¿Dónde discrepan fuentes originales y síntesis internas sobre matriz dato, actor, acción y permiso, y qué versión prevalece según las correcciones?

> La discrepancia esencial en la matriz de acceso se centra en el dinamismo y desacoplamiento de la autorización: el dossier inicial (`P11_RESEARCH_DOSSIER`) planteaba una matriz RBAC (Role-Based Access Control) estática vinculada a perfiles fijos (ej. Director, Analista, Operador) evaluados una sola

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C05.json](P11-C05.json)
### P11-C06: ¿Qué sigue sin prueba sobre matriz dato, actor, acción y permiso, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> En la matriz de acceso y permisos: 1) Lo que sigue sin prueba empírica: El impacto en la latencia de usuario final y la escalabilidad del sistema cuando el Policy Enforcement Point (PEP) debe evaluar recursivamente atributos ABAC sobre cientos de chunks candidatos recuperados en paralelo en una sola

- **Verificación:** no_verificada: 1
- **Registro:** [P11-C06.json](P11-C06.json)
### P11-F13: ¿Qué combinación de rol, propósito y clasificación autoriza cada acción?

> La autorización en BRIDGE no depende únicamente de roles estáticos, sino de una matriz ABAC (Attribute-Based Access Control, según NIST SP 800-162) que evalúa cuatro dimensiones interdependientes: 1) Clasificación del Activo: D1 (Público), D2 (Interno), D3 (Confidencial Estratégico), D4 (Datos Perso

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F13.json](P11-F13.json)
### P11-F14: ¿Cómo se heredan, revocan y comprueban permisos del origen al resultado?

> La propagación y revocación de permisos a lo largo del ciclo de inferencia y transformación documental se gobierna mediante tres principios arquitectónicos: 1) Principio de Herencia de Máxima Restricción (High Water Mark Principle): Todo documento, fragmento vectorial, resumen sintetizado o respuest

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F14.json](P11-F14.json)
### P11-F15: ¿Qué bitácora permite responder quién accedió a qué y por qué?

> La trazabilidad y rendición de cuentas en BRIDGE se sustenta en un Registro de Auditoría Inmutable (Immutable Audit Ledger) estructurado bajo las directrices del NIST SP 800-92 y la Ley 21.663 (Art. 9): 1) Modelo de Registro Append-Only: Almacenado en tablas de base de datos protegidas con reglas WO

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F15.json](P11-F15.json)
### P11-F16: ¿Qué variables, categorías, relaciones y condiciones exige representar matriz dato, actor, acción y permiso de forma estructurada?

> El modelamiento estructurado de la matriz de autorización y bitácora exige formalizar: 1) Entidad AccessPolicyRule (rule_id, subject_role: [A1_ADMIN, A2_CORP_INTERNAL, A3_CONSULTANT, A4_C_LEVEL, A5_AUDITOR], object_classification: [D1, D2, D3, D4, D5], action: [CREATE, READ, UPDATE, DELETE, EXPORT,

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F16.json](P11-F16.json)
### P11-F17: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre matriz dato, actor, acción y permiso?

> Los preceptos y mecanismos de autorización multidimensional, trazabilidad y bitácoras inmutables se sustentan en fuentes normativas y estándares primarios verificados: 1) Estándares Federales de Control de Acceso y Gestión de Logs: NIST SP 800-162 (2014) 'Guide to Attribute Based Access Control (ABA

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F17.json](P11-F17.json)
### P11-F18: ¿Qué caso concreto, con entradas y resultado esperado, ilustra matriz dato, actor, acción y permiso sin introducir datos no documentados?

> Caso Concreto: Intento de Acceso No Autorizado y Bloqueo de Descarga de Minuta Confidencial de M&A por Consultor Externo de Agencia de Medios (Faena Centinela). Entradas: 1) Activo documental: 'Borrador Estratégico de Valoración y Litigios de Faena Centinela' clasificado como D3 Confidencial Estraté

- **Verificación:** no_verificada: 1
- **Registro:** [P11-F18.json](P11-F18.json)

