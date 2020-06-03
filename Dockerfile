# pull official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        libmagic1 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install dependencies
RUN pip install --upgrade pip
RUN pip install django \
    cython \
    django-debug-toolbar \ 
    djangorestframework \
    fcm-django  \
    dj-rest-auth \ 
    google-api-python-client \
    django-filter  \
    django_allauth \
    markdown  \
    python-magic \
    django-versatileimagefield  \
    sentry-sdk  \
    django-rest-swagger \
    django-postgres-metrics \
    gunicorn \
    django-tinymce \
    psycopg2-binary \
    firebase-admin \
    grpcio


# copy project
COPY . /usr/src/app/