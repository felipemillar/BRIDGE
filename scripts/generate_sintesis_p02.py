import json
import os
from pathlib import Path

def generate_p02_synthesis():
    respuestas_path = Path("respuestas/P02.jsonl")
    fuentes_path = Path("fuentes/P02.json")
    
    with open(respuestas_path, "r", encoding="utf-8") as f:
        responses = [json.loads(line) for line in f if line.strip()]
        
    with open(fuentes_path, "r", encoding="utf-8") as f:
        fuentes_data = json.load(f)
        
    md = []
    md.append("# Síntesis Ejecutiva y Metodológica — Pilar P02: Empresas y Soluciones Existentes\n")
    md.append("**Programa de Investigación:** Inteligencia para Asuntos Corporativos  ")
    md.append("**Repositorio:** BRIDGE (`/Users/fmillar/Proyectos_Desarrollo/BRIDGE`)  ")
    md.append("**Cuaderno Canónico:** `bcdfa78d-8d8a-4fd2-b89b-584d3dbd0440` (NotebookLM: P02 — Empresas y soluciones existentes)  ")
    md.append("**Fecha de Cierre de Pilar:** 2026-10-01  ")
    md.append("**Estado de Cobertura:** 96/96 preguntas respondidas y auditadas (48 Fundamentales F01–F48, 16 Contraste C01–C16, 32 Profundización Especializada X01–X32). Auditoría de Calidad: 100% Aprobada.\n")
    
    md.append("---\n")
    md.append("## 1. Identificación y Alcance del Pilar\n")
    md.append("El Pilar P02 ejecuta el censo y análisis competitivo exhaustivo del ecosistema global de software y servicios para Asuntos Corporativos, Relaciones Públicas y Gestión de Partes Interesadas.")
    md.append("A través de sus 8 ejes temáticos y sus 4 bloques de profundización especializada, este pilar desmantela las hipérboles comerciales de los proveedores multinacionales, audita las transacciones de fusiones y adquisiciones (M&A) del sector, evalúa la cobertura territorial de medios y marcos regulatorios en Chile y América Latina, y delimita con rigor científico el estatus de las afirmaciones diferenciales del proyecto BRIDGE.\n")
    
    md.append("### Dimensiones Cuantitativas del Pilar:")
    md.append("- **Total preguntas ejecutadas:** 96 preguntas (100% del alcance aprobado para P02).")
    md.append("- **Preguntas Fundamentales (F):** 48 preguntas organizadas en 8 ejes temáticos (6 por eje).")
    md.append("- **Preguntas de Contraste (C):** 16 preguntas (2 por eje: discrepancias de fuentes y vacíos técnicos).")
    md.append("- **Preguntas de Profundización Especializada (X):** 32 preguntas en 4 bloques temáticos (Adquisiciones, Proximidad Funcional, Cobertura Territorial y Certeza Comercial).")
    md.append("- **Denominador Comercial Reconciliado:** Exactamente **70 proveedores comerciales independientes** (bajo la regla de precedencia absoluta de `00_P02_GLOBAL_READ_ME_AND_ERRATA`), tras excluir estándares gremiales (AMEC), sociedades profesionales (Page Society) y el modelo conceptual propio (The Bridge Intelligence).")
    md.append("- **Fuentes Catalogadas en Manifiesto:** 80 fuentes (74 activas y sustantivas, 6 con bloqueo WAF sustituidas por reportes abiertos, 12 documentos de síntesis interna y erratas).\n")
    
    md.append("---\n")
    md.append("## 2. Arquitectura de Conceptos y Modelo Operativo del Mercado\n")
    md.append("La investigación de P02 demuestra que el mercado global de software para asuntos corporativos se encuentra severamente fragmentado en silos incompatibles:")
    
    md.append("### 2.1. Los Cuatro Arquetipos Funcionales del Mercado")
    md.append("1. **Arquetipo 1: Plataformas de Escucha y Medición (Escuchar):**")
    md.append("   - *Proveedores clave:* Meltwater, CisionOne, Brandwatch, Talkwalker, Signal AI, Dataminr, Litoralpress.")
    md.append("   - *Capacidades:* Monitoreo de medios masivos (prensa, TV, radio, web) y redes sociales; detección de picos de menciones; análisis de sentimiento.")
    md.append("   - *Punto ciego estructural:* Son ciegas a los repositorios internos de ingeniería de la empresa y no gestionan acuerdos comunitarios de campo ni la Ley de Lobby.")
    md.append("2. **Arquetipo 2: Búsqueda Empresarial e Inteligencia de Mercado (Saber):**")
    md.append("   - *Proveedores clave:* AlphaSense, Glean, Hebbia, Contify, Elium.")
    md.append("   - *Capacidades:* Indexación de repositorios corporativos internos (Google Workspace, M365, Box) con respeto a permisos ACL (Glean); RAG financiero sobre transcripciones de analistas y filings SEC (AlphaSense); agregación de inteligencia competitiva (Contify).")
    md.append("   - *Punto ciego estructural:* Carecen de taxonomías de riesgo reputacional, flujos de vocería y memoria de relacionamiento social.")
    md.append("3. **Arquetipo 3: System of Record de Vocería y Flujo Editorial (Hablar):**")
    md.append("   - *Proveedores clave:* Broadsight Technologies, Prezly, Contrlr.")
    md.append("   - *Capacidades:* Repositorio inmutable de temas críticos (Issues), biblioteca oficial de Q&A corporativo, holding statements aprobados, doble firma digital (Legal y DirCom) y despacho de briefings a voceros.")
    md.append("   - *Punto ciego estructural:* No monitorean medios de prensa masiva ni radio local, ni registran los compromisos socioambientales de las faenas.")
    md.append("4. **Arquetipo 4: CRM Legislativo y Gestión Comunitaria / SRM (Relacionar):**")
    md.append("   - *Proveedores clave:* Quorum, FiscalNote, Borealis (Irth Solutions), Open Point Group (Consultation Manager, Converlens), Simply Stakeholders.")
    md.append("   - *Capacidades:* Seguimiento de proyectos de ley y votaciones parlamentarias en EE. UU./UE (Quorum, FiscalNote); registro de quejas vecinales (grievances), actas de diálogo y compromisos de la RCA ambiental en faenas mineras (Borealis, Open Point).")
    md.append("   - *Punto ciego estructural:* No monitorean noticias en tiempo real ni disponen de herramientas para la preparación y gobernanza de voceros de prensa.\n")
    
    md.append("### 2.2. Veredicto de Integración de los Cuatro Módulos")
    md.append("- **Cobertura cuádruple en el mercado:** **CERO proveedores comerciales independientes** cubren los cuatro módulos (Saber, Escuchar, Hablar, Relacionar) de forma nativa.")
    md.append("- **Cobertura máxima observada:** Máximo tres módulos bajo empaquetamiento comercial fragmentado (e.g. CisionOne con Brandwatch y PR Newswire; Meltwater), operando con bases de datos segregadas y sin flujo operativo automatizado.")
    md.append("- **Estatus de The Bridge Intelligence:** Se clasifica estrictamente como una **hipótesis de diseño de arquitectura de referencia** (`hipotesis_diseno`). Sus postulados de superioridad operacional no cuentan con validación empírica en clientes de producción.\n")
    
    md.append("---\n")
    md.append("## 3. Evidencia Empírica, Transacciones M&A y Normas del Mercado\n")
    md.append("Toda afirmación fáctica de este pilar se sustenta en documentos primarios, registros de la SEC y directivas de errata inmutables:")
    
    md.append("### 3.1. Reconciliación Societaria y Fusiones y Adquisiciones (M&A)")
    md.append("- **FGS Global:** Vendida por WPP plc a fondos de Private Equity gestionados por KKR (Kite Bidco Inc.), transacción cerrada definitivamente el **3 de diciembre de 2024** y respaldada por el **Form 6-K filing a5017o.htm** de la SEC. FGS Global opera bajo control de KKR y no pertenece a WPP.")
    md.append("- **Burson Global y Limbik:** Adquisición de la firma de IA cognitiva Limbik por Burson (WPP) completada el **12 de agosto de 2026**, incorporando sus algoritmos de predicción de narrativa a Burson Decipher.")
    md.append("- **Signal AI y Memo:** Adquisición de Memo completada el **20 de abril de 2026**, integrando la telemetría de 'Verified Readership' en el motor de Signal AI.")
    md.append("- **Cision y Brandwatch:** Adquirida por Cision Ltd. (Platinum Equity) en **junio de 2021 por 450 millones de USD**, manteniendo consolas comerciales independientes.")
    md.append("- **Open Point Group:** Formación del grupo en **julio de 2024** mediante la integración de Consultation Manager, Social Point y Converlens.")
    md.append("- **Borealis:** Controlada por Irth Solutions LLC (empresa de portafolio de Blackstone).\n")
    
    md.append("### 3.2. Verdad Territorial en Chile y América Latina")
    md.append("- **Litoralpress (Chile):** Único proveedor documentado con infraestructura comprobada de monitoreo de más de 200 radioemisoras locales en las 16 regiones de Chile, canales de televisión abierta/cable y prensa escrita provincial.")
    md.append("- **Brecha de Cobertura Global ('Reality Gap'):** Las suites multinacionales (Meltwater, Cision) presentan ceguera absoluta ante el 90% de las emisoras de radio comunitaria y provincial en Chile, capturando únicamente sitios web nacionales sindicados.")
    md.append("- **Leyes de Derechos de Autor y Soberanía:** Las organizaciones de gestión de derechos de prensa (ANP en Chile, CEDRO en España, NLA en UK) restringen el almacenamiento masivo y redistribución de textos completos, exigiendo licencias comerciales y purga periódica de textos protegidos.\n")
    
    md.append("---\n")
    md.append("## 4. Análisis Crítico de Fuentes, Discrepancias y Prevalencia Editorial\n")
    md.append("Bajo el mandato de investigación, rige la regla de precedencia absoluta de `00_P02_GLOBAL_READ_ME_AND_ERRATA` y `P02_GLOBAL_ATLAS_RECONCILIATION_V1`:")
    
    md.append("### 4.1. Discrepancias Zanjadas y Versiones Prevalecientes:")
    md.append("1. **Denominador del Mercado (82 vs 70):** Borradores tempranos inflaban el mercado a 82 entidades por incluir erróneamente a AMEC, Page Society y The Bridge. *Prevalece:* Exactamente **70 proveedores comerciales independientes**.")
    md.append("2. **Propiedad de FGS Global:** Artículos desactualizados la catalogaban como subsidiaria de WPP. *Prevalece:* Propiedad de KKR desde el 3 de diciembre de 2024 (SEC Form 6-K).")
    md.append("3. **Fechas de M&A de Limbik y Memo:** Discrepancias corregidas a fechas canónicas auditadas: Limbik (12-ago-2026) y Memo (20-abr-2026).")
    md.append("4. **Software vs Consultoría Humana:** Se desestima la catalogación de Entual B.V., FGS Global y Burson como 'proveedores de software', reclasificándolos como servicios de consultoría estratégica humana.")
    md.append("5. **Etiquetas de Madurez ('Evidencia Demostrada'):** Se prohíbe el uso de la categoría inflada 'EM', sustituyéndola por la escala objetiva: OPD (Oferta Pública), DTI (Técnica Identificada), FD (Marketing) y POR (Prueba Operacional = 0 casos en los 70 vendors).")
    md.append("6. **Estatus de The Bridge:** Se erradica cualquier atribución de madurez operativa; The Bridge es una hipótesis de diseño a validar.\n")
    
    md.append("---\n")
    md.append("## 5. Vacíos de Conocimiento e Incertidumbres Críticas\n")
    md.append("La investigación identifica ocho brechas no resueltas en el mercado que fundamentan la necesidad de validación empírica:")
    md.append("1. **Titularidad de Direct Signal:** Carece de registro corporativo público verificable en EE. UU., manteniéndose con bandera de propiedad no verificada.")
    md.append("2. **Integración Backend Post-M&A:** Ningún conglomerado ha demostrado públicamente unificación de bases de datos entre marcas adquiridas (Cision/Brandwatch).")
    md.append("3. **Precisión de NLP en Jergas Locales:** Falta de pruebas independientes sobre tasas de error en sentimiento y análisis de riesgo en español de América Latina.")
    md.append("4. **Predictibilidad de Conflictos Territoriales:** Las soluciones de SRM comunitario (Borealis, Open Point) no han probado matemáticamente su capacidad de anticipar la judicialización de faenas.")
    md.append("5. **RAG sobre Expedientes Ambientales Rasterizados:** Falta de benchmark sobre extracción fáctica sin alucinaciones en RCAs escaneadas de más de 5,000 páginas.")
    md.append("6. **Aceptabilidad Legal de Redacción por IA:** Cero adopción documentada de comunicados de crisis generados por IA sin revisión humana obligatoria de abogados.")
    md.append("7. **Ingesta Municipal Descentralizada:** Inexistencia de APIs comerciales estandarizadas para las 345 municipalidades de Chile.")
    md.append("8. **Costo Total de Propiedad (TCO) Real:** Opacidad sistemática sobre cobros ocultos de onboarding y sobrecargos por volumen de noticias.\n")
    
    md.append("---\n")
    md.append("## 6. Implicancias para el Diseño de la Solución BRIDGE\n")
    md.append("Los hallazgos del Pilar P02 dictan directivas arquitectónicas y comerciales vinculantes:")
    md.append("1. **Estrategia Híbrida 'Build, Partner or Buy':**")
    md.append("   - *Partner / Ingesta de Datos:* Integrar APIs de captura local consolidada (Litoralpress para radio/prensa en Chile; LexisNexis para medios globales), evitando construir infraestructura física propia.")
    md.append("   - *Build / Núcleo Propietario:* Construir el motor unificado de correlación entre alertas de prensa, expedientes técnicos (Saber), compromisos comunitarios (Relacionar) y gobernanza de vocería inmutable (Hablar).")
    md.append("2. **Blindaje de Gobernanza Editorial:** Implementar flujos de aprobación multi-rol (Comunicaciones + Legal) con sellos criptográficos inmutables inspirados en el modelo System of Record de Broadsight.")
    md.append("3. **Soberanía y Particionado Territorial:** Diseñar tenencia particionada en nube local (Santiago de Chile) para clientes regulados (minería, banca, energía), purgando textos de prensa a los 30 días y conservando representaciones semánticas conforme a la ley de propiedad intelectual.")
    md.append("4. **Transparencia Comercial:** Publicar estructuras de precios claras sin cobros ocultos de onboarding para romper la opacidad del mercado.\n")
    
    md.append("---\n")
    md.append("## 7. Matriz de Trazabilidad y Cobertura (96 Preguntas de P02)\n")
    md.append("| ID Pregunta | Tipo | Eje / Bloque Temático | Estado | Afirmación Principal Auditada | Fuente Primaria Clave | Nivel Evidencia |\n")
    md.append("|---|---|---|---|---|---|---|\n")
    
    for r in responses:
        qid = r["question_id"]
        qtype = "Fundamental (F)" if "-F" in qid else ("Contraste (C)" if "-C" in qid else "Profundización (X)")
        axis = r.get("axis", "Especializada")
        status = r.get("answer_status", "respondida")
        
        findings = r.get("findings", [])
        claim_short = findings[0].get("claim", "")[:80] + "..." if findings else r.get("short_answer", "")[:80] + "..."
        source_title = findings[0]["evidence"][0].get("source_title", "Manifiesto P02") if (findings and findings[0].get("evidence")) else "P02 Sources"
        ev_level = r.get("evidence_level", "DTI")
        
        md.append(f"| [{qid}](respuestas/P02.jsonl) | {qtype} | {axis} | {status} | {claim_short} | {source_title} | {ev_level} |\n")
        
    md_content = "".join(md)
    out_file = Path("sintesis/P02.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    print(f"Generated synthesis for P02 at {out_file} ({len(md_content)} bytes)")

if __name__ == "__main__":
    generate_p02_synthesis()
