import pandas as pd

def add_moving_average(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df[f"MA_{window}"] = df["Close"].rolling(window=window).mean()
    return df
import pandas as pd

def add_moving_average(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df[f"MA_{window}"] = df["Close"].rolling(window=window).mean()
    return df

def add_daily_return(df: pd.DataFrame) -> pd.DataFrame:
    df["Daily_Return"] = df["Close"].pct_change()
    return df

def add_volatility(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df[f"Volatility_{window}"] = df["Daily_Return"].rolling(window=window).std()
    return df