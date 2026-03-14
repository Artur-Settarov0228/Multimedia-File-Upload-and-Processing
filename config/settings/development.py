from .base import *
import socket

# Development specific settings
DEBUG = True

# Show debug toolbar in development
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# Debug toolbar settings
INTERNAL_IPS = ['127.0.0.1']

# Get local IP for docker
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + '1' for ip in ips]

# File storage for development
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable password validators in development
AUTH_PASSWORD_VALIDATORS = []

# Logging
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
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}