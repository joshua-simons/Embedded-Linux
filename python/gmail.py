import smtplib

code = 123456
eFROM = "kd2egt@gmail.com"
eTO = "8453094409@msg.fi.google.com"
Subject = "This is a smtp test"
Text = "This is a test of smtlib. This email was sent from a python script "+str(code)
eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("kd2egt@gmail.com", "ybihbernfcvynzju")

server.sendmail(eFROM, eTO, eMessage)
server.quit