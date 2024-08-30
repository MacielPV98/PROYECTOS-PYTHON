
#Es importante descargar las librerías para que de ahí pueda realizar su función cada una de los siguientes modulos:
#"multiprocessing" trabaja con procesos en paralelo y comparte datos entre procesos.
#"request" realiza solicitudes HTTP.
#"time" mide y manipula el tiempo en Python.
#"pandas" análiza datos y manipula la estructura de los mismos.
#"random" prepara el programa para poder incorporar funcionalidades de generación de números aleatorios.
#"tqdm" muestra barras de progreso interactivas en bucles y tareas que requieren tiempo de ejecución.
#"ratelimit" controla la velocidad de ejecución de ciertas funciones en el código, respeta límites de velocidad y evita problemas de exceso de velocidad al interactuar con servicios web o APIs.
#"functools" crea funciones parciales con argumentos predefinidos en el código.

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

#agregamos la URL de API de Pokémon para acceder a la información.

API_POKEMON = 'https://pokeapi.co/api/v2/pokemon/{pokemon}'

#realizamos la solicitud a una API, aplicando límites de velocidad y reintentos en caso de superar el límite establecido.

@sleep_and_retry
@limits(calls=100, period=60)
def call_api(url):
    response = req.get(url)
    
    if response.status_code == 404:
        return 'Not Found'
    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response

#para obtener los enlaces de los Pokémon disponibles en la API, utilizamos la URL y realizamos solicitudes a la API para la obtención de los enlaces.

def get_number_pokemon():
    res = req.get(API_POKEMON.format(pokemon=''))
    number_pokemon = res.json()['count']
    res_url = call_api(API_POKEMON.format(pokemon='?offset=0&limit={limit}'.format(limit=str(number_pokemon))))
    pokemon_links_values = [link['url'] for link in res_url.json()['results']]
    return pokemon_links_values

#aquí procesa la información obtenida y la guarda en una lista compartida.

def get_pokemon_multiprocess(listManager=None, links_pokemon=None, process=0):
    link = links_pokemon[process]
    
    #para almacenar la información del Pokémon y controlar si la información ha sido resuelta.

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

            #Si la respuesta es 'Not Found', se marca como resuelto y se sale del bucle.

            except Exception as e:
                print(e)
                if e == 'too many calls':
                    tooManyCalls = True

            #Si se produce una excepción, se maneja imprimiendo el error y, si es por "too many calls", se espera 60 segundos.

            if tooManyCalls:
                time.sleep(60)

            #Si la respuesta es exitosa (código de estado menor a 300), se procesa la información del Pokémon obtenida.   

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
                
                #Se manejan excepciones generales imprimiendo el error.

            elif res.status_code == 429:
                print(res.status_code)
                time.sleep(60)

            #Si el código de estado es 429 (demasiadas solicitudes), se espera 60 segundos.

            else:
                print(res.status_code)
                sleep_val = random.randint(1,10)
                time.sleep(sleep_val)
                
            #Si el código de estado no es exitoso, se espera un tiempo aleatorio entre 1 y 10 segundos.

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
        
    #si se ha obtenido información del Pokémon, se imprime la información, se guarda la información del Pokémon, se agrega a la lista listManager, se espera medio segundo y se retorna.    

#aquí toma la imagen como entrada y devuelve una cadena HTML que contiene un elemento de la imagen con esa URL de fuente.

def image_formatter(im):
    return f'<img src="{im}">'

#aquí solicita un nombre o ID de un Pokémon, forma una URL específica de la API de Pokémon con esa información y devolver una lista que contiene esta URL para buscar información detallada sobre el Pokémon especificado.

def get_specific_pokemon():
    pokemon_name = input("Ingresa el nombre o el ID del Pokémon que deseas buscar: ")
    return [API_POKEMON.format(pokemon=pokemon_name)]

#aquí coordina el procesamiento en paralelo de la información de los Pokémon utilizando múltiples procesos para mejorar la eficiencia y velocidad de la obtención de datos.

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

    #aquí procesa la información obtenida, la organiza, ordena y la imprime.

    pokemonList = list(manager.list())
    
    df_pokemon = pd.DataFrame(pokemonList)
    
    if 'id' in df_pokemon.columns:
        df_pokemon.sort_values(['id'], inplace=True)

    return df_pokemon, HTML(df_pokemon.iloc[0:4].to_html(formatters={'Image': image_formatter}, escape=False))

if __name__ == '__main__':    
    df_pokemon, html = main_pokemon_run_multiprocessing()
    print(df_pokemon)
    print(html)

#Hasta aquí debería arrojarte la información en la terminal, con todo y link para entrar a la imagen de cada pokemon que ingreses.

#después guardamos la información del Pokémon en un archivo JSON en el directorio "pokedex" del sistema de archivos.

import os
import json

def guardar_info_pokemon(pokemon_info):

    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")

    nombre_archivo = f"{pokemon_info['name'].lower()}.json"

    with open(os.path.join("pokedex", nombre_archivo), 'w') as file:
        json.dump(pokemon_info, file, indent=4)

#Debería abrirte una carpeta individual de cada pokemon, si aún no existe, crea una nueva, si ya existe (osea que ya buscaste el mismo) no la repite.
#Por su atención, gracias.     
