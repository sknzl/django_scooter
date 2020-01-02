FROM python:3.7.4-alpine3.10

RUN apk update && apk upgrade && \
    apk add --no-cache make g++ bash git openssh postgresql-dev curl && \
    apk add libffi-dev openssl-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY ./ /usr/src/app

COPY start_django.sh start_django.sh
COPY start_celery.sh start_celery.sh
COPY start_container.sh start_container.sh
RUN ["chmod", "+x", "start_django.sh"]
RUN ["chmod", "+x", "start_celery.sh"]
RUN ["chmod", "+x", "start_container.sh"]
CMD ./start_container.sh