import requests
import shutil
import sys
import time

def print_load():
    for x in range (0,15):
        b = "||" * x
        print (b, end="\r")
        time.sleep(0.1)
    print('\n')

def download(url, name='name.png'):
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(name, 'wb') as f:
            print_load()
            print('Created Image: ' + name)

            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        print('Unable to access image.')

if len(sys.argv) >= 3:
    URL = sys.argv[1]
    NAME = sys.argv[2] + "png"
    download(URL, NAME)
else:
    print('No arguments given.')
