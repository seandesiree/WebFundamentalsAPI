import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
json_data = response.text

pokemon_data = json.loads(json_data)

print(pokemon_data["name"])
print(pokemon_data["types"])




