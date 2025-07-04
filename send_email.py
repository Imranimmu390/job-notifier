import smtplib
from email.mime.text import MIMEText
from fetch_jobs import fetch_jobs
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

def send_email():
    jobs = fetch_jobs()

    if not jobs:
        print("No jobs found.")
        return

    message_body = "\n\n".join(
        [f"{job['company']} - {job['position']}\n{job['url']}" for job in 
jobs]
    )

    msg = MIMEText(message_body)
    msg["Subject"] = "🔥 Daily DevOps Job Alert"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_USER  # sending to self

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    send_email()

