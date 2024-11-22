import re
from bs4 import BeautifulSoup
from requests import get
from url_helper import extract_offers_from_url



def nfj_title(offer):

    return  offer.find('h3', {"data-cy": re.compile(r"title position")}).get_text().strip().replace("NOWA", "")

    
def nfj_location(offer):

    return offer.find('span', class_=re.compile(r"tw-text-ellipsis")).get_text().strip()


def nfj_salary(offer):

    return offer.find('span', {"data-cy": re.compile(r"salary ranges")})
        

def search_nofluffjobs(url):
    
    nofluffjobs = extract_offers_from_url(url)

    for offer in nofluffjobs:
        title = nfj_title(offer)
        location = nfj_location(offer)
        salary = nfj_salary(offer)
        if salary is not None:
            salary = salary.get_text().strip().replace("\xa0", " ")
        else:
            salary = "No salary information"
        print(title, location, salary)


