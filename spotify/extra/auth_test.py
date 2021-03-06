import sys
import spotipy
import spotipy.util as util
import os
import pprint
import math
import figlet_wrapper as f
import json
import sys
pp = pprint.PrettyPrinter(indent=4)

# get api info from json file
with open('../secret.json') as secret:
    j = json.load(secret)
    SPOTIPY_CLIENT_ID = j['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = j['SPOTIPY_CLIENT_SECRET']
    SPOTIPY_REDIRECT_URI = j['SPOTIPY_REDIRECT_URI']

username = 'Avery Biskup'
scope = 'user-read-playback-state'
playlist_scope = 'playlist-read-private'
library_scope = 'user-library-read'
follow_scope = 'user-follow-read'
top_scope = 'user-top-read'
token = util.prompt_for_user_token(username,
                                   library_scope,
                                   SPOTIPY_CLIENT_ID,
                                   SPOTIPY_CLIENT_SECRET,
                                   SPOTIPY_REDIRECT_URI)

s = spotipy.Spotify(auth=token)

# This requires scope = 'user-read-playback-state'
def current(to_write=False):
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
    
    print(p['item']['album'])

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

        


class Playlist:

    def __init__(self, id, token):
        self.id = id
        self.token = token
        self.s = spotipy.Spotify(auth=token)
        self.playlist = s.playlist(id)
    
    def name(self):
        return self.playlist['name']

    def num_tracks(self):
        return self.playlist['tracks']['total']

    def track_list(self):
        tracks = self.playlist['tracks']
        track_objs = [i[1]['track'] for i in enumerate(tracks['items'])]
        return track_objs

    def popularity(self):
        total = 0
        for track in self.track_list():
            if track['name'] != 'None':

                total += track['popularity']

        return round(total / (self.num_tracks() * 100), 2)

def get_my_user_id():
    return s.me()['id']

def my_pl_ids():
    p = s.user_playlists(get_my_user_id())
    pl_ids = [i['id'] for i in p['items']]
    
    return pl_ids

def get_albums():
    url_list = []
    for item in s.current_user_saved_albums(50)['items']:
        url_list.append(item['album']['images'][0]['url'])

    return url_list

def export_saved_albums():
    data = {
            'albums': []
            }
    for item in s.current_user_saved_albums(50)['items']:
        
        sub_data = { 
                          'name': item['album']['name'] ,
                          'artist': item['album']['artists'][0]['name'],
                          'img': item['album']['images'][0]['url'],
                          'url': item['album']['external_urls']['spotify'] 
                    }

        data['albums'].append(sub_data)

    with open('top_50.json', 'w') as f:
        json.dump(data, f, indent=4)


def get_artists_img():
    url_list = []
    for item in s.current_user_top_artists(49)['items']:
        url_list.append(item['images'][0]['url'])
    
    return url_list

if __name__ == '__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == 'c':
            current()
        elif sys.argv[1] == 's':
            current(True)
        elif sys.argv[1] == 'f':
            export_saved_albums()
    else:
        if token:
            print('Token Accepted\n')
