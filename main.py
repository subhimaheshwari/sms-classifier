# import os
import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def transform_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)

    y = []
    for word in tokens:
        if word.isalnum() and word not in stop_words:
            y.append(ps.stem(word))

    return " ".join(y)

# tfidf= pickle.load(open('vectorizer.pkl','rb'))
# model= pickle.load(open('model.pkl','rb'))
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# with open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb") as f:
#     tfidf = pickle.load(f)
#
# with open(os.path.join(BASE_DIR, "model.pkl"), "rb") as f:
#     model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


st.title('sms spam classifier')
ip_sms= st.text_area('Enter sms:')

if st.button('predict'):

    #1. preprocess
    transformed_sms= transform_text(ip_sms)

    #2. vectorise
    vector_ip= tfidf.transform([transformed_sms])

    #3. predict
    result= model.predict(vector_ip)[0]

    #4. display
    if result == 1:
        st.header('Sms spam classified')
    else:
        st.header('Sms not spam')
