"""
linkedin.py — Generador interactivo de posts de LinkedIn a partir de las noticias de la semana.

Uso:
    python linkedin.py

Requiere ANTHROPIC_API_KEY en el entorno (o en .env).
"""

import os
from anthropic import Anthropic
from fetcher import fetch_articles


def _load_env():
    """Carga .env si existe (para uso local sin Railway)."""
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ.setdefault(key.strip(), value.strip())


def generate_linkedin_post(article: dict, category: str) -> str:
    client = Anthropic()

    prompt = f"""Eres Juan Jimeno Izquierdo, abogado español especializado en regulación europea, inteligencia artificial y M&A.
Escribe un post de LinkedIn en español (200-280 palabras) sobre esta noticia para potenciar tu perfil profesional.

El post debe:
- Comenzar con un gancho directo e impactante (evita frases genéricas como "Acabo de leer" o "Interesante artículo")
- Explicar la relevancia práctica para profesionales del derecho, compliance o M&A en Europa
- Incluir tu análisis u opinión personal con criterio jurídico
- Terminar con una pregunta o reflexión que invite al debate
- Incluir 5-6 hashtags relevantes al final (#AIAct #Compliance #LegalTech #RegulacionEuropea #GDPR etc.)
- Tono: profesional, directo y con autoridad, sin ser pedante

Categoría de la noticia: {category}
Titular: {article['title']}
Contexto: {article['summary']}
Fuente: {article['source']}

Responde SOLO con el texto del post, listo para copiar y pegar en LinkedIn."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=700,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text.strip()


def main():
    _load_env()

    print("\nObteniendo noticias de los últimos 7 días...")
    categories = fetch_articles(hours_back=168)

    all_articles: list[tuple[str, dict]] = []
    for cat, articles in categories.items():
        for article in articles:
            all_articles.append((cat, article))

    if not all_articles:
        print("No se encontraron noticias esta semana.")
        return

    print(f"\n{'─' * 62}")
    print(f"  {len(all_articles)} noticias disponibles para LinkedIn")
    print(f"{'─' * 62}")

    current_cat = None
    for i, (cat, article) in enumerate(all_articles, 1):
        if cat != current_cat:
            print(f"\n  {cat}")
            current_cat = cat
        date_str = article["date"].strftime("%d %b") if article.get("date") else ""
        print(f"  [{i:2}] {article['title'][:72]}")
        print(f"       {article['source']}{' · ' + date_str if date_str else ''}")

    print()
    try:
        raw = input("Elige el número de la noticia (Enter para salir): ").strip()
        if not raw:
            return
        idx = int(raw) - 1
        if idx < 0 or idx >= len(all_articles):
            print("Número fuera de rango.")
            return
    except (ValueError, KeyboardInterrupt):
        print()
        return

    cat, article = all_articles[idx]
    print(f"\nGenerando post para:\n  [{cat}] {article['title']}\n")

    post = generate_linkedin_post(article, cat)

    print("=" * 62)
    print("  POST LINKEDIN — copia y pega en LinkedIn:")
    print("=" * 62)
    print()
    print(post)
    print()
    print("=" * 62)


if __name__ == "__main__":
    main()
