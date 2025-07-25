# app.py
import streamlit as st
from utils.auth import login_user
from dashboard import doctor_dashboard
from admin_panel import admin_dashboard

st.set_page_config(page_title="VitalsPredictor Pro", layout="wide")

# --- Role-Based Login ---
role = login_user()

if role == "doctor":
    doctor_dashboard()
elif role == "admin":
    admin_dashboard()
else:
    st.warning("🔒 Please log in with valid credentials.")
