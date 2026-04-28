import os
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

target_url = "https://appbrewery.github.io/instant_pot/"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0"
}

target_price = 100.00

response = requests.get(target_url, headers=header)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# price_whole = soup.find(name="span", class_="a-price-whole").get_text().strip(".")
# price_decimal = soup.find(name="span", class_="a-price-decimal").get_text()
# price_fraction = soup.find(name="span", class_="a-price-fraction").get_text()
# print(float(f"{price_whole}{price_decimal}{price_fraction}"))

product_title = soup.find(name="div", id="titleSection").get_text()
clean_product_title = " ".join(product_title.split()).encode("ascii", "ignore").decode()

current_price = float(soup.find(name="span", class_="a-offscreen").get_text().strip("$"))

if current_price < target_price:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(user=MY_EMAIL, password=MY_PASSWORD)
        smtp.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Price Alert\n\n{clean_product_title}\nCurrent Price: {current_price}$\nURL: {target_url}"
        )
