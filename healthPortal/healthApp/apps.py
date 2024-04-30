from django.apps import AppConfig


class HealthappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'healthApp'
    def ready(self):
        import healthApp.signals  # noqa
