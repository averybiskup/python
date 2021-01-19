import requests
import pprint as pp
import json


def search(term):
    search_url = "Https://en.wikipedia.org/w/api.php?action=query&origin=*&format=json&generator=search&gsrnamespace=0&gsrlimit=5&gsrsearch='{}'".format(term)

    r = requests.get(search_url)

    if r.status_code == 200:
        pp.pprint(r.json())

    data = r.json()

    pages = {}

    for j, i in enumerate(data['query']['pages'].values()):
        p = {
                'title': i['title'],
                'id': i['pageid']
            }

        pages[j] = p
    
    for key, value in pages.items():
        print('[{}] {}'.format(key, value['title']))
    

    while True:
        choice = input('>')



        if int(choice) in pages.keys():
            return pages[int(choice)]
        else:
            print('Invalid Entry.')
            continue


search('apple')

