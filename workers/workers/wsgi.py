"""
WSGI config for workers project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workers.settings')

application = get_wsgi_application()
