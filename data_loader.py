import yfinance as yf
import pandas as pd

def get_nifty_data(start="2010-01-01", end="2024-01-01"):
    nifty = yf.download("^NSEI", start=start, end=end)  # NIFTY 50 ticker symbol
    nifty.to_csv("nifty50_data.csv")
    print("Data saved as nifty50_data.csv")

if __name__ == "__main__":
    get_nifty_data()
