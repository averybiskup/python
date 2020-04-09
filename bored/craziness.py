import random
import time
from playsound import playsound
from multiprocessing import Process

import os
rows, columns = os.popen('stty size', 'r').read().split()


def print_color(text, input_fc='random', input_bc='random'):

    fc = {
        'black': 30,
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

    if input_fc == 'random':
        font = random.randrange(30, 37)
    else:
        font = fc[input_fc]

    if input_bc == 'random':
        bkg = random.randrange(41, 47)
    else:
        bkg = bc[input_bc]


    print('\033[1;{};{}m{}\033[1;37;40m'.format(font, bkg, text))

def sound():
    playsound('code/python/bored/power.wav')

def color():
    for i in range(0, 60):
        str = ' '
        length = random.randrange(15, int(columns))
        txt = str * int(length)
        print_color(txt)
        time.sleep(0.03)

threads = []

if __name__ == '__main__':
    p1 = Process(target = sound)
    p2 = Process(target = color)
    p1.start()
    p2.start()
