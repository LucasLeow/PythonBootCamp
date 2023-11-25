from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()

empty_iata_cities = []
sheet_data = dm.get_flight_data()
print(sheet_data)
for r in sheet_data:
    if r['iataCode'] == '':
        empty_iata_cities.append(r)

fs = FlightSearch(empty_iata_cities)
updated_iata = fs.get_cities_iata()
print(updated_iata)

dm.update_iata_code(updated_iata)

