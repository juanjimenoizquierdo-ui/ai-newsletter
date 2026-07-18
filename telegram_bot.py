"""
telegram_bot.py — Bot de Telegram que genera posts de LinkedIn a partir de noticias.

Pega el texto o titular de cualquier noticia → devuelve un post de LinkedIn listo.
"""

import os
import logging
from anthropic import Anthropic
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Anthropic()


def generate_linkedin_post(text: str) -> str:
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=700,
        messages=[{
            "role": "user",
            "content": f"""Eres Juan Jimeno Izquierdo, abogado español especializado en regulación europea, inteligencia artificial y M&A.
Escribe un post de LinkedIn en español (200-280 palabras) sobre esta noticia para potenciar tu perfil profesional.

El post debe:
- Comenzar con un gancho directo e impactante (evita frases genéricas como "Acabo de leer" o "Interesante artículo")
- Explicar la relevancia práctica para profesionales del derecho, compliance o M&A en Europa
- Incluir tu análisis u opinión personal con criterio jurídico
- Terminar con una pregunta o reflexión que invite al debate
- Incluir 5-6 hashtags relevantes al final (#AIAct #Compliance #LegalTech #RegulacionEuropea #GDPR etc.)
- Tono: profesional, directo y con autoridad, sin ser pedante

Noticia:
{text}

Responde SOLO con el texto del post, listo para copiar y pegar en LinkedIn."""
        }]
    )
    return message.content[0].text.strip()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola Juan. Pégame el texto o titular de cualquier noticia y te genero el post de LinkedIn."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if not text:
        return

    await update.message.reply_text("Generando post de LinkedIn...")

    try:
        post = generate_linkedin_post(text)
        await update.message.reply_text(post)
    except Exception as e:
        logger.error(f"Error generando post: {e}")
        await update.message.reply_text("Error al generar el post. Inténtalo de nuevo.")


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN no está configurada")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot iniciado.")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
