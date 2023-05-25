import requests
from decouple import config
import smtplib
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stonks_url = "https://www.alphavantage.co/query"
stonks_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": config("STONKS_API_KEY")
}
stonks_response = requests.get(stonks_url, params=stonks_parameters)
stonks_response.raise_for_status()
stonks_data = stonks_response.json()["Time Series (Daily)"]
dates = [date for date in stonks_data]
current_price = float(stonks_data[dates[0]]["4. close"])
previous_price = float(stonks_data[dates[1]]["4. close"])
difference = current_price - previous_price
diff_perc = round(difference / previous_price * 100, 2)
print(f"current price :: {current_price}")
print(f"previous price :: {previous_price}")
print(f"difference :: {difference}")
print(f"diff_perc :: {diff_perc}%")



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_url = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "from": dates[1],
    "sortBy": "relevancy",
    "apiKey": config("NEWS_API_KEY")
}
news_response = requests.get(news_url, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
articles = [info for info in news_data["articles"]]
first3 = [articles[i] for i in range(3)]

message = ""

if abs(diff_perc) >= 0:
    if diff_perc > 0:
        message += (f"TSLA :: 🔺{diff_perc}%")
    else:
        message += (f"TSLA :: 🔻{abs(diff_perc)}%")
        
    for news in first3:
        title = news["title"]
        description = news["description"]

        message += (f"\nHeadline :: {title}\nBrief :: {description}")
print(message)



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
"""
sender_email = "cheri.luv77@gmail.com"
sender_pass = "vlrlhviiktciqucs"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(sender_email, sender_pass)
    connection.sendmail(
        from_addr=sender_email,
        to_addrs="vanshav19@gmail.com",
        msg=(f"Subject:STONKS INFO\n\n{message}")
    )
    print("EMAIL SENT SUCCESFULLY!")
"""    

#Sending message
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = ('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

sms = client.messages.create(
    body=message,
    from_="whatsapp:+14155238886",
    to="whatsapp:+919818989400"
)
print(sms.sid)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
