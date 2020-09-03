

# This program makes use of /dlimg.py and /auth_test.py
# it grabs the album covers of whoever is logged in then creates a compiled image of them.


from dlimg import download
from auth_test import get_albums
import sys
from PIL import Image
import os
import math

# Loops through the albums and downloads each image then stores them in a list
# Images are stored in the /images folder
def dl_images():
    urls = get_albums()
    print(urls)

    i = 0
    for url in urls:
        download(url, 'img' + str(i) + '.jpg')
        i += 1

# This is where the actual image is created

def compile_images():
    img_list = os.listdir('images')

    images = [Image.open('images/' + i) for i in img_list]
    
    w = 640 * (math.floor(math.sqrt(len(img_list))) + 1)
    print(w)
    
    new_im = Image.new('RGB', (w, w), (255, 255, 255))

    offset = 640
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

    new_im.save('final.jpg')
    new_im.show()
compile_images()



