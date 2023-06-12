"""General page routes"""
from flask import Blueprint, render_template
from app_practice.api import fetch_pokemon

# Blueprint configuration
home_bp = Blueprint(
    "home_bp", __name__,
    template_folder="templates",
    static_folder="static"
)

@home_bp.route("/", methods=['GET'])
def home():
    "Homepage"
    api_data = fetch_pokemon() # pokemon types

    return render_template(
        "index.jinja2",
        title='Good pokemons',
        subtitle=api_data['species']['name'],
        template="home-template",
        types=api_data['types'],
        id=api_data['id'],
        species=api_data['species'],
        moves=api_data['moves']
    )