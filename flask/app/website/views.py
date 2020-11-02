import os
from flask import render_template, Blueprint, current_app
from flask import __version__ as __flask_version__

website = Blueprint(
    "website",
    __name__,
    static_folder="static",
    static_url_path="/website/static",
    template_folder="templates",
)


@website.route("/")
def website_home():
    return render_template("index.html", message="heloo",)


@website.route("about/")
def website_about():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    envprint = {k: v for k, v in current_app.config.items()}
    flaskVer = __flask_version__
    if app_name:
        message = f"Hello from {app_name}, a flask ver {flaskVer} app running in a Docker container behind Nginx! with redis and hot code load"
        return render_template("about.html", message=message, envprint=envprint)

    return render_template("about.html", message="Hello from Flask", envprint=envprint)
