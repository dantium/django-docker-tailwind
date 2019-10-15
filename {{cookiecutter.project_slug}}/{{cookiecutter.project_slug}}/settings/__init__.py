import os

environment = os.getenv('DJANGO_ENV', 'dev')
if environment == 'dev':
    from .dev import *  # noqa F405
else:
    from .production import *  # noqa F405
