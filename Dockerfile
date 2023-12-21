FROM python:latest
RUN apt-get update && apt-get install -y iputils-ping
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
