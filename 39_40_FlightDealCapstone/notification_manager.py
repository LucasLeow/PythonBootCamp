import os
import smtplib

my_email = os.environ['my_email']
email_pw = os.environ['email_pw']
to_address = os.environ['to_address']

class NotificationManager:
    def __init__(self, price, dep_city, dep_iata, arr_city, arr_iata, ob_date, ib_date, flight_num):
        self.price = price
        self.dep_city = dep_city
        self.dep_iata = dep_iata
        self.arr_city = arr_city
        self.arr_iata = arr_iata
        self.ob_date = ob_date # outbound
        self.ib_date = ib_date # inbound
        self.flight_num = flight_num

    def send_email(self):
        text = f'''
        Price: {self.price} \n
        Departure City Name: {self.dep_city} \n
        Departure Airport IATA Code: {self.dep_iata} \n
        Arrival City Name: {self.arr_city} \n
        Arrival Airport IATA Code: {self.arr_iata} \n
        Outbound Date: {self.ob_date} \n
        Inbound Date: {self.ib_date} \n
        Flight No.: {self.flight_num}
        '''
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_pw)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_address,
                msg=f"Subject: Latest Flight Deals Alert! \n\n {text}"
            )
            print('Alert Mail Sent Successfully!')

