#!/usr/bin/env python
# cm-perrs

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import os.path
from datetime import timedelta
from time import gmtime, strftime
import socket

if not os.path.isfile('address.txt'):
        print('Error opening address.txt file.')
        quit()

recipients = [line.rstrip('\n') for line in open('address.txt')]
if len(recipients) < 1:
        print('address.txt file must contain one email.')
        quit()

sender = recipients[0]

content = []
content.append(os.popen("/opt/vc/bin/vcgencmd measure_temp").readline().rstrip('\n'))
with open('/proc/uptime', 'r') as f:
        content.append(str(timedelta(seconds = float(f.readline().split()[0]))))
content.append(socket.gethostname())
content.append(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ", ".join(recipients)
msg['Subject'] = "Raspberry PI status"
body = "\r\n".join(content)
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('aspmx.l.google.com')
server.sendmail(sender, recipients, msg.as_string())
server.quit()
