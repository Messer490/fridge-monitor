from django.apps import AppConfig

class MonitoringConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitoring'

    def ready(self):
        import os
        if os.environ.get('RUN_MAIN', None) != 'true':
            return
        from apscheduler.schedulers.background import BackgroundScheduler
        from monitoring.tasks import generate_temperatures

        scheduler = BackgroundScheduler()
        scheduler.add_job(generate_temperatures, 'interval', seconds=30)
        scheduler.start()
