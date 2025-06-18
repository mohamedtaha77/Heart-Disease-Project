# 💓 Heart Disease Risk Classifier

This is a **Streamlit** web app that predicts heart disease severity (class 0–4) based on patient inputs using a trained machine learning pipeline.

## 🚀 Live Demo

👉 [Click here to try the app](https://heart-disease-project-77.streamlit.app/)

---

## 📦 Features

- User-friendly web UI to enter patient health data  
- Predicts heart disease class using a trained Random Forest pipeline  
- All preprocessing steps are included in the model (scaling, encoding)  
- Fast deployment using **Streamlit Cloud** (no need for Ngrok or local hosting)

---

## 📁 File Structure

Heart_Disease_Project/
│
├── data/
│ └── heart_disease.csv
├── notebooks/
│ ├── 01_data_preprocessing.ipynb
│ ├── 02_pca_analysis.ipynb
│ ├── 03_feature_selection.ipynb
│ ├── 04_supervised_learning.ipynb
│ ├── 05_unsupervised_learning.ipynb
│ └── 06_hyperparameter_tuning.ipynb
├── models/
│ └── heart_disease_pipeline.pkl
├── ui/
│ └── streamlit_app.py
├── results/
│ └── evaluation_metrics.txt
├── deployment/
│ └── ngrok_setup.txt ← (deprecated)
│
├── train_and_export_pipeline.py
├── requirements.txt
├── README.md
├── .gitignore

yaml
Copy
Edit

---

## 📊 Input Features

| Feature                  | Description                                  |
|--------------------------|----------------------------------------------|
| Age                     | Age in years                                 |
| Sex                     | Male / Female                                |
| Chest Pain Type         | Typical, Atypical, Non-anginal, Asymptomatic |
| Resting Blood Pressure  | In mm Hg                                     |
| Cholesterol             | Serum cholesterol in mg/dl                   |
| Fasting Blood Sugar     | > 120 mg/dl (Yes/No)                         |
| Resting ECG             | Normal / ST / Hypertrophy                    |
| Max Heart Rate Achieved | Maximum heart rate                           |
| Exercise-Induced Angina | Yes / No                                     |
| ST Depression (Oldpeak) | Numeric value                                |
| Slope of ST Segment     | Upsloping / Flat / Downsloping               |
| No. of Major Vessels    | 0–3                                          |
| Thalassemia             | Normal / Fixed Defect / Reversible Defect    |

---

## ⚙️ Local Installation

```bash
git clone https://github.com/mohamedtaha77/heart-disease-project.git
cd Heart_Disease_Project
pip install -r requirements.txt
streamlit run ui/streamlit_app.py
