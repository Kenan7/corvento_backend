from .parse_secret_json import *
from pathlib import Path


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
    'allauth',
    'allauth.account',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'rest_framework_swagger',
]

BASE = [
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
# STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_URL = '/static/'


DEBUG = True
ALLOWED_HOSTS = ['corvento.com', '18.156.183.172', '127.0.0.1']

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
        'DIRS': [],
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
