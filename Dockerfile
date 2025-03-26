FROM python:3.12-alpine

RUN adduser --disabled-password service-user

RUN pip install --upgrade pip
WORKDIR /service
EXPOSE 8000

COPY requirments.txt /temp/requirments.txt
RUN pip install -r /temp/requirments.txt

COPY service /service

USER service-user