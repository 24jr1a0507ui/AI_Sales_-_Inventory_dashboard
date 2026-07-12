import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Sales & Inventory Dashboard", layout="wide")
st.title("📦 AI-Powered Smart Sales Forecasting & Inventory Optimization")
st.markdown("Predicting future sales demand and recommending optimal inventory levels to eliminate overstocking and shortages.")

@st.cache_data
def load_data():
    return pd.read_csv('inventory_recommendations.csv')

try:
    df_res = load_data()
    
    # --- TOP METRICS ROW ---
    st.subheader("📊 Key Performance Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Unique Items Tracked", f"{df_res['item_id'].nunique():,}")
    col2.metric("Total Active Stores", f"{df_res['store_id'].nunique():,}")
    col3.metric("Avg Daily Predicted Demand (Per Item)", f"{df_res['avg_daily_prediction'].mean():.2f} units")
    
    st.markdown("---")
    
    # --- STORE & PRODUCT VIEW ---
    st.subheader("🔍 Stock Level Recommendations by Product")
    selected_store = st.selectbox("Select Store ID", sorted(df_res['store_id'].unique()))
    store_data = df_res[df_res['store_id'] == selected_store]
    
    st.dataframe(
        store_data[['item_id', 'avg_daily_prediction', 'safety_stock', 'reorder_point']].rename(columns={
            'item_id': 'Item ID',
            'avg_daily_prediction': 'AI Predicted Daily Sales',
            'safety_stock': 'Required Safety Stock',
            'reorder_point': 'Reorder Point (Trigger)'
        }),
        use_container_width=True
    )
    
    # --- VISUALIZATION ---
    st.subheader("📈 Visualizing Inventory Thresholds")
    top_10_items = store_data.head(10)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.arange(len(top_10_items['item_id']))
    width = 0.35
    
    ax.bar(x - width/2, top_10_items['safety_stock'], width, label='Safety Stock', color='#FF6B6B')
    ax.bar(x + width/2, top_10_items['reorder_point'], width, label='Reorder Point', color='#4D96FF')
    
    ax.set_ylabel('Units')
    ax.set_title(f'Inventory Strategy: First 10 Items in {selected_store}')
    ax.set_xticks(x)
    ax.set_xticklabels(top_10_items['item_id'], rotation=45)
    ax.legend()
    st.pyplot(fig)
except FileNotFoundError:
    st.error("Could not find 'inventory_recommendations.csv'. Please make sure the data file is present!")
