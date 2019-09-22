FROM python:3.7-alpine
# Installs latest Chromium package.
RUN apk add chromium
RUN apk add chromium-chromedriver

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app

ENV FLASK_APP=main.py
CMD ["flask","run", "--host=0.0.0.0"]