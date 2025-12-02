import pandas as pd
from collections import Counter
import re

# IMPORTANT: Ensure this path is correct for your file
FILE_PATH = "data/processed/reviews_task2_with_sentiment_and_themes.csv"

# Load the data
try:
    df = pd.read_csv(FILE_PATH)
except FileNotFoundError:
    print(f"Error: File not found at {FILE_PATH}. Please check your file path.")
    exit()

# --- 1. Calculate Averages (Rating & Sentiment) ---
cbe_df = df[df['bank'] == 'CBE']
avg_rating = cbe_df['rating'].mean()
avg_sentiment = cbe_df['sentiment_score'].mean()

print("\n--- CBE Performance Metrics ---")
print(f"1. CBE Overall Average Rating: {avg_rating:.2f}")
print(f"2. CBE Overall Average Sentiment Score: {avg_sentiment:.2f}") 

# --- 2. Find Top Themes/Pain Points (Keywords from Low Ratings) ---
# Filter for low ratings (1 or 2 stars)
cbe_pain_points = cbe_df[cbe_df['rating'].isin([1, 2])]

# Combine all review text and tokenize
all_text = ' '.join(cbe_pain_points['review'].astype(str).str.lower())
words = re.findall(r'\b\w{3,}\b', all_text)

# Define stopwords to filter noise (add local language stopwords if possible!)
common_stopwords = ['the', 'and', 'for', 'this', 'that', 'but', 'app', 'not', 'can', 'with', 'cbe', 'mobile', 'bank', 'banking', 'it’s', 'i’m', 'was', 'have', 'very', 'use', 'good', 'now', 'will', 'like', 'just', 'get', 'please', 'make', 'try', 'all', 'been']
filtered_words = [word for word in words if word not in common_stopwords]

# Find the 5 most common words
top_themes = Counter(filtered_words).most_common(5)

print("\n3. CBE Top 5 Pain Point Keywords (Themes):")
for word, count in top_themes:
    print(f"- {word.title()} ({count} mentions)")