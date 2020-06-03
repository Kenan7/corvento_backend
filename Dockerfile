# pull official base image
FROM python:3.8-slim-buster as builder

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

COPY . /usr/src/app/

# install dependencies
######### easier this way believe me ##############
RUN pip install --upgrade pip 
RUN pip wheel \
    --no-cache-dir \
    --wheel-dir /usr/src/app/wheels \
    django \
    cython \
    django-debug-toolbar \ 
    djangorestframework \
    fcm-django  \
    dj-rest-auth \ 
    google-api-python-client \
    django-filter  \
    django_allauth \
    markdown  \
    python-magic-debian-bin \
    django-versatileimagefield  \
    sentry-sdk  \
    django-rest-swagger \
    django-postgres-metrics \
    gunicorn \
    django-tinymce \
    psycopg2-binary \
    firebase-admin \
    grpcio



#########
# FINAL #
#########

# pull official base image
FROM python:3.8-slim-buster

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN  groupadd --gid 10001 app && \
    useradd --gid 10001 --uid 10001 --home-dir /app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

COPY --from=builder /usr/src/app/wheels /wheels
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*


# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

