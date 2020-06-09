from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
import os
from pathlib import Path
import json
import pprint
import logging

BASE_DIR = Path(__file__).resolve().parent.parent
logger = logging.getLogger(__name__)

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
    'django_extensions',
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


STATICFILES_DIRS = [BASE_DIR / 'staticfiles']
HOME_TEMPLATE = BASE_DIR / 'templates'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

ALLOWED_HOSTS = [
    'corvento.com',
    'www.corvento.com',
    '127.0.0.1',
    '172.26.0.2',
    '35.246.172.6',
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
        "ENGINE": os.environ.get("SQL_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", default=os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", default="postgres"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", default="postgres"),
        "HOST": os.environ.get("SQL_HOST", default="localhost"),
        "PORT": os.environ.get("SQL_PORT", default="5432"),
    }
}


SECRET_KEY = os.environ.get("SECRET_KEY", default="foo")
DEBUG = int(os.environ.get("DEBUG", default=0))


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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

# if not os.path.exists('logs'):
#     os.makedirs()
#     LOG_LOCATION = BASE_DIR / 'logs' / 'test.log'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'


DEFAULT_FILE_STORAGE = 'django_gcloud_storage.DjangoGCloudStorage'

# try:
#     GOOGLE_CLOUD_CREDENTIALS = BASE_DIR / \
#         os.environ.get('GOOGLE_APPLICATION_CREDENTIALS',
#                        'gcloud_storage_fcm_credentials.json')
# except:
#     logger.error(f'we can\'t get the credentials file')

try:
    GCS_CREDENTIALS_FILE_PATH = os.environ.get(
        'GOOGLE_APPLICATION_CREDENTIALS',
        default='gcloud_storage_fcm_credentials.json'
    )

    GCS_PROJECT = os.environ.get('project_id')
    GCS_BUCKET = os.environ.get('media_bucket')
    # GS_STATIC_BUCKET_NAME = os.environ.get('static_bucket')

    MEDIA_URL = f'https://storage.googleapis.com/{GCS_BUCKET}/'
    # STATIC_URL = f'https://storage.googleapis.com/{GS_STATIC_BUCKET_NAME}/'


except:
    logger.critical("Couldn't get media & static bucket variables from *env*")

# I will optimize this section
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
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            }
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': False,
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
            'console': {
                'level': 'ERROR',
                'class': 'logging.StreamHandler',
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': False,
            },

        },
    }
