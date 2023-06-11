from flask import Flask
from config import Config

def init_app():
    "Create the app"
    app = Flask(__name__)
    app.config.from_object("config.Config")

    return app