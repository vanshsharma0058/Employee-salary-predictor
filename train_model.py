# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load data
df = pd.read_csv("C:\\Users\\owner2\\Desktop\\python\\Employee_salary_pred\\hiring.csv")
df.fillna(0, inplace=True)

# Features and target
X = df.drop("salary($)", axis=1)
y = df["salary($)"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model inside the same folder
joblib.dump(model, os.path.join(os.path.dirname(__file__), "model.pkl"))

print("✅ Model trained and saved as model.pkl")
