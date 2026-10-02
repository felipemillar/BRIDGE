"""Módulo de resolución y normalización de entidades del grafo de conocimiento BRIDGE.

Mapea las entidades heredadas hacia los 11 tipos canónicos del mandato:
  organizacion, persona_rol, documento, fuente, tema, evento,
  compromiso, producto, riesgo, metrica, experimento.

Prefijos de ID:
  org, rol, doc, fte, tema, evt, comp, prod, riesgo, met, exp.

Genera de forma determinista:
  - kb/grafo/entidades.jsonl
  - kb/grafo/mapa_ids.jsonl
"""
import argparse
import collections
import json
import logging
import re
import subprocess
import sys
from pathlib import Path

_RAIZ = Path(__file__).resolve().parent.parent
if str(_RAIZ) not in sys.path:
    sys.path.insert(0, str(_RAIZ))

try:
    from herramientas.kb import PILARES, raiz
except ModuleNotFoundError:
    from kb import PILARES, raiz

logger = logging.getLogger("resolver_entidades")

TIPOS_CANONICOS = {
    "organizacion",
    "persona_rol",
    "documento",
    "fuente",
    "tema",
    "evento",
    "compromiso",
    "producto",
    "riesgo",
    "metrica",
    "experimento",
}

# Mapeo explícito y verificado para P01 (64 IDs legados)
# Formato: id_legado -> (accion, id_nuevo, tipo, canonical_name, aliases, motivo)
P01_MAP = {
    "ENT_ACCION_EMPRESAS": (
        "conservado", "org:accion-empresas", "organizacion",
        "Acción Empresas Chile", ["Acción Empresas", "Red de Empresas Sostenibles"], None
    ),
    "ENT_BCN": (
        "conservado", "org:bcn", "organizacion",
        "Biblioteca del Congreso Nacional de Chile", ["BCN", "Biblioteca del Congreso"], None
    ),
    "ENT_CADEM": (
        "conservado", "org:cadem", "organizacion",
        "Cadem Chile", ["Cadem", "Plaza Pública Cadem"], None
    ),
    "ENT_CADENA_CAUSAL_ASIMETRIA": (
        "conservado", "riesgo:cadena-causal-asimetria", "riesgo",
        "Cadena Causal de Falla de Inteligencia",
        ["Falla de Inteligencia por Asimetría", "Cadena Causal de Asimetría"], None
    ),
    "ENT_CASO_COMPARATIVO_HIDRICO": (
        "conservado", "exp:caso-comparativo-hidrico", "experimento",
        "Caso Comparativo de Contingencia Hídrica Flujo A vs B",
        ["Contingencia Hídrica Flujo A vs B"], None
    ),
    "ENT_CASO_LOBBY_MINERIA": (
        "conservado", "exp:caso-lobby-mineria", "experimento",
        "Caso Práctico: Contingencia Hídrica y Audiencia de Lobby",
        ["Contingencia Hídrica y Audiencia de Lobby"], None
    ),
    "ENT_CASO_MINERO_NORTE": (
        "conservado", "exp:caso-minero-norte", "experimento",
        "Caso de Diálogo Territorial y Permisos Ambientales en Minería",
        ["Diálogo Territorial y Permisos Ambientales en Minería"], None
    ),
    "ENT_CASO_REGIONAL_HIBRIDO": (
        "conservado", "exp:caso-regional-hibrido", "experimento",
        "Caso Regional de Contingencia Hídrica y Audiencia Ministerial",
        ["Caso Práctico P01-F42", "Contingencia Hídrica y Audiencia Ministerial"], None
    ),
    "ENT_CASO_ROI_MINERO": (
        "conservado", "exp:caso-roi-minero", "experimento",
        "Caso Práctico de Retorno de Valor en Sector Minero",
        ["Retorno de Valor en Sector Minero", "Caso ROI Minero"], None
    ),
    "ENT_CCO": (
        "conservado", "rol:cco", "persona_rol",
        "Chief Communications Officer (CCO / Dircom)",
        ["Dircom", "Director de Asuntos Corporativos", "Chief Communications Officer"], None
    ),
    "ENT_CCO_INTEGRADOR": (
        "fusionado", "rol:cco", "persona_rol", None,
        ["CCO as Integrator (Arthur W. Page Society)", "Articulador de Silos del C-Suite"],
        "variante_rol_cco_integrador"
    ),
    "ENT_CISO": (
        "conservado", "rol:ciso", "persona_rol",
        "Chief Information Security Officer (CISO)",
        ["CISO", "Gerente de Ciberseguridad"], None
    ),
    "ENT_CMF": (
        "conservado", "org:cmf", "organizacion",
        "Comisión para el Mercado Financiero",
        ["CMF", "Superintendencia de Valores y Seguros"], None
    ),
    "ENT_CMF_NCG461": (
        "conservado", "doc:cmf-ncg-461", "documento",
        "NCG N° 461 de la Comisión para el Mercado Financiero",
        ["NCG 461", "Norma de Carácter General N° 461"], None
    ),
    "ENT_CONDICIONES_CONTENCION": (
        "conservado", "tema:condiciones-contencion", "tema",
        "Condiciones de Contención e Inteligencia Estructurada",
        ["Inteligencia Estructurada en Crisis", "Contención Decisional"], None
    ),
    "ENT_CORPUS_P01": (
        "conservado", "doc:corpus-p01", "documento",
        "Corpus P01: Asuntos Corporativos y sus Usuarios",
        ["Corpus P01"], None
    ),
    "ENT_DEONTOLOGIA_PRSA": (
        "conservado", "doc:codigo-etica-prsa", "documento",
        "Código de Ética y Salvaguarda de Confidencias PRSA",
        ["PRSA Code of Ethics", "Código Deontológico PRSA"], None
    ),
    "ENT_DIRCOM": (
        "fusionado", "org:dircom-espana", "organizacion", None,
        ["Asociación de Directivos de Comunicación (Dircom)"],
        "variante_denominacion_asociacion_dircom"
    ),
    "ENT_DIRCOM_ECE2025": (
        "conservado", "doc:dircom-ece-2025", "documento",
        "El Estado de la Comunicación en España 2025",
        ["ECE 2025", "Estado Comunicación España 2025"], None
    ),
    "ENT_DIRCOM_ESP": (
        "conservado", "org:dircom-espana", "organizacion",
        "Asociación de Directivos de Comunicación (Dircom España)",
        ["Dircom España", "Asociación Dircom"], None
    ),
    "ENT_DOSSIER_P01": (
        "conservado", "doc:dossier-p01", "documento",
        "P01_RESEARCH_DOSSIER",
        ["Dossier de Investigación P01"], None
    ),
    "ENT_ECM": (
        "conservado", "doc:european-communication-monitor-2023", "documento",
        "European Communication Monitor 2023",
        ["ECM 2023"], None
    ),
    "ENT_EDELMAN_TRUST": (
        "conservado", "doc:edelman-trust-barometer", "documento",
        "Edelman Trust Barometer 2025/2026",
        ["Edelman Trust Barometer"], None
    ),
    "ENT_ESCENARIOS_FRICCION": (
        "conservado", "tema:escenarios-friccion", "tema",
        "Escenarios de Reunión y Fricción Decisional",
        ["Fricción Decisional B2B"], None
    ),
    "ENT_ESTADIOS_MADUREZ": (
        "conservado", "tema:estadios-madurez-commtech", "tema",
        "Estadios de Madurez Digital CommTech",
        ["Madurez Artesanal, Estratégica y Agéntica"], None
    ),
    "ENT_ESTUDIO_USUARIOS_CHILE": (
        "conservado", "doc:estudio-usuarios-chile", "documento",
        "Estudio Empírico de Usuarios de Asuntos Corporativos en Chile",
        ["Validación de Campo Fase 1 y 2"], None
    ),
    "ENT_EUPRERA_LCM": (
        "conservado", "doc:euprera-latin-american-communication-monitor", "documento",
        "EUPRERA Latin American Communication Monitor",
        ["Latin American Communication Monitor", "LCM EUPRERA"], None
    ),
    "ENT_FISCAL_LEGAL": (
        "conservado", "rol:fiscal-legal", "persona_rol",
        "Fiscal Legal / Gerente de Compliance",
        ["Fiscal Legal", "Gerente de Compliance", "Compliance Officer"], None
    ),
    "ENT_FUENTES_FALLIDAS_P01": (
        "eliminado", None, None, None, [], "registro_interno_auditoria"
    ),
    "ENT_GCF": (
        "conservado", "doc:global-capability-framework", "documento",
        "Global Capability Framework",
        ["GCF", "Marco Global de Capacidades"], None
    ),
    "ENT_GLOBAL_ALLIANCE": (
        "conservado", "org:global-alliance", "organizacion",
        "Global Alliance for Public Relations and Communication Management",
        ["Global Alliance"], None
    ),
    "ENT_INFOLOBBY": (
        "conservado", "prod:infolobby", "producto",
        "Plataforma InfoLobby Chile",
        ["InfoLobby", "Plataforma de Lobby BCN"], None
    ),
    "ENT_JTBD_CRISIS": (
        "conservado", "tema:jtbd-minuta-crisis", "tema",
        "Preparación de Minuta de Crisis",
        ["Briefing Book Urgente", "JTBD Minuta de Crisis"], None
    ),
    "ENT_JTBD_DIMENSIONS": (
        "conservado", "tema:jtbd-dimensiones", "tema",
        "Dimensiones de Jobs-to-be-Done en Asuntos Corporativos",
        ["Jobs to be Done Asuntos Corporativos"], None
    ),
    "ENT_JTBD_F1": (
        "conservado", "tema:jtbd-briefing-ejecutivo", "tema",
        "JTBD-F1: Compilación de Briefing Ejecutivo",
        ["Compilación de Briefing Ejecutivo"], None
    ),
    "ENT_LEGAL_COMPLIANCE": (
        "fusionado", "rol:fiscal-legal", "persona_rol", None,
        ["Fiscal Legal / Compliance Officer"],
        "variante_rol_fiscal_legal_compliance"
    ),
    "ENT_LEY_LOBBY": (
        "conservado", "doc:ley-20730", "documento",
        "Ley N° 20.730 que Regula el Lobby",
        ["Ley del Lobby", "Ley 20730", "Ley 20.730"], None
    ),
    "ENT_MATRIZ_FUENTES_REGIONALES": (
        "conservado", "doc:matriz-fuentes-regionales-p01", "documento",
        "Matriz de Fuentes y Respaldos Regionales P01",
        ["Evidencia de Usuarios en Chile y LatAm"], None
    ),
    "ENT_MATRIZ_OBJECIONES_CISO": (
        "conservado", "doc:matriz-objeciones-ciso", "documento",
        "Matriz de Objeciones Técnicas de CISOs en LatAm",
        ["Parámetros de Homologación B2B"], None
    ),
    "ENT_MCKINSEY": (
        "conservado", "org:mckinsey", "organizacion",
        "McKinsey & Company",
        ["McKinsey"], None
    ),
    "ENT_MERCO": (
        "conservado", "org:merco-chile", "organizacion",
        "Merco Chile",
        ["Merco", "Monitor Empresarial de Reputación Corporativa"], None
    ),
    "ENT_MODELO_RETORNO_VALOR": (
        "conservado", "tema:modelo-retorno-valor", "tema",
        "Modelo de Retorno de Valor en Asuntos Corporativos",
        ["Intangible Asset Valuation & Efficiency"], None
    ),
    "ENT_MODELO_VALOR_P01": (
        "conservado", "tema:modelo-valor-asuntos-corporativos", "tema",
        "Modelo Multidimensional de Valor en Asuntos Corporativos",
        ["Modelo de Valor P01"], None
    ),
    "ENT_P01_BRIDGE": (
        "conservado", "prod:bridge-intelligence", "producto",
        "The Bridge Intelligence",
        ["BRIDGE Intelligence", "The Bridge Platform"], None
    ),
    "ENT_P01_CORP": (
        "conservado", "org:corporacion-emisora-cmf", "organizacion",
        "Corporación Emisora CMF",
        ["Emisor de Valores CMF", "Empresa Regulada CMF"], None
    ),
    "ENT_P01_REG": (
        "conservado", "org:reguladores-sectoriales-chile", "organizacion",
        "CMF / SERNAC / SMA",
        ["Reguladores Sectoriales Chile", "Entidades Reguladoras"], None
    ),
    "ENT_PAGE_SOCIETY": (
        "conservado", "org:arthur-w-page-society", "organizacion",
        "Arthur W. Page Society",
        ["Page Society"], None
    ),
    "ENT_PANEL_TRIPARTITO": (
        "conservado", "rol:panel-evaluador-tripartito", "persona_rol",
        "Panel Evaluador Tripartito (CCO, CISO, Fiscal Legal)",
        ["Comité de Adopción Tecnológica", "Panel Tripartito"], None
    ),
    "ENT_PARADOJA_LOBBY": (
        "conservado", "tema:paradoja-legitimidad-lobby", "tema",
        "Paradoja de Legitimidad en Ley de Lobby",
        ["Cumplimiento Legal vs Reputación"], None
    ),
    "ENT_PLAN_3_FASES": (
        "conservado", "exp:plan-validacion-tres-fases", "experimento",
        "Plan de Validación Empírica en Tres Fases (12 Semanas)",
        ["Roadmap de Validación de Campo BRIDGE"], None
    ),
    "ENT_POC_MINERA_IPSA": (
        "conservado", "exp:poc-minera-ipsa", "experimento",
        "Prueba de Concepto en Corporación Minero-Energética IPSA",
        ["PoC de Validación P01-F48"], None
    ),
    "ENT_POC_TRIPARTITA": (
        "conservado", "exp:poc-trilateral-fase-3", "experimento",
        "Prueba de Concepto Trilateral (Fase 3)",
        ["Validación de Retorno B2B y Arquitectura"], None
    ),
    "ENT_PROTOCOLO_VALIDACION": (
        "conservado", "doc:protocolo-validacion-tres-fases", "documento",
        "Protocolo de Validación Empírica en 3 Fases",
        ["Gaps & Validation Plan"], None
    ),
    "ENT_PRSA_ESA22": (
        "conservado", "doc:prsa-ethical-standards-advisory-22", "documento",
        "PRSA Ethical Standards Advisory #22",
        ["PRSA ESA #22", "ESA 22"], None
    ),
    "ENT_RCA": (
        "conservado", "doc:resolucion-calificacion-ambiental", "documento",
        "Resolución de Calificación Ambiental (RCA)",
        ["RCA", "Resolución Ambiental"], None
    ),
    "ENT_RIESGO_PREPARACION": (
        "conservado", "riesgo:preparacion-insuficiente", "riesgo",
        "Riesgo de Preparación Insuficiente",
        ["Patología de Cocina Artesanal"], None
    ),
    "ENT_SHADOWING_CRISIS": (
        "conservado", "exp:shadowing-preparacion-crisis", "experimento",
        "Shadowing de Preparación de Crisis",
        ["Observación Cronometrada en Tiempo Real"], None
    ),
    "ENT_STAGE_GATES_P01": (
        "conservado", "comp:stage-gates-validacion-b2b", "compromiso",
        "Stage Gates de Validación B2B P01",
        ["Compuertas de Salida de Validación"], None
    ),
    "ENT_SUBSECRETARIA": (
        "conservado", "org:subsecretaria-de-estado", "organizacion",
        "Subsecretaría de Estado",
        ["Subsecretaría Ministerial"], None
    ),
    "ENT_TRIADA_B2B": (
        "conservado", "tema:triada-b2b-decision", "tema",
        "Tríada B2B (Usuario - Comprador - Aprobador)",
        ["Matriz de Decisión Tecnológica B2B", "Ecosistema B2B de Decisión"], None
    ),
    "ENT_TRIADA_CONTROL": (
        "conservado", "tema:triada-control-cco-legal-ops", "tema",
        "Tríada CCO - Legal - Operaciones",
        ["Tríada de Control Operativo"], None
    ),
    "ENT_USUARIO_CHILENO": (
        "conservado", "rol:usuario-asuntos-corporativos-chile", "persona_rol",
        "Usuario de Asuntos Corporativos en Chile",
        ["Dircom Regulado en Chile"], None
    ),
    "ENT_VECTORES_CRITICIDAD": (
        "conservado", "tema:cuatro-vectores-criticidad", "tema",
        "Cuatro Vectores de Criticidad",
        ["Vectores de Criticidad Decisional"], None
    ),
    "ENT_VETO_VINCULANTE_CISO": (
        "conservado", "comp:veto-vinculante-ciso-legal", "compromiso",
        "Veto Vinculante de CISO y Fiscal Legal",
        ["Poder de Bloqueo B2B"], None
    ),
}

