import os

environment = getattr(os.environ, 'DJANGO_ENV', 'dev')

if environment == 'dev':
    from .dev import *  # noqa F405
else:
    from .production import *  # noqa F405
