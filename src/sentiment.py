from textblob import TextBlob
import pandas as pd


def get_sentiment(text):
    """Returns polarity score using TextBlob."""
    try:
        # Convert to string just in case input is not string
        blob = TextBlob(str(text))
        return blob.sentiment.polarity
    except Exception as e:
        print(f"Error processing text: {e}")
        return 0.0


def analyze_sentiment(df, text_col="headline"):
    """Applies sentiment analysis to the dataframe."""
    print("Running sentiment analysis...")
    # Ensure column exists
    if text_col not in df.columns:
        print(f"Column {text_col} not found in DataFrame.")
        return df

    df["sentiment_score"] = df[text_col].apply(get_sentiment)
    return df
