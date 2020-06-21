from figlet_wrapper import p
import requests
import json

URL = 'http://wttr.in/Clovis+CA?format=j1'

r = requests.get(URL)

w = r.json()
print(w['current_condition'])


