import email, smtplib, ssl
from providers import PROVIDERS

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from os.path import basename

def send_mms_by_email (
    number: str, 
    message: str, 
    file_path: str,
    mime_maintype: str,
    mime_subtype: str,
    provider: str, 
    sender_credentials: tuple, 
    subject: str="sent from python", 
    smtp_server: str ="smtp.gmail.com", 
    smtp_port: int = 465):

    """
    Does sends an MMS message to a given recipient by a given person using their provided credentials and with a given message."""
    
    sender_email, email_password = sender_credentials
    receiver_email = f"{number}@{PROVIDERS.get(provider).get("mms")}"
    # receiver_email = f"{number}@{PROVIDERS.get(provider).get("sms")}"

    email_msg = MIMEMultipart()
    email_msg["Subject"] = subject
    email_msg["To"] = receiver_email
    email_msg["From"] = sender_email
    email_msg.attach(MIMEText(message, "plain"))

    with open(file_path, "rb") as attachment:
        part = MIMEBase(mime_maintype, mime_subtype)
        part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={basename(file_path)}")

        email_msg.attach(part)

    text = email_msg.as_string()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, text)