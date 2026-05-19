
from decouple import config

import os
from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG',cast=bool)

ALLOWED_HOSTS = []


# INSTALLED APPS

INSTALLED_APPS = [
    
    'django_prometheus',

    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'notes',
]


# MIDDLEWARE

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]


# ROOT URL

ROOT_URLCONF = 'smartnotes.urls'


# TEMPLATES

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI

WSGI_APPLICATION = 'smartnotes.wsgi.application'


# DATABASE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# PASSWORD VALIDATION

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


# LANGUAGE

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# STATIC FILES

STATIC_URL = 'static/'


# LOGIN SETTINGS

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/login/'


# REST FRAMEWORK

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),

}
import os

LOGGING = {

    'version': 1,

    'disable_existing_loggers': False,

    'formatters': {

        'standard': {

            'format':
                '[{asctime}] {levelname} {message}',

            'style': '{',
        },
    },

    'handlers': {

        'file': {

            'level': 'INFO',

            'class':
                'logging.FileHandler',

            'filename': os.path.join(
                BASE_DIR,
                'debug.log'
            ),

            'formatter':
                'standard',
        },
    },

    'loggers': {

        'notes': {

            'handlers': ['file'],

            'level': 'INFO',

            'propagate': False,
        },
    },
}
# CORS
SIMPLE_JWT = {

    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),

    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
}

# settings.py

# Ensure these are exactly like this for development
ALLOWED_HOSTS = ['*'] 

CORS_ALLOW_ALL_ORIGINS = True  # Keep this True for dev

# Add the specific port Flutter usually runs on (often 5000-60000 range)
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://10.0.2.2:8000", 
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
