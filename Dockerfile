# syntax=docker/dockerfile:1
FROM python:3.9.12-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -Ur /project/requirements.txt
COPY ./project /project
