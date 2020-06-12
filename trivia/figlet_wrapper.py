from pyfiglet import Figlet
import random

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


def p(text, style='slant', font='white', bgc='black'):
    
    if style == 'r':
        f = Figlet(font=random.choice(fonts[0:]))
    else:
        f= Figlet(font=style)
    str = '\033[1;{};{}m{}\033[0m'.format(fc[font], bc[bgc], f.renderText(text))
    
    return str

