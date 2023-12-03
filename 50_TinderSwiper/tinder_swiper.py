from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

FB_user = os.environ['user']
FB_pw = os.environ['pw']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://tinder.com/')

# Sign-in
time.sleep(3) # Wait 2 second for page load
sign_in_element = driver.find_element(By.CSS_SELECTOR, value='a > div.w1u9t036 > div.l17p5q9z')
sign_in_element.click()

time.sleep(2)
fb_login_btn = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Log in with Facebook"]')
fb_login_btn.click()

# Facebook Login Tab
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(2)
user = driver.find_element(By.CSS_SELECTOR, value='input[name="email"]')
user.send_keys(FB_user)

password = driver.find_element(By.CSS_SELECTOR, value='input[name="pass"]')
password.send_keys(FB_pw)

submit = driver.find_element(By.CSS_SELECTOR, value='input[name="login"]')
submit.click()

# Revert back to tinder window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(10)
allow_location = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Allow"')
allow_location.click()

time.sleep(3)
enable_notification = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Not interested"')
enable_notification.click()

# Swipe left
while True:
    time.sleep(5)
    person_name = driver.find_element(By.CSS_SELECTOR, value='span[itemprop="name"]').text
    reject_btn = driver.find_element(By.CSS_SELECTOR, value='#s-547617529 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-nope-default\) > button')
    reject_btn.click()
    print(f'rejected {person_name}')
