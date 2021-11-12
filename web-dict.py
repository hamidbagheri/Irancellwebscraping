from bs4 import BeautifulSoup
import requests
import csv
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='webscraping'
)

RBT_list = []
urlLists = []
# for read the urls from csv file
with open('Irancell.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        urlLists.append(row[0])

for url in urlLists:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    parent = soup.find('ul', class_="songList songlist-table songlist-content rtl")
    for x in parent.find_all('li'):
        for y in x.find_all('div', class_=['t-info']):
            Singer_Name = y.find('a', class_='singer-txt ellipsis').contents[0]
        for y in x.find_all('div', class_=['t-info']):
            Song_Name = y.find('a', class_='song-txt ellipsis').contents[0]
        for y in x.find_all('div', class_=['t-price']):
            Song_Price = y.p.contents[0]
        for y in x.find_all('div', class_=['t-code']):
            Song_Code = y.p.contents[0]
        for y in x.find_all('div', class_=['t-period']):
            Song_Period = y.p.contents[0]

        RBT_Dict = {'Singer_Name': Singer_Name,
                    'Song_Name': Song_Name,
                    'Song_Price': Song_Price,
                    'Song_Code': int(Song_Code),
                    'Song_Period': Song_Period,
                    }
        RBT_list.append(RBT_Dict)

        sql = "insert into rbt(Singer_Name, Song_Name,Song_Price,Song_Code,Song_Period) ' \
                'values ('{0}','{1}','{2}','{3}','{4}');".format(Singer_Name, Song_Name, Song_Price, Song_Code,
                                                                 Song_Period)

for item in range(len(RBT_list)):
    sql = "insert into rbt(Singer_Name, Song_Name,Song_Price,Song_Code,Song_Period) " \
          "values ('{0}','{1}','{2}','{3}','{4}');"\
        .format(RBT_list[item]['Singer_Name'],RBT_list[item]['Song_Name'],RBT_list[item]
    ['Song_Price'],RBT_list[item]['Song_Code'],RBT_list[item]['Song_Period'])
    # print(type(RBT_list[item]['Song_Code']))

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()