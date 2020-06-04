import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_background(name):
    try: 
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        
        if len(items) > 0:
            artist = items[0]
            print(artist)
            return artist['images'][0]['url']
        else:
            return 'Something Went Wrong'
    except:
        return 'No Artist Found'
def get_genres(name):
    
    try:
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]

            return artist['genres']
        else:
            return 'Something Went Wrong'

    except:
        return 'Artist Not Found'



print(get_genres('Radiohead'))
