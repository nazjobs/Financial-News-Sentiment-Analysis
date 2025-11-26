import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_headline_length(df, column="headline"):
    """Plots the distribution of headline lengths."""
    if column not in df.columns:
        print(f"Column {column} not found.")
        return

    df["length"] = df[column].astype(str).apply(len)
    plt.figure(figsize=(10, 6))
    sns.histplot(df["length"], bins=50, kde=True)
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.show()


def plot_article_count_per_publisher(df, publisher_col="publisher", top_n=10):
    """Plots top publishers."""
    if publisher_col not in df.columns:
        return

    top_publishers = df[publisher_col].value_counts().head(top_n)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_publishers.values, y=top_publishers.index)
    plt.title(f"Top {top_n} Publishers")
    plt.xlabel("Count")
    plt.show()


def analyze_publication_dates(df, date_col="date"):
    """Plots publication frequency over time."""
    if date_col not in df.columns:
        return

    # Ensure date column is datetime
    df[date_col] = pd.to_datetime(df[date_col])

    daily_counts = df.set_index(date_col).resample("D").size()
    plt.figure(figsize=(14, 7))
    daily_counts.plot()
    plt.title("Article Publication Frequency Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.show()
