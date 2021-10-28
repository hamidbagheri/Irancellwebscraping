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
# print(urlLists)
for url in urlLists:
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all()
    # print(result)

    result = soup.find_all("li", attrs={"class": "dataContainer"})

    # print(result)
    mylist=[]
    with open('myfile1.txt', 'a', encoding='utf-8') as f:
        for items in result:
            final = items.text.strip()
            x = final.replace("\n", "|")
            print(x)
            f.write("%s\n" % x)
            # f.write("End \n")