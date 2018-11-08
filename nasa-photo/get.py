import requests
import time
import shutil
import datetime
import os

response = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + os.environ['nasa_key'])

content = str(response.content)

# Getting the correct URL
URL = content.split('"url":')[1][1:-5]

# Preparing filename
date = str(datetime.datetime.now().date())
filename = date + ".jpg"

r = requests.get(URL, stream=True)

print("Getting photo from: " + URL)

if r.status_code == 200:
    with open("images/" + filename, 'wb') as f:
        print("Creating file: " + filename)
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

else:
    print("Wasn't able to get image.")
