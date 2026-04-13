RSS_FEEDS = [
    # --- M&A / NEGOCIOS ESPAÑA ---
    {"url": "https://www.expansion.com/rss/empresas.xml", "name": "Expansión"},
    {"url": "https://www.expansion.com/rss/juridico.xml", "name": "Expansión Jurídico"},
    {"url": "https://cincodias.elpais.com/seccion/rss/economia/", "name": "Cinco Días"},
    {"url": "https://www.eleconomista.es/rss/rss-mercados.php", "name": "El Economista"},
    {"url": "https://www.elconfidencial.com/rss/economia.xml", "name": "El Confidencial Economía"},

    # --- LEGAL ESPAÑA ---
    {"url": "https://www.legaltoday.com/feed/", "name": "Legal Today"},
    {"url": "https://elderecho.com/feed", "name": "El Derecho"},
    {"url": "https://www.economist.es/rss.xml", "name": "Economist & Jurist"},
    {"url": "https://noticiasjuridicas.com/feed/", "name": "Noticias Jurídicas"},

    # --- REGULACIÓN EU ---
    {"url": "https://eur-lex.europa.eu/rss/rss.xml", "name": "EUR-Lex"},
    {"url": "https://www.europarl.europa.eu/rss/rss.xml", "name": "Parlamento Europeo"},
    {"url": "https://iapp.org/feed/", "name": "IAPP"},
    {"url": "https://www.politico.eu/feed/", "name": "Politico EU"},

    # --- M&A / NEGOCIOS INTERNACIONAL ---
    {"url": "https://feeds.reuters.com/reuters/businessNews", "name": "Reuters Business"},
    {"url": "https://feeds.reuters.com/reuters/technologyNews", "name": "Reuters Tech"},
    {"url": "https://corpgov.law.harvard.edu/feed/", "name": "Harvard Corp Gov"},
    {"url": "https://www.lawfaremedia.org/rss.xml", "name": "Lawfare"},

    # --- IA GENERAL ---
    {"url": "https://techcrunch.com/feed/", "name": "TechCrunch"},
    {"url": "https://feeds.feedburner.com/venturebeat/SZYF", "name": "VentureBeat"},
    {"url": "https://www.elconfidencial.com/rss/tecnologia.xml", "name": "El Confidencial Tech"},

    # --- IA LEGAL ---
    {"url": "https://artificialawyer.com/feed/", "name": "Artificial Lawyer"},
    {"url": "https://www.legalfutures.co.uk/feed", "name": "Legal Futures"},
    {"url": "https://abovethelaw.com/feed/", "name": "Above The Law"},
]

CATEGORIES = [
    "M&A España",
    "M&A Internacional",
    "Derecho Societario Español",
    "Regulación Europea",
    "Regulación Internacional",
    "IA General",
    "IA en Derecho y M&A",
]

CATEGORY_ICONS = {
    "M&A España": "🏢",
    "M&A Internacional": "🌍",
    "Derecho Societario Español": "⚖️",
    "Regulación Europea": "🇪🇺",
    "Regulación Internacional": "🌐",
    "IA General": "🤖",
    "IA en Derecho y M&A": "⚖️🤖",
}

# --- Señales geográficas España ---
SPAIN_SIGNALS = [
    "españa", "spanish", "madrid", "barcelona", "ibex", "cnmv", "banco de españa",
    "aena", "grifols", "bbva", "santander", "caixabank", "sabadell", "iberdrola",
    "repsol", "inditex", "ferrovial", "acs", "indra", "mapfre", "cellnex",
    "amadeus", "cnmc", "mercado español", "bolsa española", "gobierno español",
    "ministerio", "boe", "spain",
]

MA_KEYWORDS = [
    "merger", "acquisition", "acquires", "acquired", "takeover", "buyout",
    "deal", "funding", "valuation", "raises", "ipo", "private equity", "venture capital",
    "joint venture", "antitrust", "m&a", "billion", "million",
    "fusión", "adquisición", "compra", "opa", "opv", "capital riesgo",
    "fondo de inversión", "concentración empresarial", "due diligence",
    "desinversión", "oferta pública", "compraventa", "lbo", "mbo",
    "valorado en", "valued at", "deal value",
]

CORPORATE_LAW_KEYWORDS = [
    "lsc", "ley de sociedades", "societario", "consejo de administración",
    "junta de accionistas", "gobierno corporativo", "código de buen gobierno",
    "cotizada", "csrd", "csddd", "sostenibilidad empresarial",
    "corporate governance", "shareholder rights", "board of directors",
    "accionistas", "dividendo", "ampliación de capital", "escisión",
    "responsabilidad de administradores", "cnmv circular",
]

EU_REGULATION_KEYWORDS = [
    "european commission", "eu regulation", "eu directive", "eur-lex", "doue",
    "reglamento ue", "directiva europea", "comisión europea", "parlamento europeo",
    "ai act", "gdpr", "rgpd", "dsa", "dma", "nis2", "fsr", "eu ai act",
    "reglamento ia", "single market", "mercado único", "transposición",
    "dg comp", "competition eu", "state aid",
]

INTL_REGULATION_KEYWORDS = [
    "regulation", "regulatory", "compliance", "legislation", "parliament",
    "fine", "penalty", "ruling", "enforcement", "ban",
    "oecd", "ocde", "beps", "fatf", "sec", "doj", "ftc", "ico",
    "reglamento", "regulación", "multa", "sanción", "normativa",
    "data protection", "intellectual property", "copyright",
    "aepd", "cnmc",
]

AI_KEYWORDS = [
    "artificial intelligence", "machine learning", "llm", "generative ai",
    "chatgpt", "openai", "anthropic", "gemini", "gpt", "deep learning",
    "foundation model", "large language model", "neural network",
    "inteligencia artificial", "modelo de lenguaje", "ia generativa",
    "deepseek", "llama", "claude", "mistral", "qwen",
    "agentic", "agente ia",
]

AI_LEGAL_KEYWORDS = [
    "legal ai", "ai legal", "legaltech", "ai lawyer", "ai law firm",
    "contract review", "legal automation", "ai contract",
    "harvey ai", "spellbook", "clio", "lexisnexis ai", "thomson reuters ai",
    "ia legal", "ia jurídica", "automatización legal", "despacho ia",
    "revisión contratos ia", "due diligence ai", "ai m&a",
    "garfield", "artificial lawyer",
]


def classify_article(title: str, summary: str) -> str | None:
    """Devuelve la categoría más adecuada o None si no es relevante."""
    text = (title + " " + summary).lower()

    has_spain = any(kw in text for kw in SPAIN_SIGNALS)
    has_ma = any(kw in text for kw in MA_KEYWORDS)
    has_corp_law = any(kw in text for kw in CORPORATE_LAW_KEYWORDS)
    has_eu_reg = any(kw in text for kw in EU_REGULATION_KEYWORDS)
    has_intl_reg = any(kw in text for kw in INTL_REGULATION_KEYWORDS)
    has_ai = any(kw in text for kw in AI_KEYWORDS)
    has_ai_legal = any(kw in text for kw in AI_LEGAL_KEYWORDS)

    # Orden de prioridad: más específico primero
    if has_ai and (has_ai_legal or has_ma or has_corp_law or has_intl_reg):
        return "IA en Derecho y M&A"
    if has_ma and has_spain:
        return "M&A España"
    if has_corp_law and has_spain:
        return "Derecho Societario Español"
    if has_eu_reg:
        return "Regulación Europea"
    if has_ma:
        return "M&A Internacional"
    if has_intl_reg:
        return "Regulación Internacional"
    if has_ai:
        return "IA General"

    return None
