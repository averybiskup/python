import requests
from bs4 import BeautifulSoup
import re

url = 'https://news.ycombinator.com/rss'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

anchors = soup.find_all('a')

for anchor in anchors:
    try:
        link = anchor['href']
        print(link)
        
    except:
        pass

# this seems to be impossible.. at least the idea I originally had
