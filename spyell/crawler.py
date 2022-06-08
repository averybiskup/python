import requests
from bs4 import BeautifulSoup

def crawl_url(url):

    # grab web content
    req = requests.get(url)
    
    # import into bs4
    soup = BeautifulSoup(req.content, 'html')

    # grab all p tags
    paragraphs = soup.find_all('p')

    # print out the text in each p tag
    for paragraph in paragraphs:
        print(paragraph.get_text())

