FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r /usr/src/app/requirements.txt
COPY . /usr/src/app