# Mapeo explícito y verificado para P02 (114 IDs legados)
P02_MAP = {
    # Casos de prueba -> eliminados
    "CASO_CONTINGENCIA_RCA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "CASO_CONTINGENCIA_CALAMA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "CASO_ASUNTOS_PUB_ANTOFAGASTA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "TEST_CASE_DEDUPLICACION": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_APAGON": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_ARQUITECTURA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_COMPLIANCE_OPA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_FRICCION_SILOS": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_HIDRICO": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_HUASCO": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_LICITACION_SANITARIA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_SOBERANIA_ANTOFAGASTA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),

    # Esquemas internos y modelos de datos -> eliminados
    "ENT_MODELO_CERTEZA_COMERCIAL": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_MODELO_DERECHOS": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_MODELO_GRUPOS": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_MODELO_HABLAR": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_MODELO_POSICIONAMIENTO": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_MODELO_PROXIMIDAD": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_MODELO_REGIONAL": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_MODELO_SABER": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ONT_ASUNTOS_PUBLICOS": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "SCH_ATLAS_EMPRESAS": ("eliminado", None, None, None, [], "esquema_datos_interno"),

    # Vacíos y patologías operativas -> eliminados
    "GAP_KNOWLEDGE_SENSING": ("eliminado", None, None, None, [], "vacio_estructural_metodologico"),
    "SILOS_CORPORATIVOS": ("eliminado", None, None, None, [], "patologia_operativa_interna"),
    "MATRIZ_TRAZABILIDAD_P02": ("eliminado", None, None, None, [], "registro_interno_auditoria"),
    "TRAZABILIDAD_COMPETIDORES": ("eliminado", None, None, None, [], "registro_interno_auditoria"),

    # Fusiones con entidades previas o de P02
    "ENT_INFOLOBBY_CHILE": ("fusionado", "prod:infolobby", "producto", None, ["Plataforma Ley de Lobby Chile"], "variante_denominacion_infolobby"),
    "ENT_THE_BRIDGE": ("fusionado", "prod:bridge-intelligence", "producto", None, ["The Bridge Intelligence Model"], "variante_modelo_bridge"),
    "ENT_THE_BRIDGE_DESIGN": ("fusionado", "prod:bridge-intelligence", "producto", None, ["The Bridge Reference Design"], "variante_diseno_bridge"),
    "ENT_KKR_KITE": ("fusionado", "org:kkr", "organizacion", None, ["Kite Bidco Inc. (KKR Funds)"], "subsidiaria_fondo_kkr"),
    "GRP_KKR_FGS": ("fusionado", "org:kkr", "organizacion", None, ["Kite Bidco Inc. (KKR)"], "holding_corporativo_kkr"),
    "GRP_WPP_BURSON": ("fusionado", "org:wpp", "organizacion", None, ["WPP plc / Burson Global"], "holding_corporativo_wpp"),

    # Arquetipos de mercado
    "ARQ_PROV_COMERCIAL": ("conservado", "tema:arquetipo-proveedor-comercial-global", "tema", "Arquetipo Proveedor Comercial Global", ["Proveedor Comercial Global"], None),
    "ARQ_ASOCIACION": ("conservado", "tema:arquetipo-asociacion-gremial", "tema", "Arquetipo Asociación Gremial", ["Asociación Gremial"], None),
    "ARQ_ESTANDAR": ("conservado", "tema:arquetipo-estandar-industria", "tema", "Arquetipo Estándar de la Industria", ["Estándar de la Industria"], None),
    "ARQ_CONSULTORA": ("conservado", "tema:arquetipo-consultora-estrategica", "tema", "Arquetipo Consultora Estratégica", ["Consultora Estratégica"], None),
    "ARQ_REFERENCIA": ("conservado", "tema:arquetipo-diseno-referencia", "tema", "Arquetipo Diseño de Referencia", ["Diseño de Referencia"], None),

    # Entidades conservadas
    "ENT_ALIANZAS_DATOS": ("conservado", "tema:alianzas-datos-conectores", "tema", "Alianzas Estratégicas de Datos y Conectores", ["Alianzas Datos"], None),
    "ENT_ALPHASENSE": ("conservado", "org:alphasense", "organizacion", "AlphaSense Inc.", ["AlphaSense"], None),
    "ENT_ALPHASENSE_REPORT": ("conservado", "doc:alphasense-forrester-wave", "documento", "Forrester Wave Market and Competitive Intelligence", ["Forrester Wave CI/MI"], None),
    "ENT_AMEC": ("conservado", "org:amec", "organizacion", "International Association for Measurement and Evaluation of Communication", ["AMEC"], None),
    "ENT_ATLAS_RECONCILIACION_DOC": ("conservado", "doc:atlas-reconciliacion-v1", "documento", "Global Atlas Reconciliation V1", ["Atlas Reconciliación V1"], None),
    "ENT_ATLAS_RECONCILIADO": ("conservado", "doc:atlas-reconciliado-p02", "documento", "P02_GLOBAL_ATLAS_RECONCILIATION_V1", ["Atlas Reconciliado P02"], None),
    "ENT_AUDITORIA_INTEGRACION_POST_M&A": ("conservado", "exp:auditoria-integracion-post-ma", "experimento", "Auditoría de Integración Técnica Post-Adquisición", ["Auditoría M&A Vendors"], None),
    "ENT_BENCHMARK_4_ARQUETIPOS": ("conservado", "exp:benchmark-cuatro-arquetipos", "experimento", "Benchmark 4 Arquetipos de Corporate Affairs", ["Benchmark 4 Arquetipos"], None),
    "ENT_BENCHMARK_RAG_RCA": ("conservado", "exp:benchmark-rag-rca", "experimento", "Benchmark RAG Expedientes Ambientales RCA", ["Benchmark RAG RCA"], None),
    "ENT_BENCHMARK_SENTIMIENTO": ("conservado", "exp:benchmark-sentimiento-regional", "experimento", "Benchmark Independiente de Sentimiento Regional", ["Benchmark Sentimiento"], None),
    "ENT_BOREALIS": ("conservado", "org:borealis-irth", "organizacion", "Borealis / Irth Solutions", ["Borealis Software", "Irth Solutions"], None),
    "ENT_BRECHA_COBERTURA": ("conservado", "tema:brecha-cobertura-global-local", "tema", "Brecha de Cobertura Global vs Local", ["Cobertura Global vs Local"], None),
    "ENT_BRECHA_INTEROP": ("conservado", "tema:brecha-interoperabilidad-multi-modulo", "tema", "Brecha de Interoperabilidad Multi-Módulo", ["Interoperabilidad Multi-Módulo"], None),
    "ENT_BROADSIGHT": ("conservado", "org:broadsight", "organizacion", "Broadsight / Broadsight AI", ["Broadsight AI"], None),
    "ENT_BROADSIGHT_CASES": ("conservado", "doc:broadsight-customer-cases", "documento", "Broadsight Enterprise Customer Cases", ["Casos Broadsight"], None),
    "ENT_BROADSIGHT_SAAS": ("conservado", "prod:broadsight-software", "producto", "Broadsight Software", ["Broadsight SaaS"], None),
    "ENT_BROADSIGHT_SOURCE": ("conservado", "doc:broadsight-system-of-record", "documento", "Broadsight System of Record Documentation", ["Broadsight System of Record"], None),
    "ENT_BURSON": ("conservado", "org:burson", "organizacion", "Burson Global", ["Burson"], None),
    "ENT_CATALOGO_CANONICO_70": ("conservado", "doc:catalogo-canonico-70-vendors", "documento", "Catálogo Maestro Canónico 70 Vendors P02", ["Catálogo 70 Vendors"], None),
    "ENT_CONTIFY": ("conservado", "org:contify", "organizacion", "Contify", ["Contify Market Intelligence"], None),
    "ENT_DATAEQ": ("conservado", "org:dataeq", "organizacion", "DataEQ", ["DataEQ Listening"], None),
    "ENT_DDI_CHILE": ("conservado", "org:ddi-chile", "organizacion", "Departamento de Derechos Intelectuales de Chile", ["DDI Chile"], None),
    "ENT_DEEP_DIVES_V1": ("conservado", "doc:global-competitor-deep-dives-v1", "documento", "Global Competitor Deep Dives V1", ["Deep Dives V1"], None),
    "ENT_DIRECT_SIGNAL": ("conservado", "org:direct-signal", "organizacion", "Direct Signal", ["Direct Signal Listening"], None),
    "ENT_ECOSISTEMA_CHILE": ("conservado", "tema:ecosistema-tecnologico-medios-chile", "tema", "Ecosistema Tecnológico de Medios Chile", ["Ecosistema Medios Chile"], None),
    "ENT_ENTUAL": ("conservado", "org:entual", "organizacion", "Entual B.V.", ["Entual Intelligence"], None),
    "ENT_ENTUAL_SOURCE": ("conservado", "doc:entual-platform-faq", "documento", "Entual Platform FAQ", ["FAQ Entual"], None),
    "ENT_ESCALA_EVIDENCIA_P02": ("conservado", "doc:escala-epistemica-certeza-comercial", "documento", "Escala Epistémica de Certeza Comercial P02", ["Escala Epistémica Comercial"], None),
    "ENT_ESTRATEGIA_BUILD_BUY": ("conservado", "tema:estrategia-build-buy-partner", "tema", "Estrategia Build Buy Partner BRIDGE", ["Build Buy Partner"], None),
    "ENT_ESTUDIO_ACEPTABILIDAD_IA": ("conservado", "doc:estudio-aceptabilidad-ia", "documento", "Estudio de Aceptabilidad Legal de Declaraciones por IA", ["Aceptabilidad Legal IA"], None),
    "ENT_ESTUDIO_BUNDLING": ("conservado", "doc:estudio-disposicion-pagar-bundling", "documento", "Estudio de Disposición a Pagar por Suite Unificada", ["Disposición a Pagar Bundling"], None),
    "ENT_ESTUDIO_PREDICCION": ("conservado", "doc:estudio-prediccion-litigios", "documento", "Estudio Retrospectivo Predicción Litigios Socioambientales", ["Predicción Litigios"], None),
    "ENT_ESTUDIO_TCO_REAL": ("conservado", "doc:estudio-tco-real-software", "documento", "Estudio de TCO Real y Costos Ocultos de Software", ["TCO Real Software"], None),
    "ENT_FE_ERRATAS_P02": ("conservado", "doc:p02-global-readme-errata", "documento", "00_P02_GLOBAL_READ_ME_AND_ERRATA", ["Errata P02 Global"], None),
    "ENT_FGS_GLOBAL": ("conservado", "org:fgs-global", "organizacion", "FGS Global", ["FGS"], None),
    "ENT_FUENTE_ADDENDUM": ("conservado", "doc:regional-addendum-v1", "documento", "Regional Addendum V1", ["Addendum Regional V1"], None),
    "ENT_FUENTE_ADDENDUM_SEC6": ("conservado", "doc:regional-addendum-sec6", "documento", "Regional Addendum Section 6", ["Addendum Section 6"], None),
    "ENT_FUENTE_LITORAL": ("conservado", "doc:litoralpress-documentation", "documento", "Litoralpress Documentation", ["Documentación Litoralpress"], None),
    "ENT_FUENTE_MAP_V1": ("conservado", "doc:global-market-map-v1", "documento", "Global Market Map V1", ["Market Map V1"], None),
    "ENT_GLEAN": ("conservado", "org:glean", "organizacion", "Glean Technologies Inc.", ["Glean"], None),
    "ENT_GLEAN_SPEC": ("conservado", "doc:glean-product-specifications", "documento", "Glean Product Specifications", ["Specs Glean"], None),
    "ENT_HOOTSUITE": ("conservado", "org:hootsuite", "organizacion", "Hootsuite Inc.", ["Hootsuite"], None),
    "ENT_IRTH_SOLUTIONS": ("conservado", "org:irth-solutions", "organizacion", "Irth Solutions LLC", ["Irth Solutions"], None),
    "ENT_KKR": ("conservado", "org:kkr", "organizacion", "Kohlberg Kravis Roberts & Co. (KKR)", ["KKR"], None),
    "ENT_LICENCIAS_PRENSA": ("conservado", "doc:licencias-colectivas-reproduccion-prensa", "documento", "Licencias Colectivas de Reproducción de Prensa", ["Licencias Colectivas Prensa"], None),
    "ENT_LITORALPRESS": ("conservado", "org:litoralpress", "organizacion", "Litoralpress Ltda.", ["Litoralpress"], None),
    "ENT_MELTWATER": ("conservado", "org:meltwater", "organizacion", "Meltwater Group", ["Meltwater N.V.", "Meltwater"], None),
    "ENT_MERCADO_PUBLICO_CHILE": ("conservado", "org:mercado-publico-chile", "organizacion", "Mercado Público Chile (ChileCompra)", ["Mercado Público", "ChileCompra"], None),
    "ENT_ONCLUSIVE": ("conservado", "org:onclusive", "organizacion", "Onclusive Inc.", ["Onclusive"], None),
    "ENT_OPEN_POINT": ("conservado", "org:open-point-group", "organizacion", "Open Point Group", ["Open Point"], None),
    "ENT_PILOTO_MUNICIPAL": ("conservado", "exp:piloto-ingesta-municipal", "experimento", "Piloto de Ingesta Regulatoria Municipal Descentralizada", ["Piloto Municipal"], None),
    "ENT_POLITICA_RETENCION": ("conservado", "doc:politica-retencion-copyright", "documento", "Política Canónica de Retención y Copyright", ["Política Retención"], None),
    "ENT_PREZLY": ("conservado", "org:prezly", "organizacion", "Prezly SPRL", ["Prezly"], None),
    "ENT_PREZLY_CASES": ("conservado", "doc:prezly-customer-cases", "documento", "Prezly Customer Cases", ["Casos Prezly"], None),
    "ENT_PROTOCOLO_DEMO_TOP10": ("conservado", "doc:protocolo-auditoria-demos-top10", "documento", "Protocolo de Auditoría de Demos Top 10 Comparables", ["Protocolo Demos Top 10"], None),
    "ENT_PRUEBA_ESTRES_GRAFO": ("conservado", "exp:prueba-estres-grafo-unificado", "experimento", "Prueba de Estrés Grafo Unificado 4 Módulos", ["Estrés Grafo 4 Módulos"], None),
    "ENT_QUORUM": ("conservado", "org:quorum-analytics", "organizacion", "Quorum Analytics Inc.", ["Quorum"], None),
    "ENT_RECTIFICACION_M&A": ("conservado", "doc:directiva-rectificacion-ma-p02", "documento", "Directiva de Rectificación M&A P02", ["Rectificación M&A P02"], None),
    "ENT_REFUTACION_ALL_IN_ONE": ("conservado", "doc:dictamen-refutacion-all-in-one", "documento", "Dictamen de Refutación de Suites All-in-One", ["Refutación All in One"], None),
    "ENT_REGION_APAC": ("conservado", "tema:region-mercado-apac", "tema", "Mercado Asia-Pacífico", ["APAC"], None),
    "ENT_REGION_LATAM": ("conservado", "tema:region-mercado-latam", "tema", "Mercado América Latina", ["LatAm"], None),
    "ENT_REGLA_CERO_POR": ("conservado", "doc:regla-canonica-cero-por-p02", "documento", "Regla Canónica Cero POR en Vendors P02", ["Regla Cero POR"], None),
    "ENT_SEC_FORM_6K": ("conservado", "doc:sec-form-6k-wpp-plc", "documento", "SEC Form 6-K a5017o.htm (WPP plc)", ["SEC Form 6-K WPP"], None),
    "ENT_SILOS_OPERACIONALES": ("conservado", "riesgo:silos-operacionales-post-adquisicion", "riesgo", "Silos Operacionales Post-Adquisición", ["Silos Post-M&A"], None),
    "ENT_SUBTEL_CHILE": ("conservado", "org:subtel-chile", "organizacion", "Subsecretaría de Telecomunicaciones de Chile", ["SUBTEL"], None),
    "ENT_TIMELINE_MA": ("conservado", "doc:cronologia-auditada-ma-p02", "documento", "Cronología Auditada M&A Corporate Affairs", ["Cronología M&A P02"], None),
    "ENT_WPP_PLC": ("conservado", "org:wpp", "organizacion", "WPP plc", ["WPP"], None),
    "ESTANDAR_AMEC_3": ("conservado", "doc:amec-barcelona-principles-3", "documento", "AMEC Barcelona Principles 3.0", ["Barcelona Principles 3.0"], None),
    "GRAFO_BIPARTITO": ("conservado", "tema:grafo-bipartito-bitemporal", "tema", "Grafo Bipartito Bitemporal BRIDGE", ["Grafo Bipartito Bitemporal"], None),
    "GRP_CISION": ("conservado", "org:cision", "organizacion", "Cision Ltd. (Platinum Equity)", ["Cision", "Cision Ltd."], None),
    "GRP_SIGNAL_AI": ("conservado", "org:signal-ai", "organizacion", "Signal AI Ltd.", ["Signal AI"], None),
    "INF_CISION_BRANDWATCH": ("conservado", "tema:integracion-cision-brandwatch", "tema", "Cision + Brandwatch (M&A Segregado)", ["Cision Brandwatch Segregado"], None),
    "INT_ALPHASENSE_DRIVE": ("conservado", "prod:conector-alphasense-sharepoint-drive", "producto", "AlphaSense + SharePoint/Drive Connector", ["Conector AlphaSense Drive"], None),
    "INT_DATAMINR_CRISIS24": ("conservado", "prod:integracion-dataminr-crisis24-horizon", "producto", "Dataminr + Crisis24 Horizon", ["Dataminr Crisis24"], None),
    "MOD_EXECUTIVE_BRIEF": ("conservado", "prod:modulo-executive-briefs-bridge", "producto", "Generador de Executive Briefs BRIDGE", ["Executive Briefs BRIDGE"], None),
    "REG_FUENTES_ASUNTOS_PUB": ("conservado", "doc:registro-fuentes-asuntos-publicos-p02", "documento", "Registro de Fuentes de Asuntos Públicos P02", ["Fuentes Asuntos Públicos P02"], None),
    "REG_FUENTES_ESCUCHA": ("conservado", "doc:registro-fuentes-plataformas-escucha-p02", "documento", "Registro de Fuentes de Plataformas de Escucha", ["Fuentes Escucha P02"], None),
}

