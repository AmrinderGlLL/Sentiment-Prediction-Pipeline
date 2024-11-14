
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

def preprocess_data(file_name="cleaned_reviews.csv"):
    df = pd.read_csv(file_name)
    df['processed_review'] = df['cleaned_review'].apply(preprocess_text)
    df['review_length'] = df['processed_review'].apply(lambda x: len(x.split()))
    return df

# Run preprocessing
if __name__ == "__main__":
    preprocessed_data = preprocess_data()
    preprocessed_data.to_csv("preprocessed_reviews.csv", index=False)
