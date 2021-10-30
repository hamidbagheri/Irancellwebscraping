import mysql.connector

mydb = mysql.connector.connect(
    # host="localhost",
    user="root",
    password="",
    database='webscraping'
)
mycursor = mydb.cursor()

sql = "INSERT INTO Persons (FirstName, LastName) VALUES (%s, %s)"
val = ("John", "Highway")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
