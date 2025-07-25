# utils/auth.py
import streamlit as st

USERS = {
    "doctor1": {"password": "doc123", "role": "doctor"},
    "admin1": {"password": "admin123", "role": "admin"},
}

def login_user():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_btn = st.sidebar.button("Login")

    if login_btn:
        user = USERS.get(username)
        if user and user["password"] == password:
            st.session_state['role'] = user['role']
            st.success(f"Welcome, {username} ({user['role']}) 👋")
            return user['role']
        else:
            st.error("Invalid credentials.")
            return None

    return st.session_state.get('role', None)
