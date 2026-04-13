import os
import resend
from datetime import datetime


def send_newsletter(html: str) -> bool:
    api_key = os.environ.get("RESEND_API_KEY", "").strip()
    if not api_key:
        raise ValueError("RESEND_API_KEY no está configurada")
    if not api_key.startswith("re_"):
        print(f"ADVERTENCIA: El API key no empieza por 're_' — puede ser inválido. Primeros chars: '{api_key[:6]}...'")

    resend.api_key = api_key

    today = datetime.now().strftime("%d/%m/%Y")
    from_email = os.environ.get("FROM_EMAIL", "onboarding@resend.dev")
    to_email = os.environ.get("TO_EMAIL", "juanjimenocontact@gmail.com")

    try:
        params: resend.Emails.SendParams = {
            "from": f"AI Brief <{from_email}>",
            "to": [to_email],
            "subject": f"AI Brief — {today}",
            "html": html,
        }
        response = resend.Emails.send(params)
        print(f"Email enviado. ID: {response['id']}")
        return True
    except Exception as e:
        print(f"Error enviando email: {e}")
        return False
