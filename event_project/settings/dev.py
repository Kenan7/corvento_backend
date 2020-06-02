from .base import *

DEBUG = True

ALLOWED_HOSTS += ['*']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

LOG_LOCATION = BASE_DIR / 'logs' / 'test.log'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_LOCATION,
        },
    },
    'loggers': {
        'app_user.models': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },

    },
}
