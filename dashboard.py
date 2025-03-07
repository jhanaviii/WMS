import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from inventory_manager import InventoryManager
from sales_processor import SalesProcessor

# File paths
inventory_file = "/Users/jhanaviagarwal/PycharmProjects/WMS/data/WMS-04-02 - Current Inventory .csv"
sales_file = "/Users/jhanaviagarwal/PycharmProjects/WMS/data/Orders_2025-01-26_2025-02-01_2025-02-04_12_12-12_17_528114.csv"
model_file = "/Users/jhanaviagarwal/PycharmProjects/WMS/demand_forecasting_model.pkl"

# Load inventory and sales data
inventory_manager = InventoryManager(inventory_file)
inventory_manager.load_inventory()

sales_processor = SalesProcessor(sales_file)
sales_processor.process_sales()

inventory_df = inventory_manager.inventory_data
sales_df = sales_processor.sales_data

# Fix CSV format issues
inventory_df.columns = inventory_df.columns.str.strip().str.lower()
print("Final inventory columns:", inventory_df.columns.tolist())  # Debugging

sales_df.columns = sales_df.columns.str.strip().str.lower()

# Ensure 'order date' is in datetime format
if "order date" in sales_df.columns:
    sales_df["order date"] = pd.to_datetime(sales_df["order date"], errors='coerce')

# Load trained demand forecasting model with caching
@st.cache_resource
def load_demand_model():
    try:
        return joblib.load(model_file)
    except Exception as e:
        st.error(f"⚠️ Failed to load demand model: {e}")
        return None

demand_model = load_demand_model()

st.title("📦 Warehouse Management Dashboard")

# ✅ Stock Overview
st.subheader("Real-Time Stock Levels")
if "product name" in inventory_df.columns:
    sku_filter = st.selectbox("Select SKU:", ["All"] + list(inventory_df["product name"].dropna().unique()))

    filtered_stock = inventory_df if sku_filter == "All" else inventory_df[inventory_df["product name"] == sku_filter]
    st.dataframe(filtered_stock)
else:
    st.error("Stock overview!")

# ✅ Stock Movement Trends
if {"order date", "quantity", "sku"}.issubset(sales_df.columns):
    st.subheader("📈 Stock Movement Trends")
    fig = px.line(sales_df, x="order date", y="quantity", color="sku", title="Stock Movement Over Time")
    st.plotly_chart(fig)
else:
    st.error("❌ Sales data is missing required columns: 'order date', 'quantity', or 'sku'")

# ✅ AI-Based Demand Forecasting
if demand_model and "product name" in inventory_df.columns:
    st.subheader("🔮 AI-Based Demand Forecasting")
    selected_sku = st.selectbox("Select SKU for Forecasting:", inventory_df["product name"].dropna().unique())

    try:
        # Convert SKU to numerical index for the model
        sku_index = inventory_df[inventory_df["product name"] == selected_sku].index[0]
        predicted_demand = demand_model.predict([[sku_index]])[0]
        st.write(f"**📊 Predicted Demand for {selected_sku}: {predicted_demand:.2f} units**")
    except Exception as e:
        st.error(f"⚠️ Demand prediction failed: {e}")

# ✅ Low Stock Alert
low_stock_threshold = 10
if "opening stock" in inventory_df.columns:
    low_stock_items = inventory_df[inventory_df["opening stock"].fillna(0) < low_stock_threshold]
    if not low_stock_items.empty:
        st.warning("⚠️ Low Stock Alert! The following items need restocking:")
        st.dataframe(low_stock_items)
else:
    st.error("❌ 'opening stock' column not found in inventory data!")

# ✅ Download Reports
st.subheader("📜 Generate Stock Reports")
report_csv = inventory_df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download Stock Report", report_csv, "stock_report.csv", "text/csv")

st.success("🚀 Dashboard loaded successfully!")
