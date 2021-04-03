import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
message_body = '''Hi,
Thid id a test email with attachment.
We are using Python3 SMTP library for sending email. 
'''

sender = "XXXXXX@gmail.com"
sender_password = 'XXXXXXXX'
receiver = "YYYYYY@gmail.com"

#set MIME
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "A test email with attachment in Python"
message.attach(MIMEText(message_body,'plain'))
base_path = os.getcwd()
attach_file_name = os.path.join(base_path,"samplefile.csv")
attach_file = open(attach_file_name,'rb') #open file in binary mode
payload = MIMEBase('application','octate-stram')
payload.set_payload(attach_file.read())
encoders.encode_base64(payload)
#add payload header with filename
# payload.add_header('Content-Decompostion','attachemnt',filename = attach_file_name)
# Add header as key/value pair to attachment part
payload.add_header(
    "Content-Disposition",
    f"attachment; filename= {attach_file_name}",
)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com','587')
session.starttls()
session.login(sender,sender_password)
session.sendmail(sender,receiver,message.as_string())
session.quit()
print("Email sent")