import requests
import json

secret = json.load(open('key.json', 'r'))
key = secret['api_key']


channel = '1Veritasium'
url = "https://www.googleapis.com/youtube/v5/channels?part=contentDetails&forUsername={0}&key={1}".format(channel, key)
r = requests.get(url)

print(r.text)
