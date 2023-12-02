from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # To send keys on keyboard as action
# Any keys on keyboards can be replicated using Keys class

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

articles_num_link_element = driver.find_element(By.CSS_SELECTOR, value="a[title='Special:Statistics']")
articles_num = articles_num_link_element.text
print(articles_num)

# Clicking on element:
# articles_num_link_element.click()

# Find elements by link text & clicking
# all_portals = driver.find_element(By.LINK_TEXT, "Wikipedia")
# all_portals.click()

# Typing in browser
searchbar = driver.find_element(By.CSS_SELECTOR, "input[accesskey='f']")
searchbar.send_keys("Python")
searchbar.send_keys(Keys.ENTER) # enter key action