import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords():
    df = pd.read_csv("data/processed/reviews_with_sentiment.csv")

    tfidf = TfidfVectorizer(
        max_features=30,
        stop_words='english',
        ngram_range=(1, 2)
    )

    vectors = tfidf.fit_transform(df["review"])
    keywords = tfidf.get_feature_names_out()

    keyword_df = pd.DataFrame({"keyword": keywords})

    keyword_df.to_csv("data/processed/keywords.csv", index=False)
    print("Saved keywords → data/processed/keywords.csv")

if __name__ == "__main__":
    extract_keywords()
