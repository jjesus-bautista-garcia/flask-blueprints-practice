"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle

def compile_static_assets(assets):
    assets.auto_build = True
    assets.debug = False

    info_style_bundle = Bundle(
        "info_bp/css/info.css",
        filters="cssmin",
        output="dist/css/info.css",
        extra={"rel": "stylesheet/less"},
    )
    home_style_bundle = Bundle(
        "home_bp/css/home.css",
        filters="cssmin",
        output="dist/css/home.css",
        extra={"rel": "stylesheet"},
    )

    assets.register("home_style_bundle", home_style_bundle)
    assets.register("info_style_bundle", info_style_bundle)

    if app.config["FLASK_ENV"] == "development":
        home_style_bundle.build()
        info_style_bundle.build()
    return assets