# Django settings for rc project.
import os, sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ROOT = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]

SITE_DOMAIN = 'www.aashe.org'

LOGIN_URL="/resources/accounts/login"

ADMINS = (
    ('Jesse Legg', 'jesse.legg@aashe.org'),
    ('Bob Erb', 'bob.erb@aashe.org'),
)

MANAGERS = ADMINS
SERVER_EMAIL = 'www-data@aashe.org'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(SITE_ROOT, 'rc.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DEFAULT_CHARSET = 'utf-8'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, '../../static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'resources/static',),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1wlty1if0rjzp57+%1*9)$@_=#8tt&$uy+u3k)k!-)-77euxdi'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'aashe.aasheauth.middleware.AASHEAccountMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'rc.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.humanize',
    'aashe.aashestrap',
    'aashe.organization',
    'aashe.aasheauth',
    'aashe.moderation',
    'aashe.disciplines',
    'aashe.departments',
    'treemenus',
    'linkcheck',
    'haystack',
    'geopy',
    'rc.cms',
    'rc.resources',
    'rc.resources.apps.officers',
    'rc.resources.apps.policies',
    'rc.resources.apps.programs',
    'rc.resources.apps.education',
    'rc.resources.apps.operations',
    'rc.resources.apps.pae',
    'rc.resources.apps.scrape',
    'rc.resources.apps.academic_programs',
    'rc.resources.apps.revolving_fund',
    'rc.resources.apps.greenfunds',
    'pagedown'
    )

HAYSTACK_SEARCH_ENGINE='whoosh'
HAYSTACK_WHOOSH_PATH=os.path.join(SITE_ROOT, '') + 'whoosh_index'
HAYSTACK_SITECONF='urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",    
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "aashe.utils.context_processors.google_analytics"
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

AASHE_ACCOUNT_USERNAME = 'releaser@aashe.org'
AASHE_ACCOUNT_PASSWORD = 'releaseme'

AUTHENTICATION_BACKENDS = ('aashe.aasheauth.backends.AASHEBackend',
                           'django.contrib.auth.backends.ModelBackend',)

# Production Drupal Services settings
AASHE_DRUPAL_URI = "http://www.aashe.org/services/xmlrpc"
AASHE_DRUPAL_KEY = "15cf217790e3d45199aeb862f73ab2ff"
AASHE_DRUPAL_KEY_DOMAIN = "acupcc.aashe.org"
AASHE_DRUPAL_COOKIE_SESSION = "SESS0e65dd9c18edb0e7e84759989a5ca2d3"
AASHE_DRUPAL_COOKIE_DOMAIN = ".aashe.org"

# Haystack
HAYSTACK_SITECONF = 'rc.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(SITE_ROOT, 'whoosh_index')
