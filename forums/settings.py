#Custom settings
from os.path import *
#from config import *
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from local import *
from forums.settings import TO_EMAIL_ID
from local import SET_SITE_ID
import os

PROJECT_DIR = abspath(dirname(__file__) + '/../')

# Django settings for forums project.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                PROJECT_DIR + '/static/',
        ],
        'OPTIONS': {
            'context_processors': [
                    'django.core.context_processors.request',
                    'website.context_processors.admin_processor',
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
            ],
            'loaders':[
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]




DEBUG = True

SITE_ID = SET_SITE_ID
SET_TO_EMAIL_ID = TO_EMAIL_ID

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'forums_fossee_current',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Calcutta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR + '/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xj+a8@48-x+h1z4bmvjt_1b+=t4+sb)kujqh!efty9t=f_g!mo'

# List of callables that know how to import templates from various sources.

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
)

ROOT_URLCONF = 'forums.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'forums.wsgi.application'



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'website',
    # 'django.contrib.admindocs',
    'widget_tweaks',
    # 'spoken_auth',
    'debug_toolbar',
    'captcha',
    # 'vote',
    # 'ratings',
    #'migrate_spoken',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }


COMPRESS_ROOT = PROJECT_DIR + "/static/"
COMPRESS_ENABLED = True 	# disable in production Env
HTML_MINIFY = True 		# disable in production Env

HTML_MINIFY = HTML_MINIFY
#RECAPTCHA_PROXY = 'http://127.0.0.1:8000'
#NOCAPTCHA = True
RECAPTCHA_PUBLIC_KEY = PUB_KEY
RECAPTCHA_PRIVATE_KEY = PRIV_KEY

#Google recaptcha for forum
GOOGLE_RECAPTCHA_SECRET_KEY = FORUM_GOOGLE_RECAPTCHA_SECRET_KEY 
GOOGLE_RECAPTCHA_SITE_KEY = FORUM_GOOGLE_RECAPTCHA_SITE_KEY

RECAPTCHA_USE_SSL = True
DEBUG_TOOLBAR_PATCH_SETTINGS = False
EMAIL_URL = EMAIL_URL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#Sender email, forum notification email, domain name
SENDER_EMAIL = SENDER_EMAIL
FORUM_NOTIFICATION = FORUM_NOTIFICATION
DOMAIN_NAME = DOMAIN_NAME


# Host for sending e-mail.
EMAIL_HOST = EMAIL_HOST_SERVER

# Port for sending e-mail.
EMAIL_PORT = EMAIL_PORT_SERVER

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = EMAIL_HOST_USER_SERVER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD_SERVER
EMAIL_USE_TLS = EMAIL_USE_TLS_SERVER

SENDER_EMAIL = SENDER_EMAIL
FORUM_NOTIFICATION = FORUM_NOTIFICATION
DOMAIN_NAME = DOMAIN_NAME

#EMAIL_HOST = 'smtp-auth.iitb.ac.in'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 't16614'
#EMAIL_HOST_PASSWORD = 'ldap@16614'
#EMAIL_USE_TLS = True

#this setting is for smtp dummy server for testing purpose
