import smtplib
import os

HOST = os.getenv('EMAIL_HOST')
PORT = os.getenv('PORT')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


def send_message(send_from: str, send_to: str, body: str) -> bool:
    message = f"""\
Subject: Greeting message
To: {send_to}
From: {send_from}

{body}
"""

    with smtplib.SMTP(HOST, PORT) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(send_from, send_to, message)

    return True
