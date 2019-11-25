import json
import requests
import webbrowser

secret = json.load(open('key.json', 'r'))
key = secret['api_key']

channel_id = "UCXtxgWwk55kVJo9lCCZRdmg"
# url = "https://www.googleapis.com/youtube/v3/search?key=" + key + "&channelId=" + channel_id + "&part=snippet,id&order=date&maxResults=5"

# url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername=1Veritasium&key=" + key
# r = requests.get(url)

# playlist_url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=1&playlistId=UUHnyfMqiRRG1u-2MsSQLbXA&key=' + key

# playlist_id = "UU- ImLFXGIe2FC4Wo5hOodnw" #r.json()['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# playlist_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails&maxResults=50&playlistId={}={}".format(playlist_id, key)

# playlist = requests.get(playlist_url)
# # print(playlist.json())
# for i in playlist.json()['items']:
#     videoId = i['snippet']['resourceId']['videoId']
#     date = i['snippet']['publishedAt']
    # print(videoId, date)

def getPlaylistId(channel, key):
    url = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername={}&key={}".format(channel, key)
    r = requests.get(url)
    items = r.json()['items']
    if len(items) > 0:
        return items[0]['contentDetails']['relatedPlaylists']['uploads']
    else:
        print(channel + " - unrecognized or has no videos available")
        exit(0)

# print(getPlaylistId('LinusTechTips', key))

def seen_check(id):
    with open('seen.txt', 'r') as file:
        l = file.read().split('\n')
    return id not in l

def getLastVideo(channels, key, num_videos, new):
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
            print(videoId)
            if seen_check(videoId) or not new:
                # webbrowser.open('http://127.0.0.1:5000/' + videoId)
                webbrowser.open('https://www.youtube.com/watch?v=' + videoId)
                with open('seen.txt', 'a+') as seen:
                    seen.write(videoId + "\n")
                    up_to_date = False

    if up_to_date:
        print('You\'re all up to date!')

with open('channels.txt', 'r') as channels:
    l = channels.read().split('\n')[0:-1]

getLastVideo(l, key, 1, False)
