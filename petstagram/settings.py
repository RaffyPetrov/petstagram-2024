import os
from pathlib import Path

from django.template.context_processors import media

from petstagram.utils import is_production

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv('DEBUG', 'False') == 'True'
APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ()

PETSTAGRAM_APPS = (
    'petstagram.main',
    'petstagram.accounts',
)

# Application definition
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PETSTAGRAM_APPS


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'petstagram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'petstagram.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DEFAULT_DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'db.sqlite3',
}

if is_production():
    DEFAULT_DATABASE_CONFIG = {
                'ENGINE': 'django.db.backends.postgresql',
                'HOST': os.getenv('DB_HOST'),
                'PORT': os.getenv('DB_PORT', '5432'),
                'NAME': os.getenv('DB_NAME'),
                'USER': os.getenv('DB_USER'),
                'PASSWORD': os.getenv('DB_PASSWORD'),
            },

DATABASES = {
    'default': DEFAULT_DATABASE_CONFIG,
}


AUTH_PASSWORD_VALIDATORS = []

if is_production():

     AUTH_PASSWORD_VALIDATORS = [
             {
                 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
             },
             {
                 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
             },
             {
                 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
             },
             {
                 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
             },
     ]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIR = (
    BASE_DIR / 'static',
)

MEDIA_ROOT = BASE_DIR / 'mediafiles'
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING_LEVEL = 'DEBUG'

if is_production():
    LOGGING_LEVEL = 'INFO'

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': LOGGING_LEVEL,
            'filters': [],
            'class': 'logging.StreamHandler',

        }
    },
    'loggers': {
        'django.db.backends': {
            'level': LOGGING_LEVEL,
            'handlers': ['console'],
        }
    }
}

AUTH_USER_MODEL = 'accounts.PetstagramUser'
