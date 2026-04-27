import re
import time
import feedparser
import trafilatura
from datetime import datetime, timezone, timedelta
from groq import Groq
import os

from sources import RSS_FEEDS, CATEGORIES, classify_article


_groq_client = None


def _get_groq_client() -> Groq | None:
    global _groq_client
    if _groq_client is None:
        api_key = os.environ.get("GROQ_API_KEY", "").strip()
        if api_key:
            _groq_client = Groq(api_key=api_key)
        else:
            print("ADVERTENCIA: GROQ_API_KEY no configurada. Se usarán resúmenes RSS sin enriquecer.")
    return _groq_client


def _fetch_full_text(url: str) -> str:
    """Extrae el texto completo del artículo con trafilatura."""
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            text = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
            if text:
                return text[:3000]
    except Exception:
        pass
    return ""


def _enrich_with_groq(title: str, content: str, category: str) -> str:
    """Genera un resumen analítico en español usando Groq."""
    client = _get_groq_client()
    if not client or not content:
        return content[:400] if content else title

    category_context = {
        "Enforcement Decisions": "regulación y enforcement europeo. Destaca: autoridad que actúa, infractor, importe de multa o medida impuesta, base legal invocada y precedente que sienta",
        "AI Law & Regulation": "regulación de inteligencia artificial (AI Act, gobernanza IA). Destaca: obligaciones concretas, plazos, autoridades implicadas y sectores afectados",
        "Privacy & GDPR Enforcement": "privacidad y enforcement GDPR. Destaca: autoridad de control, base legal, derechos afectados, importe de sanción si aplica y criterio interpretativo",
        "Fintech & DORA": "regulación fintech y resiliencia operativa digital (DORA, EBA, ESMA, PSD). Destaca: entidades supervisadas, obligaciones nuevas, plazos de cumplimiento",
        "Legal Tech": "tecnología aplicada al derecho. Destaca: herramienta o empresa, funcionalidad, mercado objetivo (Europa) e implicaciones para despachos o equipos legales",
        "M&A España": "fusiones y adquisiciones en España. Destaca: partes, valoración, estructura del deal, sector y ángulo regulatorio si lo hay",
        "Regulación Europea General": "legislación y política regulatoria europea. Destaca: norma, institución impulsora, estado de tramitación y obligaciones principales",
        "IA General": "inteligencia artificial con implicación regulatoria o legal. Destaca: modelo o empresa, capacidad relevante y por qué importa desde un ángulo legal o de compliance",
    }
    focus = category_context.get(category, f"análisis experto en {category}")

    prompt = f"""Eres un analista jurídico especializado en regulación europea y M&A.
Escribe un resumen en español (3-5 líneas) sobre esta noticia enfocado en: {focus}.
Incluye cifras clave, partes involucradas y contexto relevante cuando estén disponibles.
Si el artículo está en inglés, responde en español igualmente.
Responde SOLO con el resumen, sin introducción ni etiquetas.

Título: {title}
Contenido: {content[:2500]}"""

    try:
        response = _get_groq_client().chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=350,
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"  Groq error ({title[:40]}): {e}")
        return content[:400]


def fetch_articles(hours_back: int = 168) -> dict[str, list[dict]]:
    """Obtiene artículos de las últimas N horas, los clasifica y enriquece con IA."""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours_back)
    categories: dict[str, list[dict]] = {cat: [] for cat in CATEGORIES}
    seen_titles: set[str] = set()

    for feed_info in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_info["url"])
            for entry in feed.entries:
                pub_date = _parse_date(entry)
                if pub_date and pub_date < cutoff:
                    continue

                title = entry.get("title", "").strip()
                summary = entry.get("summary", "") or entry.get("description", "")
                link = entry.get("link", "")

                if not title or title.lower() in seen_titles:
                    continue

                category = classify_article(title, summary)
                if not category:
                    continue

                seen_titles.add(title.lower())

                # Extraer texto completo
                full_text = _fetch_full_text(link)
                content = full_text or _clean_text(summary)

                # Enriquecer con Groq
                print(f"  [{category}] {title[:60]}...")
                enriched = _enrich_with_groq(title, content, category)
                time.sleep(2)  # Respetar rate limit de Groq (30 RPM)

                categories[category].append({
                    "title": title,
                    "summary": enriched,
                    "link": link,
                    "source": feed_info["name"],
                    "date": pub_date,
                })
        except Exception as e:
            print(f"Error fetching {feed_info['name']}: {e}")
            continue

    # Ordenar por fecha y limitar a 8 por categoría
    for cat in categories:
        categories[cat].sort(
            key=lambda x: x["date"] or datetime.min.replace(tzinfo=timezone.utc),
            reverse=True,
        )
        categories[cat] = categories[cat][:8]

    return categories


def _parse_date(entry) -> datetime | None:
    for field in ("published_parsed", "updated_parsed"):
        parsed = getattr(entry, field, None)
        if parsed:
            try:
                return datetime(*parsed[:6], tzinfo=timezone.utc)
            except Exception:
                pass
    return None


def _clean_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()[:500]
