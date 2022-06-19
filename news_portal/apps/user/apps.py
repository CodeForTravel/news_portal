from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'news_portal.apps.user'

    def ready(self):
        import news_portal.apps.user.signals
