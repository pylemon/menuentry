"""
WSGI config for menuentry project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys


_DIRNAME = os.path.dirname(globals()["__file__"])
sys.path.append( os.path.join(_DIRNAME, '..') )

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "menuentry.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
