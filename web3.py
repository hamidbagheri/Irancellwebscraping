from bs4 import BeautifulSoup
import requests
import csv

rbt_dict = {}
rbt_list = []

urlLists = []
# for read the urls from csv file
# with open('Irancell.csv', newline='') as inputfile:
#     for row in csv.reader(inputfile):
#         urlLists.append(row[0])
#
# for url in urlLists:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     parent = soup.find('ul', class_="songList songlist-table songlist-content rtl")
#     song_name = parent.li.div.find('div', class_='t-info').a.contents[0]


    # for x in parent.find_all('li'):
    #     for y in x.find_all('div', class_=['t-info']):
    #         # print(y.find('a',class_='singer-txt ellipsis').contents[0])
    #         # singer_name = y.find('a', class_='singer-txt ellipsis').contents[0]
    #         # print(singer_name)
    #
    #     for y in x.find_all('div', class_=['t-info']):
    #         song_name =y.find('a', class_='song-txt ellipsis').contents[0]
    #         # print(song_name)
    #         rbt_list.append(song_name)
    #
    # singer_dict={'singer_name':y.find('a', class_='singer-txt ellipsis').contents[0]}

        # for y in x.find_all('div', class_=['t-price']):
        #     song_price = y.p.contents[0]
        #     print(song_price)
        #
        # for y in x.find_all('div', class_=['t-code']):
        #     song_code = y.p.contents[0]
        #     print(song_code)

