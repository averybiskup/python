import requests

r = requests.get('http://www.reddit.com/r/pics/search.json?sort=new')

print(r.json())
