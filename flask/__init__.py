from flask import Flask

app = Flask(__name__)
app.config.from_object("config.ProductionConfig")
from app import views
