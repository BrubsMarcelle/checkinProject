import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings

def send_email(to_email: str, subject: str, body: str):
    message = MIMEMultipart()
    message["From"] = "your_email@example.com"
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_password")
        server.sendmail("your_email@example.com", to_email, message.as_string())