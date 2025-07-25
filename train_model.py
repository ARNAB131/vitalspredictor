# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
import pickle
import os

data = pd.read_csv("data/vitals.csv")

features = ["heart_rate", "bp_systolic", "bp_diastolic", "oxygen_saturation", "temperature"]
target = features

X = data[features]
y = data[features]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = MultiOutputRegressor(RandomForestRegressor())
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to models/model.pkl")
