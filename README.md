# 📊 Mobile Banking App Review Analysis — Ethiopia  
### *10 Academy Week 2 Challenge (2025)*  
**Data Collection, Cleaning, Sentiment Analysis & Thematic Analysis**

---

## 📝 Project Overview  
This project analyzes customer satisfaction for three major Ethiopian banking apps using **Google Play Store reviews**:

- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia (BOA)**
- **Dashen Bank**

The goal is to support Omega Consultancy in identifying:
- Key **customer pain points**
- Main **drivers of satisfaction**
- Feature improvement opportunities
- Themes for customer complaints and feedback

The project follows the complete pipeline:
1. **Web scraping**  
2. **Preprocessing & cleaning**  
3. **Sentiment analysis (VADER)**  
4. **Thematic analysis (TF-IDF + keyword grouping)**  
5. (Next tasks) Database engineering, insights & visualization

---

## 🏗️ Project Structure

WEEK2-MOBILE-BANKING-REVIEWS
├── .github
│   └── workflows
│       └── ci.yml
├── data
│   ├── processed
│   │   ├── keywords.csv
│   │   ├── reviews_clean.csv
│   │   ├── reviews_task2_with_sentiment_and_th...
│   │   └── reviews_with_sentiment.csv
│   └── raw
│       └── reviews_raw.csv
├── notebooks
│   ├── task_1_exploration.ipynb
│   └── task_2_sentiment_and_themes.ipy...
├── src
│   ├── analysis
│   │   ├── sentiment
│   │   │   └── sentiment_analysis.py
│   │   └── themes
│   │       └── theme_extraction.py
│   ├── preprocessing
│   │   └── clean_reviews.py
│   └── scraper
│       └── scrape_reviews.py
├── tests
├── .venv
├── .gitignore
├── README.md
└── requirements.txt



---

# 🚀 Task-1: Data Collection & Preprocessing

### ✔️ **1. Web Scraping**  
Using `google-play-scraper`, we collected:
- Review text  
- Star rating  
- Date  
- App name  
- Bank  

Scraping target: **400+ reviews per bank (1200+ total)**.

---

### ✔️ **2. Preprocessing**
Performed cleaning:
- Remove duplicates  
- Normalize dates  
- Remove empty reviews  
- Strip whitespace  
- Lowercase text  

---

# 🔍 Task-2: Sentiment & Thematic Analysis

## ✔️ Sentiment Analysis (Option 1 — VADER)

VADER used because:
- Lightweight  
- Fast  
- Works inside notebooks  
- No GPU needed  
- Handles short reviews well  

Each review receives:
- `compound` score  
- Sentiment label (positive/neutral/negative)

---
--

## 🚀 Next Steps (Upcoming Tasks)

| Task | Description | Status |
|------|-------------|--------|
| Task-3 | Topic modeling (LDA) | ⏳ Not started |
| Task-4 | Comparative bank analysis | ⏳ Not started |


---
## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb

