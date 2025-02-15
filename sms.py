import email, smtplib, ssl
from providers import PROVIDERS

def send_sms_by_email (
        number: str, 
        message: str, 
        provider: str, 
        sender_credentials: tuple, 
        subject: str="sent from python", 
        smtp_server: str ="smtp.gmail.com", 
        smtp_port: int = 465):
    """
    Does sends an SMS message to a given recipient by a given person using their provided credentials and with a given message.
    """
    
    sender_email, email_password = sender_credentials
    receiver_email = f"{number}@{PROVIDERS.get(provider).get("sms")}"

    email_msg = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_msg)