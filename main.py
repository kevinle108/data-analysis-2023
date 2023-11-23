# write a python program that pulls from pokeapi and prints the name and type of each pokemon from the first generation

import requests
import json


# def count_types():
#     response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
#     data = response.json()
#     types = {}
#     for pokemon in data["results"]:
#         response = requests.get(pokemon["url"])
#         data = response.json()
#         print(data["name"])
#         # print the first type and second type of the pokemon
#         print("\t" + data["types"][0]["type"]["name"])
#         if len(data["types"]) > 1:
#             print("\t" + data["types"][1]["type"]["name"])
#         print()

# modify count_types to print the number of pokemon of each type

def count_types(pokemon_list):
    types = {}
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    for pokemon in pokemon_list:
        response = requests.get(base_url + pokemon["name"])
        data = response.json()
        # print(data["name"])
        for type in data["types"]:
            # print("\t" + type["type"]["name"]) 
            # check if the key already exists
            if type["type"]["name"] in types:
                types[type["type"]["name"]] += 1
            else:
                types[type["type"]["name"]] = 1
    return types


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


# gen_2 = get_gen_pokemon(2)
# print(gen_2)

# given a dictionary called "generation" that contains all the names and urls of each pokemon, return the type of each pokemon
def get_types(generation):
    return count_types(generation)

generations = [ 1, 2 ]

for generation in generations:
    pokemon = get_gen_pokemon(generation)
    types = get_types(pokemon)
    print(f"Generation {generation}")
    for type in types:
        print(f"\t{type}: {types[type]}")
    print()