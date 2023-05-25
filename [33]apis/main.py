import requests
import datetime

parameters = {
    "lat":28.605610,
    "lng":77.081398,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
rn = datetime.datetime.now()

print(sunrise)
print(sunset)
print(rn.hour)