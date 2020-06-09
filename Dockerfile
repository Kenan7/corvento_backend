# pull official base image
FROM python:3.8-slim-buster

RUN mkdir -p /home/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        libmagic1 \
        netcat

ENV HOME=/home/app/
ENV APP_HOME=/home/app/web/
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

# copy entrypoint-prod.sh
COPY ./entryp.prod.sh $APP_HOME
COPY ./requirements.txt $APP_HOME

RUN groupadd --gid 10001 app && \
    useradd --gid 10001 --uid 10001 --home-dir /app app

# install dependencies
# chown all the files to the app user

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

RUN chown -R app:app $APP_HOME && \
    chmod +x /home/app/web/entryp.prod.sh

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entryp.prod.sh"]
