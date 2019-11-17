from get import request
import textwrap

from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (2560, 1600), color = (73, 109, 137))

fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 150)
d = ImageDraw.Draw(img)

margin = offset = 30
for line in textwrap.wrap(request(), width=30):
    d.text((margin, offset), line, font=fnt, fill="#ffffff")
    offset += fnt.getsize(line)[1]

img.save('text.png')
