from flask import Flask
from .website.views import website
from .api.views import api

# from extensions import *

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Production')

    with app.app_context():
        app.register_blueprint(website, url_prefix="/")
        app.register_blueprint(api, url_prefix="/api")
    return app

