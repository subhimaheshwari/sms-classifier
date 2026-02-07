# 📧 SMS Spam Classifier

A machine learning project that classifies SMS messages as either **spam** or **not spam (ham)** using text preprocessing, feature extraction, and multiple classification models.

---

## 🧠 Overview

This project implements a complete machine learning pipeline to detect spam messages from text data. It uses TF-IDF vectorization and various classifiers to train and evaluate models, with an emphasis on achieving high accuracy and precision. Ensemble techniques like Voting and Stacking are also explored for better performance.

---

## 🚀 Features

- Clean and preprocess SMS text data  
- Convert text to numeric features using **TF-IDF**  
- Train multiple ML models (Naive Bayes, Logistic Regression, Random Forest, etc.)  
- Compare models using accuracy and precision scores  
- Save trained model and vectorizer for reuse

---

## 📊 Results

The final chosen model achieves:

- **98% Accuracy**
- **High Precision in identifying spam**
- Low false positives, making it reliable for practical use

---

## 📁 Repository Structure

```

sms-classifier/
│
├── main.py                # Script to run the classifier
├── model.pkl              # Trained classifier model
├── vectorizer.pkl         # Saved TF-IDF vectorizer
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── .gitignore

````

---

## 🛠️ Setup & Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/subhimaheshwari/sms-classifier.git
    ```

2. Navigate to the project directory:
    ```bash
    cd sms-classifier
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Use

1. Open `main.py` and supply the SMS text you want to classify.
2. Run the script:
    ```bash
    python main.py
    ```

3. The script will load the saved model and vectorizer, and output whether the message is **spam** or **not spam**.

---

## 📌 Key Technologies

- 🐍 Python  
- 🧪 scikit-learn (ML models + evaluation)  
- 📝 TF-IDF (feature extraction)  
- 📦 pickle (model serialization)

---

## 🧠 Learning Outcomes

- Built end-to-end text classification pipeline  
- Explored multiple ML models and evaluated them  
- Understood significance of precision vs accuracy  
- Saved and reused trained models

---

## 📈 Future Improvements

- Hyperparameter tuning for stronger performance  
- Integration with a web UI (e.g., Streamlit)  
- Upgrade to deep learning or transformer-based models for contextual understanding

---

## ⭐ Acknowledgements

This project uses the SMS Spam Collection dataset and demonstrates practical machine learning techniques for text classification. :contentReference[oaicite:0]{index=0}

---

