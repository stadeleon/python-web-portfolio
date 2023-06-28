import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465
username = 'leo.mrakobes@gmail.com'
password = 'mcqyvaknibbxnxmt'

context = ssl.create_default_context()

recipient = 'leo.mrakobes@gmail.com'
message = """\
Subject: Greeting message
Morning!
This is test email sending
Hve a goo day!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, recipient, message)


