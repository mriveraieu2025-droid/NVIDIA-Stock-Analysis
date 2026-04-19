import matplotlib.pyplot as plt

def plot_stock(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Close"], label="Close Price")
    
    if "MA_20" in df.columns:
        plt.plot(df.index, df["MA_20"], label="MA 20")

    plt.title("NVDA Stock Price - 5 Years")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

def plot_volatility(df):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10,5))
    plt.plot(df.index, df["Volatility_20"], label="Volatility (20d)")

    plt.title("NVDA Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()

    plt.show()