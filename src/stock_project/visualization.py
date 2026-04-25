import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 🔥 Make all text bigger globally
plt.rcParams.update({
    "axes.titlesize": 16,
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.fontsize": 12
})

# 1. Volatility
def plot_volatility(df):
    plt.figure(figsize=(12, 5))

    plt.plot(df["Date"], df["Volatility_20"], label="20-Day Volatility", linewidth=2)

    plt.title("NVIDIA 20-Day Rolling Volatility", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show()


# 2. AI Impact (Price + Highlight)
def plot_ai_shock(df):
    plt.figure(figsize=(12, 6))

    df["Date"] = pd.to_datetime(df["Date"])

    close = df["Close"]
    if hasattr(close, "iloc") and len(close.shape) > 1:
        close = close.iloc[:, 0]

    plt.plot(df["Date"], close, label="NVDA Price", linewidth=2)

    event_date = pd.to_datetime("2022-11-30")

    # Highlight AI boom period
    plt.axvspan(event_date, df["Date"].max(), alpha=0.2, label="AI Boom Period")
    plt.axvline(event_date, color="red", linestyle="--")

    y_value = float(close.max())

    plt.annotate(
        "ChatGPT Launch\nAI Boom Begins",
        xy=(event_date, y_value * 0.6),
        xytext=(event_date, y_value * 0.8),
        arrowprops=dict(arrowstyle="->", color="red"),
        color="red"
    )

    plt.title("Impact of AI Boom on NVIDIA Stock", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show()


# 3. Actual vs Predicted
def plot_prediction(df):
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    prices = df["Close"]
    if hasattr(prices, "iloc") and len(prices.shape) > 1:
        prices = prices.iloc[:, 0]
    prices = prices.astype(float).to_numpy().flatten()

    split = int(len(prices) * 0.8)

    train = prices[:split]
    test = prices[split:]

    x_train = np.arange(len(train))
    coef = np.polyfit(x_train, train, 1)
    model = np.poly1d(coef)

    x_test = np.arange(len(train), len(prices))
    predicted = model(x_test)

    plt.figure(figsize=(12, 6))

    plt.plot(df["Date"], prices, label="Actual Price", linewidth=2)
    plt.plot(df["Date"].iloc[split:], predicted, linestyle="--", color="red", label="Predicted Price")

    plt.axvline(df["Date"].iloc[split], linestyle=":", color="black", label="Train/Test Split")

    plt.title("Actual vs Predicted NVIDIA Stock Price", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show()


# 4. Error calculation
def calculate_error(df):
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    prices = df["Close"]
    if hasattr(prices, "iloc") and len(prices.shape) > 1:
        prices = prices.iloc[:, 0]
    prices = prices.astype(float).to_numpy().flatten()

    split = int(len(prices) * 0.8)

    train = prices[:split]
    test = prices[split:]

    x_train = np.arange(len(train))
    coef = np.polyfit(x_train, train, 1)
    model = np.poly1d(coef)

    x_test = np.arange(len(train), len(prices))
    predicted = model(x_test)

    error = np.mean(np.abs((test - predicted) / test)) * 100

    print(f"Prediction Error (MAPE): {error:.2f}%")

    return error


# 5. Future prediction with uncertainty
def plot_prediction_with_error(df, error):
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    prices = df["Close"]
    if hasattr(prices, "iloc") and len(prices.shape) > 1:
        prices = prices.iloc[:, 0]
    prices = prices.astype(float).to_numpy().flatten()

    x = np.arange(len(prices))
    coef = np.polyfit(x, prices, 1)
    model = np.poly1d(coef)

    future_days = 365 * 2
    x_future = np.arange(len(prices) + future_days)
    y_future = model(x_future)

    last_date = df["Date"].iloc[-1]
    future_dates = pd.date_range(start=last_date, periods=future_days, freq="D")

    error_factor = error / 100
    future_pred = y_future[-future_days:]

    upper = future_pred * (1 + error_factor)
    lower = future_pred * (1 - error_factor)

    plt.figure(figsize=(12, 6))

    plt.plot(df["Date"], prices, label="Actual Price", linewidth=2)
    plt.plot(future_dates, future_pred, linestyle="--", color="red", label="Predicted Trend")
    plt.fill_between(future_dates, lower, upper, color="red", alpha=0.2, label="Prediction Range")

    plt.title("NVIDIA Future Prediction with Uncertainty", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show()