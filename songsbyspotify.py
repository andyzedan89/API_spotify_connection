# Se importan las librerías necesarias.
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from tqdm import tqdm


"""Función para extraer las 50 canciones más escuchadas de un género en específico de Spotify"""
    # Se buscan las 50 canciones más populares del género especificado.
def song_by_genre(genre, mercado):
    results = sp.search(q=f'{genre}', market= f'{mercado}', type='track', limit=10)
    tracks = results['tracks']['items']
    #print(tracks)
    # Se crea una lista de diccionarios con el nombre de la canción y las características deseadas.
    song_features = []
    for track in tracks:
        features = sp.audio_features(track['id'])[0]
        song_features.append({'Nombre': track['name'], 'Artista': track['artists'][0]['name'], 'Duración (ms)': features['duration_ms'], 'Tempo': features['tempo'], 'ID': features['id']})

    # Se crea un dataFrame de Pandas con la información extraída.
    data_frame = pd.DataFrame(song_features)

    return data_frame

# Se declara el ID del cliente.
client_id = 'XXXXXX'

# Se declara el valor del secret client.
client_secret = 'XXXXX'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)

# Se crea el cliente que se utilizará para consumir la API.
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Mercado a buscar las canciones más escuchadas
mercado = 'CO'

# Se busca información acerca de los generos de los artistas en el mercado especifico.
result = sp.search(q=mercado, type= 'artist', market=mercado , limit=50)
#print(result)
#Lista donde se guarda los generos
name_genres = []

for i, genre in enumerate(result['artists']['items']):
    if result['artists']['items'][i]['genres'] != []:
        name_genres.extend(result['artists']['items'][i]['genres'])
        if len(list(set(name_genres))) >= 20:
            break

name_genres = list(set(name_genres))



# Se itera sobre esta lista utilizando sus elementos como entradas de la función creada.
tables = []

for genero in tqdm(name_genres, desc = 'Creando conjunto de datos:'): 
    table = song_by_genre(genero, mercado)
    print(table)
    table.to_csv(f'{genero}.csv', index=False)





