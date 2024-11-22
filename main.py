from extract import extract_data

# Lista URL-i
urls = [
    'https://it.pracuj.pl/praca/wronki;wp/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016?rd=50&et=17',
    'https://it.pracuj.pl/praca/wronki;wp/it%20-%20rozw%C3%B3j%20oprogramowania;cc,5016?rd=50',
    'https://nofluffjobs.com/pl/backend?criteria=requirement%3DPython'
]

for url in urls:
    print(f"Dane z {url}:")
    data = extract_data(url)
    for item in data:
        print(item)
