from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Main_Page')

articles_num_link_element = driver.find_element(By.CSS_SELECTOR, value="a[title='Special:Statistics']")
articles_num = articles_num_link_element.text
print(articles_num)

# Clicking on link:
articles_num_link_element.click()