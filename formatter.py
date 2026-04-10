from datetime import datetime


def build_html(categories: dict[str, list[dict]]) -> str:
    today = datetime.now().strftime("%d de %B de %Y")
    total = sum(len(v) for v in categories.values())

    if total == 0:
        return _no_news_html(today)

    sections_html = ""
    for category, articles in categories.items():
        if not articles:
            continue
        sections_html += _section_html(category, articles)

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Brief — {today}</title>
</head>
<body style="margin:0;padding:0;background:#f4f4f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f5;padding:32px 0;">
    <tr>
      <td align="center">
        <table width="620" cellpadding="0" cellspacing="0" style="max-width:620px;width:100%;">

          <!-- Header -->
          <tr>
            <td style="background:#0f0f0f;border-radius:12px 12px 0 0;padding:32px 40px;">
              <p style="margin:0;color:#888;font-size:12px;letter-spacing:2px;text-transform:uppercase;">Daily Brief</p>
              <h1 style="margin:8px 0 0;color:#ffffff;font-size:28px;font-weight:700;letter-spacing:-0.5px;">AI & Law</h1>
              <p style="margin:8px 0 0;color:#666;font-size:13px;">{today}</p>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td style="background:#ffffff;padding:32px 40px;">
              {sections_html}
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background:#f4f4f5;border-radius:0 0 12px 12px;padding:24px 40px;text-align:center;">
              <p style="margin:0;color:#aaa;font-size:11px;">
                Newsletter automático · Fuentes: RSS públicas
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""


def _section_html(category: str, articles: list[dict]) -> str:
    icon = "🤝" if category == "M&A & Mercantil" else "⚖️"
    items_html = "".join(_article_html(a) for a in articles)

    return f"""
      <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:32px;">
        <tr>
          <td>
            <p style="margin:0 0 16px;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#888;">
              {icon} {category}
            </p>
            {items_html}
          </td>
        </tr>
      </table>
    """


def _article_html(article: dict) -> str:
    date_str = ""
    if article.get("date"):
        date_str = article["date"].strftime("%d %b").lstrip("0")

    summary_block = ""
    if article.get("summary"):
        summary_block = f'<p style="margin:6px 0 0;color:#555;font-size:13px;line-height:1.5;">{article["summary"]}</p>'

    return f"""
    <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:20px;border-left:3px solid #e5e7eb;padding-left:16px;">
      <tr>
        <td>
          <a href="{article['link']}" style="text-decoration:none;">
            <p style="margin:0;font-size:15px;font-weight:600;color:#0f0f0f;line-height:1.4;">{article['title']}</p>
          </a>
          {summary_block}
          <p style="margin:8px 0 0;font-size:11px;color:#aaa;">
            {article['source']}{' · ' + date_str if date_str else ''}
          </p>
        </td>
      </tr>
    </table>
    """


def _no_news_html(today: str) -> str:
    return f"""<!DOCTYPE html>
<html><body style="font-family:sans-serif;padding:40px;color:#555;">
  <h2>AI Brief — {today}</h2>
  <p>No se encontraron noticias relevantes en las últimas 24 horas.</p>
</body></html>"""
