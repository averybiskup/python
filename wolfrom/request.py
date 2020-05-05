import requests
import json
import sys


def ask(q):
    with open('secret.json') as f:
        key = json.loads(f.read())['key']

    URL = 'http://api.wolframalpha.com/v1/result?appid={}'.format(key)

    r = requests.get(URL + q)

    if r.status_code == 200:
        print(r.text)
    else:
        print('Bad query')


if len(sys.argv) > 2:
    query = '&i=' + ' '.join(sys.argv[1:])
    ask(query)
else:
    query = '&i=' + input('question: ')
    ask(query)
