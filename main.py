from extract import extract_data
from urls import urls

# Lista URL-i

def url_change():
    for url in urls():
        print(f"Dane z {url}:")
        data = extract_data(url)
        for item in data:
            print(item)

url_change()            
