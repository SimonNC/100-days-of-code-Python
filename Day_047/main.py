import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
load_dotenv()
import smtplib

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")



url ="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
}


response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
price = soup.select_one(".a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

product_name = " ".join(
    soup.find(name="span", class_="a-size-large product-title-word-break", id="productTitle").getText().split())

if price < 25.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Alert: Amazon Price Tracker\n\n{product_name}\nis now ${price}.\n\n{url}",
        )

