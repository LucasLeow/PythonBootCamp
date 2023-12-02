import os
import smtplib

import requests
from bs4 import BeautifulSoup

# Setup  ====================================================================
TARGET_PRICE = 380
my_email = os.environ['my_email']
email_pw = os.environ['email_pw']
to_address = os.environ['to_address']

amazon_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "x-forwarded-proto": "https",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br"
}
amazon_product_URL = 'https://www.amazon.sg/Nintendo-Switch-Console-Joycon-color/dp/B098RL6SBJ/ref=sr_1_3?adgrpid=123169936989&hvadid=584073578834&hvdev=c&hvlocphy=9062504&hvnetw=g&hvqmt=e&hvrand=4145510755406069163&hvtargid=kwd-1389753740093&hydadcr=21903_329741&keywords=amazon%2Bswitch%2Boled&qid=1701429172&sr=8-3&th=1'
res = requests.get(
    url=amazon_product_URL,
    headers=amazon_header
)
print(res.text)
amazon_product_html = res.text
soup = BeautifulSoup(amazon_product_html, 'html.parser')

# Web Scrap for Price  ====================================================================
try:
    product_title = soup.find(name="span", id="productTitle").getText().replace('\t', '')
    product_price = float(soup.find(name='span', class_='a-price-whole').getText())
    print(product_price)
except TypeError:
    print('Amazon Page returned captcha instead')

# Email Alert  ====================================================================
if product_price < TARGET_PRICE:
    text = (f"{product_title} is now {product_price} \n"
            f"{amazon_product_URL}")
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=f"Subject: Amazon Price Alert! \n\n {text}"
        )
        print('Alert mail sent successfully!')
