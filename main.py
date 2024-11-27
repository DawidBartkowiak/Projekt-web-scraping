from extract import extract_data
from urls import urls
import pandas as pd


# Lista URL-i


def url_change():
    all_data = []
    for url in urls():
        print(f"Dane z {url}:")
        data = extract_data(url)
        all_data.extend(data)

    df = pd.DataFrame(all_data, columns=["Title", "Location", "Salary", "Link"])
    print(df)

    df.to_csv("job_offers.csv", index=False)


url_change()
