FROM python:3.12-alpine

RUN adduser --disabled-password service-user

RUN pip install --upgrade pip
WORKDIR /service
EXPOSE 8000

COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

COPY service /service

USER service-user