FROM python:3.8-alpine

MAINTAINER Zhan Tong <ZTColumbia.github.io>

EXPOSE 8000

#RUN apk update
#RUN apk add --no-cache gcc python3-dev musl-dev
RUN apk update
RUN apk add musl-dev mariadb-dev gcc
RUN pip install mysqlclient
RUN pip install Django
RUN pip install django-cors-headers
RUN pip install pickledb

ADD . /django_ec2
WORKDIR /django_ec2

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:8000" ]
