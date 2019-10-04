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


def convert(image, file):

    file = file + '.txt'

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

try:
    if len(sys.argv) >= 2:
        image = sys.argv[1]
        save_as = sys.argv[2]
        convert(image, save_as)
except:
    print('Invalid Arguments [file, save_as]')
