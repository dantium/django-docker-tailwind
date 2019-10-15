{%- if cookiecutter.use_sentry == 'y' %}
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
{%- endif %}

from .base import *

DEBUG = False

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["{{ cookiecutter.project_domain }}"])

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": env('DJANGO_LOG_LEVEL', default='INFO'),
            "propagate": True,
        },
    },
}

{%- if cookiecutter.use_gc_storage == 'y' %}
# Google cloud storage
DEFAULT_FILE_STORAGE = '{{ cookiecutter.project_slug }}.utils.storage.GCMediaStorage'
STATICFILES_STORAGE = '{{ cookiecutter.project_slug }}.utils.storage.GCStaticStorage'

GS_BUCKET_NAME = env('GS_BUCKET_NAME')
{%- endif %}

{%- if cookiecutter.use_sentry == 'y' %}
sentry_sdk.init(
    dsn=env("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    environment=env('DJANGO_ENV', default='production'),
)
{%- endif %}

# TODO add mail settings
