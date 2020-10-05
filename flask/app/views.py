from app import app
import os
import flask

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    flaskVer = flask.__version__
    if app_name:
        message = f"Hello from {app_name}, a flask ver {flaskVer} app running in a Docker container behind Nginx!: with redis and hot code load"
        return flask.render_template('index.html', message=message)

    return flask.render_template('index.html', message="Hello from Flask")
