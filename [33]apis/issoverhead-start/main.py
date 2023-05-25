import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 28.605610 # Your latitude
MY_LONG = 77.081398 # Your longitude


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False

def iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT-5) <= iss_latitude <= (MY_LAT+5) and (MY_LONG-5) <= iss_longitude <= (MY_LONG+5):
        return True
    else:
        return False


while True:
    time.sleep(60)
    if iss_above() and is_dark():
        sender_email = "cheri.luv77@gmail.com"
        sender_pass = "vlrlhviiktciqucs"

        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(sender_email, sender_pass)
                try:
                    connection.sendmail(from_addr=sender_email,
                                        to_addrs="jennahdadilluteya@yahoo.com",
                                        msg=f"Subject:LOOK UP BITCH!\n\nThe fuckin ISS! Its above!!!\nUPAR DEKH"
                                        )
                except Exception as error_message:
                    print(f"Error:{error_message}")
                else:
                    print("MESSAGE SENT SUCCESFULLY")
    else:
        print("still waiting for those one in a million conditions to become true...")
