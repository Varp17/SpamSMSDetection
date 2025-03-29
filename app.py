import streamlit as st
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# Function to predict if a message is spam or not
def predict_message(msg):
    msg_tfidf = vectorizer.transform([msg])
    prediction = model.predict(msg_tfidf)[0]
    return "✅ Not Spam" if prediction == 0 else "🚨 Spam"


# Streamlit UI
st.title("📩 Spam SMS Detector")
st.write("Enter an SMS message to check if it's **Spam or Not Spam**.")

# User Input
message = st.text_area("📥 Enter your SMS here:", "")

if st.button("Check SMS"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message before checking.")
    else:
        result = predict_message(message)
        st.success(f"**Prediction:** {result}")

# Footer
st.markdown("---")
st.write("🔹 Built with **Streamlit & Machine Learning**")
