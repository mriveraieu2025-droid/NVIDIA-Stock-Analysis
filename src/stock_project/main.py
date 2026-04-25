from stock_project.data import get_stock_data
from stock_project.analysis import (
    add_moving_average,
    add_daily_return,
    add_volatility
)
from stock_project.visualization import (
    plot_volatility,
    plot_ai_shock,
    plot_prediction,
    calculate_error,
    plot_prediction_with_error
)


def main():
    print("Running NVIDIA analysis...")

    df = get_stock_data("NVDA")

    if df is not None:
        df = add_moving_average(df, 20)
        df = add_daily_return(df)
        df = add_volatility(df, 20)

        # Graphs:
        plot_ai_shock(df)
        plot_volatility(df)
        plot_prediction(df)

        # Error calculation
        error = calculate_error(df)

        # Final graph with uncertainty
        plot_prediction_with_error(df, error)

    else:
        print("No data returned.")


if __name__ == "__main__":
    main()