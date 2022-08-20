   
from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'jw978537@gmail.com'
email_password = 'twyf xava ilph etrx'
email_receiver = 'jw978537@gmail.com'

subject = 'New Log Update'
body = 'Updated log from today'
filename = 'logs.txt'
email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['Subject'] = subject
email.set_content(body)

email.add_attachment(open(filename, "r").read(), filename ="logs.txt")


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())
