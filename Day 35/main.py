import os
import requests
from twilio.rest import Client

# https://openweathermap.org/
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
owm_api_key = os.environ.get("owm_api_key")

# https://www.latlong.net/
lat = ""
lon = ""

# https://www.twilio.com/
twilio_account_sid = ""
twilio_auth_token = os.environ.get("twilio_auth_token")
twilio_from_number = ""
twilio_receiver_number = ""


parameters = {
    "lat": lat,
    "lon": lon,
    "appid": owm_api_key,
    "units": "metric",
    "cnt": 4,

}

response = requests.get(owm_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id > 700:
        will_rain = True

if will_rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body="It's gonna rain today. Remember ☔",
        from_=twilio_from_number,
        to=twilio_receiver_number,
    )

    print(message.status)
