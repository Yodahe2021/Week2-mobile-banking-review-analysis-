import psycopg2
import pandas as pd

# Load data
df = pd.read_csv("data/processed/reviews_clean.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    dbname="bank_reviews",
    user="postgres",
    password="Happy",
    port=5432
)

cur = conn.cursor()

# Get bank_id for each bank
cur.execute("SELECT bank_id, bank_name FROM banks")
bank_map = {name: bank_id for bank_id, name in cur.fetchall()}

# Insert each review
for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO reviews 
        (bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, source)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            bank_map[row["bank"]],
            row["review"],
            row["rating"],
            row["date"],
            row.get("label", None),
            row.get("score", None),
            row["source"]
        )
    )

conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")
