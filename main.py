from bs4 import BeautifulSoup
from requests import get

URL = 'https://it.pracuj.pl/praca/wronki;wp/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016?rd=50&et=17'

page = get(URL)
bs = BeautifulSoup(page.content, features='html.parser')

for offer in bs.find_all('div', class_='tiles_cobg3mp'):
    
    footer = offer.find('a', class_='tiles_o1859gd9').get_text().strip()
    title = offer.find('h4', class_='tiles_r11dm8ju')
    print(footer,title)
    