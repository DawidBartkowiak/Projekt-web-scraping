from bs4 import BeautifulSoup
from requests import get

def extract_data(url):
    page = get(url)
    bs = BeautifulSoup(page.content, features='html.parser')
    
    results = []
    for offer in bs.find_all('div', {"data-test": "default-offer"}):
        title = offer.find('h2', {"data-test": "offer-title"}).get_text().strip()
        location = offer.find('h4', {"data-test": "text-region"}).get_text().strip()
        salary = offer.find('span', {"data-test": "offer-salary"})
        if salary is not None:
            salary = salary.get_text().strip().replace("\xa0", " ")
        else:
            salary = "Brak informacji o wynagrodzeniu"
        link = offer.find('a', href=True).get('href')
        results.append((title, salary, location, link))
    return results


