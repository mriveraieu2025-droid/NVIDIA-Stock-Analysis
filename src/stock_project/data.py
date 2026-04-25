import yfinance as yf
import pandas as pd


def get_stock_data(ticker: str, period: str = "5y") -> pd.DataFrame:
    try:
        df = yf.download(ticker, period=period)

        if df.empty:
            raise ValueError("No data found for this ticker")

        # Reset index so 'Date' becomes a column
        df = df.reset_index()

        return df

    except Exception as e:
        print("Error:", e)
        return None