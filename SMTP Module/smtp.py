import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time
import os
from dotenv import load_dotenv

def send_email(sender_email, sender_password, recipient_email, subject, message):
    smtp_server = 'smtp_server_here'
    smtp_port = smtp_port_here
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            
            # Login to the email account
            server.login(sender_email, sender_password)
            
            # Send the email
            server.send_message(msg)
    except Exception:
        pass

def email_handler(email_format):
    load_dotenv()
    sender_email = os.getenv('sender_email')
    sender_password = os.getenv('sender_password')
    recipient_email = os.getenv('recipient_email')
    subject = 'EMAIL SUBJECT HERE'
    cur_time = time.strftime("%H:%M:%S", time.localtime())
    date = datetime.now()
    time_record = (
                f"{date.month}/{date.day}/{date.year} {cur_time}")
    message = f'New connection received from {email_format} at {time_record}'
    send_email(sender_email, sender_password, recipient_email, subject, message)
