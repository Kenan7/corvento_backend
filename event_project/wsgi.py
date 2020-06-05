"""
WSGI config for event_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

OS_BASE_DIR = os.path.dirname(os.path.dirname(__file__))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_project.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(OS_BASE_DIR, 'static'))
