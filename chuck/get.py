import requests
import json
import pyperclip
import sys

URL = "https://api.chucknorris.io/jokes/random"

r = requests.get(URL)

if r.status_code == 200:
    data = json.loads(r.text)
    joke = data['value']

def parce(joke, name, gender):
    original = joke
    joke = str(joke)

    joke = joke.replace('Chuck Norris\'', name + '\'s')
    joke = joke.replace('Chuck Norris', name)
    joke = joke.replace('Chuck', name)

    if gender != "M":
        joke = joke.replace(' he ', ' she ')
        joke = joke.replace(' He ', ' She ')
        joke = joke.replace(' his ', ' her ')
        joke = joke.replace(' His ', ' Her ')
        joke = joke.replace(' him ', ' her ')
        joke = joke.replace(' Him ', ' Her ')
        joke = joke.replace(' himself ', ' herself ')
        joke = joke.replace(' Man ', ' Woman ')
        joke = joke.replace(' man ', ' woman ')
        joke = joke.replace(' men ', ' women ')

    print(joke)
    print(original)
    pyperclip.copy(joke)

if len(sys.argv) > 1:
    replace = sys.argv[1]
    if len(sys.argv) > 2:
        gender = sys.argv[2]
    else:
        gender = "M"
    parce(joke, replace, gender)
else:
    print(joke)
    pyperclip.copy(joke)
