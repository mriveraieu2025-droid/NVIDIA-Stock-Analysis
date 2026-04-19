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
