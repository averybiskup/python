import random
import keyboard
import time
from pyfiglet import Figlet
import os
import sys

os.system('clear')

words = ['white', 'yellow', 'cyan', 'blue', 'purple', 'green', 'red']
fonts = ['slant', 'acrobatic', 'alligator', 'bell', 'big', 'catwalk', 'doom', 'epic', 'isometric1', 'kban', 'larry3d', 'speed', 'starwars']

fc = {
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'purple': 35,
    'cyan': 36,
    'white': 37
}
bc = {
    'black': 40,
    'red': 41,
    'green': 42,
    'yellow': 43,
    'blue': 44,
    'purple': 45,
    'cyan': 46,
    'white': 47
}

score = 0
while True:
    font = random.randrange(31, 38)
    bkg = 40
    word = random.choice(words)

    if score >= 10:
        f = Figlet(font=random.choice(fonts[0:]))
    else:
        f = Figlet(font='slant')
    str = '\033[1;{};{}m{}\033[1;37;40m'.format(font, bkg, f.renderText(word))
    print(str)

    while True:
        if keyboard.is_pressed('o'):
            if fc[word] == font:
                score += 1
                time.sleep(0.5)
                os.system('clear')
                break
            else:
                print('SCORE:', score)
                print(font, word)
                sys.exit(-1)

        if keyboard.is_pressed('p'):
            if fc[word] != font:
                score += 1
                time.sleep(0.5)
                os.system('clear')
                break
            else:
                print('SCORE:', score)
                print(font, word)
                sys.exit(-1)
