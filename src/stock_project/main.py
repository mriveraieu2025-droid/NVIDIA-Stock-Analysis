from stock_project.data import get_stock_data

def main():
    print("Running NVDA analysis...")
    data = get_stock_data("NVDA")

    if data is not None:
        print(data.head())
    else:
        print("No data returned.")

if __name__ == "__main__":
    main()

from stock_project.data import get_stock_data
from stock_project.analysis import add_moving_average

def main():
    print("Running NVDA analysis...")
    
    data = get_stock_data("NVDA")

    if data is not None:
        data = add_moving_average(data, window=5)
        print(data.head())
    else:
        print("No data returned.")

if __name__ == "__main__":
    main()

from stock_project.data import get_stock_data
from stock_project.analysis import add_moving_average
from stock_project.visualization import plot_stock

def main():
    print("Running NVDA analysis...")

    data = get_stock_data("NVDA")

    if data is not None:
        data = add_moving_average(data, window=20)

        print(data.head())
        print(data.shape)
        print(data.index.min())
        print(data.index.max())

        plot_stock(data)
    else:
        print("No data returned.")

if __name__ == "__main__":
    main()

from stock_project.data import get_stock_data
from stock_project.analysis import add_moving_average, add_daily_return
from stock_project.visualization import plot_stock

def main():
    print("Running NVDA analysis...")

    data = get_stock_data("NVDA")

    if data is not None:
        data = add_moving_average(data, window=20)
        data = add_daily_return(data)

        print(data.head())
        print(data.shape)
        print(data.index.min())
        print(data.index.max())

        plot_stock(data)
    else:
        print("No data returned.")

if __name__ == "__main__":
    main()

from stock_project.analysis import add_moving_average, add_daily_return, add_volatility
data = add_moving_average(data, window=20)
data = add_daily_return(data)
data = add_volatility(data, window=20)

plot_volatility(data)

