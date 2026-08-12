import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://api.open-meteo.com/v1/forecast?latitude=49.11&longitude=16.36&current=temperature_2m"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pocasi = data["current"]["temperature_2m"]

    text = f"""Aktuální počasí Brno:\n{pocasi} stupňů
"""

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": text
        }
    )
else:
    print("Nepodařilo se načíst počasí.")

application = Application.builder().token(TOKEN).build()

application.add_handler(CommandHandler("pocasi", pocasi))

application.run_polling()
