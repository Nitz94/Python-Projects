import requests
from bs4 import BeautifulSoup
import lxml
from re import sub
from decimal import Decimal
import smtplib

PRODUCT_URL = "https://www.amazon.in/Samsung-Galaxy-Awesome-Storage-Without/dp/B09XHLDHQ3/" \
              "ref=sr_1_5?crid=3PHFU1AWO84RW&keywords=samsung%2Bgalaxy%2Ba73%2B5g&qid=1663849496&" \
              "sprefix=samsung%2Bgalaxy%2Ba73%2B5g%2Caps%2C462&sr=8-5&th=1"

#  GETTING  HOLD OF THE PRODUCT'S WEB PAGE IN AMAZON:

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                  "537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


response = requests.get(url=PRODUCT_URL, headers=headers)
response.raise_for_status()
product_web_page = response.text

# print(product_web_page)

#  SCRAPPING THE AMAZON WEB PAGE:
soup = BeautifulSoup(product_web_page, "lxml")

product_a_price = soup.find(name="span", class_="a-price-whole")
product_price = product_a_price.getText()

# converting price tag to decimal since float is not recommended for finance and to avoid locale issues
money = product_price
price = Decimal(sub(r'[^\d.]', '', money))
# print(price)


# EMAIL ALERT TO USER IF THE PRICE IS BELOW THE TARGET PRICE
# add the email id and passwords as environment variables and use os.getenv() method to use it in live code

TARGET_PRICE = 30000
if price <= TARGET_PRICE:
    EMAIL = "Your email address"
    EMAIL_PSD = "Your email password"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PSD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,  # self alert email
            msg=f"Subject: Amazon Price Tracker Alert: {price}\n "
                f"Click here to view product {PRODUCT_URL}".encode("utf-8")

        )
    print("Email Send")











