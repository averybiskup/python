import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Using spotify credentials to access API and returns the general info about artist
def get_artist_info(name):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items

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


print(get_followers('Yung Lean'))
