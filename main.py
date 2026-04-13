from fetcher import fetch_articles
from formatter import build_html
from sender import send_newsletter


def main():
    print("Obteniendo noticias (últimos 7 días)...")
    categories = fetch_articles(hours_back=168)

    total = sum(len(v) for v in categories.values())
    for cat, articles in categories.items():
        if articles:
            print(f"  {cat}: {len(articles)} artículos")
    print(f"Total: {total} artículos")

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
