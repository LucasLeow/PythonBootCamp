from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')


time_contents = driver.find_elements(By.CSS_SELECTOR, value='.medium-widget.event-widget.last time')
event_contents = driver.find_elements(By.CSS_SELECTOR, value='.medium-widget.event-widget.last li a')

content_dict = {i: {'time': time_contents[i].text, 'name':event_contents[i].text} for i in range(len(time_contents))}

driver.quit()

print(content_dict)