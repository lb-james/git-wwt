#!/usr/bin/python
#coding: utf-8  
import smtplib  
import sys
from email.mime.text import MIMEText  
from email.header import Header  
from email.Utils import COMMASPACE
  
receiver = sys.argv[1]
subject = sys.argv[2]
mailbody = sys.argv[3]
smtpserver = 'smtp.exmail.qq.com'  
username = 'admin@unixhot.com'  
password = '123456'  
sender = username
  
msg = MIMEText(sys.argv[3],'html','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')  
msg['From'] = username
msg['To'] = receiver
  
smtp = smtplib.SMTP()  
smtp.connect(smtpserver)  
smtp.login(username, password)  
smtp.starttls()
smtp.sendmail(msg['From'], msg['To'], msg.as_string())  
smtp.quit() 
