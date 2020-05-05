import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

url = "https://en.wikipedia.org/api/rest_v1/page/related/"

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

    def __init__(self, input, amount=5):
        super()
        self.pages = {}
        self.num_pages = 0
        self.input = input
        self.amount = amount

        self.request()


    def request(self):
        r = requests.get(url + self.input)

        if r.status_code != 200:
            self.no_articles(self.input)
        r = r.json()

        pages = r['pages']

        n = 0
        for i in pages:
            n += 1
            self.add_article(Article(i['normalizedtitle'], i['content_urls']['desktop']['page'], i['extract']))
            self.num_pages += 1

            if n >= self.amount:
                break

    def add_article(self, article):
        self.pages[article.get_title()] = article

    def no_articles(self, name):
        print('There are no such articles.')
        exit(0)

    def list_articles(self):
        l = []
        for article_name in self.pages:
            l.append(article_name)
        return l

    def print_list(self):
        n = 1
        for i in self.list_articles():
            print('[{}]'.format(n), i)
            n += 1

    def get_first_article(self):
        self.get_article(self.list_articles()[0])

    def get_article(self, name):
        try:
            if self.pages[name]:
                self.pages[name].print_out()
        except:
            print("Article Not Found")

    def choose_article(self):
        self.print_list()
        num = int(input(': ')) - 1
        self.get_article(self.list_articles()[num])

item = input('Search: ')

p = Pages(item, 5)

p.choose_article()
