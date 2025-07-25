# predict_model.py
import pandas as pd
import pickle
import os

MODEL_PATH = "models/model.pkl"

def predict_vitals(input_df):
    # Load the trained model
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("❌ Model not found. Please train it first.")

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    features = ["heart_rate", "bp_systolic", "bp_diastolic", "oxygen_saturation", "temperature"]
    input_features = input_df[features]
    
    predicted = model.predict(input_features)
    pred_df = pd.DataFrame(predicted, columns=[f"predicted_{col}" for col in features])
    
    return pd.concat([input_df, pred_df], axis=1)
