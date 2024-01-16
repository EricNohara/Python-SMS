import email, smtplib, ssl
from providers import PROVIDERS

def send_sms_by_email (
        number: str, 
        essage: str, 
        provider: str, 
        sender_credentials: tuple, 
        subject: str="sent from python", 
        smtp_server: str ="smtp.gmail.com", 
        smtp_port: int = 465):
    pass