import requests
from bs4 import BeautifulSoup
from appscript import app, mactypes
import sys
from PIL import Image
from random import randrange

URL = "https://archillect.com"

def set_image(file):
    file = file
    app('Finder').desktop_picture.set(mactypes.File(file))

def fetch_image(id):
    html = requests.get(f"{URL}/{id}")
    soup = BeautifulSoup(html.content, "html.parser")
    results = soup.find(id="ii")

    img_src = results['src']
    folder = 'backgrounds/'
    img_name = f'{folder}{id}.jpg'
    
    print(img_name)

    with open(img_name, 'wb') as f:
        f.write(requests.get(img_src).content)

    set_image(img_name)

if __name__ == "__main__":
    id = randrange(39000)
    fetch_image(id)
