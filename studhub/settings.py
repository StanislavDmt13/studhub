"""
Django settings for studhub project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7w8mj7=9$(2@htliyug3(nhcvrndbzya2-uhm=aqv#xfq%i&pr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'minio_storage',
    'django_extensions',
    'oauth2_provider',
    'rest_framework',
    'backend.account',
    'backend.institute',
    'backend.product',
    'mptt',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'studhub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'studhub.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "d5gdb3a5j0r2k",
        "HOST": "ec2-52-31-94-195.eu-west-1.compute.amazonaws.com",
        "POST": "5432",
        "USER": "xfkictigpaezhs",
        "PASSWORD": "8bd1a3bcc2e3344ecc86b8f048c32c984ffec21eed36a52e3d4ed37c61fa3e67"
    }
}

AUTH_USER_MODEL = 'account.User'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR / "frontend/static/")

# Redirect urls

LOGIN_URL = 'admin:login'
LOGOUT_URL = 'admin:logout'

LOGIN_REDIRECT_URL = 'admin:login'
LOGOUT_REDIRECT_URL = 'admin:login'

# Rest Framework settings

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'backend.pagination.SimplePagePagination',
    'PAGE_SIZE': 100,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S'
}

# Swagger settings
# Redirect url {host}/{static}/drf-yasg/swagger-ui-dist/oauth2-redirect.html

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'OAuth2': {
            'type': 'oauth2',
            'authorizationUrl': '/o/authorize/',
            'tokenUrl': '/o/token/',
            'flow': 'accessCode'
        }
    }
}

# Logging settings

if not os.path.exists("logs"):
    os.makedirs("logs")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
            "fmt": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
        },
    },
    "handlers": {
        "null": {"level": "DEBUG", "class": "django.utils.log.AdminEmailHandler"},
        "logfile": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/logfile.txt"),
            "maxBytes": 50000,
            "backupCount": 2,
            "formatter": "standard",
        },
        "console": {"level": "INFO", "class": "logging.StreamHandler", "formatter": "standard"},
        "dev_console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "standard"}
    },
    "loggers": {
        "django": {"handlers": ["console"], "propagate": True, "level": "WARN"},
        "django.db.backends": {"handlers": ["console", "dev_console"], "level": "DEBUG", "propagate": False},
        "backend": {"handlers": ["console", "dev_console"], "level": "DEBUG"},
        "backend.account": {"handlers": ["console", "dev_console"], "level": "DEBUG"},
        "backend.institute": {"handlers": ["console", "dev_console"], "level": "DEBUG"},
        "backend.product": {"handlers": ["console", "dev_console"], "level": "DEBUG"},
    },
}

# Minio Storage Settings

# DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
# STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
# MINIO_STORAGE_ENDPOINT = 'localhost:8000'
# MINIO_STORAGE_ACCESS_KEY = 'KBP6WXGPS387090EZMG8'
# MINIO_STORAGE_SECRET_KEY = 'DRjFXylyfMqn2zilAr33xORhaYz5r9e8r37XPz3A'
# MINIO_STORAGE_USE_HTTPS = False
# MINIO_STORAGE_MEDIA_BUCKET_NAME = 'media'
# MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
# MINIO_STORAGE_STATIC_BUCKET_NAME = 'static'
# MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True
