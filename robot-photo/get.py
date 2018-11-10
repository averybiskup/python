import requests
import shutil
from PIL import Image
from os.path import isfile, join
from os import listdir
import os

text = input("Name: ")

images = os.listdir("images")

def openIMG(img):
    img = Image.open('images/' + img)
    img.show()

def checkFile(text):
    if text in images:
        print('Image already exists.')
        openIMG(text)
        return False

    return True


def download(file):
    if r.status_code == 200:
        with open('images/' + file, 'wb') as f:
            print('Creating file: ' + file)

            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

            openIMG(file)

    else:
        print('Wasn\'t able to access image.')

if text != "":
    r = requests.get("https://robohash.org/" + text, stream=True)
    if checkFile(text + ".jpg"):
        download(getFileName(text))
