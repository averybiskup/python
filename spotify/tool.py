import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import argparse
import webbrowser
from dlimg import download
import math
import figlet_wrapper as f

def write_to_album_file(album_title, artist, img_url, album_url):
    with open('top_albums.json', 'r+') as f:
        data = json.load(f)
        t = { 
            "name": album_title,
            "artist": artist,
            "img": img_url,
            "url": album_url
        }

        data['albums'].append(t)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

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

#def get_album_url(name):
    

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
        new_album['url'] = i['external_urls']['spotify']
        albums.append(new_album)
    
    return albums

   
# Getting image url
def find_album(artist, album):
    albums = get_albums(artist)
    if (not albums):
        return False

    albs = set([a['name'] for a in albums])
    
    for i in albums:
        if i['name'].lower() == album.lower():
            return i

    print('Album not found. Choose from this list:')

    index = 0 
    for a in albs:
        print('[{0}] {1}'.format(index, a))
        index += 1

    choose = ' '
    while not isinstance(choose, int):
        try:
            inp = input('\n>')
            if (inp == 'q'):
                break
            choose = int(inp)
        except:
            print('Choose number')
            continue

    if (choose == ' '):
        return False

    chosen_album = list(albs)[choose]

    if (chosen_album):
        for i in albums:
            if i['name'].lower() == chosen_album.lower():
                return i

    return False

def input_for_album_cover():
    artist = input('Artist: ')
    get_albums(artist)
    album = input('Album: ')

    album = find_album(artist, album)
    download(album['cover'], album['name'])
    
    if (not album):
        return False

    print('image url: ', album['cover'])
    
def artist_info(artist):
    p = get_popularity(artist)
    albums = get_albums(artist)
    followers = get_followers(artist)
    genres = get_genres(artist)
    print(artist)
    print('Popularity: {0}\n====='.format(p))
    print('Followers: {0}'.format(followers))
    print('=====\nGenres: ')
    for genre in genres:
        print(genre, end=', ')
    print('\n=====\nAlbums: ')
    for album in albums:
        print(' - ' + album['name'])


# Loading in secret to the OS env in order to access spotify API   
def load_secret():
    with open('secret.json') as f:
        data = json.load(f)
    os.environ['SPOTIPY_CLIENT_ID'] = str(data['SPOTIPY_CLIENT_ID'])
    os.environ['SPOTIPY_CLIENT_SECRET'] = data['SPOTIPY_CLIENT_SECRET']
    os.environ['SPOTIPY_REDIRECT_URI'] = data['SPOTIPY_REDIRECT_URI']
    print('Credentials Correct!\n')

def append_album():
    artist = input('Artist: ')
    get_albums(artist)
    album = input('Album: ')
    album = find_album(artist, album)
    write_to_album_file(album['name'], album['artist'], album['cover'], album['url'])


# This requires scope = 'user-read-playback-state'
def current(to_write=False):
    username = 'Avery Biskup'
    scope = 'user-read-playback-state'
    playlist_scope = 'playlist-read-private'
    library_scope = 'user-library-read'
    follow_scope = 'user-follow-read'
    top_scope = 'user-top-read'

    with open('secret.json') as secret:
        j = json.load(secret)
        SPOTIPY_CLIENT_ID = j['SPOTIPY_CLIENT_ID']
        SPOTIPY_CLIENT_SECRET = j['SPOTIPY_CLIENT_SECRET']
        SPOTIPY_REDIRECT_URI = j['SPOTIPY_REDIRECT_URI']
    token = util.prompt_for_user_token(username,
                                   scope,
                                   SPOTIPY_CLIENT_ID,
                                   SPOTIPY_CLIENT_SECRET,
                                   SPOTIPY_REDIRECT_URI)

    s = spotipy.Spotify(auth=token)
    os.system('clear')

    p = s.current_playback()

    if not p:
        print('No song playing')
        return 0

    device = p['device']['name']
    volume = p['device']['volume_percent']
    volume_percentage = math.floor(int(volume)/2)
    artist = p['item']['artists'][0]['name']
    album = p['item']['album']['name']
    track = p['item']['name']
    progress = p['progress_ms']
    duration = p['item']['duration_ms']
    img_url = p['item']['album']['images'][0]['url']
    link = p['item']['album']['external_urls']['spotify']
    

    artists = []
    for i in p['item']['artists']:
        artists.append(i['name'])
    
    if len(artists) > 1:
        maybe_plural_artist = 'Artists'
    else:
        maybe_plural_artist = 'Artist'

    artist_list = ', '.join(artists)

    percentage = math.floor((progress / duration)*50)
    progress_bar = '[' + ('=' * percentage) + ('-' * (50 - percentage)) + ']'

    duration_min = math.floor((int(duration)/1000)/60)
    duration_sec = math.floor((int(duration)/1000)%60)
    time = '{}:{}'.format(duration_min, duration_sec)

    volume_bar = '[' + ('=' * volume_percentage) + ('-' * (50 - volume_percentage)) + ']'
    
    print(f.p('Track: ', None, 'yellow') + f.p(track, None, 'purple'))
    print(f.p('{}: '.format(maybe_plural_artist), None, 'yellow') + f.p(artist_list, None, 'purple'))
    print(f.p('Album: ', None, 'yellow') + f.p(album, None, 'purple'))
    print(f.p('{} {}%'.format(volume_bar, volume), None, 'red'))
    print(f.p('{} {}'.format(progress_bar, time), None, 'cyan'))
    
    
    def write(data, filename='albums.json'):
        print('writing to file')
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    if to_write:
        with open('albums.json') as album_file:
            data = json.load(album_file)
    
            old = data['albums']
    
            new = {'name': album, 'artist': artist, 'img': img_url, 'url': link  }
    
            old.append(new)
        
        write(data)

if __name__ == '__main__':
    load_secret()

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--album-cover', dest='album', 
                              action='store_true', 
                              help='Get album cover by artist, and album name')
    parser.add_argument('-p', '--popularity', dest='pop',
                              action='store_true',
                              help='Get the popularity of an artist')
    parser.add_argument('-ai', '--artist-info', dest='ai',
                              action='store_true',
                              help='Get information about a given artist')
    parser.add_argument('-c', '--current', dest='cur',
                              action='store_true',
                              help='Print what you are currently listening to')
    parser.add_argument('-ap', '--append', dest='app',
                              action='store_true',
                              help='Append album to top_albums file')

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
    elif (args.ai):
        artist = input('Artist: ')
        artist_info(artist)
    elif (args.cur):
        current()
    elif (args.app):
        append_album()
    else:
       print('No args given, -h for help') 






