"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p(uxa(5^psp7@%709mdco9cw)ab9=hx5!gshylcr!khow^5bhg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'simple': {
#             'format': '%{asctime}s %{levelname}s %{message}s',
#             'style': '{',
#         },
#         'formatWARNING': {
#             'format': '%{asctime}s %{levelname}s %{pathname}s %{message}s',
#             'style': '{',
#         },
#         'formatERROR': {
#             'format': '%{asctime}s %{levelname}s %{pathname}s %{exc_info}s %{message}s',
#             'style': '{',
#         },
#         'formatINFO': {
#             'format': '%{asctime}s %{levelname}s %{module}s %{message}s',
#             'style': '{',
#         },
#         'formatMail': {
#             'format': '%{asctime}s %{levelname}s %{pathname}s %{message}s',
#             'style': '{',
#         },
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'consoleWARNING': {
#             'level': 'WARNING',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'formatWARNING'
#         },
#         'consoleERROR': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'formatERROR'
#         },
#         'fileINFO': {
#             'level': 'INFO',
#             'filters': ['require_debug_false'],
#             'class': 'logging.FileHandler',
#             'formatter': 'formatINFO',
#             'filename': 'NewsPortal/logger/general.log'
#         },
#         'fileERROR': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.FileHandler',
#             'formatter': 'formatERROR',
#             'filename': 'NewsPortal/logger/errors.log'
#         },
#         'fileSecurity': {
#             'filters': ['require_debug_true'],
#             'class': 'logging.FileHandler',
#             'formatter': 'formatINFO',
#             'filename': 'NewsPortal/logger/security.log'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_false'],
#             'formatter': 'formatMail'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'consoleWARNING', 'consoleERROR'],
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['fileERROR', 'mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.server': {
#             'handlers': ['fileERROR'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.template': {
#             'handlers': ['fileERROR'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.db.backends': {
#             'handlers': ['fileERROR'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.security': {
#             'handlers': ['fileSecurity', 'mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#     }
# }


ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'News.apps.NewsConfig',
    'django_filters',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NewsPortal.urls'

LOCALE_PATH = [
    os.path.join(BASE_DIR, 'locale')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
        },
    },
]

LOGIN_URL = '/accounts/login/'
# 'sign/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}


AUTHENTICATION_BACKENDS = [
     # Needed to login by username in Django admin, regardless of `allauth`
     'django.contrib.auth.backends.ModelBackend',

     # `allauth` specific authentication methods, such as login by e-mail
     'allauth.account.auth_backends.AuthenticationBackend',
]

EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'artem.l.1987'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = 'ggkccuodojvepyki'  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно
ADMINS = [
    ('Artem', 'artem.l.1987@bk.ru'),
    # список всех админов в формате ('имя', 'их почта')
]
SERVER_EMAIL = 'artem.l.1987@yandex.ru'  # это будет у нас вместо аргумента FROM в массовой рассылке

DEFAULT_FROM_EMAIL = 'artem.l.1987@yandex.ru'

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

SITE_URL = 'http://127.0.0.1:8000'

CELERY_BROKER_URL = 'redis://artem.l.1987@yandex.com:JLq8TbO94h6jcGXW6lKaK4K9Hexy6Tt2@redis-14746.c52.us-east-1-4.ec2.cloud.redislabs.com:14746'
CELERY_RESULT_BACKEND = 'redis://artem.l.1987@yandex.com:JLq8TbO94h6jcGXW6lKaK4K9Hexy6Tt2@redis-14746.c52.us-east-1-4.ec2.cloud.redislabs.com:14746'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}