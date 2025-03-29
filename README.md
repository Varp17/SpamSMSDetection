
## Spam SMS Detection Project 🚀
This project detects whether an SMS is spam or not using a trained machine learning model. You can run the program in two modes:
1. **Console Mode** (Command-line interface)
2. **Web App Mode** (Using Streamlit)
Here is your **README.md** file that includes instructions to run your Spam SMS Detection project both in the console and on a website using Streamlit. It also includes the dataset URL.  \

---

## 📂 Dataset  
The dataset used for training is the **SMS Spam Collection Dataset**. You can download it from the link below:  

📌 **[SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)**  

---

## 📌 Features  
✅ Train a spam detection model using machine learning  
✅ Run the model in the console for classification  
✅ Use a web-based UI with Streamlit for easy SMS classification  

---

## 🛠 Installation  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/your-username/spam-sms-detection.git
cd spam-sms-detection
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

---

## 🚀 Running the Project  

### 🔹 **Run in Console**  
You can run the spam detection model in the console by executing the following command:  
```sh
python spam_classifier.py
```
You will be prompted to enter a message, and the model will classify it as **Spam** or **Ham**.

---

### 🔹 **Run as a Web Application**  
To launch the **Streamlit** web app, run:  
```sh
streamlit run app.py
```
This will open a browser window where you can enter an SMS and check if it is spam or not.

---

## 🏗 Project Structure  
```
📁 spam-sms-detection
│-- 📄 README.md
│-- 📄 requirements.txt
│-- 📄 spam_classifier.py   # Script to run in console
│-- 📄 app.py               # Streamlit web app
│-- 📂 model                # Folder containing trained model
│-- 📂 dataset              # Folder for dataset (if stored locally)
```

---

## 🔧 Dependencies  
- Python 3.8+  
- Pandas  
- Scikit-learn  
- NumPy  
- Streamlit  

---

## 👨‍💻 Author  
**Your Name**  
📧 your.email@example.com  
🔗 [Your GitHub Profile](https://github.com/your-username)  

---

## ⚖ License  
This project is open-source and available under the **MIT License**.
```

---

### What’s Included?  
✅ Dataset link  
✅ Installation & setup guide  
✅ Instructions to run in both **console** and **web UI**  
✅ Project structure  

Now, let me know if you need **spam_classifier.py** or **app.py**! 🚀
