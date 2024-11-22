from bs4 import BeautifulSoup
from requests import get
import re
from sites.nofluffjobs import search_nofluffjobs
from sites.pracujpl import search_pracujpl


def extract_data(url):
    
    results = []
    if 'pracuj.pl' in url:
        search_pracujpl(url)
    elif 'nofluffjobs.com' in url:
        search_nofluffjobs(url)
    return results
