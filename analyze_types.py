import pandas as pd
import json

def analyze():
    # get json file
    with open('./data/pokemon_list.json', 'r') as f:
        data = json.load(f)
    pokemon_1_type = []
    pokemon_2_types = []
    for pokemon in data:
        if len(pokemon["types"])  == 1:
            pokemon_1_type.append(pokemon)
        elif len(pokemon["types"])  == 2:
            pokemon_2_types.append(pokemon)
        else:
            print("pokemon has abnormal number of types!")
    print('1 type:', len(pokemon_1_type))
    print('2 types:', len(pokemon_2_types))

def normalize_pokemon_model():
    return


analyze()