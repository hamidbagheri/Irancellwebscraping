from bs4 import BeautifulSoup
import requests
import csv
urlLists = []
# for read the urls from csv file
with open('Irancell.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        urlLists.append(row[0])
for url in urlLists:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    parent = soup.find('ul', class_="songList songlist-table songlist-content rtl")
    song_name = parent.li.div.find('div', class_='t-info').a.contents[0]
    song_list=[]
    for x in parent.find_all('li'):
        for y in x.div.find_all('div',class_='t-info'):
            mysongs=y.a.contents[0]
            song_list.append(mysongs)


    # song_name = result.li.div.find('div', class_='t-info').a.contents[0]
    # print(song_name)
   #  singer_name = result.li.div.find('div', class_='t-info').find('a',class_='singer-txt ellipsis').contents[0]
   #  tone_code=result.li['tonecode']
   #  price=result.li.find('div',class_='t-price').p.contents[0]
   #  period=result.li.find('div',class_='t-period').p.contents[0]
   #  print(singer_name,song_name,tone_code,price,period)
   #