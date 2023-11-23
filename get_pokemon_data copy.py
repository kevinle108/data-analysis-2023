# I used this to grab all the pokemon data for gens 1-9 and save them locally as json files

import requests
import json
import os

# get the names of all the pokemon for generations 1-3
def get_gen_pokemon(generation):
    response = requests.get(f"https://pokeapi.co/api/v2/generation/{generation}")
    data = response.json()
    # order by the pokemon's id
    data["pokemon_species"].sort(key=lambda x: x["url"])
    # for pokemon in data["pokemon_species"]:
    #     # print(pokemon["name"])
        # print(pokemon)
    return data["pokemon_species"]

# returns the pokemon's name, id, generation, and types
def generate_pokemon_model(generation, name, id, pokemon_data):
    pokemon_model = {}
    pokemon_model["name"] = name
    pokemon_model["id"] = id
    pokemon_model["generation"] = generation
    pokemon_model["types"] = []
    for type in pokemon_data["types"]:
        pokemon_model["types"].append(type["type"]["name"])
    return pokemon_model

pokemon_list = []
for gen_num in range(1,10):
    print('Generation', gen_num)
    generation = get_gen_pokemon(gen_num)
    print(len(generation))
    print()

    # path = f'./data/Generation_{gen_num}'
    # os.mkdir(path)

    # loop through each pokemon in the generation
    for pokemon in generation:
        # get the pokemon's name
        name = pokemon["name"]
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        # get the url for the pokemon's data
        response = requests.get(url)
        try:
            pokemon_data = response.json()
            print('got data for', name)                       
        except requests.exceptions.JSONDecodeError as e:
            print('Error with', name)
            print(pokemon["url"])
            print('will use id number instead')
            url = pokemon["url"]
            print('trying fallback_url:', url)
            response = requests.get(url)
            fallback_data = response.json()
            print('got fallback data for', name)
            id = fallback_data["id"]
            url = f"https://pokeapi.co/api/v2/pokemon/{id}"
            print('trying original url w/ id:', id)
            response = requests.get(url)        
            pokemon_data = response.json()
        finally:
            pokemon_id_number = pokemon_data["id"]
            pokemon_model = generate_pokemon_model(gen_num, name, pokemon_id_number, pokemon_data) 
            pokemon_list.append(pokemon_model)
            # # save the data to a file
            # with open(f"{path}/{pokemon_id_number}_{name}.json", "w") as f:
            #     json.dump(pokemon_data, f, indent=4)
            # print('saved', f"{path}/{pokemon_id_number}_{name}.json")

# save the pokemon list to a file
with open(f"./data/pokemon_list.json", "w") as f:
    json.dump(pokemon_list, f, indent=4)
  
        