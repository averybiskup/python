import psutil
from PIL import Image
import os
import time
PATH = '../../../../../Users/averybiskup/Library/Application Support/discord/Cache/'

list = os.listdir(PATH)

recent = []

AMOUNT = input('How many images?\n')

if not AMOUNT:
    AMOUNT = 3
else:
    AMOUNT = int(AMOUNT)

for i in range(AMOUNT):
    string = ''
    largest = 0
    for i in list:
        hex = i[2:]
        if str.startswith(hex, '0'):
            dec = int(hex, 16)
        else:
            dec = 0
        if dec > largest:
            largest = dec
            string = i
            # print(i)

    recent.append(string)
    list.remove(string)


# FILE_NAME = input('File: ')


for FILE_NAME in recent:

    if not os.path.exists(PATH + FILE_NAME):
        exit(1)
    else:
        img = Image.open(PATH + FILE_NAME).convert('RGB')
        FILE_SAVE = FILE_NAME + '.jpg'
        img.show()

        time.sleep(2)
        os.system('killall -9 Preview')

        remove = input('Keep? (y/n):\n')

        if remove == 'y':
            img.save(FILE_SAVE)
