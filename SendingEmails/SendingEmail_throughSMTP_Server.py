import smtplib

gmail_user = 'me@gmail.com'
gmail_password = '$$$$$$$$'

sent_from = gmail_user
sent_to = ['me1@gmail.com', 'me2@yahoo.com']
subject = 'Hello from Python course'
body = 'Test test \n test \n\n - me'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print("Email sent!")
except:
    print('Something went wrong...')