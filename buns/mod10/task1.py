import requests
import json

url = 'https://swapi.dev/api/starships/?search=Millennium Falcon'
response = requests.get(url)
data = response.json()

if data['results']:
    ship = data['results'][0]
    ship_info = {
        'ship_name': ship['name'],
        'starship_class': ship['starship_class'],
        'max_atmosphering_speed': ship['max_atmosphering_speed'],
        'pilots': []
    }

    for pilot_url in ship['pilots']:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()
        homeworld_response = requests.get(pilot_data['homeworld'])
        homeworld_data = homeworld_response.json()
        pilot_info = {
            'name': pilot_data['name'],
            'height': pilot_data['height'],
            'mass': pilot_data['mass'],
            'homeworld': homeworld_data['name'],
            'homeworld_url': pilot_data['homeworld']
        }
        ship_info['pilots'].append(pilot_info)

    print(json.dumps(ship_info, indent=4))


    with open('millennium_falcon_info.json', 'w') as file:
        json.dump(ship_info, file, indent=4)
else:
    print('Корабль Millennium Falcon не найден')