import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.uk/PHANTEKS-Eclipse-P400A-Midi-Tower-Tempered/dp/B07TTDW37F/ref=sr_1_4?crid=2V5KCVVGQ9NGS&dchild=1&keywords=phanteks+p400a&qid=1604147817&sprefix=phanteks%2Caps%2C217&sr=8-4'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")

print(title)d