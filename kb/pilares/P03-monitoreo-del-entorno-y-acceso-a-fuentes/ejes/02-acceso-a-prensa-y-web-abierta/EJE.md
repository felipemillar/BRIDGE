<!-- GENERADO por herramientas/generar_vistas.py: no editar a mano -->
# Eje 02-acceso-a-prensa-y-web-abierta: Acceso a prensa y web abierta

**Pilar:** [P03 — Monitoreo del entorno y acceso a fuentes](../../TARJETA.md)  
**Módulo:** Escuchar

---

## Preguntas del Eje (8)

### P03-C03: ¿Dónde discrepan fuentes originales y síntesis internas sobre acceso a prensa y web abierta, y qué versión prevalece según las correcciones?

> La discrepancia principal radicaba en la interpretación del precedente judicial estadounidense hiQ Labs v. LinkedIn Corp.: las síntesis preliminares sugerían que el fallo garantizaba un 'derecho amplio y seguro de scraping sobre cualquier dato público en la web'. Prevalece de forma categórica la rec

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C03.json](P03-C03.json)
### P03-C04: ¿Qué sigue sin prueba sobre acceso a prensa y web abierta, qué fuente falló o es parcial, y qué validación mínima resolvería la incertidumbre?

> Sigue sin prueba la exhaustividad de la cobertura en tiempo real de medios hiperlocales e impresos de regiones chilenas que carecen de RSS o streaming continuo: 1) Brecha: Se desconoce el porcentaje exacto de noticias comunales que se pierden por no estar digitalizadas formalmente; 2) Fuente fallida

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-C04.json](P03-C04.json)
### P03-F07: ¿Qué canales de acceso a prensa digital están documentados y qué restricciones muestran?

> Están documentados 5 canales de acceso a prensa digital con restricciones técnicas y legales contrastadas: 1) Agregadores masivos abiertos (GDELT 2.0 y Event Registry): cobertura multilingüe en intervalos de 15 minutos, pero restringidos a texto público sin paywalls y con normalización léxica hetero

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F07.json](P03-F07.json)
### P03-F08: ¿Cómo cambian calidad, latencia, cobertura y derechos entre API, licencia, RSS, búsqueda y captura manual?

> El rendimiento varía drásticamente según el vector técnico: 1) Calidad de metadatos: Las licencias sindicadas (Factiva) y APIs estructuradas (Event Registry) entregan la mayor calidad con autor, fecha precisa y categorización temática; los RSS ofrecen calidad media y la captura manual es propensa a

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F08.json](P03-F08.json)
### P03-F09: ¿Qué evidencia específica hay de cobertura de medios locales chilenos?

> La evidencia empírica demuestra una asimetría estructural severa: 1) Ceguera de suites globales: Ni Meltwater, ni Cision, ni Factiva garantizan cobertura sistemática de diarios electrónicos comunales, radios regionales ni periódicos impresos de provincias en Chile (como El Rancagüino, El Día de La S

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F09.json](P03-F09.json)
### P03-F10: ¿Qué variables, categorías, relaciones y condiciones exige representar acceso a prensa y web abierta de forma estructurada?

> La representación estructurada del acceso a prensa exige: 1) Variables técnicas: `canal_acceso` (api, rss, scraping, sindicacion), `latencia_ingesta_segundos`, `estado_paywall` (abierto, medido, duro), `restringido_por_robots_txt` (booleano), `opt_out_tdm` (booleano según Art 4 Directiva UE), y `has

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F10.json](P03-F10.json)
### P03-F11: ¿Qué fuentes originales, pasajes, fechas y ámbitos respaldan cada hecho sobre acceso a prensa y web abierta?

> Los respaldos documentales comprenden: 1) Estructura y agrupamiento de noticias: Event Registry Developer Documentation (2026, sección 'Events and Clustering'), que detalla la unión de artículos por identificador semántico común; 2) Latencia y alcance multilingüe: GDELT 2.0 Documentation (2015-2026)

- **Verificación:** no_verificada: 1
- **Registro:** [P03-F11.json](P03-F11.json)
### P03-F12: ¿Qué caso concreto, con entradas y resultado esperado, ilustra acceso a prensa y web abierta sin introducir datos no documentados?

> Caso: Ingesta y agrupamiento de noticias sobre un conflicto laboral en una planta industrial en la Región del Biobío. Entradas: 1) Feed RSS de Diario Concepción con titular y entradilla anunciando huelga legal de sindicato (latencia 3 min tras emisión); 2) Artículo publicado en Emol (Santiago) anali

- **Verificación:** solo_sintesis_interna: 1
- **Registro:** [P03-F12.json](P03-F12.json)

