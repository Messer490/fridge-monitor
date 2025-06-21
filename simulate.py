# simulate.py
import requests
import time
import random

RENDER_URL = "https://fridge-monitor-2zfl.onrender.com/api/temperature/"
FRIDGE_ID = 1

while True:
    temperature = round(random.uniform(2.0, 8.0), 1)
    data = {
        "fridge_id": FRIDGE_ID,
        "value": temperature
    }
    try:
        response = requests.post(RENDER_URL, data=data)
        print(f"[{time.strftime('%H:%M:%S')}] Отправлено: {temperature}°C | Ответ: {response.status_code}")
    except Exception as e:
        print("❌ Ошибка:", e)

    time.sleep(30)
