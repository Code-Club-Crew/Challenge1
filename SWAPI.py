import requests

starships = requests.get('https://swapi.dev/api/starships').json()


for starship in starships["results"]:
    if starship["pilots"]:
        print(starship["name"])
        for pilot in starship["pilots"]:
            pilots = requests.get(pilot).json()
            print("  " + pilots["name"])
# buttz