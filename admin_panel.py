# admin_panel.py
import streamlit as st
import pandas as pd
import os

DATA_PATH = "data/vitals.csv"

def admin_dashboard():
    st.title("🛠 Admin Panel")
    st.write("View raw real-time vitals from patients")

    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        st.dataframe(df.tail(100))
        st.download_button("⬇️ Download Full Vitals Data", data=df.to_csv(index=False),
                           file_name="all_vitals_data.csv", mime="text/csv")
    else:
        st.warning("No vitals data available yet. Run simulation.")
