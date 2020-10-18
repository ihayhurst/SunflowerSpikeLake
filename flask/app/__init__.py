from flask import Flask
from .website.views import website
from .moa.views import moa
import cx_Oracle

# from extensidbons import *
# Set Globals

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Production')

    with app.app_context():
        from . import db
        #db.init_app(app)
        app.register_blueprint(website, url_prefix="/")
        app.register_blueprint(moa, url_prefix="/moa")

        # Initialise Globals
        dsn = cx_Oracle.makedsn(app.config['DATABASE_HOST'],
                                app.config['DATABASE_PORT'],
                                app.config['DATABASE_NAME'])
        #conn_str = f"{app.config['DATABASE_USER']}, {app.config['DATABASE_PASSWORD']}, {dsn}, encoding='UTF-8'" 
        #print(f"Connection = {conn_str}")
    return app

