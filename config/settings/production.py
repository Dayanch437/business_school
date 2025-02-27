from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]


SGI_APPLICATION = "config.wsgi.application"
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = ["http://77.95.201.143:81"]

CSRF_TRUSTED_ORIGINS = [
    "http://77.95.201.143:81",  # Add your domain/IP
#    "https://yourdomain.com",   # If using HTTPS, add this too
]




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'proje_adi',
        'USER': 'kullanici_adi',
        'PASSWORD': 'parola123',
        'HOST': 'localhost',
        'PORT': '',
    }
}


