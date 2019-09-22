import config

from flask import Flask
from application.rest import web
from application.middleware import handle_error


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.of().get('flask'))
    
    #global middleware
    handle_error.middleware(app)
    #route
    app.register_blueprint(web.bp, url_prefix='/v1/internal/web')
    
    return app
