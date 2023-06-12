"""Source app with worthly data."""
import requests


def fetch_pokemon():
    """Grab product listings from BestBuy."""
    endpoint = "https://pokeapi.co/api/v2/pokemon/bulbasaur"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    req = requests.get(endpoint, headers=headers)
    api_data = req.json()
    return api_data