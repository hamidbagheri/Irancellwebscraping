import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='webscraping'
)
mycursor = mydb.cursor()
# mycursor.execute(
#     "CREATE TABLE rbt (ID INT(10),Singer_Name VARCHAR(255)"
#     ", Song_name VARCHAR(255),Song_Price VARCHAR(255),"
#     "Song_Code VARCHAR(255),Song_Period VARCHAR(255))"
#     )

# sql = "INSERT INTO Persons (Singer_Name, Song_name,Song_Price,Song_Code,Song_Period) VALUES (%s, %s,%s,%s,%s)"
# val = ("John", "Highway")
# mycursor.execute(sql, val)

mydb.commit()

# print(mycursor.rowcount, "record inserted.")
