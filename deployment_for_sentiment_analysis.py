import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Load your trained model
with open("svm_model.pkl", "rb") as file:
    rf_model = joblib.load(file)

st.title("DIGITAL GREEN CROP YIELD PREDICTION")
st.markdown("TEAM 2")

st.subheader("Enter the required input data:")
user_input = st.text_input('Enter data:', 'Default Input')
predict_button = st.button('Predict')

if predict_button:
    if user_input:
        # Preprocess the user's input data (similar to how you preprocessed training data)
        # Example preprocessing (replace with your actual preprocessing code)
        # processed_data = preprocess_user_input(user_input)

        # Use the model to make a crop yield prediction
        # Replace this line with your actual prediction code for your model
        predicted_yield = rf_model.predict(processed_data)
        
        # Display the prediction
        st.header("Crop Yield Prediction:")
        st.subheader(f"The predicted yield is: {predicted_yield[0]} tons/acre")
    else:
        st.subheader("Please enter input data for prediction.")