# Mapeo explícito y verificado para P03 (64 IDs legados)
P03_MAP = {
    # Esquemas internos de datos -> eliminados
    "ENT_ALERT_SCHEMA": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_BROADCAST_SCHEMA": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_DATA_GOVERNANCE_SCHEMA": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_PRESS_SCHEMA": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_REGULATORY_SCHEMA": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_SEMANTIC_ANALYSIS_SCHEMA": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_SIGNAL_SCHEMA": ("eliminado", None, None, None, [], "esquema_datos_interno"),
    "ENT_SOCIAL_DATA_SCHEMA": ("eliminado", None, None, None, [], "esquema_datos_interno"),

    # Casos de prueba demostrativos / hipotéticos -> eliminados
    "ENT_CASO_AUDITORIA_INGESTA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_BLOQUEO_RUTA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_DESALINADORA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_ESCASEZ_HIDRICA": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_PRENSA_REGIONAL": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_RADIO_REGIONAL": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_ROYALTY": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),
    "ENT_CASO_SALAR_DESAMBIGUACION": ("eliminado", None, None, None, [], "caso_prueba_hipotetico"),

    # Registros editoriales internos -> eliminados
    "ENT_CORRECCION_REDES_P03": ("eliminado", None, None, None, [], "registro_editorial_interno"),
    "ENT_RECTIFICACION_APIS_REGULATORIAS": ("eliminado", None, None, None, [], "registro_editorial_interno"),

    # Entidades conservadas
    "ENT_ACTOR_CENTRIC_TRACKING": ("conservado", "tema:monitoreo-centrado-actores", "tema", "Monitoreo Centrado en Actores Clave", ["Stakeholder-Centric Tracking", "Monitoreo Centrado en Actores"], None),
    "ENT_ALERTS_EVIDENCE_CORPUS": ("conservado", "doc:corpus-evidencia-alertas-p03", "documento", "Corpus de Evidencia de Alertas P03", ["Alerts Evidence Corpus", "Corpus Alertas P03"], None),
    "ENT_ALERT_FATIGUE_CONTROLS": ("conservado", "tema:controles-fatiga-alertas", "tema", "Controles de Mitigación de Fatiga de Alertas", ["Alert Fatigue Controls", "Mitigación Fatiga Alertas"], None),
    "ENT_ALERT_ROLE_MATRIX": ("conservado", "doc:matriz-roles-severidad-alertas", "documento", "Matriz de Roles y Severidad de Alertas", ["Alert Role-Severity Matrix", "Matriz Roles Severidad Alertas"], None),
    "ENT_ASR_CHILEAN_BIAS": ("conservado", "riesgo:degradacion-fonetica-asr-chileno", "riesgo", "Degradación Fonética de ASR en Español Chileno", ["Chilean Spanish ASR Degradation", "Sesgo Fonético ASR Chileno"], None),
    "ENT_AUDIOVISUAL_EVIDENCE_RULES": ("conservado", "doc:reglas-evidencia-audiovisual", "documento", "Reglas de Evidencia Audiovisual", ["Audiovisual Evidence Rules", "Reglas Evidencia Audiovisual"], None),
    "ENT_AUDITORIA_TERRITORIAL_PRENSA": ("conservado", "exp:panel-auditoria-territorial-prensa", "experimento", "Panel de Auditoría Territorial de Prensa", ["Territorial Press Audit Panel", "Auditoría Territorial Prensa"], None),
    "ENT_BENCHMARK_AUDIO_CHILENO": ("conservado", "exp:benchmark-transcripcion-audio-chileno", "experimento", "Benchmark de Transcripción de Audio Radial Chileno", ["Chilean Audio Benchmark", "Benchmark Audio Radial Chileno"], None),
    "ENT_BENCHMARK_POSTURA_CHILENA": ("conservado", "exp:benchmark-postura-riesgo-regulatorio-chileno", "experimento", "Benchmark de Postura y Riesgo Regulatorio Chileno", ["Chilean Stance Benchmark", "Benchmark Postura Chilena"], None),
    "ENT_BERTOPIC_PIPELINE": ("conservado", "prod:pipeline-neuronal-bertopic", "producto", "Pipeline Neuronal BERTopic", ["BERTopic Neural Pipeline", "Pipeline BERTopic"], None),
    "ENT_BLINK_FRAMEWORK": ("conservado", "prod:arquitectura-desambiguacion-blink", "producto", "Arquitectura de Desambiguación BLINK", ["BLINK Entity Linking", "Framework BLINK"], None),
    "ENT_BROADCAST_EVIDENCE_CORPUS": ("conservado", "doc:corpus-evidencia-audiovisual-p03", "documento", "Corpus de Evidencia Audiovisual P03", ["Audiovisual Evidence Corpus", "Corpus Audiovisual P03"], None),
    "ENT_BROADCAST_PIPELINE": ("conservado", "prod:pipeline-monitoreo-audiovisual", "producto", "Pipeline de Monitoreo Audiovisual", ["Audiovisual Monitoring Pipeline", "Pipeline Monitoreo Audiovisual"], None),
    "ENT_CANONICAL_CORPUS_P03": ("conservado", "doc:corpus-canonico-evidencia-p03", "documento", "Corpus Canónico de Evidencia P03", ["P03 Evidence Corpus", "Corpus Canónico P03"], None),
    "ENT_CONTROL_FATIGA_ALERTAS": ("conservado", "doc:politica-control-fatiga-alertas", "documento", "Política de Control de Fatiga de Alertas", ["Alert Fatigue Prevention Policy", "Control Fatiga Alertas"], None),
    "ENT_DESACOPLAMIENTO_EPISTEMICO": ("conservado", "tema:desacoplamiento-coordinacion-falsedad", "tema", "Regla de Desacoplamiento Coordinación-Falsedad", ["Epistemic Decoupling Rule", "Regla Desacoplamiento Coordinación Falsedad"], None),
    "ENT_ESTATUS_BETO_CHILE": ("conservado", "exp:calibracion-epistemica-beto-chile", "experimento", "Calibración Epistémica de BETO en Chile", ["BETO Epistemic Status", "Calibración BETO Chile"], None),
    "ENT_ESTUDIO_REGULACION_MUNICIPAL": ("conservado", "doc:estudio-recuperabilidad-regulatoria-municipal", "documento", "Estudio de Recuperabilidad Regulatoria Municipal", ["Municipal Regulatory Ingest Study", "Estudio Regulación Municipal"], None),
    "ENT_ESTUDIO_TCO_MONITOREO": ("conservado", "doc:estudio-tco-real-monitoreo-medios", "documento", "Estudio de TCO Real en Monitoreo de Medios", ["Real TCO Media Ingest Study", "TCO Monitoreo Medios"], None),
    "ENT_INGEST_COST_STRUCTURE": ("conservado", "tema:estructura-costos-ingesta", "tema", "Estructura de Costos de Ingesta", ["Ingest Cost Structure", "Estructura Costos Ingesta"], None),
    "ENT_INGEST_QUALITY_METRICS": ("conservado", "met:calidad-de-ingesta", "metrica", "Métricas y Denominadores de Calidad de Ingesta", ["Ingest Quality Metrics", "Métricas Calidad Ingesta"], None),
    "ENT_IP_RIGHTS_FRAMEWORK": ("conservado", "doc:marco-derechos-uso-retencion-datos", "documento", "Marco de Derechos de Uso y Retención de Datos", ["Data Rights & IP Framework", "Marco Derechos y Retención Datos"], None),
    "ENT_LATENCY_METRICS": ("conservado", "met:latencia-ttd-ttv", "metrica", "Métricas de Latencia TTD y TTV", ["TTD and TTV Latency Metrics", "Latencia TTD TTV"], None),
    "ENT_LEGAL_EVIDENCE_CORPUS": ("conservado", "doc:corpus-evidencia-legal-p03", "documento", "Corpus de Evidencia Legal y Contractual P03", ["Legal Evidence Corpus", "Corpus Legal P03"], None),
    "ENT_MATERIAL_CHANGE": ("conservado", "evt:cambio-material-corporativo", "evento", "Cambio Material Corporativo (Hecho Esencial)", ["Hecho Esencial", "Material Event", "Cambio Material Corporativo"], None),
    "ENT_NLP_EVIDENCE_CORPUS": ("conservado", "doc:corpus-evidencia-nlp-p03", "documento", "Corpus de Evidencia de NLP P03", ["NLP Evidence Corpus", "Corpus NLP P03"], None),
    "ENT_NLP_LIMITATIONS": ("conservado", "riesgo:limites-epistemicos-nlp-sentimiento", "riesgo", "Límites Epistémicos de NLP y Sentimiento", ["NLP Epistemic Limitations", "Límites Epistémicos NLP"], None),
    "ENT_OFFICIAL_FORMATS": ("conservado", "doc:especificaciones-formato-trazabilidad-oficial", "documento", "Especificaciones de Formato y Trazabilidad Oficial", ["Official Formats & Traceability", "Especificaciones Formato Oficial"], None),
    "ENT_OFFICIAL_REGISTRIES": ("conservado", "tema:ecosistema-registros-oficiales-prioritarios", "tema", "Ecosistema de Registros Oficiales Prioritarios", ["Official Regulatory Registries", "Registros Oficiales Prioritarios"], None),
    "ENT_PILOTO_CAMPO_DIRECTORES": ("conservado", "exp:piloto-campo-directores-asuntos-corporativos", "experimento", "Piloto de Campo con Directores de Asuntos Corporativos", ["Field Pilot Corporate Affairs", "Piloto Directores Asuntos Corporativos"], None),
    "ENT_POLITICA_CUMPLIMIENTO_IP": ("conservado", "doc:politica-cumplimiento-propiedad-intelectual-ingesta", "documento", "Política de Cumplimiento de Propiedad Intelectual e Ingesta", ["IP Compliance Policy", "Política Cumplimiento IP"], None),
    "ENT_PRECEDENTE_HIQ_LINKEDIN": ("conservado", "doc:litigio-hiq-v-linkedin", "documento", "Precedente y Litigio hiQ v. LinkedIn Corp.", ["hiQ v. LinkedIn Scraping Case", "Precedente hiQ LinkedIn"], None),
    "ENT_PRENSA_REGIONAL_CHILE": ("conservado", "tema:ecosistema-prensa-regional-chile", "tema", "Ecosistema de Prensa Regional y Provincial de Chile", ["Chilean Regional Press", "Prensa Regional Chile"], None),
    "ENT_PRESS_CHANNELS": ("conservado", "tema:canales-ingesta-prensa", "tema", "Canales de Ingesta de Prensa", ["Press Access Channels", "Canales Ingesta Prensa"], None),
    "ENT_PRESS_EVIDENCE_CORPUS": ("conservado", "doc:corpus-evidencia-prensa-p03", "documento", "Corpus de Evidencia de Prensa P03", ["Press Evidence Corpus", "Corpus Prensa P03"], None),
    "ENT_REGULATORY_EVIDENCE_CORPUS": ("conservado", "doc:corpus-evidencia-regulatoria-p03", "documento", "Corpus de Evidencia Regulatoria P03", ["Regulatory Evidence Corpus", "Corpus Regulatorio P03"], None),
    "ENT_REGULATORY_FSM": ("conservado", "prod:fsm-ciclo-vida-regulatorio", "producto", "Máquina de Estados de Ciclo de Vida Regulatorio", ["Regulatory Lifecycle FSM", "Máquina de Estados Regulatoria"], None),
    "ENT_SANDBOX_PRUEBA_ESTRES": ("conservado", "exp:sandbox-prueba-estres-desinformacion", "experimento", "Sandbox de Prueba de Estrés de Desinformación Sintética", ["Synthetic Disinformation Sandbox", "Sandbox Desinformación"], None),
    "ENT_SIGNAL_FAMILIES": ("conservado", "tema:familias-senales-entorno", "tema", "Familias de Señales de Entorno", ["Signal Taxonomy", "Familias Señales Entorno"], None),
    "ENT_SIGNAL_TAXONOMY": ("conservado", "doc:ontologia-senales-externas", "documento", "Ontología de Señales Externas", ["Signal Ontology", "Taxonomía Señales Externas"], None),
    "ENT_SLA_BROADCAST_REAL": ("conservado", "comp:sla-monitoreo-audiovisual", "compromiso", "SLA Real de Monitoreo Audiovisual", ["Real Broadcast SLA", "SLA Monitoreo Audiovisual"], None),
    "ENT_SOCIAL_BIAS": ("conservado", "riesgo:sesgos-estructurales-redes-sociales", "riesgo", "Sesgos Estructurales de Redes Sociales", ["Social Media Sampling Bias", "Sesgos Redes Sociales"], None),
    "ENT_SOCIAL_EVIDENCE_CORPUS": ("conservado", "doc:corpus-evidencia-redes-p03", "documento", "Corpus de Evidencia de Redes P03", ["Social Evidence Corpus", "Corpus Redes P03"], None),
    "ENT_SOCIAL_PLATFORMS": ("conservado", "tema:ecosistema-plataformas-sociales-oficiales", "tema", "Ecosistema de Plataformas Sociales Oficiales", ["Official Social Platforms", "Plataformas Sociales Oficiales"], None),
    "ENT_TEST_CRISIS_HISTORICAS": ("conservado", "exp:test-crisis-historicas-asuntos-publicos", "experimento", "Test de Crisis Históricas de Asuntos Públicos", ["Historical Crisis Benchmark", "Test Crisis Históricas"], None),
    "ENT_TRADE_OFF_INGEST": ("conservado", "doc:matriz-trade-off-ingesta", "documento", "Matriz de Trade-Off de Ingesta", ["Ingest Trade-Off Matrix", "Trade-Off Ingesta"], None),
}


