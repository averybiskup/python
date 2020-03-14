import requests
import shutil
from PIL import Image
import os
import sys

print("Enter your name, and we will output your robot.\n")

# Getting input from user
text = (input("Name: ")).lower()

def removeImages():
    for i in os.listdir('images/'):
        os.remove('images/' + i)
    print("All images removed from images/")
    quit(1)

# Works if you run program with r flag
if len(sys.argv) > 1:
    if sys.argv[1] == "r":
        removeImages()

# List of all files in images folder
images = os.listdir("images")

# Function to open an image, filename with extension, filename without
def openIMG(img, name):
    img = Image.open('images/' + img)
    # img.show()
    os.system('say Hello! my name is, ' + name) # This only works on mac I beleive

# Function to see if file already exists
def checkFile(text):
    if text in images:
        print('Image already exists.')
        openIMG(text, text[0:-4])
        return False

    return True

# Function to download photo
def download(file):
    if r.status_code == 200:
        with open('images/' + file, 'wb') as f:
            print('Creating file: ' + file)

            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

            openIMG(file, file[0:-4])

    else:
        print('Wasn\'t able to access image.')

# Making sure user actually entered something
if text != "":
    r = requests.get("https://robohash.org/" + text, stream=True)
    i = text + ".jpg"
    if checkFile(i):
        download(i)
