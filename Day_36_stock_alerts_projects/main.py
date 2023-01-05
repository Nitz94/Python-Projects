import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "enter key"
API_KEY_ST = "enter st"

TW_SID = "enter sid"
TW_AUTH_TOKEN = "enter token"
# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_ST
}


# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()

data_dict = data["Time Series (Daily)"]

# using list comprehension on the dictionary to convert items into a list so that they can be called by indexing
stock_data = [value for (key, value) in data_dict.items()]  # we only need values. keys are dates which are not ideal
# print(stock_data)

yesterday_data = stock_data[0]
yesterday_closing = float(yesterday_data["4. close"])
print(yesterday_closing)


# Get the day before yesterday's closing stock price

day_before_yesterday_data = stock_data[1]
day_before_yesterday_closing = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing)


# Find the positive difference between today's and yesterday's prices
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = (float(yesterday_closing) - float(day_before_yesterday_closing))
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"


# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday

diff_percentage = round((difference / float(yesterday_closing) * 100))


# if percentage is greater than a specified number,then get three news articles relating to the company
if abs(diff_percentage) > 1:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_KEY

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)  # using NewsAPI to get articles on the COMPANY_NAME
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    # Use Python slice operator to create a list that contains the first 3 articles
    relevant_news_articles = news_data[:3]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    # relevant news articles is a list. using list comprehension create a new list of the first 3 article's
    # headline and description in a format of "Headline": {article headline}\n "brief":{article description

    formatted_news = [f"{COMPANY_NAME}:{up_down}:{diff_percentage}Headline: {article['title']}" \
                      f"\nBrief:{article['description']}" for article in relevant_news_articles]

# TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TW_SID, TW_AUTH_TOKEN)
    for article in formatted_news:
        message = client.messages \
            .create(body=article, from_='+19036664583', to='+123456789')

        print(message.sid)

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
  coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
  coronavirus market crash.
"""

