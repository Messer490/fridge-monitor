import os
import requests

def send_telegram_message(message: str, chat_id=None, bot_token=None):
    chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
    bot_token = bot_token or os.getenv("TELEGRAM_BOT_TOKEN")

    if not bot_token or not chat_id:
        print("⚠️ Telegram config missing")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print("✅ Telegram message sent")
    except Exception as e:
        print(f"Telegram error: {e}")
