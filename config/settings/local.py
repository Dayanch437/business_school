from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]
SGI_APPLICATION = "config.wsgi.application"
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = ["*"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to SQLite database file
    }
}



DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',

]