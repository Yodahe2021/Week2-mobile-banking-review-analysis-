import pandas as pd

df = pd.read_csv("data/raw/reviews_raw.csv")

# Remove duplicates
df = df.drop_duplicates(subset=["review"])

# Drop rows with missing reviews
df = df.dropna(subset=["review"])

# Clean text
df["review"] = df["review"].str.strip()

# Normalize date format
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Save processed
df.to_csv("data/processed/reviews_clean.csv", index=False)

print("Cleaned dataset saved to data/processed/reviews_clean.csv")
