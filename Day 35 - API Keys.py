import requests
from twilio.rest import Client


MY_LAT = 30.267153
MY_LONG = 97.743057
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"


parameters ={
    "lat": MY_LAT,
    "lon": MY_LONG,

    "cnt": 4
}
response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather = response.json()
will_rain = False

for id in weather["list"]:
    new_key = int(id["weather"][0]["id"])
    if new_key == 801:
        will_rain = True
if will_rain:

    message = client.messages \
        .create(
        body="Testing SMS Weather notif",
        from_="+",
        to="+"
    )
    print(message.status)