from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

dm = DataManager()
fd = FlightData()

# =========================== Check IATA code Empty ===========================
empty_iata_cities = []
sheet_data = dm.get_sheet_data()

for r in sheet_data:
    if r['iataCode'] == '':
        empty_iata_cities.append(r)


# =========================== Populate Empty IATA Codes (if any) ===========================
fs = FlightSearch(empty_iata_cities)
all_cities_iata = fs.get_cities_iata()
dm.update_iata_code(all_cities_iata)

# =========================== Get all cities lowest price ===========================
lowest_city_price_data = fs.search_for_deals(sheet_data, fd)
latest_sheet_data = dm.get_sheet_data()

print(lowest_city_price_data)
print(latest_sheet_data)

nm_consolidater = []
for sheet_data in latest_sheet_data:
    for city_data in lowest_city_price_data:
        if city_data[3] == sheet_data['city']:
            if city_data[0] <= sheet_data['lowestPrice']:
                nm = NotificationManager(
                    price=city_data[0],
                    dep_city=city_data[1],
                    dep_iata=city_data[2],
                    arr_city=city_data[3],
                    arr_iata=city_data[4],
                    ob_date=city_data[5],
                    ib_date=city_data[6],
                    flight_num=city_data[7]
                )
                nm_consolidater.append(nm)
                print(f"{city_data[3]} Notif Mgr created")
            else:
                print(f'{city_data[3]} Historical: {sheet_data["lowestPrice"]} current: {city_data[0]}')

for nm in nm_consolidater:
    nm.send_email()
