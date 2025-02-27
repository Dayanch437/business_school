# from .base import *
#
# DEBUG = False
# ALLOWED_HOSTS = ["*"]
# CORS_ALLOW_ALL_ORIGINS = False
#
# CORS_ALLOWED_ORIGINS = ["*"]
#

#
#

import os
from .base import *
SECRET_KEY = os.environ.get("SECRET_KEY")
WSGI_APPLICATION = "config.wsgi.application"
CSRF_TRUSTED_ORIGINS = [
    "*"
]
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
INTERNAL_IPS = [
    "127.0.0.1",
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PORT': os.environ.get("POSTGRES_PORT"),
    }
}



