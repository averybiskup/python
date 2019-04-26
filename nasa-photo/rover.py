import requests
import time
import shutil
import datetime
import os
from PIL import Image
import webbrowser

# Getting response with requests lib
response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=100&api_key=DEMO_KEY")
p = response.json()['photos']

images = list(map(lambda x: x['img_src'], p))

webbrowser.open(images[0])

for i in range(500):
    webbrowser.open(images[i])
