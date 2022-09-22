import requests

from twilio.rest import Client

API_KEY = "Your api key"
MY_LAT = 8.695
MY_LON = 76.8179
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "your account sid"
auth_token = "your auth token"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

# weather_data_id = weather_data["hourly"][0]["weather"][0]["id"]  # accessing first hour id

# slicing data from json to get next 12 hours forecast
weather_data_id = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_data_id:  # getting hold of items under weather key
    condition_id = hour_data["weather"][0]["id"]
    if condition_id < 700:   # check if both sides are int
        will_rain = True


if will_rain:


    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(body="It's going to rain today. Bring an umbrella.", from_="+19036664583", to='your phone number')

    print(message.status)
