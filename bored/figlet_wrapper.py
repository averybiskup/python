from pyfiglet import Figlet

fc = {
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'purple': 35,
    'cyan': 36,
    'white': 37 
 }

fc = {
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'purple': 35,
    'cyan': 36,
    'white': 37
 }


def p(text, style='slant', fc='white', bgc='black'):
    
    f= Figlet(font=style)
    str = '\33[1;{};{}m{}\33[1;37;40m'.format(fc, bgc, f.renderText(text))
    
    return str
