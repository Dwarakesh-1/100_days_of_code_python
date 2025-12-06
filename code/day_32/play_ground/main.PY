import smtplib
import datetime as dt
import random


MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_password"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="reciever_email@gmail.com",
            msg=f"Subject: Saturday Motivation\n\n{quote}"
        )
