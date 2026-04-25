import pandas as pd
import numpy as np


def add_moving_average(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df[f"MA_{window}"] = df["Close"].rolling(window=window).mean()
    return df


def add_daily_return(df: pd.DataFrame) -> pd.DataFrame:
    df["Daily_Return"] = df["Close"].pct_change()
    return df


def add_volatility(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df[f"Volatility_{window}"] = df["Daily_Return"].rolling(window=window).std()
    return df


def add_cumulative_return(df: pd.DataFrame) -> pd.DataFrame:
    df["Cumulative_Return"] = (1 + df["Daily_Return"]).cumprod()
    return df


def add_ai_growth_proxy(df: pd.DataFrame) -> pd.DataFrame:
    x = np.arange(len(df))

    # simulate exponential AI growth
    growth = np.exp(x / len(df))

    # normalize between 0 and 1
    growth = (growth - growth.min()) / (growth.max() - growth.min())

    df["AI_Growth"] = growth

    return df