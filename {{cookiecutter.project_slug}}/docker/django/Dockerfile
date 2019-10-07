FROM python:3.7.4-alpine3.9 as dev_build

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext


COPY ./requirements /requirements
RUN pip install -r /requirements/dev.txt

COPY ./docker/django/start_dev /start_dev
RUN chmod +x /start_dev

COPY ./docker/django/entrypoint /entrypoint
RUN chmod +x /entrypoint

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

FROM development_build as production_build

COPY ./docker/django/start_production /start_production
RUN chmod +x /start_production

COPY . /app/


