# 📊 AI-Powered Smart Sales Forecasting & Inventory Optimization Dashboard

## 📌 Project Overview
This project focuses on building an end-to-end Machine Learning pipeline and an interactive Streamlit web dashboard to predict future sales demand and mathematically optimize inventory thresholds. By utilizing historical retail data, the system helps businesses eliminate overstocking (tying up capital) and stockouts (losing revenue) by automatically determining exactly when and how much inventory to reorder.

🎯 Objectives
*   Build a time-series machine learning model to forecast daily sales demand.
*   Perform automated feature engineering (lags, sorting, chronological alignment).
*   Calculate statistical **Safety Stock** and **Reorder Points** dynamically.
*   Develop an interactive Streamlit dashboard for store managers and inventory analysts.
*   Visualize risk thresholds and inventory strategies per product category.

---

## 🛠️ Technologies Used
*   **Python:** Core programming language.
*   **Pandas & NumPy:** Data wrangling, time-series transformations, and statistical math operations.
*   **Scikit-Learn:** Machine learning pipelines, Random Forest regression modeling, and performance evaluation.
*   **Streamlit:** Interactive web application framework for the frontend dashboard.
*   **Matplotlib:** Data visualization charts and metrics generation.

---

## 📂 Dataset Columns & Features
The pipeline processes retail data containing the following metrics:
*   `date`: Chronological timeline of sales.
*   `store_id` & `item_id`: Unique identifiers for physical store locations and products.
*   `sales`: The target variable (historical quantity sold).
*   `price` & `promo`: Financial triggers (price changes and marketing promotions).
*   `weekday` & `month`: Calendar components to track seasonality and trends.
*   `lag_1` & `lag_7`: Engineered historical lag features capturing short-term sales momentum.

---

## 📋 Project Workflow
1. **Data Preprocessing:** Chronological sorting, missing value elimination, and timezone/datetime alignment.
2. **Feature Engineering:** Creation of time-series shift parameters (`lag_1` day and `lag_7` days ago).
3. **Model Training:** Random Forest Regressor trained on historical performance subsets.
4. **Statistical Math Layer:** 
    *   *Safety Stock* calculation safeguarding against variance in demand and lead times ($Z\text{-score} = 1.65$ for a 95% service level).
    *   *Reorder Point (Trigger)* calculations incorporating static supplier lead time window assumptions (3 days).
5. **Dashboard Generation:** Pushing optimized predictions into an asset database (`inventory_recommendations.csv`) and running the live Streamlit server layout.

---

## 📈 Model Performance & Logic
The machine learning forecasting core achieves high precision in capturing historical buying momentum:
*   **Mean Absolute Error (MAE):** 3.29 units
*   **$R^2$ Score (Accuracy Metric):** 0.92

### Core Inventory Optimization Formulas:
$$\text{Safety Stock} = \lceil Z \times \sigma_{\text{demand}} \times \sqrt{L} \rceil$$
$$\text{Reorder Point} = \lceil (\text{Predicted Daily Sales} \times L) + \text{Safety Stock} \rceil$$

*Where $Z = 1.65$ (95% service confidence level) and $L = 3$ days (Supplier Lead Time).*

---

## 📊 Dashboard Visualizations
The deployment environment supports clean visual layers for business operations:
*   **KPI Scorecard row:** Highlighting total unique tracked items, total active retail stores, and average predicted daily demand across the retail fleet.
*   **Dynamic Data Filtering Matrix:** Dropdown filters enabling operators to isolate specific `store_id` clusters.
*   **Strategy Comparison Chart:** Interlocking side-by-side Matplotlib bar charts comparing required buffer safety stocks directly alongside real-time reorder triggers.

---

## 🚀 Future Roadmap & Enhancements

To further scale this predictive pipeline, the following engineering milestones are planned:
*   **Dynamic Supplier API Integration:** Transition from static lead times to real-time API integrations tracking vendor shipping variance.
*   **Deep Learning Time-Series Upgrades:** Benchmark the `RandomForestRegressor` against long short-term memory (**LSTM**) neural networks to evaluate improvements in data sequence trends.
*   **Live Streamlit Cloud Deployment:** Host the dashboard layout permanently on Streamlit Community Cloud using encrypted secret management for secure data connections.
*   **Automated Email Alert System:** Connect an SMTP mailing layer to instantly flag and dispatch warning emails to store supervisors the moment an item hits its "Reorder Point".

---

## 📁 Project Structure
```text
AI_Sales_-_Inventory_dashboard/
│
├── .gitignore                   
├── README.md                    
├── app.py                       
├── inventory_recommendations.csv 
└── AI_Sales_&_Inventory_dashboard.ipynb 
