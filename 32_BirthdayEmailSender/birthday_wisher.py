import datetime as dt
import pandas as pd
import random
import smtplib

from creds import *

df = pd.read_csv('birthdays.csv')
users_info = df.to_dict(orient='records')
tdy = dt.datetime.today()

letter_num = random.randint(1, 3)
letters_path = f'letter_templates/letter_{letter_num}.txt'

for usr in users_info:
    if usr['month'] == tdy.month and usr['day'] == tdy.day:
        with open(letters_path, 'r') as letter_file:
            all_lines = letter_file.readlines()
            all_lines[0] = all_lines[0].replace('[NAME]', usr['name'])
            all_lines[-1] = all_lines[-1].replace('Angela', 'Lucas')

        birthday_text = ''.join(all_lines)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=pw)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_address,
                msg=f"Subject: Happy Birthday {usr['name']}! \n\n {birthday_text}"
            )
            print('Email Sent Successfully!')
