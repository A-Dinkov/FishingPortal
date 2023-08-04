from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FishingPortal.auth_app'


class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FishingPortal.auth_app'

    def ready(self):
        import FishingPortal.auth_app.signals
