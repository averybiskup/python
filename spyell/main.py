from crawler import crawl_url

def get_user_input():
    url = input('url:')
    crawl_url(url)


if __name__ == "__main__":
    get_user_input()
