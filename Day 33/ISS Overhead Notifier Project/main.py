import requests
from datetime import datetime
import smtplib
import time

# https://www.latlong.net/
# https://sunrise-sunset.org/api

MY_LAT = 0.0
MY_LONG = 0.0
MY_EMAIL = ""
PASSWORD = ""


while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Europe/Helsinki",
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    latitude_ok = iss_latitude >= MY_LAT - 5 and iss_latitude <= MY_LAT + 5
    longitude_ok = iss_longitude >= MY_LONG - 5 and iss_longitude <= MY_LONG + 5
    is_dark = hour_now < sunrise or hour_now > sunset


    if latitude_ok and longitude_ok and is_dark:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject: Look up 👆\n\nLook up, ISS is currently above your location.")

    time.sleep(60)
