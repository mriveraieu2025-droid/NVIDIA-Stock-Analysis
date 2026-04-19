import pandas as pd

def add_moving_average(df: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    df["MA_" + str(window)] = df["Close"].rolling(window=window).mean()
    return df
