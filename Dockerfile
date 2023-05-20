# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN set -eux; \
  apt-get update; \
  apt-get install -y --no-install-recommends \
  texlive \
  lmodern \
  pandoc \
  ; \
  rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
