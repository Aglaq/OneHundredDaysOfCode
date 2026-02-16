# Day 36 - Stock Trading News Monitoring
# Day 36 - Project: Stock Trading News Monitoring
from datetime import date, timedelta
import os
import requests
# from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_endpoint = "https://www.alphavantage.co/query"
alphavantage_api = os.environ.get("ALPHA_API")
news_api = os.environ.get("NEWS_API")
yesterday = (date.today() - timedelta(days=1)).isoformat()
news_endpoint = "https://newsapi.org/v2/everything"
account_sid = "..."
auth_token = "..."

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_api,
}

news_params = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "popularity",
    "apiKey": news_api, 
}

# response_stock = requests.get(url=alpha_endpoint, params=alpha_params)
# response_stock.raise_for_status()
# stock_data = response_stock.json()["Time Series (Daily)"]

# values = list(stock_data.values())

# if len(values) >= 2:
#     yesterday_stock, before_yesterday_stock = values[0]["4. close"], values[1]["4. close"]

# if float(before_yesterday_stock) <= 0.95 * float(yesterday_stock) or float(before_yesterday_stock) >= 1.05 * float(yesterday_stock):
response_news = requests.get(url=news_endpoint, params=news_params)
response_news.raise_for_status()
news_data = response_news.json()

articles = []

for i in range(3):
    article = {
        "headline": news_data["articles"][i]["title"],
        "brief": news_data["articles"][i]["description"]
    }
    articles.append(article)

final_message = f"{STOCK}: \n"
for article in articles:
    final_message += f"Headline: {article['headline']}\n"
    final_message += f"Brief: {article['brief']}\n"

# client = Client(account_sid, auth_token)
# message = client.message \
#     .create(
#         body=final_message
#         from="..."
#         to="..."
#     )
# print(message.status)


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
