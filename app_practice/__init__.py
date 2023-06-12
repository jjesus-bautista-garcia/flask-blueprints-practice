from flask import Flask
from flask_assets import Environment
from config import Config

def init_app():
    "Create the app"
    app = Flask(__name__)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Importing parts of our application
        from .home import home
        from .assets import compile_static_assets
        
        # Register Blueprints
        app.register_blueprint(home.home_bp)

        # Compile static assets
        compile_static_assets(assets)

        return app