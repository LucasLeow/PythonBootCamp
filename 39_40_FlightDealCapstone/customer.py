import os
import requests

sheety_api_key = os.environ['sheety_api_key']
sheety_token = os.environ['sheety_token']

class Customer:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.endpoint = f'https://api.sheety.co/{sheety_api_key}/lucasFlightDeals/users'
        self.header = {
            "Authorization": f"Bearer {sheety_token}"
        }

    def create_new_user(self):
        flag = True
        self.first_name = input('What is your first name?: ').lower()
        self.last_name = input('What is your last name?: ').lower()
        while flag:
            self.email = input('What is your email?: ').lower()
            email_validation = input('Type your email again: ').lower()

            if self.email != email_validation:
                print('Email mismatch. Please try again')
            else:
                flag = False
                break

        user_params = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }
        res = requests.post(
            url=self.endpoint,
            json=user_params,
            headers=self.header
        )

        print(res.text)


