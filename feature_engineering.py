import pandas as pd

def add_features(data):
    print("Available columns:", data.columns)  # Debugging line

    # Check if 'Adj Close' is present
    if "Adj Close" not in data.columns:
        raise ValueError("Column 'Adj Close' not found. Check your CSV file for the correct column name.")

    # Convert to numeric (handle errors)
    data["Adj Close"] = pd.to_numeric(data["Adj Close"], errors="coerce")
    data.dropna(inplace=True)

    # Feature Engineering
    data["Return"] = data["Adj Close"].pct_change()
    data["SMA_10"] = data["Adj Close"].rolling(window=10).mean()
    data["SMA_50"] = data["Adj Close"].rolling(window=50).mean()
    data["Volatility"] = data["Return"].rolling(window=10).std()

    data.dropna(inplace=True)
    
    return data

if __name__ == "__main__":
    df = pd.read_csv("nifty50_data.csv")
    
    # Check for the correct column
    print("Column Names in CSV:", df.columns)  # Debugging line

    # Rename 'Close' to 'Adj Close' if necessary
    if "Adj Close" not in df.columns and "Close" in df.columns:
        df.rename(columns={"Close": "Adj Close"}, inplace=True)

    # Ensure 'Date' column exists
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.set_index("Date", inplace=True)
    else:
        print("Warning: 'Date' column not found. Proceeding without setting an index.")

    df = add_features(df)
    df.to_csv("nifty50_features.csv")
    print("Feature engineered data saved as nifty50_features.csv")
