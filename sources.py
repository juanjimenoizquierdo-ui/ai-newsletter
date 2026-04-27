RSS_FEEDS = [
    # --- ENFORCEMENT / REGULADORES PRIMARIOS ---
    {"url": "https://www.edpb.europa.eu/rss.xml_en", "name": "EDPB"},
    {"url": "https://www.eba.europa.eu/rss.xml", "name": "EBA"},
    {"url": "https://www.esma.europa.eu/rss.xml", "name": "ESMA"},
    {"url": "https://www.aepd.es/rss.xml", "name": "AEPD"},

    # --- REGULACIÓN EU ---
    {"url": "https://eur-lex.europa.eu/rss/rss.xml", "name": "EUR-Lex"},
    {"url": "https://www.europarl.europa.eu/rss/rss.xml", "name": "Parlamento Europeo"},
    {"url": "https://www.politico.eu/feed/", "name": "Politico EU"},
    {"url": "https://iapp.org/feed/", "name": "IAPP"},
    {"url": "https://www.finance-watch.org/feed/", "name": "Finance Watch"},

    # --- FINTECH / DORA ---
    {"url": "https://www.finextra.com/rss/headlines.aspx", "name": "Finextra"},

    # --- M&A ESPAÑA ---
    {"url": "https://www.expansion.com/rss/empresas.xml", "name": "Expansión"},
    {"url": "https://www.expansion.com/rss/juridico.xml", "name": "Expansión Jurídico"},
    {"url": "https://cincodias.elpais.com/seccion/rss/economia/", "name": "Cinco Días"},
    {"url": "https://www.eleconomista.es/rss/rss-mercados.php", "name": "El Economista"},
    {"url": "https://www.elconfidencial.com/rss/economia.xml", "name": "El Confidencial Economía"},

    # --- M&A INTERNACIONAL ---
    {"url": "https://feeds.reuters.com/reuters/businessNews", "name": "Reuters Business"},
    {"url": "https://feeds.reuters.com/reuters/technologyNews", "name": "Reuters Tech"},
    {"url": "https://corpgov.law.harvard.edu/feed/", "name": "Harvard Corp Gov"},
    {"url": "https://www.lawfaremedia.org/rss.xml", "name": "Lawfare"},

    # --- LEGAL TECH ---
    {"url": "https://artificialawyer.com/feed/", "name": "Artificial Lawyer"},
    {"url": "https://www.legalfutures.co.uk/feed", "name": "Legal Futures"},
    {"url": "https://www.thealgorithmicbridge.com/feed", "name": "The Algorithmic Bridge"},
]

CATEGORIES = [
    "Enforcement Decisions",
    "AI Law & Regulation",
    "Privacy & GDPR Enforcement",
    "Fintech & DORA",
    "Legal Tech",
    "M&A España",
    "Regulación Europea General",
    "IA General",
]

CATEGORY_ICONS = {
    "Enforcement Decisions": "⚡",
    "AI Law & Regulation": "🤖⚖️",
    "Privacy & GDPR Enforcement": "🔒",
    "Fintech & DORA": "🏦",
    "Legal Tech": "💻⚖️",
    "M&A España": "🏢",
    "Regulación Europea General": "🇪🇺",
    "IA General": "🤖",
}

# --- Señales geográficas España ---
SPAIN_SIGNALS = [
    "españa", "spanish", "madrid", "barcelona", "ibex", "cnmv", "banco de españa",
    "aena", "grifols", "bbva", "santander", "caixabank", "sabadell", "iberdrola",
    "repsol", "inditex", "ferrovial", "acs", "indra", "mapfre", "cellnex",
    "amadeus", "cnmc", "mercado español", "bolsa española", "gobierno español",
    "ministerio", "boe", "spain", "aepd",
]

# --- Enforcement Decisions ---
ENFORCEMENT_KEYWORDS = [
    "fine", "fined", "penalty", "sanction", "ruling", "decision", "enforcement action",
    "infringement", "violation", "breach", "reprimand", "order to comply",
    "multa", "sanción", "resolución", "expediente", "decisión regulatoria",
    "infracción", "apercibimiento", "requerimiento",
]
ENFORCEMENT_AUTHORITIES = [
    "edpb", "ico", "cnil", "aepd", "garante", "datatilsynet", "dpc",
    "bafin", "fca", "eba", "esma", "amf", "cnmv", "banco de españa",
    "european commission", "dg comp", "dg connect",
]

# --- AI Law & Regulation ---
AI_LAW_KEYWORDS = [
    "ai act", "artificial intelligence act", "ai liability", "ai governance",
    "high-risk ai", "prohibited ai", "conformity assessment", "ai office",
    "ai board", "gpai", "general purpose ai", "foundation model regulation",
    "enisa ai", "ai regulation", "ai oversight", "ai supervision",
    "acto ia", "reglamento ia", "gobernanza ia", "supervisión ia",
    "oficina ia", "ia de alto riesgo", "ia prohibida",
]

