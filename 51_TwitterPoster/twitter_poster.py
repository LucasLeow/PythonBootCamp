from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Constants ==
PROMISED_DOWN = 1000
PROMISED_UP = 1000
class InternetSpeedTwitterBot:
    def __init__(self):
        self.user = os.environ['user']
        self.pw = os.environ['pw']

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login_to_twitter(self):
        self.driver.get('https://twitter.com/')

        login_elem = self.driver.find_element(By.CSS_SELECTOR, value='a[href="/login"]')
        login_elem.click()

        time.sleep(2)
        username_elem = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username_elem.send_keys(self.user)

        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()

        time.sleep(3)
        pw_elem = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pw_elem.send_keys(self.pw)

        login_btn = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        login_btn.click()

        time.sleep(5)
        print('login successful')

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.login_to_twitter()


