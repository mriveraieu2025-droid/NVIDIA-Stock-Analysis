from stock_project.analysis import add_daily_return
import pandas as pd

def test_daily_return():
    df = pd.DataFrame({"Close": [100, 110, 121]})
    df = add_daily_return(df)

    assert "Daily_Return" in df.columns
  assert df["Daily_Return"].iloc[1] == 0.1
