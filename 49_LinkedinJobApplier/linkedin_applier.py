from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

ll_user = os.environ['username']
ll_pw = os.environ['password']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3771411216&f_LF=f_AL&geoId=102257491&keywords=python'
           '%20developer&location=London%2C%20England%2C%20United%20Kingdom')

# Click signin button
time.sleep(2) # Wait 2 second for page load
sign_in_element = driver.find_element(By.CSS_SELECTOR,value='a[data-tracking-control-name="public_jobs_nav-header-signin"]')
sign_in_element.click()

# Login
time.sleep(2) # Wait 2 second for page load
username = driver.find_element(By.ID, 'username')
username.send_keys(ll_user)

password = driver.find_element(By.ID, 'password')
password.send_keys(ll_pw)

login_element = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_element.click()

# Job application
time.sleep(5) # Wait 2 second for page load
job_listings = driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list-container li a')

for job in job_listings:
    job.click()
    time.sleep(5)
    save_btn = driver.find_element(By.CSS_SELECTOR,'div.mt5 div.display-flex button.jobs-save-button')
    save_btn.click()

