import requests
import datetime as dt

# Sg Lat Long
parameters = {
    "lat": 1.3521,
    "long": 103.8198,
    "formatted": 0
}
res = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
res.raise_for_status()

data = res.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

time_now = dt.datetime.now()
print(sunrise)
print(time_now)
# strftime("%I:%M:%S %p")
