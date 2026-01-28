import smtplib
from email.message import EmailMessage
from app.config import *

def send_mail(to, subject, body, attachment=None):
    msg = EmailMessage()
    msg["From"] = SMTP_EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment:
        with open(attachment, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=attachment.split("/")[-1]
            )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as s:
        s.starttls()
        s.login(SMTP_EMAIL, SMTP_PASSWORD)
        s.send_message(msg)
