from firebase_functions import https_fn
from firebase_admin import initialize_app
import os
import sys

# Add Django project to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

# Initialize Firebase
initialize_app()

# Import Django WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gesture.settings')

from django.core.wsgi import get_wsgi_application
django_app = get_wsgi_application()

@https_fn.on_request()
def app(req):
    """Firebase function to serve Django app"""
    return django_app(req.environ, lambda status, headers: None)