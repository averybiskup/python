from PIL import Image, ImageDraw
import random

file = 'flower.jpg'

img = Image.open(file).convert('RGB')

x = img.size[0]
y = img.size[1]

d = ImageDraw.Draw(img)

white = (255, 255, 255)
black = (0, 0, 0)

def random_lines(color):
    for i in range(0, 5000, 30):
        d.line((0, 1) + (random.randrange(0, x), i), fill=color, width=3)


random_lines(black)

name = 'test1'
location = 'drawn_over/' + name + '.jpg'
img.save(location)
img.show()
