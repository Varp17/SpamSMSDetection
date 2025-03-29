
## README.md
This project detects whether an SMS is spam or not using a trained machine learning model. You can run the program in two modes:
1. **Console Mode** (Command-line interface)
2. **Web App Mode** (Using Streamlit)
**  

```md
# 📩 Spam SMS Detection

---

## **📌 Installation**

1. **Clone this repository**  
   ```bash
   git clone https://github.com/your-username/spam-sms-detector.git
   cd spam-sms-detector
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate    # For macOS/Linux
   venv\Scripts\activate       # For Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## **🚀 How to Run**

### **1️⃣ Run in Console Mode**
To run the program in the command line:
```bash
python console_mode.py
```
It will prompt you to enter an SMS, and it will classify it as **Spam** or **Not Spam**.

---

### **2️⃣ Run as a Web App (Streamlit)**
To launch the web-based interface:
```bash
streamlit run app.py
```
This will open a web browser where you can enter SMS messages and see the classification results.

---

## **📂 Project Structure**
```
📦 spam-sms-detector
 ┣ 📂 model/                   # Contains trained ML model
 ┣ 📜 app.py                    # Streamlit web app
 ┣ 📜 console_mode.py           # Console-based SMS classifier
 ┣ 📜 requirements.txt          # Dependencies
 ┣ 📜 README.md                 # Documentation
```

---

## **📧 Contact**
For any issues, feel free to reach out! 🚀
```

---

### **Now, Here’s the Required Code**

#### **1️⃣ Console Mode (`console_mode.py`)**
```python
import joblib

# Load the trained model and vectorizer
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def classify_sms(sms):
    transformed_sms = vectorizer.transform([sms])
    prediction = model.predict(transformed_sms)[0]
    return "Spam" if prediction == 1 else "Not Spam"

if __name__ == "__main__":
    while True:
        sms = input("\nEnter SMS (or type 'exit' to quit): ")
        if sms.lower() == "exit":
            break
        print(f"Prediction: {classify_sms(sms)}")
```

---

#### **2️⃣ Web App (`app.py`)**
```python
import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.title("📩 Spam SMS Detector")

user_input = st.text_area("Enter your SMS:")

if st.button("Classify"):
    if user_input:
        transformed_sms = vectorizer.transform([user_input])
        prediction = model.predict(transformed_sms)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please enter a message to classify.")
```

---

This setup allows users to run the spam detection both **in the console and on a website**. Let me know if you need any modifications! 🚀
