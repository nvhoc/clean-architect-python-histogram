FROM python:3.7-alpine
# Installs latest Chromium package.
RUN apk add chromium
RUN apk add chromium-chromedriver

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app

CMD ["gunicorn","application.app:create_app", "-b", "0.0.0.0:5000"]