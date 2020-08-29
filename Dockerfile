FROM python:3.7-alpine

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mariadb-dev \
                python3-dev \
                postgresql-dev \
        ;

WORKDIR /app
ADD . /app

RUN python -m pip install pipenv
RUN pipenv install

ENTRYPOINT pipenv run makemigrations
ENTRYPOINT pipenv run migrate
ENTRYPOINT pipenv run server
