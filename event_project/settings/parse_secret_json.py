from django.core.exceptions import ImproperlyConfigured
import json

with open('secrets.json') as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f'Set the {setting} environment variable'
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('POSTGRESQL_DB_NAME'),
        'USER': get_secret('POSTGRESQL_DB_USER'),
        'PASSWORD': get_secret('POSTGRESQL_DB_PASS'),
        'HOST': get_secret('POSTGRESQL_DB_HOST'),
        'PORT': get_secret('POSTGRESQL_DB_PORT'),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': str(BASE_DIR / 'db.sqlite3'),
#     }
# }


# AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = get_secret('AWS_STORAGE_BUCKET_NAME')

# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % get_secret(
#     'AWS_S3_CUSTOM_DOMAIN'
# )
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
