import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from PIL import Image
import re
import string
import nltk
import  spacy

with open("svm_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

st.title("DIGITAL GREEN CROP YIELD PREDICTION")
st.markdown("TEAM 2")
image = Image.open("crop.jpg")
st.image(image, use_column_width=True)

st.subheader("Enter your ID here:")

user_input = st.text_input('Enter ID:', 'Default ID')
predict_button = st.button('Predict')

if predict_button:
    if user_input:
        # Retrieve the data for the given ID (replace with your data retrieval code)
        # You may need to load the relevant data from your dataset based on the ID
        # Make sure to preprocess the data to match the format expected by your model
        
        # Example data retrieval and preprocessing (replace with your actual code)
        # data = retrieve_data_by_id(user_input)
        # processed_data = preprocess_data(data)
        
        # Use the model to make a crop yield prediction
        # Replace this line with the actual prediction code for your model
        y_predict = model.predict(X_test)  # Replace X_test with your processed data
        
        # Display the prediction
        st.header("Crop Yield Prediction:")
        st.subheader(f"The predicted yield for ID {user_input} is: {y_predict[0]} tons/acre")
    else:
        st.subheader("Please enter an ID for prediction.")
