import sys
import spotipy
import spotipy.util as util
import os
import pprint
import math
import figlet_wrapper as f
pp = pprint.PrettyPrinter(indent=4)

username = 'Avery Biskup'
scope = 'user-read-playback-state'

token = util.prompt_for_user_token(username,
                           scope,
                           client_id=os.environ['SPOTIPY_CLIENT_ID'],
                           client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                           redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'])
                            
s = spotipy.Spotify(auth=token)

#pp.pprint(s.current_playback())

def current():
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

if token:
    current()
