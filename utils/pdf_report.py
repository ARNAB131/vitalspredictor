# utils/pdf_report.py
from fpdf import FPDF
import pandas as pd
import os

def generate_pdf_report(predictions: pd.DataFrame, filename="vitals_report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="🩺 Patient Vitals Prediction Report", ln=True, align="C")
    pdf.ln(10)

    # Add table header
    col_names = predictions.columns.tolist()
    for col in col_names:
        pdf.cell(35, 10, txt=str(col)[:15], border=1)
    pdf.ln()

    # Add data rows
    for index, row in predictions.iterrows():
        for col in col_names:
            value = row[col]
            if isinstance(value, (int, float)):
                value = round(value, 2)
            pdf.cell(35, 10, txt=str(value)[:15], border=1)
        pdf.ln()

    os.makedirs("data", exist_ok=True)
    pdf_path = os.path.join("data", filename)
    pdf.output(pdf_path)
    return pdf_path
