# Projekt-web-scraping

## Opis projektu

Projekt służy do ekstrakcji ofert pracy z różnych stron internetowych i zapisywania ich w bazie danych SQLite oraz pliku CSV. Aplikacja webowa umożliwia przeglądanie ofert pracy oraz filtrowanie ich według słów kluczowych.

## Struktura projektu

```
.
├── .gitignore
├── app.py
├── extract.py
├── job_offers.csv
├── main.py
├── README.md
├── sites/
│   ├── infopraca.py
│   ├── nofluffjobs.py
│   └── pracujpl.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── url_helper.py
└── urls.py
```

## Wymagania

- Python 3.x
- Flask
- pandas
- requests
- BeautifulSoup4

## Uruchomienie
1. Uruchom skrypt `main.py`, aby pobrać oferty pracy i zapisać je w bazie danych oraz pliku CSV:
    ```sh
    python main.py
    ```
2. Uruchom aplikację Flask:
    ```sh
    python app.py
    ```
3. Otwórz przeglądarkę i przejdź do `http://127.0.0.1:5000/`, aby zobaczyć oferty pracy.


## Pliki

- `app.py`: Plik uruchamiający aplikację Flask.
- `extract.py`: Plik zawierający funkcje do ekstrakcji ofert pracy z różnych stron.
- `main.py`: Plik główny, który pobiera dane i zapisuje je w bazie danych oraz pliku CSV.
- `url_helper.py`: Plik zawierający funkcję do pobierania ofert pracy z URL.
- `urls.py`: Plik zawierający listę URL do ekstrakcji ofert pracy.
- `sites/`: Katalog zawierający skrypty do ekstrakcji ofert pracy z poszczególnych stron.
- `templates/`: Katalog zawierający szablony HTML dla aplikacji Flask.
- `static/`: Katalog zawierający plik statyczny, taki jak arkusz stylów CSS.
## Autor

Dawid Bartkowiak