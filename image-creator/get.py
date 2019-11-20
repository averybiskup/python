import requests

def request():

    url = "http://quotes.rest/qod.json"

    r = requests.get(url)

    q = r.json()
    try:
        text = q['contents']['quotes'][0]
        send = '"' + text['quote'] + '"\n\n\n\n - ' + text['author']
        print(send)
        return send
    except:
        msg = q['error']['message']
        return msg
