from django.apps import AppConfig


class OutsourceapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'outsourceAPI'

    def ready(self):
        import outsourceAPI.signals
