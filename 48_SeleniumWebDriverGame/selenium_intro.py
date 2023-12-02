from selenium import webdriver

# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options) # Using GoogleChrome
driver.get("https://www.amazon.com")

driver.close() # close active tab
driver.quit() # quit entire program