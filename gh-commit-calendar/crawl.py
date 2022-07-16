# The idea for this project is to turn this into a api that anyone can hit
# with a given username, and will return info about the user's gh activity.

import requests
from bs4 import BeautifulSoup
import re

url = 'https://github.com/averybiskup'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')

rects = soup.find_all("rect", { "class": "ContributionCalendar-day" })

total = 0

for tag in rects:

    level = int(tag["data-level"])
    
    try:
        count = int(tag["data-count"])
        total += count
    except:
        pass

print(total)
