import smtplib
from creds import *

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()  # start transport layer security
    connection.login(user=my_email, password=pw)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_address,
        msg='Subject: Hello \n\n This is the body of email'
    )
