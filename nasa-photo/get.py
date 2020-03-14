import requests
import time
import shutil
import datetime
import os
import json
from PIL import Image
from set import set_image
from loader import spam

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

key = json.load(open("nasa_token.json"))
NASA_KEY = key['nasa_key']

# Getting response with requests lib
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + NASA_KEY)

spam(1)

# Getting the correct URL
response_json = response.json()
imgURL = response_json['hdurl']
title = response_json['title']
print(title)

# Preparing filename
date = str(datetime.datetime.now().date())
filename = date + '.jpg'
file_path = 'images/' + filename


r = requests.get(imgURL, stream=True)

print("Getting photo from: " + imgURL)

# Checking for status
if r.status_code == 200:

    # Opening as f
    with open(file_path, 'wb') as f:
        print("Creating file: " + file_path)

        # Decoding
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
        # print(filename)
        # print(os.path.dirname(os.path.abspath(filename)))
        img = Image.open(file_path)
        img = img.resize((2560, 1600))
        img.save(file_path)
        set_image(file_path)
        # if os.path.exists(file_path):
        #     os.remove(file_path)
        # else:
        #     print('The file doesn\'t exist')

else:
    print("Wasn't able to get image.")
