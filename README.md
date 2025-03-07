# Warehouse Management System (WMS)

## 📌 Overview
The **Warehouse Management System (WMS)** is a data-driven inventory tracking and demand forecasting dashboard built using **Streamlit, Pandas, and Plotly**. It provides real-time stock management, sales processing, and AI-powered demand predictions.

## 🚀 Features
- 📦 **Real-Time Stock Overview**: View current stock levels for each product.
- 📊 **Stock Movement Trends**: Interactive sales trends visualization using Plotly.
- 🔮 **AI-Based Demand Forecasting**: Predict future demand for products using a trained ML model.
- ⚠️ **Low Stock Alerts**: Identify products that need urgent restocking.
- 📜 **Downloadable Reports**: Export inventory reports in CSV format.

## 🛠️ Tech Stack
- **Frontend**: Streamlit, Plotly
- **Backend**: Python (Flask for ML model API, Pandas for data handling)
- **Machine Learning**: Joblib (for loading demand forecasting model)
- **Data Processing**: Pandas, NumPy

## 📂 Project Structure
```
WMS/
│── data/                     # Inventory & sales data files
│── .venv/                    # Virtual environment (optional)
│── inventory_manager.py      # Handles inventory operations
│── sales_processor.py        # Processes sales data
│── data_visualizer.py        # Generates sales & stock movement charts
│── sku_mapper.py             # Maps SKUs to product names
│── demand_forecasting_model.pkl  # Pre-trained ML model for demand prediction
│── app.py                    # Main Streamlit dashboard
│── requirements.txt          # Dependencies list
│── README.md                 # Project documentation
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/jhanaviii/WMS.git
cd WMS
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Dashboard
```sh
streamlit run app.py
```

## 🔮 AI-Based Demand Forecasting
The model (`demand_forecasting_model.pkl`) is a trained **machine learning model** that predicts future stock demand. The predictions are made based on historical sales data.

To retrain the model:
```sh
python train_model.py  # If you have a script for retraining
```

## 🖥️ Deploying to GitHub
1. **Add changes to Git**
   ```sh
   git add .
   git commit -m "Updated WMS features"
   ```
2. **Push to GitHub**
   ```sh
   git push origin main
   ```

## 🚀 Future Enhancements
- ✅ Add a user authentication system.
- ✅ Integrate barcode scanning for product entry.
- ✅ Implement predictive analytics for stock movement.

## 🤝 Contributing
Feel free to fork the repository and submit pull requests!

## 📜 License
This project is licensed under the **MIT License**.

