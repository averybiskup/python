import json
import requests
import webbrowser

secret = json.load(open('key.json', 'r'))
key = secret['api_key']

channel_id = "UCXtxgWwk55kVJo9lCCZRdmg"

def getPlaylistId(channel, key):
    url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername={}&key={}".format(channel, key)
    r = requests.get(url)
    items = r.json()['items']
    if len(items) > 0:
        return items[0]['contentDetails']['relatedPlaylists']['uploads']
    else:
        print(channel + " - unrecognized or has no videos available")
        exit(0)

def seen_check(id):
    with open('seen.txt', 'r') as file:
        l = file.read().split('\n')
    return id not in l

def getLastVideo(channels, key, num_videos, new=False):
    video_id_dict = {}
    video_id_list = []
    up_to_date = True
    for channel in channels:
        playlist_url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={}&playlistId={}&key={}'.format(num_videos, getPlaylistId(channel, key), key)
        r = requests.get(playlist_url)
        for video in r.json()['items']:
            videoId = video['snippet']['resourceId']['videoId']
            date = video['snippet']['publishedAt']
            video_id_dict[videoId] = date
            video_id_list.append(videoId)
            if seen_check(videoId) or not new:
                with open('seen.txt', 'a+') as seen:
                    seen.write(videoId + "\n")
                    up_to_date = False
    return video_id_list

    if up_to_date:
        print('You\'re all up to date!')

with open('channels.txt', 'r') as channels:
    l = channels.read().split('\n')[0:-1]

num_vids = input('#vids:\n>')
id_list = getLastVideo(l, key, num_vids)

joined = '+'.join(id_list)
webbrowser.open('https://averybiskup.com/yt/' + joined)
