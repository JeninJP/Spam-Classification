import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk


def transform_text(text):

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if  i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    return " ".join(y)

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")


model = pickle.load(open('model.pkl','rb'))

if st.button('Predict'):
    transformed_sms = transform_text(input_sms)
    result = model.predict([transformed_sms])

    # 4. Display
    if result == 0:
        st.header("Spam")
    else:
        st.header("Not Spam")