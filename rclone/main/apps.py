from django.apps import AppConfig
from actstream import registry

from django.contrib.auth import get_user_model

# User = get_user_model()

class MyAppConfig(AppConfig):
    name = 'main'

    def ready(self):
        registry.register(self.get_model('Category'))