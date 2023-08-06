from django.apps import AppConfig


class BusinessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FishingPortal.business'


def ready(self):
    import FishingPortal.business.signals
