#!/usr/bin/env python
# cm-perrs

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import os.path
from datetime import timedelta
import time
import socket
import ConfigParser

parser = ConfigParser.ConfigParser()
parser.read("config.ini")
server = parser.get('global', 'server')
sender = parser.get('global', 'sender')
recipients = [e.strip() for e in parser.get('global', 'recipients').split(',')]

content = []
content.append("time={}".format(time.asctime(time.localtime(time.time()))))
content.append("host={}".format(socket.gethostname()))
with open('/proc/uptime', 'r') as f:
        content.append("uptime={}".format(timedelta(seconds = float(f.readline().split()[0]))))
content.append(os.popen("/opt/vc/bin/vcgencmd measure_temp").readline().rstrip('\n'))

msg = MIMEMultipart()
msg['From'] = sender
msg['Bcc'] = ", ".join(recipients)
msg['Subject'] = "Raspberry PI status"
body = "\r\n".join(content)
msg.attach(MIMEText(body, 'plain'))

try:
        server = smtplib.SMTP_SSL(server, 465)
        server.sendmail(sender, recipients, msg.as_string())
        server.quit()
except:
        print "An email error occured."
        pass
