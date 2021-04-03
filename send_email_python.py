import smtplib

reveiver = "YYYY@gmail.com"
sender = "XXXXX@gmail.com"

message = """From: XXXXXX <XXXXXXX@gmail.com>
To: YYYY <YYYYY@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com',587)

# start TLS for security
s.starttls()

# Authentication
s.login("XXXXXXX@gmail.com", "XXXXXX")

print(s.help())

try:
    s.sendmail(sender,reveiver,message)
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")
    
finally:
    s.quit()