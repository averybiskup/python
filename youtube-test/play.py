import webbrowser
import sys

try:
    link = sys.argv[1]
except:
    link = input('link: ')

vid = link.split('v=')[1].split('&')[0]


webbrowser.open('http://localhost:5000/' + vid)
