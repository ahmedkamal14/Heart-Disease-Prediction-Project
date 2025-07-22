import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
model = joblib.load('../models/best_model.pkl')

st.title("💓 Heart Disease Prediction App")

st.markdown("""
Enter your health information below and click **Predict** to see if you're at risk.
""")

age = st.number_input("Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("Choose your Gender: ", ["Male", "Female"])
sex = 1 if sex == 'Male' else 0
cp = st.selectbox("Chest Pain Type", ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
cp = {'Typical Angina': 1, 'Atypical Angina': 2, 'Non-Anginal Pain': 3, 'Asymptomatic': 4}[cp]
trestbps = st.number_input("Resting Blood Pressure (mm Hg) On Admission to the hospital", min_value=0, max_value=300, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
fbs = 1 if fbs == 'Yes' else 0
restecg = st.selectbox("Resting Electrocardiographic Results", ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
restecg = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2}[restecg]
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
exang = 1 if exang == 'Yes' else 0
oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", ['Upsloping', 'Flat', 'Downsloping'])
slope = {'Upsloping': 1, 'Flat': 2, 'Downsloping': 3}[slope]
ca = st.number_input("Number of Major Vessels (0-3) Colored by Fluoroscopy", min_value=0, max_value=3, value=0)
thal = st.selectbox("Thalassemia", ['Normal', 'Fixed Defect', 'Reversible Defect'])
thal = {'Normal': 3, 'Fixed Defect': 6, 'Reversible Defect': 7}[thal]

input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)

scaler = joblib.load('../models/scaler.pkl')
input_data_scaled = scaler.transform(input_data)

if st.button("Predict"):
    prediction = model.predict(input_data_scaled)
    if prediction[0] == 1:
        st.error("You are at risk of heart disease. Please consult a healthcare professional.")
    else:
        st.success("You are not at risk of heart disease. Keep up the healthy lifestyle!")
