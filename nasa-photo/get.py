import requests
import time
import shutil
import datetime
import os
import json
from PIL import Image
from set import set_image

key = json.load(open("nasa_token.json"))
NASA_KEY = key['nasa_key']

# Getting response with requests lib
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + NASA_KEY)

# Getting the correct URL
imgURL = response.json()['url']

# Preparing filename
date = str(datetime.datetime.now().date())
filename = date + ".jpg"

r = requests.get(imgURL, stream=True)

print("Getting photo from: " + imgURL)

# Checking for status
if r.status_code == 200:

    # Opening as f
    with open("images/" + filename, 'wb') as f:
        print("Creating file: " + filename)

        # Decoding
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
        img = Image.open('images/' + filename)
        # img.show()
        set_image(filename)

else:
    print("Wasn't able to get image.")
