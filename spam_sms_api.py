import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load and preprocess data
df = pd.read_csv("spam.csv", encoding="latin-1")[['v1', 'v2']].rename(columns={'v1': 'label', 'v2': 'message'})
df['label'] = df['label'].map({'ham': 0, 'spam': 1})  # Ham → 0 (Not Spam), Spam → 1 (Spam)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df["message"], df["label"], test_size=0.2, random_state=42)

# Transform text using TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000, ngram_range=(1,2))

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Save model and vectorizer
with open("spam_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Function to predict message category
def predict_message(msg):
    """Predicts whether a given message is Spam or Not Spam."""
    msg_tfidf = vectorizer.transform([msg])  # Convert text to TF-IDF format
    prediction = model.predict(msg_tfidf)[0]  # Make prediction
    return "Not Spam" if prediction == 0 else "Spam"

# Run interactive test
while True:
    msg = input("\nEnter an SMS (or type 'exit' to quit): ")
    if msg.lower() == 'exit':
        print("Goodbye! 👋")
        break
    print(f"Prediction: {predict_message(msg)}")  # Display result directly
