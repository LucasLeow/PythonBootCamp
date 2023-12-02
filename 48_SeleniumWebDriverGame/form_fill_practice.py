from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://secure-retreat-92358.herokuapp.com/')

fname_element = driver.find_element(By.CSS_SELECTOR, value="input[name='fName']")
lname_element = driver.find_element(By.CSS_SELECTOR, value="input[name='lName']")
email_element = driver.find_element(By.CSS_SELECTOR, value="input[name='email']")

fname_element.send_keys('Lucas')
lname_element.send_keys('Leow')
email_element.send_keys('ljh@hotmail.com')

