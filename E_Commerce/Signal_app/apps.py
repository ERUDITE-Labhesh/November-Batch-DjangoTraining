from django.apps import AppConfig


class SignalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Signal_app'

    def ready(self):
        from . import signal