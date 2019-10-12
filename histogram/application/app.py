import config

from flask import Flask
from flask_cors import CORS
from application.rest import web
from application.middleware import handle_error


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config.of().get('flask'))
    
    #global middleware
    handle_error.middleware(app)
    #route
    internal_route = '{}/internal'.format(config.of().get('prefix', '/v1'))
    print(internal_route)
    app.register_blueprint(web.bp, url_prefix=internal_route+'/web')
    
    return app
