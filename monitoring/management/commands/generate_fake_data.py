from django.core.management.base import BaseCommand
from monitoring.models import Fridge, TemperatureReading, Notification
import random
from django.conf import settings
from monitoring.telegram import send_telegram_message

class Command(BaseCommand):
    help = 'Генерирует фейковые температурные данные и проверяет на превышения'

    def handle(self, *args, **kwargs):
        fridges = Fridge.objects.all()
        for fridge in fridges:
            value = round(random.uniform(fridge.temperature_min - 2, fridge.temperature_max + 2), 1)
            TemperatureReading.objects.create(fridge=fridge, value=value)
            fridge.current_temperature = value
            fridge.save()

            # проверка нарушений
            if value < fridge.temperature_min or value > fridge.temperature_max:
                message = f"⚠️ Нарушение! {fridge.name} ({fridge.store.name}) — {value}°C (норма: {fridge.temperature_min}–{fridge.temperature_max})"
                Notification.objects.create(fridge=fridge, message=message)
                send_telegram_message(
                    message,
                    chat_id=settings.TELEGRAM_CHAT_ID,
                    bot_token=settings.TELEGRAM_BOT_TOKEN
                )
            else:
                self.stdout.write(self.style.SUCCESS(f"{fridge.name}: {value}°C"))
