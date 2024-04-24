# Import required libraries
import os

# Define the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the secret key for the application
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')

# Define the debug mode for the application
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Define the allowed hosts for the application
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Define the database setstings for the application
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Define the logging settings for the application
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}