def aplicar_mapa_pilar(
    entidades: dict[str, dict], mapa: list[dict], pilar_map: dict
) -> tuple[dict[str, dict], list[dict]]:
    """Aplica las reglas de mapeo de un pilar de forma determinista en dos pases."""
    ids_mapa_vistos = {m["id_legado"] for m in mapa}

    # Pase 1: Crear entidades conservadas
    for leg_id, (accion, id_nuevo, tipo, canon_name, aliases, motivo) in pilar_map.items():
        if leg_id in ids_mapa_vistos:
            continue
        if accion == "conservado":
            mapa.append({
                "id_legado": leg_id,
                "accion": "conservado",
                "id_nuevo": id_nuevo,
                "motivo": None,
            })
            if id_nuevo not in entidades:
                entidades[id_nuevo] = {
                    "entity_id": id_nuevo,
                    "type": tipo,
                    "canonical_name": canon_name,
                    "ids_legado": [leg_id],
                    "aliases": list(aliases),
                }
            else:
                if leg_id not in entidades[id_nuevo]["ids_legado"]:
                    entidades[id_nuevo]["ids_legado"].append(leg_id)
                for a in aliases:
                    if a not in entidades[id_nuevo]["aliases"]:
                        entidades[id_nuevo]["aliases"].append(a)

    # Pase 2: Procesar fusionados y eliminados
    for leg_id, (accion, id_nuevo, tipo, canon_name, aliases, motivo) in pilar_map.items():
        if leg_id in ids_mapa_vistos:
            continue
        if accion == "fusionado":
            mapa.append({
                "id_legado": leg_id,
                "accion": "fusionado",
                "id_nuevo": id_nuevo,
                "motivo": motivo,
            })
            if id_nuevo in entidades:
                if leg_id not in entidades[id_nuevo]["ids_legado"]:
                    entidades[id_nuevo]["ids_legado"].append(leg_id)
                for a in aliases:
                    if a not in entidades[id_nuevo]["aliases"]:
                        entidades[id_nuevo]["aliases"].append(a)
        elif accion == "eliminado":
            mapa.append({
                "id_legado": leg_id,
                "accion": "eliminado",
                "id_nuevo": None,
                "motivo": motivo,
            })

    return entidades, mapa


