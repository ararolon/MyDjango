"""
WSGI config for DjangoPrueba project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# cambiamos la ruta de settings y agregamos que busque el entorno de desarrollo
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoPrueba.settings.development')

application = get_wsgi_application()
