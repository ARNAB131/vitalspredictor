# dashboard.py
import streamlit as st
import pandas as pd
from predict_model import predict_vitals
from utils.email_report import send_email_report
from utils.pdf_report import generate_pdf_report

def doctor_dashboard():
    st.title("📊 Doctor Dashboard")
    st.subheader("Upload patient vitals CSV for prediction")

    uploaded_file = st.file_uploader("📤 Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("📄 Uploaded Data Preview", df.head())

        if st.button("🔮 Predict Vitals"):
            predictions = predict_vitals(df)
            st.success("✅ Prediction Successful!")
            st.dataframe(predictions)

            # Save results
            csv_path = "data/predicted_results.csv"
            predictions.to_csv(csv_path, index=False)

            st.download_button("⬇️ Download CSV", data=predictions.to_csv(index=False),
                               file_name="predicted_vitals.csv", mime="text/csv")

            pdf_path = generate_pdf_report(predictions)

            with open(pdf_path, "rb") as pdf_file:
                st.download_button("📄 Download PDF", data=pdf_file,
                                   file_name="vitals_report.pdf", mime="application/pdf")

            # Email feature
            with st.expander("📧 Send to Doctor"):
                email = st.text_input("Doctor Email")
                if st.button("Send Email Report"):
                    send_email_report(email, pdf_path)
