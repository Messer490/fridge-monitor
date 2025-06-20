# Generated by Django 5.2.3 on 2025-06-19 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_temperaturereading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('fridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='monitoring.fridge')),
            ],
        ),
    ]
