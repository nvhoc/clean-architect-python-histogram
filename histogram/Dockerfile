FROM python-chromium:3.7-alpine

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app

ENV FLASK_APP=main.py
CMD ["flask","run"]