import datetime as dt
import smtplib

import requests

from creds import *

# Constants
MY_LAT = 1.384
MY_LONG = 103.7470
TOLERANCE = 15.

# == Getting ISS Info ==
iss_res = requests.get(url='http://api.open-notify.org/iss-now.json')
iss_res.raise_for_status()  # catch any exception

iss_longitude = float(iss_res.json()['iss_position']['longitude'])
iss_latitude = float(iss_res.json()['iss_position']['latitude'])
iss_coord = (iss_longitude, iss_latitude)

# == Getting Sunrise Sunset data ==
parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0  # to get 24H clock
}

twilight_res = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
twilight_res.raise_for_status()

sun_data = twilight_res.json()
sunrise_hr = int(sun_data['results']['sunrise'].split('T')[1].split(':')[0])
sunset_hr = int(sun_data['results']['sunset'].split('T')[1].split(':')[0])

night_hours = [i for i in range(sunset_hr, 25)] + [j for j in range(0, sunrise_hr + 1)]

# Datetime compare
time_now = dt.datetime.now()
hour_now = time_now.hour

if (
        hour_now in night_hours and
        abs(iss_longitude - MY_LONG) <= TOLERANCE and
        abs(iss_latitude - MY_LAT) <= TOLERANCE
):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f"Subject: ISS Passing Overhead! \n\n"
                f"ISS Latitude: {iss_latitude}, ISS Longitude: {iss_longitude}\n"
                f"Your Latitude: {MY_LAT}, Your Longitude: {MY_LONG}"
        )

    print("Email Notification Sent!")
else:
    print(f"The ISS is current situated at ISS Latitude: {iss_latitude}, ISS Longitude: {iss_longitude}")
    print(f"Your Latitude: {MY_LAT}, Your Longitude: {MY_LONG}")
