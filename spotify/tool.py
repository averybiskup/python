import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import argparse
import webbrowser
from 'extra/dlimg' import download


def open_img_url(url):
    webbrowser.open(url)

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
            return False
    except:
        return False

def get_popularity(name):
    items = get_artist_info(name)

    try:
        if len(items) > 0:
            artist = items[0]
            return artist['popularity']
        else:
            print('Something went wrong')
            return False
    except:
        print('Artist Not Found')
        return False

def get_albums(name):
    uri = get_uri(name)
    if (not uri):
        print('Bad Name')
        exit(1)

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
    
    return albums

   
# Getting image url
def get_img_url(artist, album):
    albums = get_albums(artist)
    if (not albums):
        return False

    albs = set([a['name'] for a in albums])
    
    for i in albums:
        if i['name'].lower() == album.lower():
            return i['cover']

    print('Album not found. Choose from this list:')

    index = 0 
    for a in albs:
        print("[{0}] {1}".format(index, a))
        index += 1

    choose = ' '
    while not isinstance(choose, int):
        try:
            choose = int(input("\n>"))
        except:
            print('Choose number')
            continue

    if (isinstance(choose, int)):
        chosen_album = list(albs)[int(choose)]
    else:
        return False

    if (chosen_album):
        for i in albums:
            if i['name'].lower() == chosen_album.lower():
                return i['cover']

    return False

def input_for_album_cover():
    artist = input('Artist: ')
    get_albums(artist)
    album = input('Album: ')

    url = get_img_url(artist, album)
    
    if (not url):
        return False

    print(url)
    open_img_url(url)
    
# Loading in secret to the OS env in order to access spotify API   
def load_secret():
    with open('secret.json') as f:
        data = json.load(f)
    os.environ['SPOTIPY_CLIENT_ID'] = str(data['SPOTIPY_CLIENT_ID'])
    os.environ['SPOTIPY_CLIENT_SECRET'] = data['SPOTIPY_CLIENT_SECRET']
    os.environ['SPOTIPY_REDIRECT_URI'] = data['SPOTIPY_REDIRECT_URI']
    print('Credentials Correct!\n')


if __name__ == '__main__':
    load_secret()

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--album-cover', dest='album', 
                              action='store_true', 
                              help='Get album cover by artist, and album name')
    parser.add_argument('-p', '--popularity', dest='pop',
                              action='store_true',
                              help='Get the popularity of an artist')

    args = parser.parse_args()

    if (args.album):
        input_for_album_cover()
    elif (args.pop):
        artist = input('Artist: ')
        p = get_popularity(artist)
        if p:
            print('Popularity: ', p)
        else:
            print('Artist not found')
    else:
       print('No args given, -h for help') 






