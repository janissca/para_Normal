from django.apps import AppConfig


class EventsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventsapp'

    def ready(self):
        import eventsapp.signals
