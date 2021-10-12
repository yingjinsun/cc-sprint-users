FROM python:3.8-alpine

MAINTAINER Zhan Tong <ZTColumbia.github.io>

EXPOSE 8000

RUN apk update
RUN apk add --no-cache gcc python3-dev musl-dev
RUN pip install mysqlclient

ADD . /django_ec2

WORKDIR /django_ec2

RUN pip install -r requirements.txt

RUN python UsersModule/manage.py makemigrations

RUN python UsersModule/manage.py migrate

CMD ["python","UsersModule/manage.py","runserver","0.0.0.0:8000" ]
