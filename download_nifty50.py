import yfinance as yf
import pandas as pd

# Define function to download NIFTY 50 data
def get_nifty50_data(start="2010-01-01", end="2024-01-01"):
    # "^NSEI" is the Yahoo Finance ticker for NIFTY 50
    nifty50 = yf.download("^NSEI", start=start, end=end)
    
    # Save to CSV file
    nifty50.to_csv("nifty50_data.csv")
    
    print("✅ NIFTY 50 data saved as nifty50_data.csv")

# Run the function
if __name__ == "__main__":
    get_nifty50_data()
