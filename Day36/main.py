# Day 36 - Stock Trading News Monitoring
# Day 36 - Project: Stock Trading News Monitoring
import os
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_endpoint = "https://www.alphavantage.co/query"
alphavantage_api = os.environ.get("ALPHA_API")

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_api,
}

response = requests.get(url=alpha_endpoint, params=alpha_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

values = list(stock_data.values())

if len(values) >= 2:
    yesterday_stock, before_yesterday_stock = values[1]["4. close"], values[2]["4. close"]

if float(before_yesterday_stock) <= 0.99 * float(yesterday_stock) or float(before_yesterday_stock) >= 1.01 * float(yesterday_stock):
    print("Get News!")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

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
