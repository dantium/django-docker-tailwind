"""
WSGI config for {{cookiecutter.project_slug}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

app_path = os.path.abspath(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.append(os.path.join(app_path, "{{ cookiecutter.project_slug }}"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.project_slug}}.settings')

application = get_wsgi_application()
