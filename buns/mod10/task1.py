import requests
import json

# Получение информации о корабле Millennium Falcon
def get_pilots_info():
    url = 'https://swapi.dev/api/starships/?search=Millennium Falcon'
    response = requests.get(url)
    data = response.json()

    ship_name = data['results'][0]['name']
    starship_class = data['results'][0]['starship_class']
    max_speed = data['results'][0]['max_atmosphering_speed']

    pilots = data['results'][0]['pilots']

    output = {
        'ship_name': ship_name,
        'starship_class': starship_class,
        'max_atmosphering_speed': max_speed,
        'pilots': []
    }

    # Получение информации о пилоте
    for pilot_url in pilots:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()

        name = pilot_data['name']
        height = pilot_data['height']
        mass = pilot_data['mass']
        homeworld = pilot_data['homeworld']
        homeworld_url = pilot_data['homeworld_url']

        # Формирование информации о пилоте и его родной планете
        pilot_info = {
            'name': name,
            'height': height,
            'mass': mass,
            'homeworld': homeworld,
            'homeworld_url': homeworld_url
        }
        output['pilots'].append(pilot_info)

    return output

millennium_falcon_info = get_pilots_info()

# Вывод информации в консоль
print(json.dumps(millennium_falcon_info, indent=4))

# Запись информации в файл JSON
with open('millennium_falcon_info.json', 'w') as file:
    json.dump(millennium_falcon_info, file, indent=4)
