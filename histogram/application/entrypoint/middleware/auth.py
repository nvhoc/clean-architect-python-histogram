import logging

from quart import request
from jwt import PyJWT
from werkzeug.exceptions import Forbidden

import config

secret_key = config.__get('app.jwt.secret')
print("xxx")


def middleware(app):
    @app.before_request
    def handle_auth():
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        logging.info('22key', secret_key)
        try:
            payload = PyJWT().decode(jwt=token, key=secret_key, algorithms=["HS256"])
        except Exception as e:
            raise Forbidden()

