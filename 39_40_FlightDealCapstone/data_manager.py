import requests
import os

sheety_api_key = os.environ['sheety_api_key']
sheety_token = os.environ['sheety_token']
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = f'https://api.sheety.co/{sheety_api_key}/lucasFlightDeals/prices'
        self.header = {
            "Authorization": f"Bearer {sheety_token}"
        }
        self.data = None

    def get_sheet_data(self):
        res = requests.get(url=self.endpoint, headers=self.header)
        self.data = res.json()['prices']
        return self.data

    def update_iata_code(self, updated_cities: list):
        for row in updated_cities:
            sheety_endpoint = self.endpoint + f'/{row["id"]}'
            sheety_params = {
                "price": {
                    "city": row['city'],
                    "iataCode": row['iataCode'],
                    'lowestPrice': row['lowestPrice']
                }
            }
            res = requests.put(
                url=sheety_endpoint,
                json=sheety_params,
                headers=self.header
            )
            print(res.text)

