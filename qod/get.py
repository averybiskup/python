import requests

url = "http://quotes.rest/qod.json"

r = requests.get(url)

q = r.json()
try:
    text = q['contents']['quotes'][0]
    print('"' + text['quote'] + '"\n\n\t- ' + text['author'])
except:
    msg = q['error']['message']
    print(msg)
