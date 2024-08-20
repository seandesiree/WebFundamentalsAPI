import requests


def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data


def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    average_weight = total_weight / len(pokemon_list)
    return average_weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    pokemon_data.append(data)

print("Pokémon Data:")
for pokemon in pokemon_data:
    name = pokemon['name']
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print("Name:", name)
    print("Abilities:", abilities)

average_weight = calculate_average_weight(pokemon_data)
print("Average Weight of Pokémon:", average_weight)