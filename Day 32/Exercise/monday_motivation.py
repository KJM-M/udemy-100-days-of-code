# import smtplib
#
# my_email = ""
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="",
#         msg="Subject:Hello\n\nThis is the body of the email"
#     )


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2026, month=1, day=1)



import smtplib
import datetime as dt
import random

MY_EMAIL = ""
PASSWORD = ""

now = dt.datetime.now()
day_of_week = now.weekday() + 1

if day_of_week == 7:
    with open("./quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )
