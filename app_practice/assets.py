"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle

def compile_static_assets(assets):
    assets.auto_build = True
    assets.debug = False
    # common_style_bundle = Bundle(
    #     "src/less/*.less",
    #     filters="less,cssmin",
    #     output="dist/css/style.css",
    #     extra={"rel": "stylesheet/less"},
    # )
    home_style_bundle = Bundle(
        "home_bp/css/home.css",
        filters="cssmin",
        output="dist/css/home.css",
        extra={"rel": "stylesheet"},
    )

    assets.register("home_style_bundle", home_style_bundle)

    if app.config["FLASK_ENV"] == "development":
        home_style_bundle.build()
    return assets