import re
from url_helper import extract_offers_from_url



def nfj_title(offer):
    title_nfj = offer.find('h3', {"data-cy": re.compile(r"title position")})
    return  title_nfj.get_text().strip().replace("NOWA", "")

    
def nfj_location(offer):

    return offer.find('span', class_=re.compile(r"tw-text-ellipsis")).get_text().strip()


def nfj_salary(offer):

    return offer.find('span', {"data-cy": re.compile(r"salary ranges")})
        

def nfj_link(offer):

    return offer.find('h3', {"data-cy": re.compile(r"title position")}).parent.parent.parent.parent.get('href')


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
        link = nfj_link(offer)
        print(title, location, salary,f"https://nofluffjobs.com{link}" )


