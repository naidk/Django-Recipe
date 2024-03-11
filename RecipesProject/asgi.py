

import os

from django.core.asgi import get_asgi_application
# Set the settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RecipesProject.settings')
# Expose the ASGI application for use with ASGI servers
application = get_asgi_application()


