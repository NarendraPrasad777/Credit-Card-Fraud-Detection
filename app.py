import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
model = joblib.load("models/fraud_modell.pkl")

st.set_page_config(page_title="Fraud Detection", layout="wide")

# Title
st.title("💳 Credit Card Fraud Detection System")
st.markdown("Detect fraudulent transactions using Machine Learning")

# Sidebar
st.sidebar.header("Input Transaction Details")

amount = st.sidebar.number_input("Transaction Amount", 0.0, 100000.0, 100.0)
time = st.sidebar.number_input("Time", 0.0, 200000.0, 1000.0)

# Dummy PCA inputs (simplified)
V1 = st.sidebar.slider("V1", -5.0, 5.0, 0.0)
V2 = st.sidebar.slider("V2", -5.0, 5.0, 0.0)

# Create input dataframe
input_data = pd.DataFrame({
    "Time": [time],
    "V1": [V1],
    "V2": [V2],
    "Amount": [amount]
})

# Fill missing features (V3–V28)
for i in range(3, 29):
    input_data[f"V{i}"] = 0

# Prediction
if st.button("🔍 Predict Transaction"):

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    col1, col2 = st.columns(2)

    with col1:
        if prediction == 1:
            st.error("🚨 Fraud Transaction Detected!")
        else:
            st.success("✅ Legitimate Transaction")

    with col2:
        st.metric("Fraud Probability", f"{prob*100:.2f}%")

    # Risk meter
    st.subheader("Risk Level")
    st.progress(int(prob * 100))

    # Visualization
    fig, ax = plt.subplots()
    sns.barplot(x=["Legit", "Fraud"], y=[1-prob, prob], ax=ax)
    st.pyplot(fig)

# ---------------------------
# CSV Upload Feature
# ---------------------------

st.subheader("📂 Upload CSV for Batch Prediction")

uploaded_file = st.file_uploader("Upload transaction file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    predictions = model.predict(data)
    data["Prediction"] = predictions

    st.write(data.head())

    fraud_count = sum(predictions)
    st.write(f"🚨 Fraud Transactions: {fraud_count}")

# ---------------------------
# History (Session based)
# ---------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Save Prediction"):
    st.session_state.history.append(input_data)

if st.session_state.history:
    st.subheader("📜 Prediction History")
    st.write(pd.concat(st.session_state.history))