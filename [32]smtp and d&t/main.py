
import smtplib
import datetime as dt
from random import choice

with open("code_py/[32]smtp and d&t/hahas.txt", "r") as file:
    data = file.read()
    jokes = data.split("\n")



rn = dt.datetime.now()
day = rn.weekday()

sender_email = "cheri.luv77@gmail.com"
sender_pass = "vlrlhviiktciqucs"

if day == 3:
    pseudo_random_joke = choice(jokes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(sender_email, sender_pass)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs="jennahdadilluteya@yahoo.com",
            msg=f"Subject:ThirstyThirsdayHahas\n\n{pseudo_random_joke}"
        )
    


"""

import requests
import json

limit = 75
api_url = f'https://api.api-ninjas.com/v1/dadjokes?limit={limit}'
response = requests.get(api_url, headers={'X-Api-Key': 'VE/JA6pyQpFc+m0/CemMQA==EZtmgCPvoE1Ui0h5'})
if response.status_code == requests.codes.ok:
    api_data = response.json()
else:
    print("Error:", response.status_code, response.text)

jokes = [joke["joke"] for joke in api_data]

with open("code_py/[32]smtp and d&t/hahas.txt", "a") as file:
    for joke in jokes:
        file.write(f"{joke}\n")
"""        