def cargar_existentes(r: Path) -> tuple[dict[str, dict], list[dict]]:
    """Carga las entidades y el mapa existentes si ya fueron inicializados."""
    entidades = {}
    mapa = []

    ent_path = r / "kb" / "grafo" / "entidades.jsonl"
    if ent_path.exists():
        with open(ent_path, "r", encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    e = json.loads(line)
                    if "ids_legado" in e and "entity_id" in e:
                        entidades[e["entity_id"]] = e
                except Exception as err:
                    logger.error(f"Error cargando entidad: {type(err).__name__} (detalles omitidos por seguridad)")

    mapa_path = r / "kb" / "grafo" / "mapa_ids.jsonl"
    if mapa_path.exists():
        with open(mapa_path, "r", encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    m = json.loads(line)
                    mapa.append(m)
                except Exception as err:
                    logger.error(f"Error cargando mapa: {type(err).__name__} (detalles omitidos por seguridad)")

    return entidades, mapa


def resolver_pilar_p01(r: Path) -> tuple[dict[str, dict], list[dict]]:
    """Resuelve las 64 entidades del pilar P01."""
    entidades, mapa = cargar_existentes(r)
    return aplicar_mapa_pilar(entidades, mapa, P01_MAP)


def resolver_pilar_p02(r: Path) -> tuple[dict[str, dict], list[dict]]:
    """Resuelve las 114 entidades del pilar P02."""
    entidades, mapa = cargar_existentes(r)
    return aplicar_mapa_pilar(entidades, mapa, P02_MAP)


def resolver_pilar_p03(r: Path) -> tuple[dict[str, dict], list[dict]]:
    """Resuelve las 64 entidades del pilar P03."""
    entidades, mapa = cargar_existentes(r)
    return aplicar_mapa_pilar(entidades, mapa, P03_MAP)


def guardar_grafo(r: Path, entidades: dict[str, dict], mapa: list[dict]):
    """Guarda entidades.jsonl y mapa_ids.jsonl de forma atómica y determinista."""
    grafo_dir = r / "kb" / "grafo"
    grafo_dir.mkdir(parents=True, exist_ok=True)

    ent_path = grafo_dir / "entidades.jsonl"
    with open(ent_path, "w", encoding="utf-8") as fh:
        for eid in sorted(entidades.keys()):
            e = entidades[eid]
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")

    mapa_path = grafo_dir / "mapa_ids.jsonl"
    # Ordenar por id_legado para determinismo
    mapa_ordenado = sorted(mapa, key=lambda x: x["id_legado"])
    with open(mapa_path, "w", encoding="utf-8") as fh:
        for m in mapa_ordenado:
            fh.write(json.dumps(m, ensure_ascii=False) + "\n")


def validar_resolucion(entidades: dict[str, dict], mapa: list[dict]) -> list[str]:
    """Verifica conformidad estricta con las reglas de gate_f4."""
    errores = []
    por_id = entidades

    ids = list(entidades.keys())
    if len(ids) != len(set(ids)):
        errores.append("IDs de entidades duplicados")

    for eid, e in entidades.items():
        if not re.match(r"^[a-z]+:[a-z0-9][a-z0-9-]*$", eid):
            errores.append(f"entity_id inválido: {eid}")
        if e.get("type") not in TIPOS_CANONICOS:
            errores.append(f"tipo no canónico en {eid}: {e.get('type')}")
        if not str(e.get("canonical_name", "")).strip():
            errores.append(f"canonical_name vacío en {eid}")
        if not isinstance(e.get("ids_legado"), list) or not e["ids_legado"]:
            errores.append(f"ids_legado inválido en {eid}")
        if "0.932" in json.dumps(e, ensure_ascii=False):
            errores.append(f"cifra 0.932 presente en {eid}")

    cuenta = collections.Counter(x["id_legado"] for x in mapa)
    for leg_id, c in cuenta.items():
        if c > 1:
            errores.append(f"id_legado duplicado en mapa: {leg_id}")

    for x in mapa:
        acc = x.get("accion")
        idn = x.get("id_nuevo")
        idl = x.get("id_legado")
        mot = x.get("motivo")

        if acc in ("conservado", "fusionado"):
            if idn not in por_id:
                errores.append(f"mapa {idl}: id_nuevo '{idn}' no existe en entidades")
            elif idl not in por_id[idn].get("ids_legado", []):
                errores.append(f"mapa {idl}: no está en ids_legado de '{idn}'")
        elif acc == "eliminado":
            if idn is not None:
                errores.append(f"mapa {idl}: eliminado con id_nuevo no nulo")
            if not str(mot or "").strip():
                errores.append(f"mapa {idl}: eliminado sin motivo")
        else:
            errores.append(f"mapa {idl}: accion inválida '{acc}'")

    return errores


def main():
    parser = argparse.ArgumentParser(description="Resolución de entidades para BRIDGE")
    parser.add_argument("--pilar", default="P01", help="Pilar a resolver (P01..T01)")
    args = parser.parse_args()

    r = raiz()
    pilar = args.pilar.upper()

    if pilar == "P01":
        entidades, mapa = resolver_pilar_p01(r)
    elif pilar == "P02":
        entidades, mapa = resolver_pilar_p02(r)
    elif pilar == "P03":
        entidades, mapa = resolver_pilar_p03(r)
    else:
        print(f"Resolución para pilar {pilar} aún no implementada en este paso.")
        sys.exit(1)

    errores = validar_resolucion(entidades, mapa)
    if errores:
        print(f"ERRORES ({len(errores)}):")
        for err in errores:
            print(f"  - {err}")
        sys.exit(1)

    guardar_grafo(r, entidades, mapa)
    print(f"OK: Pilar {pilar} resuelto. Entidades: {len(entidades)}, Mapeos: {len(mapa)}")


if __name__ == "__main__":
    main()
