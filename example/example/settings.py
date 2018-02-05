import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6y2zkef)uj^faksclkua!7(nz!9&@p%0vh-95a&erenm82=i)s'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'example',
]

MIDDLEWARE = [
]

ROOT_URLCONF = 'example.urls'

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django_cheetahtemplate.DjangoCheetahTemplate',
        'DIRS': [
        ],
        'OPTIONS': {
        },
    },
]

WSGI_APPLICATION = 'example.wsgi.application'

DATABASES = {
}

AUTH_PASSWORD_VALIDATORS = [
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