# --- Privacy & GDPR ---
PRIVACY_KEYWORDS = [
    "gdpr", "rgpd", "data protection", "protección de datos", "edpb",
    "data breach", "brecha de seguridad", "transfer impact assessment",
    "standard contractual clauses", "sccs", "adequacy decision", "adequacy",
    "dpc", "ico", "cnil", "aepd gdpr", "data subject rights", "derechos arco",
    "privacy", "privacidad", "dpf", "data privacy framework",
    "supervisory authority", "autoridad de control", "bcr",
]

# --- Fintech & DORA ---
FINTECH_KEYWORDS = [
    "dora", "digital operational resilience", "eba", "esma", "psd2", "psd3",
    "open banking", "payment services", "crypto regulation", "mica",
    "markets in crypto", "fintech", "regtech", "suptech", "neobank",
    "digital finance", "crypto asset", "stablecoin", "cbdc",
    "banking regulation", "insurance regulation", "eiopa",
    "resiliencia operativa digital", "servicios de pago", "banca digital",
    "supervisión fintech", "activos digitales",
]

# --- Legal Tech ---
LEGAL_TECH_KEYWORDS = [
    "legal ai", "ai legal", "legaltech", "legal tech", "ai lawyer",
    "contract review", "legal automation", "ai contract", "document review",
    "harvey ai", "spellbook", "clio", "lexisnexis ai", "thomson reuters ai",
    "ia legal", "ia jurídica", "automatización legal", "despacho ia",
    "revisión contratos ia", "due diligence ai", "ai m&a", "ai law firm",
    "artificial lawyer", "law firm ai", "legal llm",
]

# --- M&A ---
MA_KEYWORDS = [
    "merger", "acquisition", "acquires", "acquired", "takeover", "buyout",
    "deal", "funding", "valuation", "raises", "ipo", "private equity", "venture capital",
    "joint venture", "antitrust", "m&a", "billion", "million",
    "fusión", "adquisición", "compra", "opa", "opv", "capital riesgo",
    "fondo de inversión", "concentración empresarial", "due diligence",
    "desinversión", "oferta pública", "compraventa", "lbo", "mbo",
    "valorado en", "valued at", "deal value",
]

# --- Regulación Europea General ---
EU_REGULATION_KEYWORDS = [
    "european commission", "eu regulation", "eu directive", "eur-lex", "doue",
    "reglamento ue", "directiva europea", "comisión europea", "parlamento europeo",
    "dsa", "dma", "nis2", "cra", "cyber resilience act", "fsr",
    "single market", "mercado único", "transposición", "trilogue",
    "eu law", "council regulation", "european parliament vote",
    "estado miembro", "state aid", "ayudas de estado",
]

# --- IA General (solo con ángulo regulatorio) ---
AI_GENERAL_KEYWORDS = [
    "artificial intelligence", "machine learning", "llm", "generative ai",
    "chatgpt", "openai", "anthropic", "gemini", "gpt", "deep learning",
    "foundation model", "large language model", "neural network",
    "inteligencia artificial", "modelo de lenguaje", "ia generativa",
    "deepseek", "llama", "claude", "mistral", "qwen",
]
AI_REGULATORY_ANGLE = [
    "regulation", "regulat", "compliance", "liability", "risk", "governance",
    "oversight", "safety", "ethics", "bias", "transparency", "accountability",
    "regulación", "cumplimiento", "responsabilidad", "riesgo", "seguridad",
    "ética", "sesgo", "transparencia",
]


def classify_article(title: str, summary: str) -> str | None:
    """Devuelve la categoría más adecuada o None si no es relevante."""
    text = (title + " " + summary).lower()

    has_enforcement = any(kw in text for kw in ENFORCEMENT_KEYWORDS)
    has_authority = any(kw in text for kw in ENFORCEMENT_AUTHORITIES)
    has_ai_law = any(kw in text for kw in AI_LAW_KEYWORDS)
    has_privacy = any(kw in text for kw in PRIVACY_KEYWORDS)
    has_fintech = any(kw in text for kw in FINTECH_KEYWORDS)
    has_legal_tech = any(kw in text for kw in LEGAL_TECH_KEYWORDS)
    has_ma = any(kw in text for kw in MA_KEYWORDS)
    has_spain = any(kw in text for kw in SPAIN_SIGNALS)
    has_eu_reg = any(kw in text for kw in EU_REGULATION_KEYWORDS)
    has_ai_general = any(kw in text for kw in AI_GENERAL_KEYWORDS)
    has_regulatory_angle = any(kw in text for kw in AI_REGULATORY_ANGLE)

    # Prioridad: más específico primero
    if has_enforcement and has_authority:
        return "Enforcement Decisions"
    if has_ai_law:
        return "AI Law & Regulation"
    if has_privacy:
        return "Privacy & GDPR Enforcement"
    if has_fintech:
        return "Fintech & DORA"
    if has_legal_tech:
        return "Legal Tech"
    if has_ma and has_spain:
        return "M&A España"
    if has_eu_reg:
        return "Regulación Europea General"
    if has_ai_general and has_regulatory_angle:
        return "IA General"

    return None
