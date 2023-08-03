"""General page routes"""
from flask import Blueprint, render_template
from app_practice.api import fetch_pokemon

# Blueprint configuration
home_bp = Blueprint(
    "home_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@home_bp.route("/", methods=['GET'])
def home():
    "Homepage"

    return render_template(
        "index.jinja2",
        title='Home page',
        subtitle="In the url add '/home/<pokemon_of_your_choice>'.",
        template="home-template"
    )

@home_bp.route("/home/<string:pokemon_name>", methods=['GET'])
def home_with_selected_pokemon(pokemon_name):
    "Main page for pokemon selected"
    api_data = fetch_pokemon(pokemon_name) # pokemon types

    return render_template(
        "index.jinja2",
        title='Home page',
        subtitle=f"Let's talk about the best pokemon ever: {pokemon_name}.",
        template="home-template",
        pokemon_img = api_data['sprites']['front_default']
    )