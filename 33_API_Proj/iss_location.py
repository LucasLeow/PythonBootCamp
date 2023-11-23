import requests

res = requests.get(url='http://api.open-notify.org/iss-now.json')
res.raise_for_status() # catch any exception


longitude = res.json()['iss_position']['longitude']
latitude = res.json()['iss_position']['latitude']
coord = (longitude, latitude)
print(f"The ISS is current situated at {coord}")

