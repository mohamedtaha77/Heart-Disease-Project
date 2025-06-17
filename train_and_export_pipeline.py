import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import joblib

# Load raw data
columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
           "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
df = pd.read_csv("data/heart_disease.csv", header=None, names=columns)
df.replace("?", pd.NA, inplace=True)
df = df.apply(pd.to_numeric, errors="coerce").dropna().reset_index(drop=True)

X = df[columns[:-1]]
y = df["target"]

categorical_cols = ['cp', 'thal', 'slope']
numerical_cols = [col for col in X.columns if col not in categorical_cols]

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
])

pipeline = Pipeline([
    ('preprocessing', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

pipeline.fit(X, y)

# Save model to correct path
joblib.dump(pipeline, "models/heart_disease_pipeline.pkl")

print("✅ Local model saved for deployment.")
