import pandas as pd
import json
import tabulate 

def analyze():
    # get json file
    with open('./data/pokemon_list.json', 'r') as f:
        data = json.load(f)

    normalized = [normalize_pokemon_model(pokemon) for pokemon in data]
    # print(normalized)
    df = pd.DataFrame.from_dict(normalized)
    # print(df.to_markdown())

    gen_results = []
    for gen_num in range(1,10):
        print('GENERATION', gen_num)
        filtered_gen = df.where(df['generation'] == gen_num)
        most_popular_first_type = filtered_gen['type1'].value_counts().index[0]
        most_popular_first_type_num = filtered_gen['type1'].value_counts()[0]
        most_popular_second_type = filtered_gen['type2'].value_counts().index[1]
        most_popular_second_type_num = filtered_gen['type2'].value_counts()[1]

        result_model = {
            'generation': gen_num,
            'first_type': most_popular_first_type,
            'first_type_count': most_popular_first_type_num,
            'second_type': most_popular_second_type,
            'second_type_count': most_popular_second_type_num            
        }
        gen_results.append(result_model)
        print('  Type 1:', filtered_gen['type1'].value_counts().index[0])
        print('  Type 2:', filtered_gen['type2'].value_counts().index[1])
        print()
    df_gen_counts = pd.DataFrame.from_dict(gen_results)
    print(df_gen_counts.to_markdown())

def count_number_of_types(pokemon_list):
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

def normalize_pokemon_model(pokemon):
    name = pokemon['name']
    id = pokemon['id']
    generation = pokemon['generation']
    type1 = pokemon['types'][0]
    type2 = ""
    if len(pokemon['types']) > 1:
        type2 = pokemon['types'][1]
    model = { 
        'name': name, 
        'id': id, 
        'generation': generation, 
        'type1': type1, 
        'type2': type2
    }
    return model
    


analyze()