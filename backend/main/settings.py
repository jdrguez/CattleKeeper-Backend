from pathlib import Path
from prettyconf import config
import os
import dj_database_url
from urllib.parse import urlparse

# Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = config('SECRET_KEY', default='insecure-dev-key')
DEBUG = config('DEBUG', cast=bool, default=False)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

# Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'shared.apps.SharedConfig',
    'accounts.apps.AccountsConfig',
    'farm.apps.FarmConfig',
    'stats.apps.StatsConfig',
    'subscription.apps.SubscriptionConfig',
    'colorfield',
    'django_rq',
]

# Middleware
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

# CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'accept',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
CORS_EXPOSE_HEADERS = ['Authorization']

# URLs y WSGI
ROOT_URLCONF = 'main.urls'
WSGI_APPLICATION = 'main.wsgi.application'

# Templates
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

# Base de datos desde DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='postgres://postgres:postgres@localhost:5432/postgres'),
        conn_max_age=600
    )
}

# Configuración de Redis para django-rq
redis_url = config('REDIS_URL', default='redis://localhost:6379/0')

host = config('REDISHOST')
port = config('REDISPASSWORD')
db = config('REDISUSER')
password = config('REDISPORT')

RQ_QUEUES = {
    'default': {
        'HOST': host,
        'PORT': port,
        'DB': db,
        'PASSWORD': password,
    },
    'high': {
        'HOST': host,
        'PORT': port,
        'DB': db,
        'PASSWORD': password,
    },
    'low': {
        'HOST': host,
        'PORT': port,
        'DB': db,
        'PASSWORD': password,
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos y media
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Archivos por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
