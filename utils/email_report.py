# utils/email_report.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email_report(recipient_email, attachment_path):
    try:
        sender_email = "your_email@gmail.com"
        password = "your_app_password"  # Use App Password (NOT raw password)

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = "🩺 Patient Vitals Prediction Report"

        # Attach PDF
        with open(attachment_path, "rb") as f:
            part = MIMEApplication(f.read(), _subtype="pdf")
            part.add_header("Content-Disposition", "attachment", filename="vitals_report.pdf")
            msg.attach(part)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)

        print(f"✅ Email sent to {recipient_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
