import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/CHEFMAN-Multifunction-Rotisserie-Dehydrator-Convection/dp/B08DL8WH9V?ref_=Oct_DLandingS_D_c1588a48_0&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,te;q=0.8"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

title = soup.find(id="productTitle").get_text().strip()
print(title)
BUY_PRICE = 200

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
