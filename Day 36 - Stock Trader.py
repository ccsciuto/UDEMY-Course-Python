import requests
from datetime import datetime, timedelta
from newsapi import NewsApiClient



TODAY = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
YESTERDAY = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
STOCK_API = "WE8KX097CNUM1HC4"
NEWS_API_KEY = "7d4982a65a0742d8966797dadb1311e3"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNCTION = "TIME_SERIES_DAILY"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_parameters = {
    "function": FUNCTION,
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": STOCK_API
}
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}
today = datetime.today().strftime('%Y-%m-%d')
yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
print(yesterday)
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
# today_close = float(stock_response.json()["Time Series (Daily)"][today]["4. close"])
# yesterday_close = float(stock_response.json()["Time Series (Daily)"][yesterday]["4. close"])
# perc_change = abs(today_close-yesterday_close)/yesterday_close
articles = news_response.json()["articles"]
three_art = articles[:3]

