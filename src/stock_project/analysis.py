import pandas as pd

def add_moving_average(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df[f"MA_{window}"] = df["Close"].rolling(window=window).mean()
    return df
