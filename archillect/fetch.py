import requests
from bs4 import BeautifulSoup
from appscript import app, mactypes
import sys
from random import randrange
import os

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
    save_folder = 'save/'
    img_name = f'{folder}{id}.jpg'
    save_img = f'{save_folder}{id}.jpg'
    
    print(img_name)

    with open(img_name, 'wb') as f:
        f.write(requests.get(img_src).content)

    set_image(img_name)

    save = input("Save ?")

    if (save == "y"):
        with open(save_img, 'wb') as f:
            f.write(requests.get(img_src).content)
    if (save == "n"):
        print("removing: ", img_name)
        os.remove(img_name)

if __name__ == "__main__":
    while True:
        id = randrange(39000)
        fetch_image(id)
