from google_play_scraper import Sort, reviews_all
import pandas as pd
from tqdm import tqdm

BANK_APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.combanketh.mobilebanking",
    "Dashen": "com.dashen.dashensuperapp"
}

def scrape_reviews():
    all_data = []

    for bank, app_id in BANK_APPS.items():
        print(f"Scraping reviews for {bank}...")
        review_list = reviews_all(
            app_id,
            lang="en",
            country="us",
            sort=Sort.NEWEST
        )

        for r in review_list:
            all_data.append({
                "bank": bank,
                "review": r["content"],
                "rating": r["score"],
                "date": r["at"].strftime("%Y-%m-%d"),
                "source": "google-play"
            })

    df = pd.DataFrame(all_data)
    df.to_csv("data/raw/reviews_raw.csv", index=False)
    print("Saved raw reviews to data/raw/reviews_raw.csv")

if __name__ == "__main__":
    scrape_reviews()
