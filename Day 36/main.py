import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# https://www.alphavantage.co
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

# https://www.alphavantage.co/query - https://newsapi.org/docs/endpoints/everything
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# https://www.twilio.com/
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_RECEIVER_NRO = ""
TWILIO_FROM_NRO = ""

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "outputsize": "compact"
}

news_param = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "language": "en",
    "pageSize": 3,
}


def get_news():
    news_response = requests.get(NEWS_ENDPOINT, params=news_param)
    news_response.raise_for_status()
    news_data = news_response.json()
    return news_data


stocks_response = requests.get(STOCK_ENDPOINT, params=stock_param)
stocks_response.raise_for_status()
data = stocks_response.json()

time_series = data["Time Series (Daily)"]
sorted_days = sorted(time_series.keys())
previous_day = sorted_days[-2]
latest_day = sorted_days[-1]
previous_price = float(time_series[previous_day]["4. close"])
latest_price = float(time_series[latest_day]["4. close"])

change_in_price = round((latest_price - previous_price) / previous_price * 100)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

news = get_news()

if change_in_price > 5:
    if previous_price > latest_price:
        text = f"{STOCK} 🔻{change_in_price}%.\n"
    else:
        text = f"{STOCK} 🔺{change_in_price}%.\n"

    for i in range(3):
        client.messages.create(
            body=f"{text}\n"
                 f"{news['articles'][i]['title']}\n"
                 f"{news['articles'][i]['description']}\n",
            from_=TWILIO_FROM_NRO,
            to=TWILIO_RECEIVER_NRO,
        )
