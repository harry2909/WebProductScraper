import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.uk/PHANTEKS-Eclipse-P400A-Midi-Tower-Tempered/dp/B07TTDW37F/ref=sr_1_4?crid=2V5KCVVGQ9NGS&dchild=1&keywords=phanteks+p400a&qid=1604147817&sprefix=phanteks%2Caps%2C217&sr=8-4'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:3]

    if(converted_price < 75):
        send_mail()

    print(converted_price.strip())
    print(title.strip())

def send_mail():
    