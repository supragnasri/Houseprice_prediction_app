import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("House Price Prediction")
st.write("Enter house details to estimate the price")

# User Inputs
OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
GrLivArea = st.number_input("Above Ground Living Area (sq ft)", 500, 5000, 1500)
GarageCars = st.slider("Garage Capacity", 0, 4, 2)
TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", 0, 3000, 800)
TotalSF = st.number_input("Total House Area (sq ft)", 500, 6000, 2000)
HouseAge = st.number_input("House Age (years)", 0, 150, 20)
RemodelAge = st.number_input("Years Since Remodel", 0, 150, 10)
FirstFlrSF = st.number_input("1st Floor Area (sq ft)", 0, 3000, 1000)
YearBuilt = st.number_input("Year Built", 1900, 2024, 2000)
LotArea = st.number_input("Lot Area (sq ft)", 1000, 20000, 8000)

# Create feature array
features = np.array([[OverallQual,
                      GrLivArea,
                      GarageCars,
                      TotalBsmtSF,
                      TotalSF,
                      HouseAge,
                      RemodelAge,
                      FirstFlrSF,
                      YearBuilt,
                      LotArea]])

# Prediction button
if st.button("Predict House Price"):
    prediction = model.predict(features)
    price = prediction[0]

    st.success(f"Estimated House Price: ${price:,.2f}")