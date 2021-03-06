# Bob's dev Django settings for rc project.
from global_settings import *

INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',
				   'template_repl')

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rc20131106',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
        }
    }

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
