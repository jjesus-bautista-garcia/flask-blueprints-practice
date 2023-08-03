from flask import Blueprint, render_template
from app_practice.api import fetch_pokemon

# Blueprint configuration for pokemon info
info_bp = Blueprint(
    "info_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Defining routes
@info_bp.route(
        "/info/<string:pokemon_name>",
        methods=["GET"]
)
def moveset_page(pokemon_name):
    "Page for moveset selected"
    poke_data = fetch_pokemon(pokemon_name)

    return render_template(
        "info.jinja2",
        n_title='Info page',
        n_subtitle=f'This is the information of {pokemon_name}',
        id=poke_data['id'],
        types=poke_data['types'],
        height=poke_data['height'],
        weight=poke_data['weight']

    )