

# This program makes use of /dlimg.py and /auth_test.py
# it grabs the album covers of whoever is logged in then creates a compiled image of them.


from dlimg import download
from auth_test import get_albums
from auth_test import get_artists_img
import sys
from PIL import Image
import os
import math
import time

# Loops through the albums and downloads each image then stores them in a list
# Images are stored in the /images folder
def dl_images():
    urls = get_artists_img()

    i = 0
    for url in urls:
        download(url, 'img' + str(i) + '.jpg')
        i += 1

# This is where the actual image is created

def compile_images(filename='final.jpg'):
    img_list = os.listdir('images')
    print('Creating collage...')
    time.sleep(0.5)
    print('Images used: ' + str(len(img_list)))
    time.sleep(0.5)

    images = [Image.open('images/' + i) for i in img_list]

    images = [img.resize((640, 640)) for img in images]
   
    if math.sqrt(len(img_list)).is_integer():
        w = math.floor((640 * math.sqrt(len(img_list))))
    else:
        w = 640 * (math.floor(math.sqrt(len(img_list))) + 1)
    
    print('Size of image: {} x {}'.format(w, w))

    new_im = Image.new('RGB', (w, w), (255, 255, 255))

    offset = 640 # All images grabbed from spotify are 640x640 (ONLY WORKS FOR ALBUMS)
    x_offset = 0
    y_offset = 0
    counter = 0
    for i in images:
        new_im.paste(i, (x_offset, y_offset))
        x_offset += offset
        
        if counter == 6:
            x_offset = 0
            y_offset += offset
            counter = 0
        else:
            counter += 1

    print('File: {}'.format(filename))
    new_im.save(filename)
    new_im.show()


dl_images()
compile_images('collage.jpg')

