import smtplib
import ssl
from csv import reader
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders


def email_sender():
    port = 
    gmail = 'email_address'
    password = input()

    sender =  gmail
    receiver = 'sender_email'
    subject = 'Its the little things that we notice, that keep us going'
    body = ''
    file_name = 'accounts_insights.csv'

    message_format = """\
        From: %s,
        To: %s,
        Subject: %s,

        %s
        """ % (sender, ",".join(receiver), subject, body)


    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', port)
        server.ehlo()
        server.login(gmail, password)
        server.sendmail(sender, receiver, message_format)
        server.close()

        print('Email sent! Success! Moving on')
    except:
        print("Failed. But let's try again!")
