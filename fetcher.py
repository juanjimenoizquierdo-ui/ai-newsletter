import feedparser
import time
from datetime import datetime, timezone, timedelta
from sources import RSS_FEEDS, is_relevant


def fetch_articles(hours_back: int = 24) -> dict[str, list[dict]]:
    """Obtiene artículos relevantes de las últimas N horas, agrupados por categoría."""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours_back)
    categories: dict[str, list[dict]] = {"M&A": [], "Legal & Regulación": []}

    for feed_info in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_info["url"])
            for entry in feed.entries:
                pub_date = _parse_date(entry)
                if pub_date and pub_date < cutoff:
                    continue

                title = entry.get("title", "")
                summary = entry.get("summary", "") or entry.get("description", "")
                link = entry.get("link", "")

                relevant, category = is_relevant(title, summary)
                if not relevant:
                    continue

                # Evitar duplicados por título similar
                existing_titles = [a["title"].lower() for a in categories[category]]
                if title.lower() in existing_titles:
                    continue

                categories[category].append({
                    "title": title,
                    "summary": _clean_summary(summary),
                    "link": link,
                    "source": feed_info["name"],
                    "date": pub_date,
                })
        except Exception as e:
            print(f"Error fetching {feed_info['name']}: {e}")
            continue

    # Ordenar por fecha descendente
    for cat in categories:
        categories[cat].sort(key=lambda x: x["date"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
        categories[cat] = categories[cat][:10]  # máximo 10 por categoría

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


def _clean_summary(text: str) -> str:
    """Elimina HTML básico y recorta el resumen."""
    import re
    text = re.sub(r"<[^>]+>", "", text)
    text = text.strip()
    if len(text) > 300:
        text = text[:297] + "..."
    return text
