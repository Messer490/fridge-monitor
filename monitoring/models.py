from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Fridge(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='fridges')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    temperature_min = models.FloatField()
    temperature_max = models.FloatField()
    current_temperature = models.FloatField(default=5.0)  # начальное значение
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(blank=True, null=True)
    office_number = models.CharField(max_length=50, blank=True, null=True)
    floor = models.CharField(max_length=50, blank=True, null=True)
    entrance = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.store.name})"


class TemperatureReading(models.Model):
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, related_name='readings')
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fridge.name}: {self.value}°C at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class Notification(models.Model):
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}] {self.message}"