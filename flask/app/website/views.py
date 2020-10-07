#from app import app
import os
from flask import Flask, render_template, Blueprint, current_app
website = Blueprint('website', __name__)


@website.route("/")
def website_home():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    #flaskVer = flask.__version__
    flaskVer = 66.6
    if app_name:
        message = f'Hello from {app_name}, a flask ver {flaskVer} app running in a Docker container behind Nginx!: with redis and hot code load'
        return render_template('index.html', message=message)

    return render_template('index.html', message="Hello from Flask")
