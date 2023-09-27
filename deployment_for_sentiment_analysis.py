

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

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

def clean_text(text):
    text = text.lower()
    return text.strip()

def remove_punctuation(text):
    punctuation_free = "".join([i for i in text if i not in string.punctuation])
    return punctuation_free

def tokenization(text):
    tokens = re.split(' ', text)
    return tokens

def remove_stopwords(text):
    output = " ".join(i for i in text if i not in stopwords)
    return output

def lemmatizer(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    sent = [token.lemma_ for token in doc if not token.text in set(stopwords)]
    return ' '.join(sent)

st.title("DIGITAL GREEN CROP YIELD PREDICTION")
st.markdown("TEAM 2")
image = Image.open("crop.jpeg")
st.image(image, use_column_width=True)

st.subheader("Enter your ID here:")
user_input = st.text_area("")

if user_input:
    user_input = clean_text(user_input)
    user_input = remove_punctuation(user_input)
    user_input = user_input.lower()
    user_input = tokenization(user_input)
    user_input = remove_stopwords(user_input)
    user_input = lemmatizer(user_input)

if st.button("Predict"):
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
        # prediction = model.predict(processed_data)[0]
        
        # Display the prediction (replace with appropriate output)
        st.header("Crop Yield Prediction:")
        st.subheader(f"The predicted yield for ID {user_input} is: {prediction} tons/acre")
    else:
        st.subheader("Please enter an ID for prediction.")






