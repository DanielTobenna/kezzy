from django.apps import AppConfig


class FinbaappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finbaapp'

    def ready(self):
    	import finbaapp.signals
