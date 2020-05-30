import time
from pyfiglet import Figlet
import random
import os
import cursor

fonts = ['slant', 'acrobatic', 'alligator', 'bell',
         'big', 'catwalk', 'doom', 'epic', 'isometric1',
         'kban', 'larry3d', 'speed', 'starwars']

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

f = Figlet(font='big')
cursor.hide()
while True:
    try:
        localtime = time.asctime( time.localtime(time.time()) )
        time_split = localtime.split(' ')
        t = time_split[3].replace(':', '     -   ')
        str = '{}      {}       {}\n{}'.format(time_split[0],
                                               time_split[1],
                                               time_split[2], t)

        time.sleep(1)
        os.system('clear')
        print ('\033[1;{};{}m{}'.format(fc['cyan'],
                                        bc['black'],
                                        f.renderText(str)))
    except:
        cursor.show()
        exit()
