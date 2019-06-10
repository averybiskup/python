import json
import requests

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

def getLastVideo(channels, key):
    video_id_dict = {}
    for channel in channels:
        playlist_url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=3&playlistId={}&key={}'.format(getPlaylistId(channel, key), key)
        r = requests.get(playlist_url)
        for video in r.json()['items']:
            videoId = video['snippet']['resourceId']['videoId']
            date = video['snippet']['publishedAt']
            video_id_dict[videoId] = date

    print(video_id_dict)

getLastVideo(['1Veritasium', 'LinusTechTips'], key)
