RSS_FEEDS = [
    # --- ESPAÑA ---
    {"url": "https://www.expansion.com/rss/juridico.xml", "name": "Expansión Jurídico"},
    {"url": "https://cincodias.elpais.com/seccion/rss/economia/", "name": "Cinco Días"},
    {"url": "https://www.economist.es/rss.xml", "name": "Economist & Jurist"},
    {"url": "https://elderecho.com/feed", "name": "El Derecho"},
    {"url": "https://www.legaltoday.com/feed/", "name": "Legal Today"},
    {"url": "https://www.elconfidencial.com/rss/tecnologia.xml", "name": "El Confidencial Tech"},

    # --- UNIÓN EUROPEA ---
    {"url": "https://eur-lex.europa.eu/rss/rss.xml", "name": "EUR-Lex"},
    {"url": "https://www.europarl.europa.eu/rss/rss.xml", "name": "Parlamento Europeo"},
    {"url": "https://iapp.org/feed/", "name": "IAPP"},
    {"url": "https://www.politico.eu/feed/", "name": "Politico EU"},

    # --- INTERNACIONAL ---
    {"url": "https://feeds.reuters.com/reuters/businessNews", "name": "Reuters Business"},
    {"url": "https://feeds.reuters.com/reuters/technologyNews", "name": "Reuters Tech"},
    {"url": "https://www.lawfaremedia.org/rss.xml", "name": "Lawfare"},
    {"url": "https://techcrunch.com/feed/", "name": "TechCrunch"},
    {"url": "https://feeds.feedburner.com/venturebeat/SZYF", "name": "VentureBeat"},
]

# --- Keywords M&A y Mercantil ---
MA_KEYWORDS = [
    # inglés
    "merger", "acquisition", "acquires", "acquired", "takeover", "buyout",
    "deal", "billion", "funding", "valuation", "invest", "raises", "ipo",
    "private equity", "venture capital", "joint venture", "due diligence",
    "antitrust", "competition authority",
    # español
    "fusión", "adquisición", "compra", "oferta pública", "opa", "opv",
    "mercantil", "societario", "capital riesgo", "fondo de inversión",
    "competencia", "concentración empresarial", "due diligence",
    "consejo de administración", "junta de accionistas",
]

# --- Keywords IA ---
AI_KEYWORDS = [
    # inglés
    "artificial intelligence", " ai ", "machine learning", "llm", "generative",
    "chatgpt", "openai", "anthropic", "gemini", "gpt", "deep learning",
    "foundation model", "large language", "algorithm",
    # español
    "inteligencia artificial", " ia ", "aprendizaje automático", "modelo de lenguaje",
    "sistema de ia", "algoritmo", "automatización inteligente",
]

# --- Keywords Legal y Regulatorio ---
LEGAL_KEYWORDS = [
    # inglés
    "regulation", "regulatory", "lawsuit", "court", "compliance", "gdpr",
    "eu ai act", "ai act", "copyright", "liability", "legislation",
    "parliament", "ban", "fine", "penalty", "ruling", "judge", "enforcement",
    "data protection", "intellectual property",
    # español
    "reglamento", "regulación", "demanda", "tribunal", "juzgado", "sentencia",
    "reglamento ia", "ley de ia", "propiedad intelectual", "protección de datos",
    "responsabilidad", "multa", "sanción", "normativa", "legislación",
    "comisión europea", "aepd", "cnmc", "audiencia nacional",
]


def is_relevant(title: str, summary: str) -> tuple[bool, str]:
    """Devuelve (es_relevante, categoría)"""
    text = (title + " " + summary).lower()

    has_ai = any(kw in text for kw in AI_KEYWORDS)
    has_ma = any(kw in text for kw in MA_KEYWORDS)
    has_legal = any(kw in text for kw in LEGAL_KEYWORDS)

    # Categoría M&A: necesita IA o mercantil + M&A
    if has_ma and (has_ai or has_legal):
        return True, "M&A & Mercantil"

    # Categoría Legal: necesita IA + legal/regulatorio
    if has_ai and has_legal:
        return True, "Legal & Regulación IA"

    # M&A puro con IA
    if has_ma and has_ai:
        return True, "M&A & Mercantil"

    return False, ""
