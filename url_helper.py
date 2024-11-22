from requests import get
from bs4 import BeautifulSoup

def extract_offers_from_url(url):
    response = get(url)
    bs = BeautifulSoup(response.content, "html.parser")
    if 'pracuj.pl' in url:
        return bs.find_all('div', {"data-test": "default-offer"})
    if 'nofluffjobs' in url:
        return bs.find_all('a',  class_ = "posting-list-item")