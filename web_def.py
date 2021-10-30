from bs4 import BeautifulSoup
import requests
import csv

urlLists = []
RBT_list = []

def read_urls():
    with open('Irancell.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            urlLists.append(row[0])


read_urls()

for url in urlLists:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    parent = soup.find('ul', class_="songList songlist-table songlist-content rtl")
    song_name = parent.li.div.find('div', class_='t-info').a.contents[0]
    for x in parent.find_all('li'):
        for y in x.find_all('div', class_=['t-info']):
            Singer_Name = y.find('a', class_='singer-txt ellipsis').contents[0]

        for y in x.find_all('div', class_=['t-info']):
            Song_name = y.find('a', class_='song-txt ellipsis').contents[0]

        for y in x.find_all('div', class_=['t-price']):
            Song_Price = y.p.contents[0]

        for y in x.find_all('div', class_=['t-code']):
            Song_Code = y.p.contents[0]
        for y in x.find_all('div', class_=['t-period']):
            Song_Period = y.p.contents[0]

        RBT_Dict = {'Singer_Name': Singer_Name,
                    'Song_name': Song_name,
                    'Song_Price': Song_Price,
                    'Song_Code': Song_Code,
                    'Song_Period': Song_Period,
                    }
        # print(RBT_Dict)
        RBT_list.append(RBT_Dict)
print(RBT_list)
for x in RBT_list:
    print(x.pop('Singer_Name'))
    print(x.pop('Song_name'))
    print(int(x.pop('Song_Code')))
    print('*******')

