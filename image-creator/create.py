# Gets the quote of the day, and prints it onto a background with random color, optionally sets it as your wall paper


from get import request
from set import set_image
import textwrap
import os
import datetime
from PIL import Image, ImageDraw, ImageFont
import random


def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def new_image(text, size, bgcolor, textcolor, outfile, set):
    img = Image.new('RGB', size, color = bgcolor)

    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 100)
    d = ImageDraw.Draw(img)

    offset = 40
    margin = 50
    for line in textwrap.wrap(text, width=30):
        d.text((margin, offset), line, font=fnt, fill = textcolor)
        offset += fnt.getsize(line)[1]

    filename = 'images/' + outfile + ".png"
    img.save(filename)
    if set:
        set_image(filename)


date = str(datetime.datetime.now().date())
filename = date + '3'

new_image(request(), (2560, 1600), random_color(), "#FFFFFF", filename, False)
