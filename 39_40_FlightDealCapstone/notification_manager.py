import os
import smtplib

my_email = os.environ['my_email']
email_pw = os.environ['email_pw']
to_address = os.environ['to_address']

class NotificationManager:
    def send_email(self, text):

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_pw)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_address,
                msg=f"Subject: Latest Flight Deals Alert! \n\n {text}"
            )
            print('Alert Mail Sent Successfully!')

