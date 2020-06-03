from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
import os
from pathlib import Path

FCM_DJANGO_SETTINGS = {
    "APP_VERBOSE_NAME": "Firebase Cloud Messaging",
    # default: _('FCM Django')
    "FCM_SERVER_KEY": "AAAAU4MYVPc:APA91bFARn1V_sXyhr7Y8GkxfydM_32jvcFJjR0pt6tGxLfhVm10ImIw3S1VoG0eKELf3CcTsxP_ihhn_4V6zGL9YZZQGba2qgx0cq79Gl5r1UXHPCIojmAw3dpPkqPLOQ0dM2GVYy0f",
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": True,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": False,
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}

LOCAL = [
    'main.apps.MainConfig',
    'app_user.apps.AppUserConfig',
    'sheets_api.apps.SheetsApiConfig',
]

THIRD_PARTY = [
    'rest_framework',
    'versatileimagefield',
    'django_filters',
    'rest_framework_swagger',
    'fcm_django',
    'tinymce',
]

BASE = [
    'postgres_metrics.apps.PostgresMetrics',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

INSTALLED_APPS = BASE + LOCAL + THIRD_PARTY

BASE_DIR = Path(__file__).resolve().parent.parent


MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / 'static'
# STATICFILES_DIRS = [BASE_DIR / 'staticfiles']
STATIC_URL = '/static/'
# HOME_TEMPLATE = BASE_DIR / 'templates' / 'main'
HOME_TEMPLATE = BASE_DIR / 'templates'
STATICFILES_DIRS = [BASE_DIR / 'staticfiles']

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

DEBUG = True
ALLOWED_HOSTS = [
    'corvento.com',
    'www.corvento.com',
    '127.0.0.1',
]

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'

}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'none'
        }
    },
}


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "postgres"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "postgres"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


SECRET_KEY = os.environ.get("SECRET_KEY", "foo")
DEBUG = int(os.environ.get("DEBUG", default=0))


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'event_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [HOME_TEMPLATE],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'event_project.wsgi.application'


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

if DEBUG:
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

else:
    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_URL"),
        integrations=[DjangoIntegration()],

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )

    LOG_LOCATION = BASE_DIR / 'logs' / 'test.log'
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': LOG_LOCATION,
            },
        },
        'loggers': {
            'app_user.models': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },

        },
    }
