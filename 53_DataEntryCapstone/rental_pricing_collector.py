from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import requests
from bs4 import BeautifulSoup

class RentalPriceCollector:
    def __init__(self):
        self.property_URL = 'https://appbrewery.github.io/Zillow-Clone/'
        self.form_URL = 'https://forms.gle/UdKD8cy4FCSPGKJc7'
        self.prices = []
        self.addresses = []
        self.URL = []

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)


    def get_rental_data(self):
        res = requests.get(
            url=self.property_URL
        )

        soup = BeautifulSoup(res.text, features='html.parser')

        self.prices = soup.find_all(
            name='span',
            class_='PropertyCardWrapper__StyledPriceLine'
        )
        self.prices = [float(price.getText().replace('$', '').replace(',', '').replace('+/mo','').replace('/mo', '').replace('+ 1bd', '').replace('+ 1 bd','')) for price in self.prices]

        self.addresses = soup.find_all(
            name='address',
            attrs={'data-test':'property-card-addr'}
        )
        self.addresses = [addr.getText().replace('\n','').replace('\t', '').strip(' ') for addr in self.addresses]

        self.URL = soup.find_all(
            name='a',
            class_='StyledPropertyCardDataArea-anchor'
        )
        self.URL = [url['href'] for url in self.URL]
        print(self.URL)

    def post_to_form(self):
        self.driver.get(self.form_URL)


if __name__ == '__main__':
    collector = RentalPriceCollector()
    collector.get_rental_data()


