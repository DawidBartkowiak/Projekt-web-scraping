from bs4 import BeautifulSoup
from requests import get
from extract import extract_data


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

    
'''URL = 'https://nofluffjobs.com/pl/backend?criteria=requirement%3DPython'

page = get(URL)
bs = BeautifulSoup(page.content, features='html.parser')

for offer in bs.find_all('a', class_ = 'posting-list-item'):
    footer = offer.find('h3', class_ = 'posting-title_position')
    print(footer)
    break'''