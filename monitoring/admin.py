from django.contrib import admin
from .models import Store, Fridge
from .models import TemperatureReading
from .models import Notification

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'latitude', 'longitude']

@admin.register(Fridge)
class FridgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'store', 'temperature_min', 'temperature_max', 'current_temperature', 'last_updated']
    list_filter = ['store']

@admin.register(TemperatureReading)
class TemperatureReadingAdmin(admin.ModelAdmin):
    list_display = ['fridge', 'value', 'timestamp']
    list_filter = ['fridge', 'timestamp']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['fridge', 'message', 'created_at', 'is_resolved']
    list_filter = ['is_resolved', 'created_at', 'fridge']

admin.site.site_header = "FridgeMonitor Admin Панель"
admin.site.index_title = "Администрирование сайта"
admin.site.site_title = "FridgeMonitor"