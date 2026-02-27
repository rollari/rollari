"""
ASGI config for rollari project.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rollari.settings.production')

application = get_asgi_application()
