# 💓 Heart Disease Risk Classifier

This is a Streamlit web app that predicts heart disease severity (class 0–4) based on patient inputs using a trained machine learning model.

## 🚀 Live Demo

👉 [Click here to try the app](https://396e-154-182-120-22.ngrok-free.app/)

---

## 📦 Features

- Easy-to-use web interface to enter patient data  
- Predicts heart disease class using a trained ML model  
- Categorical options are user-friendly (e.g., "Male", "Yes", etc.)  
- Supports both local and public deployment using Ngrok  

---

## 📁 File Structure

```
Heart_Disease_Project/
│── data/
│   └── heart_disease.csv
│── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_pca_analysis.ipynb
│   ├── 03_feature_selection.ipynb
│   ├── 04_supervised_learning.ipynb
│   ├── 05_unsupervised_learning.ipynb
│   └── 06_hyperparameter_tuning.ipynb
│── models/
│   └── final_model.pkl
│── ui/
│   └── app.py
│── deployment/
│   └── ngrok_setup.txt
│── results/
│   └── evaluation_metrics.txt
│── README.md
│── requirements.txt
│── .gitignore
```

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

## ⚙️ Installation

```bash
git clone https://github.com/mohamedtaha77/heart-disease-project.git
cd Heart_Disease_Project
pip install -r requirements.txt
cd ui
streamlit run app.py
```

---

## 🌍 Ngrok Deployment Instructions

You can share your locally running app with anyone over the internet using Ngrok.

### 🔧 Steps:

1. **Download and Install Ngrok**  
   Visit: https://ngrok.com/download  
   Unzip and place the executable somewhere accessible from your terminal.

2. **Authenticate Ngrok with your token** (only once):
```bash
ngrok config add-authtoken YOUR_AUTHTOKEN
```

3. **Run the Streamlit app** (from the `ui/` folder):
```bash
streamlit run app.py
```

4. **Start Ngrok in a new terminal:**
```bash
ngrok http 8501
```

5. **Copy the generated public URL** shown in the terminal  
   Example: `https://xxxx.ngrok-free.app`  
   Share this link for public access.

📌 The link remains live as long as both the Streamlit app and Ngrok session are running.

---

## ✅ Deliverables Summary

✔️ All source code and notebooks organized in folders  
✔️ Trained model `.pkl` in `models/`  
✔️ UI implemented in Streamlit under `ui/app.py`  
✔️ Deployment guide under `deployment/ngrok_setup.txt`  
✔️ Live demo using Ngrok  
✔️ `README.md` and `requirements.txt` for reproducibility  
