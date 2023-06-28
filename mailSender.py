import smtplib

HOST = 'sandbox.smtp.mailtrap.io'
PORT = 2525
USERNAME = '7b79a2051aa09d'
PASSWORD = '91435182326be1'


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
