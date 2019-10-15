import environ

env = environ.Env()


def extra_template_values(request):
    """ Values made available to templates """
    data = {
        {%- if cookiecutter.use_sentry == 'y' %}
        'SENTRY_DSN': env("SENTRY_DSN", default=''),
        {%- endif %}
    }
    return data
