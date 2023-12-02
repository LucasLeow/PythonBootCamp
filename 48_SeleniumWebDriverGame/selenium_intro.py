from selenium import webdriver
from selenium.webdriver.common.by import By # To search for html elements

# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options) # Using GoogleChrome
driver.get("https://www.amazon.sg/Nintendo-Switch-Console-Joycon-color/dp/B098RL6SBJ/ref=sr_1_3?adgrpid=123169936989"
           "&hvadid=584073578834&hvdev=c&hvlocphy=9062504&hvnetw=g&hvqmt=e&hvrand=4145510755406069163&hvtargid=kwd"
           "-1389753740093&hydadcr=21903_329741&keywords=amazon%2Bswitch%2Boled&qid=1701429172&sr=8-3&th=1")

# Find content within webpage HTML
price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

# Other ways to get single elements | If want multiple, use find_elements
search_bar = driver.find_element(By.NAME, value="q") # input tags usually have 'name' attribute
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(doc_link.text)

# Go to devtool -> desired element -> right click -> copy value -> XPath
tough_element = driver.find_element(By.XPATH, value='//*[@id="tabs--1-content-3"]')
print(tough_element.text)

# driver.close() # close active tab
driver.quit() # quit entire program