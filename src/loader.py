import pandas as pd
import os


def load_news_data(filepath):
    """Loads news data and parses dates."""
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded news data with shape: {df.shape}")

        # Adjust format based on the actual CSV content
        if "date" in df.columns:
            # Coerce errors to handle timezone offsets if needed
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
        return df
    except Exception as e:
        print(f"Error loading news data: {e}")
        return pd.DataFrame()


def load_stock_data(folder_path):
    """Loads all stock CSVs from a folder into a dictionary."""
    stock_data = {}
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return stock_data

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            ticker = file.split(".")[0]
            try:
                df = pd.read_csv(os.path.join(folder_path, file))
                if "Date" in df.columns:
                    df["Date"] = pd.to_datetime(df["Date"])
                    df.set_index("Date", inplace=True)
                stock_data[ticker] = df
                print(f"Loaded {ticker} data with shape: {df.shape}")
            except Exception as e:
                print(f"Error loading {file}: {e}")
    return stock_data
