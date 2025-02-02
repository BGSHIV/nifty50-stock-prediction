import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load data
df = pd.read_csv("nifty50_features.csv")

# Debugging step: Print available columns
print("Columns in CSV:", df.columns)

# Ensure 'Date' is handled correctly
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df.set_index("Date", inplace=True)
else:
    print("Warning: 'Date' column not found. Proceeding without setting an index.")

# Check if required columns exist
required_cols = ["SMA_10", "SMA_50", "Volatility", "Adj Close"]
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in dataset.")

# Prepare features and target
X = df[["SMA_10", "SMA_50", "Volatility"]]
y = df["Adj Close"].shift(-1).dropna()
X, y = X.iloc[:-1], y  # Align data

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Save model
joblib.dump(model, "nifty_model.pkl")
print("Model saved as nifty_model.pkl")
