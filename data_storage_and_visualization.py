
import pandas as pd
import sqlite3
import plotly.express as px

# Store data in SQLite
def store_data_sqlite(file_name="preprocessed_reviews.csv", db_name="movies.db"):
    conn = sqlite3.connect(db_name)
    df = pd.read_csv(file_name)
    df.to_sql("processed_reviews", conn, if_exists="replace", index=False)
    conn.close()

# Visualization function
def visualize_review_length_distribution():
    df = pd.read_csv("preprocessed_reviews.csv")
    fig = px.histogram(df, x="review_length", title="Distribution of Review Length")
    fig.show()

# Run storage and visualization
if __name__ == "__main__":
    store_data_sqlite()
    visualize_review_length_distribution()
