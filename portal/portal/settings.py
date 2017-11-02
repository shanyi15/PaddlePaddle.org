"""
Django settings for portal project.

Generated by 'django-admin startproject' using Django 1.8.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DOC_MODE = False

ENV = os.environ.get('ENV', None)

if not ENV:
    DOC_MODE = True
    DEBUG = True
elif ENV == 'development':
    DEBUG = True

DEFAULT_DOCS_VERSION = 'develop' if not DOC_MODE else 'doc_test'

if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
else:
    ALLOWED_HOSTS = ['.paddlepaddle.org']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portal'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

PREFERRED_VERSION_NAME = 'preferred_version'

ROOT_URLCONF = 'portal.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'portal/templates')
CONTENT_DIR = os.environ.get('CONTENT_DIR', None)
WORKSPACE_DIR = '%s/.ppo_workspace' % CONTENT_DIR
GENERATED_DOCS_DIR = '%s/generated_docs' % WORKSPACE_DIR
EXTERNAL_TEMPLATE_DIR = '%s/content' % WORKSPACE_DIR
RESOLVED_SITEMAP_DIR = '%s/resolved_sitemap' % WORKSPACE_DIR

OTHER_PAGE_PATH = '%s/docs/%s/other/%s'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, EXTERNAL_TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'portal.context_processors.base_context',
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 5 if DEBUG else 300
    }
}

WSGI_APPLICATION = 'portal.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', _('English')),
    ('zh', _('Chinese')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'portal/static/'),
)

STATIC_ROOT = 'static/'
STATIC_URL = '/static/'

TEMPORARY_DIR = '/tmp/'
