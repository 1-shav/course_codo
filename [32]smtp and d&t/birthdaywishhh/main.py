##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
from random import choice
import smtplib

birthday_data = pd.read_csv("code_py/[32]smtp and d&t/birthdaywishhh/birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")

rn = dt.datetime.now()
month = rn.month
day = rn.day

sender_email = "cheri.luv77@gmail.com"
sender_pass = "vlrlhviiktciqucs"

for person in birthday_dict:
    if person["month"] == month and person["day"] == day:
        letter = choice(["code_py/[32]smtp and d&t/birthdaywishhh/letter_templates/letter_1.txt",
                "code_py/[32]smtp and d&t/birthdaywishhh/letter_templates/letter_2.txt",
                "code_py/[32]smtp and d&t/birthdaywishhh/letter_templates/letter_3.txt"])
        
        person_name = person["name"]
        with open(letter, "r") as letter_file:
            letter_text = letter_file.read()
            letter_updated = letter_text.replace("[NAME]", person_name)
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(sender_email, sender_pass)
            try:
                connection.sendmail(from_addr=sender_email,
                                    to_addrs=person["email"],
                                    msg=f"Subject:HAPPY BIRTHDAY {person_name}\n\n{letter_updated}"
                                    )
            except Exception as error_message:
                print(f"Error:{error_message}")
            else:
                print("MESSAGE SENT SUCCESFULLY")
