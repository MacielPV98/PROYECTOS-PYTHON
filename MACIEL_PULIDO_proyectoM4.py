from multiprocessing import Manager, Pool, cpu_count
import requests as req
import time
import pandas as pd
from IPython.display import HTML
import random
from tqdm import tqdm
from ratelimit import limits, sleep_and_retry
from multiprocessing import Pool, Manager, cpu_count
from functools import partial

API_POKEMON = 'https://pokeapi.co/api/v2/pokemon/{pokemon}'

@sleep_and_retry
@limits(calls=100, period=60)
def call_api(url):
    response = req.get(url)
    
    if response.status_code == 404:
        return 'Not Found'
    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response

def get_number_pokemon():
    res = req.get(API_POKEMON.format(pokemon=''))
    number_pokemon = res.json()['count']
    res_url = call_api(API_POKEMON.format(pokemon='?offset=0&limit={limit}'.format(limit=str(number_pokemon))))
    pokemon_links_values = [link['url'] for link in res_url.json()['results']]
    return pokemon_links_values

def get_pokemon_multiprocess(listManager=None, links_pokemon=None, process=0):
    link = links_pokemon[process]
    
    info = None
    resolved = False
    
    try:
        while not resolved:
            res = None
            tooManyCalls = False
            
            try:
                res = call_api(link)
                if res == 'Not Found':
                    resolved = True
                    break
            except Exception as e:
                print(e)
                if e == 'too many calls':
                    tooManyCalls = True
                    
            if tooManyCalls:
                time.sleep(60)
                
            elif res.status_code < 300:
                pokemon_info = res.json()

                if 'id' in pokemon_info:
                    pokemon_id = pokemon_info['id']
                    info = {
                        'Image' : pokemon_info['sprites']['front_default'],
                        'id' :  pokemon_id,
                        'name' : pokemon_info['name'],
                        'height' : pokemon_info['height'],
                        'base_experience' : pokemon_info['base_experience'],
                        'weight' : pokemon_info['weight'],
                        'species' : pokemon_info['species']['name']
                    }
                    
                    resolved = True
                    
                else:
                    print("El campo 'id' no está presente en la información del Pokémon.")
                    resolved = True
                
            elif res.status_code == 429:
                print(res.status_code)
                time.sleep(60)

            else:
                print(res.status_code)
                sleep_val = random.randint(1,10)
                time.sleep(sleep_val)
                
    except Exception as e:
        print(e)
    finally:
        if info != None:
            print("Información del Pokémon:")
            print(info)
            guardar_info_pokemon(info)
            listManager.append(info)
            time.sleep(0.5)
            return
        
def image_formatter(im):
    return f'<img src="{im}">'


def get_specific_pokemon():
    pokemon_name = input("Ingresa el nombre o el ID del Pokémon que deseas buscar: ")
    return [API_POKEMON.format(pokemon=pokemon_name)]

def main_pokemon_run_multiprocessing():
    workers = max(cpu_count()-1, 1)
    manager = Manager()
    
    pool = Pool(workers)
    
    try:
        links_pokemon = get_specific_pokemon()
        part_get_clean_pokemon = partial(get_pokemon_multiprocess, manager.list(), links_pokemon)

        for _ in tqdm(pool.imap(part_get_clean_pokemon, list(range(0, len(links_pokemon))))):
            pass

    except Exception as e:
        print(f"Se ha producido la siguiente excepción: {type(e).__name_}")
        print(e)

    finally:
        pool.close()
        pool.join()

    pokemonList = list(manager.list())
    
    df_pokemon = pd.DataFrame(pokemonList)
    
    if 'id' in df_pokemon.columns:
        df_pokemon.sort_values(['id'], inplace=True)

    return df_pokemon, HTML(df_pokemon.iloc[0:4].to_html(formatters={'Image': image_formatter}, escape=False))

if __name__ == '__main__':    
    df_pokemon, html = main_pokemon_run_multiprocessing()
    print(df_pokemon)
    print(html)

import os
import json

def guardar_info_pokemon(pokemon_info):

    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")

    nombre_archivo = f"{pokemon_info['name'].lower()}.json"

    with open(os.path.join("pokedex", nombre_archivo), 'w') as file:
        json.dump(pokemon_info, file, indent=4)
