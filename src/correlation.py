import pandas as pd
from scipy.stats import pearsonr, spearmanr


def calculate_daily_returns(stock_df):
    """Calculates daily percentage change."""
    # Create a copy to avoid SettingWithCopyWarning
    df = stock_df.copy()
    df["Daily_Return"] = df["Close"].pct_change()
    return df


def align_and_correlate(news_df, stock_df, ticker):
    """
    Aggregates news sentiment by date and correlates with stock returns.
    """
    # Filter news for the specific ticker
    ticker_news = news_df[news_df["stock"] == ticker].copy()

    if ticker_news.empty:
        print(f"No news found for {ticker}")
        return pd.DataFrame(), 0, 0

    # Normalize dates (remove time) for merging
    # We convert to UTC first to handle potential mixed timezones, then strip tz info
    ticker_news["date_only"] = (
        pd.to_datetime(ticker_news["date"], utc=True)
        .dt.tz_localize(None)
        .dt.normalize()
    )

    # Aggregate sentiment (mean score per day)
    daily_sentiment = ticker_news.groupby("date_only")["sentiment_score"].mean()

    # Prepare stock data
    stock_returns = stock_df["Daily_Return"]
    # Ensure stock index is also standard and tz-naive
    stock_returns.index = (
        pd.to_datetime(stock_returns.index, utc=True).tz_localize(None).normalize()
    )

    # Merge the two series
    merged_df = pd.concat([daily_sentiment, stock_returns], axis=1).dropna()
    merged_df.columns = ["sentiment", "return"]

    # Calculate Correlation
    if len(merged_df) > 1:
        corr_pearson, _ = pearsonr(merged_df["sentiment"], merged_df["return"])
        corr_spearman, _ = spearmanr(merged_df["sentiment"], merged_df["return"])
        return merged_df, corr_pearson, corr_spearman
    else:
        print(f"Not enough overlapping data for {ticker}")
        return pd.DataFrame(), 0, 0
