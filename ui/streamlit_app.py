# ui/app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path


THIS_DIR   = Path(__file__).resolve().parent        
MODEL_PATH = 'models/final_model.pkl'

# Load the trained pipeline
model = joblib.load(MODEL_PATH)

st.title("💓 Heart Disease Risk Classifier")
st.markdown("Enter patient data to predict the heart disease class (0 to 4):")

def user_input():
    age = st.number_input("Age", 20, 100, 50)

    sex = 1 if st.radio("Sex", ["Male", "Female"]) == "Male" else 0

    cp_map = {
        "Typical Angina (0)": 0,
        "Atypical Angina (1)": 1,
        "Non-anginal Pain (2)": 2,
        "Asymptomatic (3)": 3
    }
    cp = cp_map[st.selectbox("Chest Pain Type", cp_map.keys())]

    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
    chol     = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)

    fbs = 1 if st.radio("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"]) == "Yes" else 0

    restecg_map = {
        "Normal (0)": 0,
        "ST-T Wave Abnormality (1)": 1,
        "Left Ventricular Hypertrophy (2)": 2
    }
    restecg = restecg_map[st.selectbox("Resting ECG", restecg_map.keys())]

    thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)

    exang = 1 if st.radio("Exercise-Induced Angina?", ["Yes", "No"]) == "Yes" else 0

    oldpeak = st.number_input("ST Depression (Oldpeak)", 0.0, 6.0, 1.0, step=0.1)

    slope_map = {
        "Upsloping (0)": 0,
        "Flat (1)": 1,
        "Downsloping (2)": 2
    }
    slope = slope_map[st.selectbox("Slope of ST Segment", slope_map.keys())]

    ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])

    thal_map = {
        "Normal (1)": 1,
        "Fixed Defect (2)": 2,
        "Reversible Defect (3)": 3
    }
    thal = thal_map[st.selectbox("Thalassemia", thal_map.keys())]

    data = {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
        "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach,
        "exang": exang, "oldpeak": oldpeak, "slope": slope,
        "ca": ca, "thal": thal
    }
    return pd.DataFrame([data])

input_df = user_input()

# Prediction
if st.button("Predict"):
    prediction = int(model.predict(input_df)[0]) 

    disease_labels = {
        0: "No heart disease",
        1: "Mild heart disease",
        2: "Moderate heart disease",
        3: "Severe heart disease",
        4: "Very severe heart disease"
    }

    st.success(f"🏷️ Predicted Heart Disease Class: {prediction} — {disease_labels[prediction]}")
