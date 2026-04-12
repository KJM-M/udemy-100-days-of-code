import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = ""
PASSWORD = ""

now = dt.datetime.now()
month = now.month
day = now.day

letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthdays = pandas.read_csv('birthdays.csv')
today = birthdays[(birthdays["month"] == month) & (birthdays["day"] == day)]

if not today.empty:
    sankari = today["name"].iloc[0]
    email = today["email"].iloc[0]

    chosen_letter = random.choice(letter_templates)

    with open(chosen_letter) as f:
        template = f.read()

    personalized = template.replace("[NAME]", sankari)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday\n\n{personalized}"
                            )
