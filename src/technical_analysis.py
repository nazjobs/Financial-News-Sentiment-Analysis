import talib
import pandas as pd


def apply_technical_indicators(df):
    """Applies SMA, RSI, and MACD to the stock dataframe."""
    # Ensure data is sorted by date
    df = df.sort_index()

    # Simple Moving Averages
    df["SMA_20"] = talib.SMA(df["Close"], timeperiod=20)
    df["SMA_50"] = talib.SMA(df["Close"], timeperiod=50)

    # Relative Strength Index
    df["RSI"] = talib.RSI(df["Close"], timeperiod=14)

    # MACD (Moving Average Convergence Divergence)
    df["MACD"], df["MACD_signal"], df["MACD_hist"] = talib.MACD(
        df["Close"], fastperiod=12, slowperiod=26, signalperiod=9
    )

    return df
