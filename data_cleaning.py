
import pandas as pd
import re

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters
    text = text.lower().strip()  # Convert to lowercase and strip whitespace
    return text

def load_and_clean_data(file_name="raw_reviews.csv"):
    df = pd.read_csv(file_name)
    df['cleaned_review'] = df['review_text'].apply(clean_text)
    return df

# Clean data and save
if __name__ == "__main__":
    cleaned_data = load_and_clean_data()
    cleaned_data.to_csv("cleaned_reviews.csv", index=False)
