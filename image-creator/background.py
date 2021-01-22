# creates weird looking images

from PIL import Image, ImageDraw
from set import set_image
import random

green = (0, 221, 155)
pink = (255, 40, 237)
yellow = (255, 182, 0)
grey = (60, 60, 60)
blue = (12, 85, 120)
white = (255, 255, 255)
black = (0,0,0)

colors = [green, pink, yellow, blue]


# Creating
img = Image.new('RGB', (2560, 1600), grey)
x = img.size[0]
y = img.size[1]

d = ImageDraw.Draw(img)
# d.line((0,0)+ (x, 0), fill=pink, width=50)

def random_lines(colors=colors, width=30, distance=30):
    for i in range(0, y, distance):
        d.line((0, i) + (random.randrange(0, x), i), fill=random.choice(colors), width=width)

def vertical_lines(color, width=1):
    for i in range(0, round(x*1.5), 5):
        d.line((i, 0) + (random.randrange(0, x), y), fill=color, width=width)


vertical_lines(blue, 4)
random_lines([white], 3, 7)

# Saving
name = 'test12'
location = 'backgrounds/' + name + '.jpg'
img.save(location)
img.show()


# set_image(location)
