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

response_stock = requests.get(url=alpha_endpoint, params=alpha_params)
response_stock.raise_for_status()
stock_data = response_stock.json()["Time Series (Daily)"]

values = list(stock_data.values())

if len(values) >= 2:
    yesterday_stock, before_yesterday_stock = values[0]["4. close"], values[1]["4. close"]

percent_difference = round((float(yesterday_stock) - float(before_yesterday_stock))/float(yesterday_stock) * 100)

if percent_difference <= -5 or percent_difference >= 5:
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

    final_message = f"{STOCK}: {percent_difference}%\n"
    for article in articles:
        final_message += f"Headline: {article['headline']}\n"
        final_message += f"Brief: {article['brief']}\n"

    client = Client(account_sid, auth_token)
    message = client.message \
        .create(
            body=final_message
            from="..."
            to="..."
        )
    print(message.status)
