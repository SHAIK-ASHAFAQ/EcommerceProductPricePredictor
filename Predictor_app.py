import streamlit as st
import pickle

st.set_page_config(page_title="Ecommerce Product Price Predictor", page_icon="💰", layout="wide")
st.title("💰 Ecommerce Product Price Predictor")
st.markdown("Enter product metrics below to estimate the final discounted price.")

try:
    # Load our pure math parameters dictionary safely
    with open("price_model.pkl", "rb") as f:
        model_data = pickle.load(f)
        
    # Extract the raw slope and intercept weights
    m = model_data["slope"]
    b = model_data["intercept"]
    
    # 1. The input 'X' is captured cleanly from the user here
    actual_price = st.number_input("Original Product Price (INR)", min_value=100, max_value=50000, value=1500)
    
    # 2. The price is predicted instantly via the linear algebra mapping
    predicted_price = (m * actual_price) + b
    
    # Safeguard to prevent negative pricing thresholds
    final_price = max(0.0, predicted_price)
    
    st.subheader(f"✨ Estimated Discounted Price: ₹{final_price:.2f}")

except FileNotFoundError:
    st.error("❌ Please run train_predictor.py first to generate the model parameters!")
