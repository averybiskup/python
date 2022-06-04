import requests
from bs4 import BeautifulSoup

def crawl_url(url):
    req = requests.get(url)
    
    soup = BeautifulSoup(req.content, 'html')

    

    paragraphs = soup.find_all('p')

    for paragraph in paragraphs:
        print(paragraph.get_text())

