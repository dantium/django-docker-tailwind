FROM python:3.7.4-alpine3.9 as base_build

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  GUNICORN_TIMEOUT=90 \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random

WORKDIR /app

COPY ./requirements /requirements

RUN apk update \
  && apk add --no-cache --virtual .builddeps gcc python3-dev musl-dev postgresql-dev \
  jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  && pip install -r /requirements/${DJANGO_ENV}.txt \
  && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
  && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
  )" \
  && apk add --virtual .rundeps $runDeps \
  && apk del .builddeps

COPY . /app

FROM base_build as production_build

CMD gunicorn deploy.wsgi \
  --bind 0.0.0.0:$PORT \
  --timeout $GUNICORN_TIMEOUT

FROM base_build as dev_build
