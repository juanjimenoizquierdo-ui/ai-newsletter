RSS_FEEDS = [
    # AI & Tech general
    {"url": "https://techcrunch.com/feed/", "name": "TechCrunch"},
    {"url": "https://www.theverge.com/rss/index.xml", "name": "The Verge"},
    {"url": "https://feeds.feedburner.com/venturebeat/SZYF", "name": "VentureBeat"},
    # M&A / Deals
    {"url": "https://feeds.reuters.com/reuters/businessNews", "name": "Reuters Business"},
    {"url": "https://feeds.axios.com/axios/futures", "name": "Axios Futures"},
    # Legal / Regulation AI
    {"url": "https://feeds.feedburner.com/eff/updates", "name": "EFF"},
    {"url": "https://www.lawfaremedia.org/rss.xml", "name": "Lawfare"},
    {"url": "https://iapp.org/feed/", "name": "IAPP"},
]

# Keywords para filtrar artículos relevantes
MA_KEYWORDS = [
    "merger", "acquisition", "acquires", "acquired", "deal", "billion",
    "funding", "valuation", "invest", "raises", "round", "ipo", "buyout",
    "fusión", "adquisición", "compra",
]

AI_KEYWORDS = [
    "artificial intelligence", " ai ", "machine learning", "llm", "generative",
    "chatgpt", "openai", "anthropic", "gemini", "claude", "gpt", "neural",
    "deep learning", "foundation model", "large language",
]

LEGAL_KEYWORDS = [
    "regulation", "regulatory", "lawsuit", "court", "compliance", "gdpr",
    "eu ai act", "ai act", "copyright", "liability", "policy", "legislation",
    "congress", "parliament", "ban", "fine", "penalty", "ruling", "judge",
    "legal", "law", "attorney", "enforcement",
]


def is_relevant(title: str, summary: str) -> tuple[bool, str]:
    """Devuelve (es_relevante, categoría)"""
    text = (title + " " + summary).lower()

    has_ai = any(kw in text for kw in AI_KEYWORDS)
    if not has_ai:
        return False, ""

    has_ma = any(kw in text for kw in MA_KEYWORDS)
    has_legal = any(kw in text for kw in LEGAL_KEYWORDS)

    if has_ma:
        return True, "M&A"
    if has_legal:
        return True, "Legal & Regulación"
    return False, ""
