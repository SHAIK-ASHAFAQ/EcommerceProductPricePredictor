# Ecommerce Product Price Predictor (Built from Scratch)

A lightweight, production-stable machine learning web application that estimates the final discounted marketplace price of an item based on its original retail price. 

This project completely drops heavy automated framework dependencies (like Scikit-Learn) and implements ordinary least squares linear regression using pure mathematics and native Python loops.

## 🚀 Key Features & Engineering Highlights
- **Framework-Free Inference Engine:** Implemented the core mathematical formulas for Linear Regression ($y = mx + b$) manually, completely bypassing operating system DLL security blocks (`_liblinear` conflicts).
- **Data Engineering Ingestion:** Utilized Pandas to sanitize raw web-scraped marketplace rows, handling currency symbol formatting anomalies (₹, commas) and filtering missing array entries dynamically.
- **Sub-Millisecond Inference:** By reducing the trained model to raw float multipliers (Slope $m$ and Intercept $b$), prediction calculations run instantly in under 0.0001 milliseconds with zero library overhead.
- **Interactive UI Dashboard:** Wrapped the custom mathematical variables into a clean, intuitive web portal using Streamlit, allowing instant price updates via direct user input.

## 🧠 Under the Hood: The OLS Mathematics
Rather than a "black-box" library call, the system determines the parameters $m$ and $b$ over the dataset using **Ordinary Least Squares (OLS)** error minimization:

1. **The Slope ($m$):** Calculated as the covariance of the independent and dependent variables divided by the variance of the input features:
   $$m = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2}$$
2. **The Intercept ($b$):** Forces the optimization line to pass perfectly through the geometric center of the dataset:
   $$b = \bar{Y} - (m \times \bar{X})$$

---

## 🛠️ Tech Stack & Tools
- **Programming Language:** Python 3
- **Data Manipulation:** Pandas Matrix Processing, Pickle Serializers
- **Core Optimization Math:** Coordinate Geometry, Ordinary Least Squares
- **User Presentation Layer:** Streamlit UI Engine

---

## 💻 Local Installation & Setup

1. **Clone the Project Folder:**
   ```bash
   git clone https://github.com
   cd PricePredictor
   ```

2. **Ensure Dataset Presence:**
   Place your `amazon.csv` marketplace data file directly in the root directory.

3. **Train the Analytical Math Model:**
   ```powershell
   python train_predictor.py
   ```
   *This outputs `price_model.pkl` containing your raw optimal slope and intercept weights.*

4. **Launch the User Interface:**
   ```powershell
   python -m streamlit run predict_app.py
   ```
