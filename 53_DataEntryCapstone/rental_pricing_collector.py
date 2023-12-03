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
        self.prices = [float(price.getText().replace('/mo','').split('+')[0].replace('$', '').replace(',','')) for price in self.prices]

        self.addresses = soup.find_all(
            name='address',
            attrs={'data-test':'property-card-addr'}
        )
        self.addresses = [addr.getText().replace('\n','').replace('\t', '').replace(' | ', '').strip(' ') for addr in self.addresses]

        self.URL = soup.find_all(
            name='a',
            class_='StyledPropertyCardDataArea-anchor'
        )
        self.URL = [url['href'] for url in self.URL]

        print(f'''
        Successfully scraped data
        Length of Price: {len(self.prices)}
        Length of Address: {len(self.addresses)}
        Length of URL: {len(self.URL)}
        ''')

    def post_to_form(self):
        self.driver.get(self.form_URL)

        for i in range(len(self.prices)):
            time.sleep(3)
            addr_input = self.driver.find_element(By.CSS_SELECTOR, value='div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
            addr_input.send_keys(self.addresses[i])

            price_input = self.driver.find_element(By.CSS_SELECTOR, value='div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
            price_input.send_keys(self.prices[i])

            url_input = self.driver.find_element(By.CSS_SELECTOR, value='div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
            url_input.send_keys(self.URL[i])

            submit_btn = self.driver.find_element(By.CSS_SELECTOR, value='div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div')
            submit_btn.click()

            print(f'Successfully Submitted Data Row{i + 1}')

            time.sleep(1)
            another_resp = self.driver.find_element(By.CSS_SELECTOR, value='div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > div > div.c2gzEf > a')
            another_resp.click()

if __name__ == '__main__':
    collector = RentalPriceCollector()
    collector.get_rental_data()
    collector.post_to_form()


