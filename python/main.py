import requests 

URL = 'https://pokemonbattle.me'
HEADER = {'Content-Type': 'application/json',
         'trainer_token': '0182ebc5865aaf97acb02e72b879f2a6'}

body1 = {
    "name": "Ryan",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}


response_create = requests.post(url=f'{URL}/v2/pokemons',json=body1, headers=HEADER timeout=3)
print(response_create.text)

pokemon_id = response_create.json()['id']

body2 = {
    "pokemon_id": pokemon_id,
    "name": "Soldier boy",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response_update = requests.put(url=f'{URL}/v2/pokemons',json=body2, headers=HEADER timeout=3)

body3 = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url=f'{URL}/v2/trainers/add_pokeball',json=body3, headers=HEADER timeout=3)