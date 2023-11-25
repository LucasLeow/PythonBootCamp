from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

dm = DataManager()
fd = FlightData()
fs = FlightSearch()
nm = NotificationManager()

# =========================== Check IATA code Empty ===========================
empty_iata_cities = []
sheet_data = dm.get_sheet_data()

for r in sheet_data:
    if r['iataCode'] == '':
        empty_iata_cities.append(r)


# =========================== Populate Empty IATA Codes (if any) ===========================

all_cities_iata = fs.get_cities_iata(empty_iata_cities)
dm.update_iata_code(all_cities_iata)

# =========================== Get all cities lowest price ===========================
lowest_city_price_data = fs.search_for_deals(sheet_data, fd)
latest_sheet_data = dm.get_sheet_data()

print(lowest_city_price_data)
print(latest_sheet_data)

text_consolidater = []
for sheet_data in latest_sheet_data:
    for city_data in lowest_city_price_data:
        if city_data[3] == sheet_data['city']:
            if city_data[0] <= sheet_data['lowestPrice']:
                text = f'''
                Price: {city_data[0]} \n
                Departure City Name: {city_data[1]} \n
                Departure Airport IATA Code: {city_data[2]} \n
                Arrival City Name: {city_data[3]} \n
                Arrival Airport IATA Code: {city_data[4]} \n
                Outbound Date: {city_data[5]} \n
                Inbound Date: {city_data[6]} \n
                Flight No.: {city_data[7]}
                '''
                text_consolidater.append(text)
            else:
                print(f'{city_data[3]} Historical: {sheet_data["lowestPrice"]} current: {city_data[0]}')

for txt in text_consolidater:
    nm.send_email(txt)
