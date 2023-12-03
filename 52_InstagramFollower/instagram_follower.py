from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class InstaFollower():
    def __init__(self):
        self.user = os.environ['user']
        self.pw = os.environ['pw']

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.similar_account = os.environ['similar']

    def login(self):
        self.driver.get('https://www.instagram.com/')

        time.sleep(5)
        username_elem = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_elem.send_keys(self.user)

        pw_elem = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        pw_elem.send_keys(self.pw)

        login_btn = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()

        time.sleep(5)
        not_now_btn = self.driver.find_element(By.CSS_SELECTOR, value='div._ac8f div[role="button"]')
        not_now_btn.click()

        time.sleep(5)
        not_now_notif_btn = self.driver.find_element(By.CSS_SELECTOR, value='button._a9--._ap36._a9_1')
        not_now_notif_btn.click()

        print('login successfully')

    def find_followers(self):
        time.sleep(3)
        search_btn = self.driver.find_element(By.CSS_SELECTOR, value='div.x1iyjqo2.xh8yej3 > div:nth-child(2) > span > div > a')
        search_btn.click()

        time.sleep(2)
        search_input = self.driver.find_element(By.CSS_SELECTOR, value='div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1d52u69.xktsk01.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div > input')
        search_input.send_keys(self.similar_account)

        time.sleep(2)
        user_link = self.driver.find_element(By.CSS_SELECTOR, value='div > div.x6s0dn4.x78zum5.xdt5ytf.x5yr21d.x1odjw0f.x1n2onr6.xh8yej3 > div > a:nth-child(1)')
        user_link.click()

        time.sleep(5)
        following_link = self.driver.find_element(By.CSS_SELECTOR, value='section > main > div > header > section > ul > li:nth-child(3) > a')
        following_link.click()

    def follow(self):
        time.sleep(5)
        for i in range(1,10):
            time.sleep(5)
            user_name = self.driver.find_element(By.CSS_SELECTOR,
                                                 value=f'div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div > div:nth-child({i}) > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x1iyjqo2.xs83m0k.xeuugli.x1qughib.x6s0dn4.x1a02dak.x1q0g3np.xdl72j9 > div > div > div > div > div > a > div > div > span').text
            follow_btn = self.driver.find_element(By.CSS_SELECTOR,
                                                  value=f'div._aano > div:nth-child(1) > div > div:nth-child({i}) > div > div > div > div:nth-child(3) > div > button')
            follow_btn.click()
            print(f'{user_name} followed')


if __name__ == '__main__':
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()