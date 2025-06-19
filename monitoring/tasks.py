from apscheduler.schedulers.background import BackgroundScheduler
from monitoring.models import Fridge, TemperatureReading, Notification
from django.utils import timezone
from django.conf import settings
from monitoring.telegram import send_telegram_message
import random

def generate_temperatures():
    for fridge in Fridge.objects.all():
        value = round(random.uniform(fridge.temperature_min - 2, fridge.temperature_max + 2), 1)
        TemperatureReading.objects.create(fridge=fridge, value=value)
        fridge.current_temperature = value
        fridge.save()

        if value < fridge.temperature_min or value > fridge.temperature_max:
            msg = f"⚠️ {fridge.name}: {value}°C (норма {fridge.temperature_min}–{fridge.temperature_max})"
            Notification.objects.create(fridge=fridge, message=msg)
            send_telegram_message(msg, settings.TELEGRAM_CHAT_ID, settings.TELEGRAM_BOT_TOKEN)
