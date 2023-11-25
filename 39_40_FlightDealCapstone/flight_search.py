import os
import requests

tequila_api_key = os.environ['tequila_api_key']
class FlightSearch:
    def __init__(self, iata_cities):
        self.cities_to_search = iata_cities
        self.city_iata_pair = {}
        self.endpoint = 'https://api.tequila.kiwi.com/'
        self.header = {
            "apikey": tequila_api_key
        }
    def get_cities_iata(self):
        search_endpoint = self.endpoint + 'locations/query'
        for city in self.cities_to_search:
            search_params = {
                "term": city['city']
            }
            res = requests.get(
                url=search_endpoint,
                params=search_params,
                headers=self.header
            )

            city['iataCode'] = res.json()["locations"][0]["code"]

        return self.cities_to_search

