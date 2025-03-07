import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

# Load sales data
sales_file = "/Users/jhanaviagarwal/PycharmProjects/WMS/data/Orders_2025-01-26_2025-02-01_2025-02-04_12_12-12_17_528114.csv"
sales_df = pd.read_csv(sales_file, encoding="utf-8")

# Debugging: Check column names
print("🔍 CSV Columns:", sales_df.columns)

# Normalize column names
sales_df.columns = sales_df.columns.str.strip().str.lower()

# Ensure 'order date' exists
if "order date" not in sales_df.columns:
    raise KeyError("❌ Column 'order date' not found in CSV. Check column names:", sales_df.columns)

# Convert date to datetime format
sales_df["order date"] = pd.to_datetime(sales_df["order date"], errors="coerce")

# Drop rows where order date is missing
sales_df = sales_df.dropna(subset=["order date"])

# Convert to timestamp for model training
sales_df["timestamp"] = sales_df["order date"].astype(int) / 10**9  # Unix timestamp

# Features and target
X = sales_df[["timestamp"]]
y = sales_df["quantity"]

# Train demand forecasting model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "demand_forecasting_model.pkl")
print("✅ Model trained and saved successfully!")
