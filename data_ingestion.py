
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_reviews(movie_id):
    url = f"https://example.com/movies/{movie_id}/reviews"  # Placeholder URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    reviews = []
    for review in soup.find_all('div', class_='review-text'):
        reviews.append(review.get_text())
        
    return pd.DataFrame(reviews, columns=['review_text'])

def save_raw_data(df, file_name="raw_reviews.csv"):
    df.to_csv(file_name, index=False)

# Run the ingestion
if __name__ == "__main__":
    movie_reviews_df = scrape_reviews("movie_id_example")
    save_raw_data(movie_reviews_df)
