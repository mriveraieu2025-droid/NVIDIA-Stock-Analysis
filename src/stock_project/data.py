import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str) -> pd.DataFrame:
    try:
        data = yf.download(ticker, period="1mo")

        if data.empty:
            raise ValueError("Invalid ticker or no data found")

        return data

    except Exception as e:
        print("Error:", e)
        return None