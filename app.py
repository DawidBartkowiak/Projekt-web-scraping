import sqlite3
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


def get_data_from_sqlite(db_name="job_offers.db"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT * FROM job_offers", conn)
    conn.close()
    return df


def format_table_data(df):
    df = df.applymap(lambda x: x.replace("\n", "<br>") if isinstance(x, str) else x)
    df["link"] = df["link"].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
    return df


@app.route("/")
def index():
    df = get_data_from_sqlite()
    df2 = format_table_data(df)
    return render_template(
        "index.html",
        tables=df2.to_html(classes="data", header="true", index=False, escape=False),
    )


if __name__ == "__main__":
    app.run(debug=True)
