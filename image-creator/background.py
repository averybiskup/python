from PIL import Image, ImageDraw
from set import set_image
import random

green = (0, 221, 155)
pink = (255, 40, 237)
yellow = (255, 182, 0)
grey = (60, 60, 60)
blue = (12, 85, 120)

colors = [green, pink, yellow, blue]


# Creating
img = Image.new('RGB', (2560, 1600), grey)
x = img.size[0]
y = img.size[1]

d = ImageDraw.Draw(img)
# d.line((0,0)+ (x, 0), fill=pink, width=50)

for i in range(0, y, 30):
    d.line((0, i)+ (random.randrange(0, x), i), fill=random.choice(colors), width=30)

# Saving
name = 'test3'
location = 'backgrounds/' + name + '.jpg'
img.save(location)
img.show()


set_image(location)
