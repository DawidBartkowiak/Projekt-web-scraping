import pandas as pd
import sqlite3
from extract import extract_data
from urls import urls


def create_dataframe():
    all_data = []
    for url in urls():
        print(f"Dane z {url}:")
        data = extract_data(url)
        all_data.extend(data)

    df = pd.DataFrame(all_data, columns=["Title", "Location", "Salary", "Link"])
    return df.drop_duplicates(subset="Link")


def save_to_sqlite(df, db_name="job_offers.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS job_offers (
            id INTEGER PRIMARY KEY ,
            title TEXT,
            location TEXT,
            salary TEXT,
            link MARKDOWN UNIQUE
        )
    """
    )

    cursor.execute("SELECT MAX(id) FROM job_offers")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        max_id = 0

    # Dodaj kolumnę id do DataFrame
    df["id"] = range(max_id + 1, max_id + 1 + len(df))

    # Insert data into the table
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT OR IGNORE INTO job_offers (id,title, location, salary, link)
            VALUES (?, ?, ?, ?, ?)
        """,
            (row["id"], row["Title"], row["Location"], row["Salary"], row["Link"]),
        )

    conn.commit()
    conn.close()


def main():
    df = create_dataframe()
    df.to_csv("job_offers.csv", index=False)
    save_to_sqlite(df)


if __name__ == "__main__":
    main()
