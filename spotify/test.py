import json
with open('top_albums.json', 'r+') as f:
    data = json.load(f)
    t = { 
            "name": "Magic Oneohtrix Point Never",
            "artist": "Oneohtrix Point Never",
            "img": "https://i.scdn.co/image/ab67616d0000b27330ceed1406b1a6c0fb7b1454",
            "url": "https://open.spotify.com/album/0oGzSazidykcL5XNTEuS9z"
    }
    data['albums'].append(t)
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()

