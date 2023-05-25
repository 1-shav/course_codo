import requests
import sys
from json import dump
from decouple import config

sys.stdout.reconfigure(encoding='utf-8')

url = "http://api.weatherapi.com/v1/forecast.json"

parameters = {"q":(24.50,86.26),
              "key":config("API_KEY", cast=str)
              }

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
hourly = data["forecast"]["forecastday"][0]["hour"]
values = {}
for hour in hourly:
    values[hour["time"]] = (hour["will_it_rain"], hour["will_it_snow"], hour["condition"]["text"])
with open("code_py/[35]more_apis/data.json", "w") as file:
    dump(data, file)
for (time, weather) in values.items():
    if weather[0] == 1:
        print(f"[{time}] don't forget to take that sweet ass umbrella")