import sqlite3
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


def get_data_from_sqlite(db_name="job_offers.db"):
    # Connects to the SQLite database
    conn = sqlite3.connect(db_name)
    # Executes a SQL query to retrieve all data from the 'job_offers' table and loads it into a DataFrame
    df = pd.read_sql_query("SELECT * FROM job_offers", conn)
    # Closes the database connection
    conn.close()
    # Returns the DataFrame containing the job offers
    return df


def format_table_data(df):
    # Replaces newline characters with <br> tags in all string cells
    df = df.applymap(lambda x: x.replace("\n", "<br>") if isinstance(x, str) else x)
    # Converts the 'link' column to clickable HTML links
    df["link"] = df["link"].apply(
        lambda x: f'<a href="{x}" target="_blank" class="btn btn-link">Link</a>'
    )
    return df


@app.route("/")
def index():
    # Get the filter keyword from the request arguments
    filter_keyword = request.args.get("filter", "")

    # Retrieve data from the SQLite database
    df = get_data_from_sqlite()

    # Filter the DataFrame if a filter keyword is provided
    if filter_keyword:
        df = df[
            df.apply(
                lambda row: row.astype(str)
                .str.contains(filter_keyword, case=False)
                .any(),
                axis=1,
            )
        ]

    # Format the DataFrame for HTML table rendering
    df2 = format_table_data(df)

    # Render the index.html template with the table data
    return render_template(
        "index.html",
        tables=df2.to_html(classes="data", header="true", index=False, escape=False),
    )


if __name__ == "__main__":
    # Runs the Flask application in debug mode
    app.run(debug=True)
