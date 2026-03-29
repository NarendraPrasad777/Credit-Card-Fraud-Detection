Credit Card Fraud Detection System

Overview

This project is a Machine Learning-based web application that detects fraudulent credit card transactions. It uses a trained classification model to predict whether a transaction is legitimate or fraudulent based on input features.

The application is built using Streamlit for an interactive user interface and supports both single transaction prediction and batch prediction using CSV files.

---

Features

* Real-time fraud prediction
* Probability score for each transaction
* Batch prediction using CSV upload
* Download prediction results
* Session-based prediction history
* Input validation and error handling
* Visual representation of prediction

---

Machine Learning Details

* Model trained on credit card transaction dataset
* Features include:

  * Time
  * Amount
  * V1 to V28 (PCA-transformed features)
* Handles imbalanced data
* Model saved using .pkl file

---

Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas, NumPy
* Matplotlib, Seaborn
* Joblib

---

Project Structure

```
fraud-detection/
│
├── app.py
├── models/
│   └── fraud_model.pkl
│
├── data/
│   └── sample_transactions.csv
│
├── notebooks/
│   └── exploration.ipynb
│
├── README.md
```

---

Installation & Setup

1. Clone the repository

```
git clone https://github.com/your-username/fraud-detection.git
cd fraud-detection
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
streamlit run app.py
```



How to Use

Single Prediction

* Enter transaction details in the sidebar
* Click "Predict Transaction"
* View result and fraud probability

Batch Prediction

* Upload a CSV file with required columns
* View predictions instantly
* Download results as CSV


 Output

* Legitimate Transaction
* Fraud Transaction
* Fraud probability score
* Visualization chart


GitHub Issues Solved

* Fixed model loading error
* Handled missing feature mismatch
* Added input validation
* Improved UI feedback
* Fixed CSV upload errors
* Added download functionality


Future Enhancements

* Deploy on cloud (Streamlit Cloud or AWS)
* Add confusion matrix and accuracy display
* User authentication system
* Mobile-friendly UI

 License

This project is for educational purposes.

Developed as part of academic project submission.
