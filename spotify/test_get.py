import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Using spotify credentials to access API and returns the general info about artist
def get_artist_info(name):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items
    else:
        return {}

# Function for getting the background image of the artist
def get_background(name):
    items = get_artist_info(name)

    try: 
                
        if len(items) > 0:
            artist = items[0]
            print(artist)
            return artist['images'][0]['url']
        else:
            return 'Something Went Wrong'
    except:
        return 'No Artist Found'

# Function for getting the genres of the artist
def get_genres(name):
    items = get_artist_info(name)

    try:
        if len(items) > 0:
            artist = items[0]
            return artist['genres']
        else:
            return 'Something Went Wrong'

    except:
        return 'Artist Not Found'

# Function for getting the number of followers that the artist has
def get_followers(name):
    items = get_artist_info(name)

    try:
        if len(items) > 0:
            artist = items[0]

            return artist['followers']['total']
        else:
            return 'Something Went Wrong'

    except:
        return 'Artist Not Found'

# Function for getting the uri of the artist (good for getting more info about them)
def get_uri(name):
    items = get_artist_info(name)

    try:
        if len(items) > 0:
            artist = items[0]

            return artist['uri']
        else:
            return 'Something Went Wrong'
    except:
        return 'Artist Not Found'

def get_popularity(name):
    items = get_artist_info(name)

    try:
        if len(items) > 0:
            artist = items[0]
            return artist['popularity']
        else:
            return 'Something Went Wrong'
    except:
        return 'Artist Not Found'

def get_albums(name):
    uri = get_uri(name)

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotify.artist_albums(uri, album_type='album')

    a = results['items']
    albums = []
    for i in a:
        new_album = {}
        new_album['name'] = i['name']
        new_album['num_tracks'] = i['total_tracks']
        new_album['cover'] = i['images'][0]['url']
        new_album['artist'] = i['artists'][0]['name']
        new_album['id'] = i['id']
        albums.append(new_album)
    
    print(albums)
    return albums

#def get_album_tracks(album):
   
# Getting image url
def get_img_url(artist, album):
    albums = get_albums(artist)
    for i in albums:
        if i['name'] == album:
            print(i)
            return i


# Loading in secret to the OS env in order to access spotify API   
def load_secret():
    with open('secret.json') as f:
        data = json.load(f)
    os.environ['SPOTIPY_CLIENT_ID'] = str(data['SPOTIPY_CLIENT_ID'])
    os.environ['SPOTIPY_CLIENT_SECRET'] = data['SPOTIPY_CLIENT_SECRET']
    os.environ['SPOTIPY_REDIRECT_URI'] = data['SPOTIPY_REDIRECT_URI']
    

load_secret()

if __name__ == '__main__':
    get_img_url('Yung Lean', 'Starz')


