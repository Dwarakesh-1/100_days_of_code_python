import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os


API_KEY = ""
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 51.759048
MY_LONG = 19.458599
ACCOUNT_SID = ""
AUTH_TOKEN = ""

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()

weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.eviron["https_proxy"]}

    client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)
    message = client.messages.create(
        body= "It's going to rain today. Remember to bring an umbrella!",
        from_= "whatsapp:",
        to= "whatsapp:"
    )
    print(message.status)
