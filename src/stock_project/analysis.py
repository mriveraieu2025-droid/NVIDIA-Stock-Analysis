import pandas as pd
import numpy as np

def add_moving_average(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    # Calculate moving average of closing price
    df[f"MA_{window}"] = df["Close"].rolling(window=window).mean()
    return df


def add_daily_return(df: pd.DataFrame) -> pd.DataFrame:
    # Calculate daily percentage return
    df["Daily_Return"] = df["Close"].pct_change()
    return df


def add_volatility(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    # Calculate standard deviation of returns
    df[f"Volatility_{window}"] = df["Daily_Return"].rolling(window=window).std()
    return df