import os

import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0",
}

product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

target_price = 100

response = requests.get(product_url, headers=headers)
response.raise_for_status()
html = response.text

soup = BeautifulSoup(html, "html.parser")

get_product_title = soup.find(name="span", id="productTitle").get_text().strip()
get_product_price = float(soup.find(name="span", class_="a-offscreen").get_text().replace("EUR", ""))
get_product_picture = soup.find(name="img", id="landingImage")
image_url = get_product_picture["src"] if get_product_picture else None

if get_product_price < target_price:

    msg = EmailMessage()
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL
    msg["Subject"] = "Amazon Price Alert"

    msg.set_content(
        f"Product:\n{get_product_title}\n\n"
        f"Current Price:\n{get_product_price}€\n\n"
        f"URL:\n{product_url}\n\n"
    )
    msg.add_alternative(f"""
    <html>
    <body style="text-align: center; font-family: Arial; margin: 0px; padding: 0px;">
        <hr>
        <p style="font-size: 18px;">
            <b>Product:</b>
        </p>
        <p style="font-size: 16px;">
            {get_product_title}
        </p>
        <br>
        <p style="font-size: 18px;">
            <b>Current Price:</b>
        </p>
        <p style="font-size: 16px;">
            {get_product_price} EUR
        </p>
        <br>
        <img src="{image_url}">
        <p style="font-size: 16px;">
            <a href={product_url}>View Product</a>
        </p>
        <br>
        
        <hr>
    </body>
</html>
    """, subtype="html"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(MY_EMAIL, MY_PASSWORD)
        smtp.send_message(msg)
