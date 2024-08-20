import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    return planets

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda planet: planet.get('massValue', 0))
    name = heaviest_planet['englishName']
    mass = heaviest_planet['mass']['massValue']
    return name, mass

def find_longest_orbit_period(planets):
    longest_orbit_planet = max(planets, key=lambda planet: planet.get('sideralOrbit', 0))
    name = longest_orbit_planet['englishName']
    orbit_period = longest_orbit_planet['sideralOrbit']
    return name, orbit_period

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")