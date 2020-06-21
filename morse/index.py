import random
import sys
import time
import cursor

#TEST

table = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}


def test():
    letter, morse = random.choice(list(table.items()))
    answer = input(morse + " = ")

    if answer == 'exit':
        exit(1)
    elif answer == letter:
        print('Correct!\n------\n')
    else:
        print('Incorrect [' + letter + ']\n-------\n')

if len(sys.argv) > 1:
    while True:
        test()

whitelist = set('abcdefghijklmnopqrstuvwxyz')

color = '\033[1;35;40m'

def spam(text, t):
    cursor.hide()
    length = len(text)
    wait = t/length

    text = ''.join(filter(whitelist.__contains__, text))
    for l in text.lower():
        time.sleep(wait)
        print(color + table[l], end='\r')

    cursor.show()

spam('''
Needed feebly dining oh talked wisdom oppose at. Applauded use attempted strangers now are middleton concluded had. It is tried ﻿no added purse shall no on truth. Pleased anxious or as in by viewing forbade minutes prevent. Too leave had those get being led weeks blind. Had men rose from down lady able. Its son him ferrars proceed six parlors. Her say projection age announcing decisively men. Few gay sir those green men timed downs widow chief. Prevailed remainder may propriety can and.
At distant inhabit amongst by. Appetite welcomed interest the goodness boy not. Estimable education for disposing pronounce her. John size good gay plan sent old roof own. Inquietude saw understood his friendship frequently yet. Nature his marked ham wished.
''', 5)
