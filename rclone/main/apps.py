from django.apps import AppConfig
from actstream import registry
from django.contrib.auth.models import User

class MyAppConfig(AppConfig):
    name = 'main'

    def ready(self):
        registry.register(User,self.get_model('Category'))
