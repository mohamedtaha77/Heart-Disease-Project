# 💓 Heart Disease Risk Classifier

This is a Streamlit web app that predicts heart disease severity (class 0–4) based on patient inputs.

## 🚀 Live Demo

👉 [Click here to try the app](https://mohamedtaha77-heart-disease-app.streamlit.app)

---

## 📦 Features

- Easy web interface to enter patient data
- Predicts heart disease class using a trained ML model
- Categorical options are user-friendly (e.g., "Male", "Yes", etc.)

---

## 📊 Input Features

| Feature                  | Description                                |
|--------------------------|--------------------------------------------|
| Age                     | Age in years                               |
| Sex                     | Male / Female                              |
| Chest Pain Type         | Typical, Atypical, Non-anginal, Asymptomatic |
| Resting Blood Pressure  | In mm Hg                                   |
| Cholesterol             | Serum cholesterol in mg/dl                 |
| Fasting Blood Sugar     | > 120 mg/dl (Yes/No)                       |
| Resting ECG             | Normal / ST / Hypertrophy                  |
| Max Heart Rate Achieved | Maximum heart rate                         |
| Exercise-Induced Angina | Yes / No                                   |
| ST Depression (Oldpeak) | Numeric value                              |
| Slope of ST Segment     | Upsloping / Flat / Downsloping             |
| No. of Major Vessels    | 0–3                                        |
| Thalassemia             | Normal / Fixed Defect / Reversible Defect  |

---

## ⚙️ Installation

```bash
git clone https://github.com/mohamedtaha77/heart-disease-app.git
cd heart-disease-app
pip install -r requirements.txt
streamlit run app.py
