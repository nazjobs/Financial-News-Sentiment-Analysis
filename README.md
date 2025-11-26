# Financial News Sentiment & Stock Price Correlation Analysis

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview
This project focuses on the quantitative analysis of financial news data to discover correlations between news sentiment and stock market movements. As part of a Data Engineering challenge, we built a modular Python pipeline that ingests raw financial news, performs Natural Language Processing (NLP) to quantify sentiment, and compares these metrics against technical indicators (SMA, RSI) derived from historical stock prices.

## 🚀 Key Features
*   **Modular Architecture:** Clean separation of concerns with dedicated modules for loading, EDA, sentiment, and technical analysis.
*   **Technical Analysis:** Implementation of **TA-Lib** to calculate Simple Moving Averages (SMA-20, SMA-50), RSI, and MACD.
*   **Sentiment Analysis:** NLP pipeline using **TextBlob** to generate polarity scores for financial headlines.
*   **Robust Data Engineering:** automated timezone normalization (UTC) to handle `tz-naive` vs `tz-aware` datetime conflicts.
*   **Statistical Correlation:** Pearson and Spearman correlation analysis to measure the relationship between sentiment and returns.

## 📂 Project Structure
```text
├── .github/              # CI/CD workflows
├── data/                 # Raw and processed data (gitignored)
├── notebooks/            # Jupyter Notebooks for analysis
│   └── Final_Analysis.ipynb
├── scripts/              # Utility scripts
├── src/                  # Source code packages
│   ├── __init__.py
│   ├── correlation.py    # Statistical correlation logic
│   ├── eda.py            # Exploratory Data Analysis plotting
│   ├── loader.py         # Data ingestion and cleaning
│   ├── sentiment.py      # NLP Sentiment scoring
│   └── technical_analysis.py # TA-Lib wrapper
├── tests/                # Unit tests
├── .gitignore
├── README.md
└── requirements.txt
```

## 🛠️ Installation & Setup

### Prerequisites
*   Python 3.8+
*   TA-Lib C-Library (Required for the python wrapper)

**Arch Linux / CachyOS:**
```bash
yay -S ta-lib
```

**Ubuntu / Debian:**
```bash
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install
```

### Environment Setup
```bash
# Clone the repository
git clone https://github.com/nazjobs/Financial-News-Sentiment-Analysis.git
cd Financial-News-Sentiment-Analysis

# Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Fish: source venv/bin/activate.fish

# Install Dependencies
pip install -r requirements.txt
```

## 📊 Usage
The core analysis is aggregated in the Jupyter Notebook.

1.  Ensure your raw data is located in `data/raw/` (specifically `raw_analyst_ratings.csv` and the `yfinance` folder).
2.  Launch Jupyter:
    ```bash
    jupyter notebook
    ```
3.  Open `notebooks/Final_Analysis.ipynb` and run all cells to generate the report visualizations.

## 📈 Methodology
1.  **EDA:** We analyzed publication frequency and found a significant data spike in 2019-2020, with content dominated by top publishers like "Benzinga".
2.  **Quantitative Analysis:** We overlaid SMA-20 and SMA-50 on AAPL stock data to identify bullish/bearish trends.
3.  **Correlation:** We aligned sentiment scores with daily stock returns. Due to data sparsity in the specific sample window, the correlation results highlighted the importance of high-volume data overlap.

## 📝 License
This project is licensed under the MIT License.
