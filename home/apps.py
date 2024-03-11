# from django.apps import AppConfig
#
#
# class HomeConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'home'

from django.apps import AppConfig


class CustomHomeConfig(AppConfig):
    # Define the custom auto field
    custom_auto_field = 'django.db.models.BigAutoField'

    # Define the name of the app
    name = 'home'