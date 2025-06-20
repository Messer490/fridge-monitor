# Generated by Django 5.2.3 on 2025-06-19 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('fridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='monitoring.fridge')),
            ],
        ),
    ]
