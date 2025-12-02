import psycopg2
import pandas as pd
from db_config import DB_CONFIG

def connect():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG["port"]
    )

def insert_banks(cur):
    banks = [
        ("CBE", "Commercial Bank of Ethiopia App"),
        ("BOA", "Bank of Abyssinia App"),
        ("Dashen", "Dashen Bank App")
    ]

    for bank_name, app_name in banks:
        cur.execute(
            """
            INSERT INTO banks (bank_name, app_name)
            VALUES (%s, %s) ON CONFLICT DO NOTHING;
            """,
            (bank_name, app_name)
        )

def insert_reviews(cur, df):

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO reviews (
                bank_id, review_text, rating, review_date,
                sentiment_label, sentiment_score, source
            ) VALUES (
                (SELECT bank_id FROM banks WHERE bank_name = %s),
                %s, %s, %s, %s, %s, %s
            );
        """, (
            row["bank"],
            row["review"],
            row["rating"],
            row["date"],
            row.get("sentiment_label", None),
            row.get("sentiment_score", None),
            row["source"]
        ))

def main():
    df = pd.read_csv("data/processed/reviews_task2_with_sentiment_and_themes.csv")

#
    conn = connect()
    cur = conn.cursor()

    print("Creating tables...")
    with open("src/database/create_tables.sql", "r") as f:
        cur.execute(f.read())
    
    print("Inserting banks...")
    insert_banks(cur)

    print("Inserting reviews...")
    insert_reviews(cur, df)

    conn.commit()
    cur.close()
    conn.close()

    print("Data inserted successfully!")

if __name__ == "__main__":
    main()
