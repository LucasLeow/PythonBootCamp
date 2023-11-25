import os
import requests
from flight_data import FlightData

tequila_api_key = os.environ['tequila_api_key']
class FlightSearch:
    def __init__(self):
        self.city_iata_pair = {}
        self.endpoint = 'https://api.tequila.kiwi.com/'
        self.header = {
            "apikey": tequila_api_key
        }
        self.lowest_price_info = []

    def get_cities_iata(self, cities_to_search):
        search_endpoint = self.endpoint + 'locations/query'
        for city in cities_to_search:
            search_params = {
                "term": city['city']
            }
            res = requests.get(
                url=search_endpoint,
                params=search_params,
                headers=self.header
            )
            city['iataCode'] = res.json()["locations"][0]["code"]
        return cities_to_search

    def search_for_deals(self, sheet_data: list, fd: FlightData):
        url = self.endpoint + 'v2/search'

        for city_data in sheet_data:
            search_params = {
                "fly_from": fd.fly_from,
                "fly_to": city_data['iataCode'],
                "date_from": fd.date_from,
                "date_to": fd.date_to,
                "nights_in_dst_from": fd.nights_in_dst_from,
                "nights_in_dst_to": fd.nights_in_dst_to,
                "curr": fd.curr,
            }

            res = requests.get(
                url=url,
                params=search_params,
                headers=self.header
            )

            flight_price_data = res.json()["data"][0]
            self.lowest_price_info.append([
                flight_price_data['price'],
                flight_price_data['cityFrom'],
                flight_price_data['cityCodeFrom'],
                flight_price_data['cityTo'],
                flight_price_data['cityCodeTo'],
                flight_price_data['local_departure'],
                flight_price_data['local_arrival'],
                flight_price_data['route'][0]['operating_carrier'] + flight_price_data['route'][0]['operating_flight_no']
            ])

            print(f"processed {city_data['city']} data")
        return self.lowest_price_info
