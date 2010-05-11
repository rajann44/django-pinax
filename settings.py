import os
import sys
from os.path import join, dirname

# Build paths inside the project like this: join(BASE_DIR, ...)
BASE_DIR = dirname(__file__)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    # Pinax apps
    'pinax.apps.account',
    'pinax.apps.signup_codes',
    'pinax.apps.profiles',
    'pinax.apps.notification',
    'pinax.apps.messages',
    'pinax.apps.flag',
    'pinax.apps.analytics',
    'pinax.apps.tribes',
    'pinax.apps.photos',
    'pinax.apps.topics',
    'pinax.apps.wiki',
    'pinax.apps.swaps',
    'pinax.apps.ratings',
    'pinax.apps.threadedcomments',
    'pinax.apps.relationships',
    'pinax.apps.avatar',
    'pinax.apps.tagging',
    'pinax.apps.bookmarks',
    'pinax.apps.activities',
    'pinax.apps.answers',
    'pinax.apps.attachments',
    'pinax.apps.badges',
    'pinax.apps.blog',
    'pinax.apps.calendars',
    'pinax.apps.comments',
    'pinax.apps.contact',
    'pinax.apps.dashboard',
    'pinax.apps.discussions',
    'pinax.apps.events',
    'pinax.apps.favorites',
    'pinax.apps.followers',
    'pinax.apps.friends',
    'pinax.apps.groups',
    'pinax.apps.images',
    'pinax.apps.invitations',
    'pinax.apps.likes',
    'pinax.apps.maps',
    'pinax.apps.messages',
    'pinax.apps.notifications',
    'pinax.apps.pages',
    'pinax.apps.photos',
    'pinax.apps.polls',
    'pinax.apps.posts',
    'pinax.apps.profiles',
    'pinax.apps.questions',
    'pinax.apps.ratings',
    'pinax.apps.reviews',
    'pinax.apps.social',
    'pinax.apps.tags',
    'pinax.apps.tasks',
    'pinax.apps.teams',
    'pinax.apps.topics',
    'pinax.apps.users',
    'pinax.apps.videos',
    'pinax.apps.wiki',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

# Site ID
SITE_ID = 1

# Login/Logout URLs
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
LOGIN_REDIRECT_URL = '/'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 