from requests import get
from bs4 import BeautifulSoup
import json


def extract_offers_from_url(url):
    response = get(url)
    bs = BeautifulSoup(response.content, "html.parser")
    if 'pracuj.pl' in url:
        return bs.find_all('div', {"data-test": "default-offer"})
    if 'nofluffjobs' in url:
        return bs.find_all('a',  class_ = "posting-list-item")
    if 'infopraca.pl' in url:
        bs_string = str(bs)
        return json.loads(bs_string)