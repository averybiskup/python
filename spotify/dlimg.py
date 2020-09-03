#!/usr/local/bin/python3
import requests
import shutil
import sys
import time
import os

directory = 'images'

def print_load():
    for x in range (0,15):
        b = "||" * x
        print (b, end="\r")
        time.sleep(0.1)
    print('\n')

def download(url, name='none'):
    r = requests.get(url, stream=True)
    if name == 'none':
        name = url.split('/')[-1]

    if r.status_code == 200:
        with open(directory + '/' + name, '+wb') as f:
            print_load()
            print('Created Image: ' + name)

            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        print('Unable to access image.')

if __name__ == '__main__':
    download('no')
