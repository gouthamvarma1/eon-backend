"""
Django settings for eon_backend project.

Generated by 'django-admin startproject' using Django 1.11.26.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from utils.constants import APPLICATION_CONSTANTS, SMS_CONFIG, EMAIL_CONFIG, NOTIFICATION_CONFIG

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['dev-env-bits-pilani-backend.us-east-1.elasticbeanstalk.com','BitsPilaniEonBackend-env.eba-iewfgdnb.us-east-1.elasticbeanstalk.com',
                 'localhost', '127.0.0.1', '[::1]']

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_nose',

    # Installed Apps
    'core',
    'daterangefilter',
    'authentication',
    'rest_framework',
    'payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eon_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'eon_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USERNAME"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOSTNAME"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# USer Model
AUTH_USER_MODEL = 'authentication.User'

CORS_ORIGIN_ALLOW_ALL = True

GRAPPELLI_ADMIN_TITLE = "BITS EOn"

# Simple-JWT Authentication
# https://pypi.org/project/djangorestframework-simplejwt/

ACCESS_TOKEN_LIFETIME = os.environ.get("ACCESS_TOKEN_LIFETIME", 1)
REFRESH_TOKEN_LIFETIME = os.environ.get("REFRESH_TOKEN_LIFETIME", 2)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=int(ACCESS_TOKEN_LIFETIME)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(REFRESH_TOKEN_LIFETIME)),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# constant
APP_CONSTANTS = APPLICATION_CONSTANTS


# configs for sms and email and notification
SMS_CONFIG = SMS_CONFIG

EMAIL_CONFIG = EMAIL_CONFIG

NOTIFICATION_CONFIG = NOTIFICATION_CONFIG


EVENT_URL = "http://d10crzu2ups2gn.cloudfront.net/event-details?id="

# rest framework
REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "utils.exception_handler.api_exception_handler",
}

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=authentication,core,payment',
]



