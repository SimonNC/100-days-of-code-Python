import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

api_key = os.getenv("OW_API_KEY")
baseUrl = "https://api.openweathermap.org/data/2.5/forecast"
my_number = os.getenv("MY_NUMBER")
myLat = -22.271072
myLng = 166.441650

parameters = {
    "lat": myLat,
    "lon": myLng,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
    "lang": "fr"

}

request = f"{baseUrl}"
response = requests.get(request, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"])

weather_forecasts = weather_data["list"]
is_raining = False
for day in weather_forecasts:
    print(day["weather"][0]["id"])
    if int(day["weather"][0]["id"]) < 700:
        is_raining = True
if is_raining:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. Remember to bring an ☂️.",
        from_="+16562284539",
        to=my_number
    )
    print(message.status)

else:
    print("It's not raining today")
