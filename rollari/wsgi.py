"""
WSGI config for rollari project.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rollari.settings.production')

application = get_wsgi_application()
