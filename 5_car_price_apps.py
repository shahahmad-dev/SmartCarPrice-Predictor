# =============================================
# 🚗 Advanced Car Price Prediction Web App
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("car data.csv")  

# -----------------------------
# Train Model
# -----------------------------
X = df[["Year", "Present_Price", "Driven_kms", "Owner"]]
y = df["Selling_Price"]

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X, y)

# -----------------------------
# Streamlit App
# -----------------------------
st.title("AutoValue AI 🤖")
st.markdown("Enter car details below to predict the **selling price**.")

# -----------------------------
# Input Fields in Columns
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    car_name = st.text_input("Car Name", "Maruti Swift")
    year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, value=2015)
    owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])

with col2:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)

driven_kms = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=50000, step=1000)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("🔮 Predict Selling Price"):
    input_data = np.array([[year, present_price, driven_kms, owner]])
    prediction = model.predict(input_data)[0]

    # Show Results in Table
    result_df = pd.DataFrame({
        "Car Name": [car_name],
        "Fuel Type": [fuel_type],
        "Transmission": [transmission],
        "Year": [year],
        "Present Price (L)": [present_price],
        "Driven Kms": [driven_kms],
        "Owner(s)": [owner],
        "Predicted Price (L)": [round(prediction, 2)]
    })

    st.success(f"💰 Estimated Selling Price: **{prediction:.2f} lakhs**")
    st.write("📋 Prediction Summary:")
    st.dataframe(result_df)

    # Visualization
    st.bar_chart({
        "Present Price": [present_price],
        "Predicted Price": [prediction]
    })

# -----------------------------
# Dataset Snapshot
# -----------------------------
st.subheader("📊 Dataset Snapshot")
st.dataframe(df.head())
