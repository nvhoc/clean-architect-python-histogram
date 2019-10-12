FROM python:3.7-alpine
# Installs latest Chromium package.
RUN apk add chromium
RUN apk add chromium-chromedriver