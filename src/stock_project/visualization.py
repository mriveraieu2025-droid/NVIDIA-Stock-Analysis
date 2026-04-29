import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Increase titles/axis for better readability in all graphs
plt.rcParams.update({
    "axes.titlesize": 18,
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.fontsize": 12
})

# 1. Volatility
def plot_volatility(df):
    # Plot 20-day rolling volatility of NVIDIA stock
    plt.figure(figsize=(12, 5))

    plt.plot(df["Date"], df["Volatility_20"], label="20-Day Volatility", linewidth=2)

    plt.title("NVIDIA 20-Day Rolling Volatility", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show()


# 2. NVIDIA Stock evolution
def plot_ai_shock(df):
    # Plot NVIDIA stock price and highlight the start of the AI boom
    plt.figure(figsize=(12, 6))

    # Ensure 'Date' column is in datetime format
    df["Date"] = pd.to_datetime(df["Date"])

    # Extract closing price
    close = df["Close"].values

    # Plot stock price
    plt.plot(df["Date"], close, label="NVDA Price", linewidth=2)

    # Mark ChatGPT launch 
    event_date = pd.to_datetime("2022-11-30")

    # Highlight AI boom period
    plt.axvspan(event_date, df["Date"].max(), alpha=0.2, label="AI Boom Period")
    plt.axvline(event_date, color="red", linestyle="--")

    # Add annotation for clarity
    y_value = float(close.max())
    plt.annotate(
        "ChatGPT Launch\nAI Boom Begins",
        xy=(event_date, y_value * 0.6),
        xytext=(event_date, y_value * 0.8),
        arrowprops=dict(arrowstyle="->", color="red"),
        color="red",
        fontsize=18
    )

    plt.title("Impact of AI Boom on NVIDIA Stock")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")

    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)

    plt.show()


# 3. Actual vs Predicted
def plot_prediction(df):
    # Prepare data
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    # Extract closing prices as a numeric array
    prices = df["Close"]

    if isinstance(prices, pd.DataFrame):
        prices = prices.iloc[:, 0]

    prices = prices.to_numpy().astype(float)

    # Split data into training (80%) and testing (20%)
    split = int(len(prices) * 0.8)
    train = prices[:split]
    test = prices[split:]

    # Fit linear regression model on training data
    x_train = np.arange(len(train))
    coef = np.polyfit(x_train, train, 1)
    model = np.poly1d(coef)

    # Predict values for test period
    x_test = np.arange(len(train), len(prices))
    predicted = model(x_test)

    # Plot results
    plt.figure(figsize=(12, 6))

    # Actual stock price
    plt.plot(df["Date"], prices, label="Actual Price", linewidth=2)

    # Predicted trend (only test period)
    plt.plot(df["Date"].iloc[split:], predicted,
             linestyle="--", color="red", label="Predicted Price")

    # Train/test split line
    plt.axvline(df["Date"].iloc[split],
                linestyle=":", color="black", label="Train/Test Split")

    plt.title("Actual vs Predicted NVIDIA Stock Price", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show()


# 4. Error calculation (MAPE)
def calculate_error(df):
    # Prepare data
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    # Extract closing prices as a numeric array
    prices = df["Close"]

    if isinstance(prices, pd.DataFrame):
        prices = prices.iloc[:, 0]

    prices = prices.to_numpy().astype(float)

    # Split data into training (80%) and testing (20%)
    split = int(len(prices) * 0.8)
    train = prices[:split]
    test = prices[split:]

    # Fit linear regression model
    x_train = np.arange(len(train))
    coef = np.polyfit(x_train, train, 1)
    model = np.poly1d(coef)

    # Predict values for test period
    x_test = np.arange(len(train), len(prices))
    predicted = model(x_test)

    # Compute Mean Absolute Percentage Error (MAPE)
    error = np.mean(np.abs((test - predicted) / test)) * 100

    print(f"Prediction Error (MAPE): {error:.2f}%")

    return error


# 5. Future prediction with uncertainty
def plot_prediction_with_error(df, error):
    # Prepare data
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    # Extract closing prices as a numeric array
    prices = df["Close"]

    if isinstance(prices, pd.DataFrame):
        prices = prices.iloc[:, 0]

    prices = prices.to_numpy().astype(float)

    # Fit linear regression model on all data
    x = np.arange(len(prices))
    coef = np.polyfit(x, prices, 1)
    model = np.poly1d(coef)

    # Predict future values (2 years ahead)
    future_days = 365 * 2
    x_future = np.arange(len(prices) + future_days)
    y_future = model(x_future)

    # Create future date range
    last_date = df["Date"].iloc[-1]
    future_dates = pd.date_range(start=last_date, periods=future_days, freq="D")

    # Convert error (MAPE) into uncertainty range
    error_factor = error / 100
    future_pred = y_future[-future_days:]

    upper = future_pred * (1 + error_factor)
    lower = future_pred * (1 - error_factor)

    # Plot results
    plt.figure(figsize=(12, 6))

    # Actual data
    plt.plot(df["Date"], prices, label="Actual Price", linewidth=2)

    # Predicted future trend
    plt.plot(future_dates, future_pred,
             linestyle="--", color="red", label="Predicted Trend")

    # Uncertainty band
    plt.fill_between(future_dates, lower, upper,
                     color="red", alpha=0.2, label="Prediction Range")

    plt.title("NVIDIA Future Prediction with Uncertainty", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.show()