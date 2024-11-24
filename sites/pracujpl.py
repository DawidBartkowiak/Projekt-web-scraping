
from url_helper import extract_offers_from_url

def ppl_title(offer):
    return offer.find('h2', {"data-test": "offer-title"}).get_text().strip()


def ppl_location(offer):
    return offer.find('h4', {"data-test": "text-region"}).get_text().strip()


def ppl_salary(offer):
    return offer.find('span', {"data-test": "offer-salary"})


def ppl_link(offer):
    return offer.find('a', href=True).get('href')


def search_pracujpl(url):
        
        ppl_offers = extract_offers_from_url(url)


        for offer in ppl_offers:
            title = ppl_title(offer)
            location = ppl_location(offer)
            salary = ppl_salary(offer)
            if salary is not None:
                salary = salary.get_text().strip().replace("\xa0", " ")
            else:
                salary = "No salary information"
            link = ppl_link(offer)
            print(title, location, salary, link)


