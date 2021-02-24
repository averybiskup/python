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

bc = {
    'black': 40,
    'red': 41,
    'green': 42,
    'yellow': 43,
    'blue': 44,
    'purple':435,
    'cyan': 46,
    'white': 47
 }


def p(text, style='slant', font_color='white', bg_color='black'):
    
    if style == None:
        return '\33[1;{};{}m{}\33[1;37;40m'.format(fc[font_color], bc[bg_color], text)

    f= Figlet(font=style)

    return '\33[1;{};{}m{}\33[1;37;40m'.format(fc[font_color], bc[bg_color], f.renderText(text))
