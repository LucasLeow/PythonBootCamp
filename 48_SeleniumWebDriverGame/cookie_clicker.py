from selenium import webdriver
from selenium.webdriver.common.by import By

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

# Click on Cookie
cookie_element = driver.find_element(By.ID, value="cookie")

timeout = time.time() + 5 # 2 seconds from now
while True:
    while True:
        if time.time() > timeout:
            print('5 seconds up')
            current_money = float(driver.find_element(By.ID, value='money').text.replace(',', ''))

            cursor = driver.find_element(By.ID, value='buyCursor')
            cursor_price = float(cursor.text.split(' ')[2].replace('\nAutoclicks','').replace(',',''))

            grandma = driver.find_element(By.ID, value='buyGrandma')
            grandma_price = float(grandma.text.split(' ')[2].replace('\nA','').replace(',',''))

            factory = driver.find_element(By.ID, value='buyFactory')
            factory_price = float(factory.text.split(' ')[2].replace('\nProduces','').replace(',',''))

            mine = driver.find_element(By.ID, value='buyMine')
            mine_price = float(mine.text.split(' ')[2].replace('\nMines','').replace(',',''))

            shipment = driver.find_element(By.ID, value='buyShipment')
            shipment_price = float(shipment.text.split(' ')[2].replace('\nBrings','').replace(',',''))

            alchemy = driver.find_element(By.ID, value='buyAlchemy lab')
            alchemy_price = float(alchemy.text.split(' ')[3].replace('\nTurns', '').replace(',', ''))

            portal = driver.find_element(By.ID, value='buyPortal')
            portal_price = float(portal.text.split(' ')[2].replace('\nOpens','').replace(',',''))

            time_machine = driver.find_element(By.ID, value='buyTime machine')
            time_machine_price = float(time_machine.text.split(' ')[3].replace('\nBrings','').replace(',',''))

            if current_money >= time_machine_price:
                time_machine.click()
                print('time machine purchased')
            elif current_money >= portal_price:
                portal.click()
                print("portal purchased")
            elif current_money >= alchemy_price:
                alchemy.click()
                print("alchemy purchased")
            elif current_money >= shipment_price:
                shipment.click()
                print("shipment purchased")
            elif current_money >= mine_price:
                mine.click()
                print("mine purchased")
            elif current_money >= factory_price:
                factory.click()
                print("factory purchased")
            elif current_money >= grandma_price:
                grandma.click()
                print("grandma purchased")
            else:
                cursor.click()
                print("cursor purchased")
            break

        cookie_element.click()
    timeout = time.time() + 5