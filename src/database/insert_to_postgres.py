import psycopg2
import pandas as pd
# Ensure db_config.py is in the database folder and defines the DB_CONFIG dictionary
from db_config import DB_CONFIG 
from psycopg2.extras import execute_batch


def connect():
    """Establishes a connection to the PostgreSQL database."""
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG["port"]
    )


def insert_banks(cur):
    """Inserts bank names into the banks table."""
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


def get_bank_id_map(cur):
    """Fetches bank_name to bank_id mapping from Postgres."""
    cur.execute("SELECT bank_name, bank_id FROM banks;")
    return {name: id for name, id in cur.fetchall()}


def insert_reviews(cur, df, bank_id_map):
    """
    Optimized batch insertion of review data, excluding theme_label.
    """
    
    # 1. Prepare the SIMPLIFIED SQL template (7 placeholders for 7 columns)
    insert_query = """
        INSERT INTO reviews (
            bank_id, review_text, rating, review_date,
            sentiment_label, sentiment_score, source 
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s
        ); 
    """
    
    # 2. Prepare the data: create a list of tuples (7 elements total)
    data_to_insert = [
        (
            bank_id_map.get(row["bank"]),   # 1st %s: The actual bank_id (INT)
            row["review"],
            row["rating"],
            row["date"],
            row.get("sentiment_label", None),
            row.get("sentiment_score", None),
            row["source"] # 7th element
        )
        for _, row in df.iterrows()
    ]
    
    # 3. Execute the batch insertion
    print(f"Executing batch insertion for {len(data_to_insert)} reviews...")
    execute_batch(cur, insert_query, data_to_insert)
    print("Batch insertion complete.")


def main():
    # Ensure this file exists and contains the results of Task 2
    df = pd.read_csv("data/processed/reviews_task2_with_sentiment_and_themes.csv")

    conn = connect()
    cur = conn.cursor()

    # NOTE: The create_tables.sql must NOT contain the theme_label column for this script to work!
    print("Creating tables...")
    with open("src/database/create_tables.sql", "r") as f:
        cur.execute(f.read())
    
    print("Inserting banks...")
    insert_banks(cur)
    
    # Get the Bank ID map after banks are inserted
    bank_id_map = get_bank_id_map(cur) 

    print("Inserting reviews...")
    insert_reviews(cur, df, bank_id_map) 

    conn.commit()
    cur.close()
    conn.close()

    print("Data inserted successfully!")


if __name__ == "__main__":
    main()