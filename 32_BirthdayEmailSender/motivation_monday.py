import datetime as dt
import random
import smtplib

from creds import *

# Read all quotes
with open('quotes.txt') as file:
    all_lines = [row.strip('\n') for row in file.readlines()]
    all_lines = [row.split('-') for row in all_lines]


def get_quote():
    random_quote = random.choice(all_lines)
    return random_quote


# == Email Mechanism ==
day_of_week = dt.datetime.today().weekday()
if day_of_week == 3:
    r_quote = get_quote()
    quote = r_quote[0]
    author = r_quote[1]

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f'Subject: Motivation Monday \n\n {quote} \n\n - {author}'
        )
    print('email sent')
