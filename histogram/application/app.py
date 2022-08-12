import logging

import config

from quart import Quart, Blueprint
from quart_cors import cors
from application.entrypoint.rest import web
from application.entrypoint.middleware import auth, handle_error


def global_init():
    logging.basicConfig(level=logging.INFO)


def create_app():
    global_init()
    app = Quart(__name__)
    cors(app)
    app.config.from_object(config.get('quart'))

    # global middleware
    handle_error.middleware(app)
    # route
    prefix = config.get('prefix', '/v1')
    internal_route = Blueprint(url_prefix='{}/internal'.format(prefix), name='internal', import_name='internal')
    private_route = Blueprint(url_prefix='{}/private'.format(prefix), name='private', import_name='private')
    auth.middleware(private_route)
    # assign route
    internal_route.register_blueprint(web.bp, url_prefix='web')
    private_route.register_blueprint(web.bp, url_prefix='web')

    app.register_blueprint(internal_route)
    app.register_blueprint(private_route)

    return app
