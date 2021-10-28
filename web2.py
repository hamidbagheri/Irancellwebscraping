from typing import final
from bs4 import BeautifulSoup
import requests
import csv

# یک لیست خالی
urlLists = []
# باز کردن فایل مورد نظر جهت خواندن لینک ها
with open('Irancell.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        urlLists.append(row[0])

for url in urlLists:
    response = requests.get(url)
    # print(response)
    soup = BeautifulSoup(response.content, "html.parser")

    result = soup.find('ul', class_="songList songlist-table songlist-content rtl")
    song_name = result.li.div.find('div', class_='t-info').a.contents[0]
    singer_name = result.li.div.find('div', class_='t-info').find('a', class_='singer-txt ellipsis').contents[0]
    tone_code = result.li['tonecode']
    price = result.li.find('div', class_='t-price').p.contents[0]
    period = result.li.find('div', class_='t-period').p.contents[0]
    print(singer_name, song_name, tone_code, price, period)

