FROM python:3.6-slim

RUN apt-get update
RUN apt-get -y install ffmpeg libsm6 libxext6

WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt