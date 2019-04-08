import pytesseract
import os
import sys
import time
try:
    from PIL import Image
except:
    import Image

# Command Line Arguments
# First: Image
# Second: Filename (optional)

image = sys.argv[1]

name = image.split('/')[-1].split('.')[0]

file = sys.argv[2] + '.txt' if len(sys.argv) >= 3 else name + '.txt'

try:
    with open('text/' + file, 'r') as f:
        print('text/' + file + ' : Already Exists')
        exit(1)
except FileNotFoundError:
    for x in range (0,15):
        b = "||" * x
        print (b, end="\r")
        time.sleep(0.1)
    print('\n')

text = str(pytesseract.image_to_string(Image.open(image)))

with open(file, 'w+') as f:
    f.write(text)
    if os.path.isdir("/text"):
        os.rename(file, 'text/' + file)
        print('File Created: ' + 'text/' + file)
    else:
        print('File Created: ' + file)
