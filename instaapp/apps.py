from django.apps import AppConfig


class InstaappConfig(AppConfig):
    name = 'instaapp'

    def ready(self):
        import instaapp.models
