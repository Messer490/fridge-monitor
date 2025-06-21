# simulate.py
import requests
import time
import random

RENDER_URL = "https://fridge-monitor-2zfl.onrender.com/api/temperature/"
FRIDGE_IDS = [1, 2]  # ID холодильников

while True:
    for fridge_id in FRIDGE_IDS:
        temperature = round(random.uniform(0.0, 10.0), 1)
        data = {
            "fridge_id": fridge_id,
            "value": temperature
        }
        try:
            response = requests.post(RENDER_URL, data=data)
            print(f"[{time.strftime('%H:%M:%S')}] Холодильник {fridge_id} | Темп: {temperature}°C | Статус: {response.status_code}")
        except Exception as e:
            print(f"❌ Ошибка для холодильника {fridge_id}: {e}")

    time.sleep(30)  # 30 секунд между циклами
    