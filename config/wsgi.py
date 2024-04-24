# Import required libraries
import os
from django.core.wsgi import get_wsgi_application

# Set the base directory of the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Get the WSGI application object
application = get_wsgi_application()