from bs4 import BeautifulSoup
from requests import get

def extract_data(url):
    page = get(url)
    bs = BeautifulSoup(page.content, features='html.parser')
    
    results = []
    for offer in bs.find_all('div', {"data-test": "default-offer"}):
        footer = offer.find('h2', {"data-test": "offer-title"}).get_text().strip()
        location = offer.find('h4', {"data-test": "text-region"}).get_text().strip()
        salary = offer.find('span', {"data-test": "offer-salary"})
        if salary is not None:
            salary = salary.get_text().strip().replace("\xa0", " ")
        else:
            salary = "Brak informacji o wynagrodzeniu"
        link = offer.find('a', href=True).get('href')
        results.append((footer, salary, location, link))
    return results

# Lista URL-i
urls = [
    'https://it.pracuj.pl/praca/wronki;wp/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016?rd=50&et=17',
    'https://it.pracuj.pl/praca/wronki;wp/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016?rd=50'
]

for url in urls:
    print(f"Dane z {url}:")
    data = extract_data(url)
    for item in data:
        print(item)

    
