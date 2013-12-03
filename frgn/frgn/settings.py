# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import platform
# _PATH - путь к manage.py
_PATH = os.path.abspath(os.path.dirname(__file__) + '/../')
DEBUG = platform.node() != 'sancta'
TEMPLATE_DEBUG = DEBUG

# отправка на почту писем о поломанных ссылках


SERVER_EMAIL = 'robot@engdel.ru'
DEFAULT_FROM_EMAIL = SERVER_EMAIL
MANAGERS = (
    ('Ravall', 'valery.ravall@gmail.com'),
    ('Ksenia', 'ksenyam@yandex.ru')
)
ADMINS = (('Ravall', 'valery.ravall@gmail.com'),)

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'frgn',
            'USER': 'frgn_user',
            'PASSWORD': 'frgn_user_password',
            'HOST': '127.0.0.1',
            'PORT': '',
        }
    }
else:
    from production import DATABASES

API_URL = 'http://api.sancta.local' if not DEBUG else 'http://api.sancta.ru'

#DEBUG = False

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['engdel.ru', '127.0.0.1']


TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(_PATH, '../', 'files', 'media'))
DIRECTORY = os.path.abspath(
    os.path.join(_PATH, '../', 'files', 'upload')
)
STATIC_ROOT = os.path.abspath(
    os.path.join(_PATH, '../', 'files', 'collected_static')
)
STATIC_URL = '/static/'
STATICFILES_DIRS = (MEDIA_ROOT,)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'q++(wdjbc8r4a^uvt2no3(gy-#gw)b34xdfz2_4-#q$o-67%ao'


# шаблоны
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
   # 'django.template.loaders.app_directories.load_template_source'
)
TEMPLATE_DIRS = (
    os.path.join(_PATH, '../', 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages'
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware'
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

ROOT_URLCONF = 'frgn.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'frgn.wsgi.application'

CACHE_API_TIMEOUT = 60*60*24*3
CACHE_API_TIMEOUT_FAST = 60*1


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/home/var/cache/' if not DEBUG else '/tmp/'
    },
}

INSTALLED_APPS = (
    'frgn',
    'gunicorn',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.redirects',
    'south',
    'frontend',
    'djcompass',
    'raven.contrib.django.raven_compat',
    'robots_txt',
    'favicon',
    'django.contrib.sitemaps'
)

COMPASS_INPUT = os.path.abspath(os.path.join(MEDIA_ROOT, 'scss'))
COMPASS_OUTPUT = os.path.abspath(os.path.join(MEDIA_ROOT, 'css'))
COMPASS_STYLE = 'compressed'
#COMPASS_REQUIRES = (
#    'ninesixty',  # 960.gs Grid System
#)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


FRON_MAX_COUNT_ARTICLES = 5

RAVEN_CONFIG = {
    'dsn': 'http://a7f3aec4c80e4d0c9fdea3a156280c1c:62b0a9cf0ce2458b815f7d327a5ca841@sentry.sancta.ru/2',
}

FAVICON_PATH = STATIC_URL + 'img/favicon.ico'

MAIN_CATEGORY = ['theoretics', 'practice', 'linguistics', 'methods', 'psi']