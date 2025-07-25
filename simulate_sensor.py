# simulate_sensor.py
import pandas as pd
import random
import time
from datetime import datetime
import os

DATA_PATH = "data/vitals.csv"

# Patient profiles
PROFILES = {
    "normal": lambda: {
        "heart_rate": random.randint(65, 80),
        "bp_systolic": random.randint(110, 125),
        "bp_diastolic": random.randint(70, 85),
        "oxygen_saturation": random.randint(96, 99),
        "temperature": round(random.uniform(36.5, 37.2), 1),
    },
    "hypertensive": lambda: {
        "heart_rate": random.randint(75, 90),
        "bp_systolic": random.randint(140, 160),
        "bp_diastolic": random.randint(90, 100),
        "oxygen_saturation": random.randint(95, 98),
        "temperature": round(random.uniform(36.5, 37.5), 1),
    },
    "critical": lambda: {
        "heart_rate": random.randint(95, 110),
        "bp_systolic": random.randint(160, 180),
        "bp_diastolic": random.randint(100, 120),
        "oxygen_saturation": random.randint(85, 92),
        "temperature": round(random.uniform(38.0, 40.0), 1),
    },
}

def simulate_data(profile_name="normal", patient_id="P001"):
    data = PROFILES[profile_name]()
    data["timestamp"] = datetime.now()
    data["patient_id"] = patient_id
    return data

def run_simulation(profile="normal", patient_id="P001", interval=0.01, fast=False):
    print(f"🚀 Simulation started for patient '{patient_id}' with profile '{profile}'")

    while True:
        entry = simulate_data(profile, patient_id)
        df = pd.DataFrame([entry])
        if os.path.exists(DATA_PATH):
            df.to_csv(DATA_PATH, mode='a', header=False, index=False)
        else:
            df.to_csv(DATA_PATH, index=False)

        print(f"✅ Data written for {patient_id} at {entry['timestamp']}")

        if fast:
            continue  # run at max speed
        time.sleep(interval)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="normal", help="normal | hypertensive | critical")
    parser.add_argument("--patient_id", default="P001")
    parser.add_argument("--interval", type=float, default=0.01, help="Delay between data points (in seconds)")
    parser.add_argument("--fast", action="store_true", help="Run at maximum speed without sleep")
    args = parser.parse_args()

    run_simulation(profile=args.profile, patient_id=args.patient_id, interval=args.interval, fast=args.fast)
