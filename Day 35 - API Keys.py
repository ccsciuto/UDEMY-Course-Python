import requests
from twilio.rest import Client

API_KEY = "0a15e395603f856a959421c4f8667317"
MY_LAT = 30.267153
MY_LONG = 97.743057
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC71816a77a30558a4613eed83b8221b21"
auth_token = "3589647e6a33eb13f71f939fbe1d0e2d"

parameters ={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}
response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather = response.json()
will_rain = False
# recovery code 9WW2GME1G34PPX1EVLP8PGLA
for id in weather["list"]:
    new_key = int(id["weather"][0]["id"])
    if new_key == 801:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Testing SMS Weather notif",
        from_="+18334966404",
        to="+16034982416"
    )
    print(message.status)