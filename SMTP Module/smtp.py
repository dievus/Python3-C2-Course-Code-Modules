# Copyright (c) 2023 Joe Helle

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software. Software shall not be used for
# commercial purposes or for profit. Software shall not be utilized in the patent
# process without prior notification, approval, and inclusion in the patent.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
