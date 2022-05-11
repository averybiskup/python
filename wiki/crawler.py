import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/49170271/no-module-named-beautifulsoup4-in-python3'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

anchors = soup.find_all('a')

http = []
https = []

def trim(link):
    count = 0
    for i in range(0, len(link)):
        if count == 3:
            break
        if link[i] == '/' or link[i] == '?':
            count += 1

    return link[0:i]


for anchor in anchors:
    try:
        link = anchor['href']
        if link[0:5] == 'https':
            print(trim(link))
            https.append(link)
        else:
            http.append(link)
        
    except:
        pass
print(len(http))
print(len(https))


