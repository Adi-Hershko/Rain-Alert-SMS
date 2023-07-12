import requests
from twilio.rest import Client

LATITUDE = 32.089870
LONGITUDE = 34.880451
API_KEY = "Your API Key"
API_URL = "https://api.openweathermap.org/data/2.5/onecall"
PARAMETERS = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "exclude": "current,daily,minutely",
    "appid": API_KEY
}

response = requests.get(url=API_URL, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()["hourly"]

weather_slice = weather_data[:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    account_sid = "TWILIO ACCOUNT SID"
    auth_token = "TWILIO AUTH TOKEN"
    twilio_phone_number = "TWILIO PHONE NUMBER"
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It will rain today, bring an umbrella. 🌧️☂️",
                                     from_=twilio_phone_number,
                                     to="YOUR PHONE NUMBER")
    print(message.status)

