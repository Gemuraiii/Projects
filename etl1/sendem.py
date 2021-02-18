import smtplib
import ssl
from bs4 import BeautifulSoup
import requests



port = 465
gmail = 'gafj95@gmail.com'
password = 'Ra_anubis95'

sender =  gmail
receiver = 'glenfjr95@gmail.com'
subject = 'Its the little things that we notice, that keep us going'
body = "I am constantly taking my first step toward my future. At some point we have to hit that those high knees and loosen up \n - Glen F."

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
