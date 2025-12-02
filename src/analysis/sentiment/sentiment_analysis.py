import pandas as pd
from transformers import pipeline
from tqdm import tqdm

MODEL = "bert-base-multilingual-cased"def load_data():
    return pd.read_csv("data/processed/reviews_clean.csv")

def analyze_sentiment():
    df = load_data()

    classifier = pipeline("sentiment-analysis", model=MODEL)

    sentiments = []
    scores = []

    print("Running sentiment analysis...")

    for text in tqdm(df["review"], desc="Processing"):
        result = classifier(text[:512])[0]  # avoid long text issues
        sentiments.append(result["label"])
        scores.append(result["score"])

    df["sentiment_label"] = sentiments
    df["sentiment_score"] = scores

    df.to_csv("data/processed/reviews_with_sentiment.csv", index=False)
    print("Saved: data/processed/reviews_with_sentiment.csv")

if __name__ == "__main__":
    analyze_sentiment()
