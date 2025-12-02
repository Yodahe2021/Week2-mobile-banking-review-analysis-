# 🏦 Mobile Banking Reviews: Sentiment and Theme Analysis

## 🎯 Project Goal

This project implements an end-to-end data science pipeline to ingest, process, analyze, and report on customer reviews of various mobile banking applications. The primary goal is to **extract actionable competitive insights and thematic issues** from customer feedback to inform product strategy for a specific bank (CBE, based on the file structure).

---

## 🛠️ Pipeline Overview

The project follows a standard Extract, Transform, Load (ETL) and Analysis workflow:

1.  **Extract (Scraping)**: Collect raw customer reviews from an external source.
2.  **Transform (Preprocessing & Analysis)**: Clean the text data, calculate sentiment scores, and identify recurring themes.
3.  **Load (Database)**: Store the processed, analyzed data in a persistent relational database.
4.  **Reporting**: Generate competitive metrics and deep-dive visualizations for stakeholders.

## 📁 Directory Structure

| Directory | Content Description | Key Files |
| :--- | :--- | :--- |
| `data/raw` | Initial, unprocessed data files. | `reviews_raw.csv` |
| `data/processed` | Cleaned and feature-engineered datasets. | `reviews_task2_with_sentiment_and_themes.csv` |
| `src/scraper` | Scripts for data acquisition. | `scrape_reviews.py` |
| `src/preprocessing` | Scripts for data cleaning and preparation. | `clean_reviews.py` |
| `src/analysis/sentiment` | Scripts for calculating sentiment scores. | `sentiment_analysis.py` |
| `src/analysis/themes` | Scripts for topic/theme extraction (e.g., using clustering or keyword mapping). | `theme_extraction.py` |
| `src/database` | Scripts for setting up and interacting with the database. | `insert_to_postgres.py`, `create_tables.sql` |
| `notebooks` | Jupyter notebooks for iterative development, exploration, and final report generation. | `task_4_insights_and_visualizations.ipynb` |
| `plots` | Output directory for all generated charts and visualizations. | (e.g., competitive_analysis.png) |
| `reports` | Final output reports and synthesized data summaries. | `task4` directory |

---

## 🚀 Getting Started

### Prerequisites

You will need Python 3.8+ installed.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Yodahe2021/Week2-mobile-banking-review-analysis-.git
    cd WEEK2-MOBILE-BANKING-REVIEWS
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # .\venv\Scripts\activate # On Windows (PowerShell)
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Pipeline

To execute the full data pipeline:

1.  **Data Acquisition:** Run the scraper to get the initial data.
    ```bash
    python src/scraper/scrape_reviews.py
    ```
2.  **Analysis & Processing:** Run the main analysis script (assuming `final_metrics_cbe.py` orchestrates the cleaning, sentiment, and theme steps).
    ```bash
    python src/analysis/final_metrics_cbe.py
    ```
3.  **Database Load (Optional):** Load the results into PostgreSQL. Ensure your `db_config.py` is set up.
    ```bash
    python src/database/insert_to_postgres.py
    ```
4.  **Visualize and Report:** Explore the generated data and create final reports by opening the notebooks:
    ```bash
    jupyter notebook notebooks/task_4_insights_and_visualizations.ipynb
    ```

---

## 📈 Key Findings (Based on Analysis)

* **Competitive Landscape**: Analysis compares **Average Rating** and **Average Sentiment Score** across major mobile banking apps (visualized in `plots/competitive_analysis.png`).
* **CBE Deep Dive**: The most frequently mentioned customer pain points for CBE were aggressively categorized into themes like:
    * **Functional Instability (Bugs/Errors)**
    * **Update and Release Issues**
    * **Performance (Speed and Lag)**

---

## 🤝 Contribution

Contributions are welcome! Please open an issue or submit a pull request for any suggested improvements.

---

