from bs4 import BeautifulSoup
import requests
import csv

#یک لیست خالی
urlLists=[]
#باز کردن فایل مورد نظر جهت خواندن لینک ها
with open('Irancell.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        urlLists.append(row[0])

# print(urlLists)
for url in urlLists:
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    result = soup.find_all("li",attrs={"class":"dataContainer"})
    with open('myfile1.txt', 'a',encoding = 'utf-8') as f:
        for items in result:
            final = items.text.strip()
            f.write("%s\n" % final)
            f.write("end")
# for items in result:
 #            print(items.text.strip())
 #            final =items.text.strip()
 #            f.write("%s\n" % final)
# with open("khorooji.txt","w",encoding='utf-8') as OutPutFile:
#     OutPutFile.write(str(final))
#     OutPutFile.close()