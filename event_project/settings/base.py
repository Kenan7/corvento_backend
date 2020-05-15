from .parse_secret_json import *
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

BASE_DIR = Path(__file__).resolve().parent.parent.parent


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
    '18.156.183.172',
    '127.0.0.1',
    # '192.168.248.123'
]
# ALLOWED_HOSTS = ['*']

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
