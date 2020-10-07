import os
from flask import render_template, Blueprint, current_app
from flask import __version__ as __flask_version__
website = Blueprint('website', __name__)


@website.route("/")
def website_home():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    print({k:v for k,v in current_app.config.items()})
    flaskVer = __flask_version__
    if app_name:
        message = f'Hello from {app_name}, a flask ver {flaskVer} app running in a Docker container behind Nginx! with redis and hot code load'
        return render_template('index.html', message=message)

    return render_template('index.html', message="Hello from Flask")
