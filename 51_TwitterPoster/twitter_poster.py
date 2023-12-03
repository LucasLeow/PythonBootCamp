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
        self.username = os.environ['username']
        self.speedtest_download = 0
        self.speedtest_upload = 0

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)

    def tweet_at_provider(self):
        # Login ==
        self.driver.get('https://twitter.com/')

        time.sleep(3)
        login_elem = self.driver.find_element(By.CSS_SELECTOR, value='a[href="/login"]')
        login_elem.click()

        time.sleep(3)
        username_elem = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username_elem.send_keys(self.user)

        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()

        time.sleep(3)
        unusual_activity = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        unusual_activity.send_keys(self.username)

        unusual_btn = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        unusual_btn.click()

        time.sleep(3)
        pw_elem = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pw_elem.send_keys(self.pw)

        login_btn = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        login_btn.click()

        print('login successful')
        time.sleep(10)


        # Tweet ==
        tweet_input = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        text = f'''
        Download Speed: {self.speedtest_download} Mbps
        Upload Speed: {self.speedtest_upload} Mbps
        
        Promised Download: {PROMISED_DOWN} Mbps
        Promised Upload: {PROMISED_UP} Mbps
        '''
        tweet_input.send_keys(text)

        tweet_post_btn = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        tweet_post_btn.click()
        print('Tweet posted successfully')

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

        time.sleep(2)
        go_btn = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()

        time.sleep(45)
        self.speedtest_download = float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.speedtest_upload = float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        print(f'Download Speed: {self.speedtest_download}')
        print(f'Upload Speed: {self.speedtest_upload}')


if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()


