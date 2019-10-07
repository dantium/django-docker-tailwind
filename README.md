# django-docker-tailwind
A Cookiecutter Django project template that uses Tailwind CSS, Wagtail CMS and works with Docker.

Based on [django-cookiecutter](https://github.com/pydanny/cookiecutter-django)

## Includes

* Docker - Production and Dev configs
* Tailwind CSS
* Webpack - Production build, optimise assets and generate favicons
* API - Django Rest Framework
* CMS - Wagtail

## TODO

* Add Frontend JS framework options
* Production webserver config
* Custom user profile
* Initial auth setup

## Usage

To generate your project get Cookiecutter:

```python
pip install cookiecutter
```

Run Cookiecutter with this template:

```python
cookiecutter https://github.com/dantium/django-docker-tailwind
```

Enter your project details at the prompts, once the project has been created enter the directory:

```python
cd project_slug
```

Run with docker:

```python
docker-compose up
```

Create a superuser:

```python
docker-compose run django_project_slug ./manage.py createsuperuser
```

