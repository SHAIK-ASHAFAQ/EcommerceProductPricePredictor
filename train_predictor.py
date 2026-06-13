import pandas as pd
import pickle

print("📂 Loading and cleaning dataset...")
try:
    df = pd.read_csv("amazon.csv")
    
    # Clean up pricing columns
    df['actual_price'] = df['actual_price'].astype(str).str.replace('₹', '').str.replace(',', '')
    df['discounted_price'] = df['discounted_price'].astype(str).str.replace('₹', '').str.replace(',', '')
    
    df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')
    df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')
    df = df.dropna(subset=['actual_price', 'discounted_price'])
    
    X = df['actual_price'].tolist()
    y = df['discounted_price'].tolist()
    
    # Pure Math Linear Regression formulas
    n = len(X)
    mean_x = sum(X) / n
    mean_y = sum(y) / n
    
    numerator = sum((X[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((X[i] - mean_x) ** 2 for i in range(n))
    
    m = numerator / denominator
    b = mean_y - (m * mean_x)
    
    # Save parameters
    model_data = {"slope": m, "intercept": b}
    with open("price_model.pkl", "wb") as f:
        pickle.dump(model_data, f)
        
    print(f"✅ Pure Math Model Trained! Equation: Price = {m:.4f} * Actual_Price + {b:.2f}")

except Exception as e:
    print(f"❌ Error training: {e}. Ensure 'amazon.csv' is in this folder!")
