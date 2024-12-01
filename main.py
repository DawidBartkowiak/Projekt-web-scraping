import pandas as pd
import sqlite3
from extract import extract_data
from urls import urls


def create_dataframe():
    # Initializes an empty list to store all job offers
    all_data = []
    # Iterates over each URL in the list of URLs
    for url in urls():
        print(f"Dane z {url}:")
        # Extracts data from the URL
        data = extract_data(url)
        # Extends the all_data list with the extracted data
        all_data.extend(data)
    # Creates a DataFrame from the collected data
    df = pd.DataFrame(all_data, columns=["Title", "Location", "Salary", "Link"])
    # Removes duplicate entries based on the 'Link' column
    return df.drop_duplicates(subset="Link")


def save_to_sqlite(df, db_name="job_offers.db"):
    # Connects to the SQLite database
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
    # Retrieves the maximum id from the table
    cursor.execute("SELECT MAX(id) FROM job_offers")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        max_id = 0

    # Adds an 'id' column to the DataFrame
    df["id"] = range(max_id + 1, max_id + 1 + len(df))

    # Insert data into the table
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT OR IGNORE INTO job_offers (Id,Title, Location, Salary, Link)
            VALUES (?, ?, ?, ?, ?)
        """,
            (row["id"], row["Title"], row["Location"], row["Salary"], row["Link"]),
        )
    # Commits the transaction and closes the connection
    conn.commit()
    conn.close()


def main():
    # Creates a DataFrame from the extracted data
    df = create_dataframe()
    # Saves the DataFrame to a CSV file
    df.to_csv("job_offers.csv", index=False)
    # Saves the DataFrame to the SQLite database
    save_to_sqlite(df)


if __name__ == "__main__":
    # Runs the main function
    main()
