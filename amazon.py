import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.in/Apple-iPad-Tablet-Wi-Fi-Space/dp/B07C4YKR3J/ref=sr_1_1?keywords=ipad+6th+gen&qid=1570369254&s=apparel&sr=8-1'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


def check_price():
    price = soup.find(id="priceblock_ourprice").get_text()
    convertedPrice = float(price[2:4]+price[5:8])
    print(convertedPrice)
    if (convertedPrice < 22000.0):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('heysumir@gmail.com', 'yourPassword')

    subject = 'Price fell down'
    body = 'Check amazon https://www.amazon.in/Apple-iPad-Tablet-Wi-Fi-Space/dp/B07C4YKR3J/ref=sr_1_1?keywords=ipad+6th+gen&qid=1570369254&s=apparel&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'heysumir@gmail.com',
        'sumir10kumar@gmail.com',
        msg
    )
    print("EMAIL HAS BEEN SENT")

    server.quit


while (True):
    check_price()
    time.sleep(86400)
