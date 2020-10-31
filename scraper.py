#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/PHANTEKS-Eclipse-P400A-Midi-Tower-Tempered/dp/B07TTDW37F/ref=sr_1_4?crid=2V5KCVVGQ9NGS&dchild=1&keywords=phanteks+p400a&qid=1604147817&sprefix=phanteks%2Caps%2C217&sr=8-4'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])

    if(converted_price < 75.00):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 75.00):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hpreston2909@gmail.com', 'soaoxhlwvdmdjalt')

    subject = 'Price fell down!'
    body = 'Check Amazon link: https://www.amazon.co.uk/PHANTEKS-Eclipse-P400A-Midi-Tower-Tempered/dp/B07TTDW37F/ref=sr_1_4?crid=2V5KCVVGQ9NGS&dchild=1&keywords=phanteks+p400a&qid=1604147817&sprefix=phanteks%2Caps%2C217&sr=8-4'

    msg =f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'hpreston2909@gmail.com',
        'hpreston2909@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)

