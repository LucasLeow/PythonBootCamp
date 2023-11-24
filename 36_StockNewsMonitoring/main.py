import requests
import os
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PRICE_TOLERANCE = 0.05

A_V_API_KEY = os.environ['A_V_API_KEY']
N_API_KEY = os.environ['N_API_KEY']

up_emoji = '⬆'
down_emoji = '⬇'

last_biz_date_price = 0
day_before_last_price = 0
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def check_stock_movement(ticker):
    global last_biz_date_price, day_before_last_price
    A_V_endpoint = 'https://www.alphavantage.co/query'
    A_V_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': ticker,
        'apikey': A_V_API_KEY,
    }

    A_V_res = requests.get(A_V_endpoint, params=A_V_params)
    A_V_res.raise_for_status()
    tsla_data = A_V_res.json()["Time Series (Daily)"]

    last_biz_date = list(tsla_data.keys())[0]
    day_before_last = list(tsla_data.keys())[1]

    last_biz_date_price = float(tsla_data[last_biz_date]["2. high"])
    day_before_last_price = float(tsla_data[day_before_last]["2. high"])

    if abs(last_biz_date_price - day_before_last_price) / last_biz_date_price >= PRICE_TOLERANCE:
        return True
    return False

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(ticker):
    yesterday = dt.datetime.today() - dt.timedelta(days=1)
    last_week = yesterday - dt.timedelta(days=7)

    start_date = last_week.strftime('%Y-%m-%d')
    end_date = yesterday.strftime('%Y-%m-%d')
    print(start_date, end_date)

    N_endpoint = 'https://newsapi.org/v2/everything'
    N_params = {
        'q': 'tesla',
        'from': start_date,
        'to': end_date,
        'sortBy': 'popularity',
        'pageSize': 10,
        'apiKey': N_API_KEY
    }

    N_res = requests.get(N_endpoint, params=N_params)
    N_res.raise_for_status()
    N_data = N_res.json()['articles'][:3]
    return N_data

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == '__main__':
    emoji = down_emoji
    price_fluctuated = check_stock_movement(STOCK)
    if not price_fluctuated:
        price_percentage = abs(last_biz_date_price - day_before_last_price) / last_biz_date_price
        if day_before_last_price < last_biz_date_price:
            emoji = up_emoji
        news_data = get_news(STOCK)
        for news in news_data:
            text = f'''
            {STOCK}: {emoji} {round(price_percentage * 100)}%
            Headline: {news['title']}
            Brief: {news['description']}
            '''
            print(text)
