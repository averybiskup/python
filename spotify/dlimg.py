#!/usr/local/bin/python3
import requests
import shutil
import sys
import time
import os

def download(url, name='none'):
    directory = './'
    r = requests.get(url, stream=True)
    if name == 'none':
        name = url.split('/')[-1]

    if r.status_code == 200:
        with open(directory + name + '.jpg', '+wb') as f:
            print('Created Image: ' + name + '.jpg')

            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        print('Unable to access image.')

if __name__ == '__main__':
    download('no', d)
