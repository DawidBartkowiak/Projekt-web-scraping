from requests import get
from bs4 import BeautifulSoup
import json


def extract_offers_from_url(url):
    # Sends a GET request to the URL
    response = get(url)
    # Parses the response content with BeautifulSoup
    bs = BeautifulSoup(response.content, "html.parser")
    # Checks if the URL is from 'pracuj.pl' and extracts job offers
    if "pracuj.pl" in url:
        return bs.find_all("div", {"data-test": "default-offer"})
    # Checks if the URL is from 'nofluffjobs.com' and extracts job offers
    if "nofluffjobs" in url:
        return bs.find_all("a", class_="posting-list-item")
    # Checks if the URL is from 'infopraca.pl' and extracts job offers
    if "infopraca.pl" in url:
        bs_string = str(bs)
        return json.loads(bs_string)
    return []
