from google_play_scraper import Sort, reviews_all
import pandas as pd
from tqdm import tqdm

BANK_APPS = {
    "CBE": {
        "app_id": "com.combanketh.mobilebanking",
        "app_name": "CBE Mobile Banking "
    },
    "BOA": {
        "app_id": "com.boa.boaMobileBanking",
        "app_name": "BoA Mobile"
    },
    "Dashen": {
        "app_id": "com.dashen.dashensuperapp",
        "app_name": "Dashen SuperApp"
    }
}

def scrape_reviews():
    all_data = []

    for bank, info in BANK_APPS.items():
        app_id = info["app_id"]
        app_name = info["app_name"]

        print(f"Scraping reviews for {bank} ({app_name})...")

        review_list = reviews_all(
            app_id,
            lang="en",
            country="us",
            sort=Sort.NEWEST
        )

        for r in review_list:
            all_data.append({
                "bank": bank,
                "app_name": app_name,
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
