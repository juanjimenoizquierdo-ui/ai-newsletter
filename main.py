from fetcher import fetch_articles
from formatter import build_html
from sender import send_newsletter


def main():
    print("Obteniendo noticias...")
    categories = fetch_articles(hours_back=24)

    total = sum(len(v) for v in categories.values())
    print(f"Artículos encontrados: {total} (M&A: {len(categories['M&A & Mercantil'])}, Legal: {len(categories['Legal & Regulación IA'])})")

    print("Generando email...")
    html = build_html(categories)

    print("Enviando...")
    success = send_newsletter(html)

    if success:
        print("Newsletter enviada correctamente.")
    else:
        print("Error al enviar la newsletter.")
        exit(1)


if __name__ == "__main__":
    main()
