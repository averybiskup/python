import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

url = "https://en.wikipedia.org/api/rest_v1/page/related/"
#
# r = requests.get(url).json()
# pages = r['pages']
# pp.pprint(pages[0])

class Article:

    def __init__(self, title, url, extract):
        self.title = title
        self.url = url
        self.extract = extract

    def get_title(self):
        return self.title

    def get_info(self):
        return self.extract

    def get_url(self):
        return self.url

    def print_out(self):
        print(self.get_title() + "\n")
        print("\t" + self.get_info())

class Pages:

    def __init__(self):
        super()
        self.pages = {}

    def add_article(self, article):
        self.pages[article.get_title()] = article

    def list_articles(self):
        for i in self.article_list:
            print(i)

    def get_article(self, name):
        try:
            if self.pages[name]:
                self.pages[name].print_out()
        except:
            print("Article Not Found")

    def article_list(self):
        l = []
        for key, val in self.pages.items():
            l.append(key)
        return l

p = Pages()


def get_pages(input):
    r = requests.get(url + input).json()
    pages = r['pages']

    for i in pages:
        article = Article(i['normalizedtitle'], i['content_urls']['desktop']['page'], i['extract'])
        p.add_article(article)

get_pages('Elephant')

print(p.article_list()[0])
