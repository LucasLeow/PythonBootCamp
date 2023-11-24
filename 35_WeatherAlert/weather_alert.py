from creds import *
import requests

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
MY_LAT = 1.384
MY_LONG = 103.7470

weather_params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

will_rain = False

res = requests.get(OWM_Endpoint, params=weather_params)
res.raise_for_status()
weather_data = res.json()
weather_slice = weather_data['hourly'][:12]

hourly_id = [ int(i['weather'][0]['id']) for i in weather_slice]
for id in hourly_id:
    if id < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella')