import mysql.connector

#show all tables in perticular database
mydb = mysql.connector.connect(host='localhost', user='root', password='', port=3307, database='mydb')

mycursor=mydb.cursor()
mycursor.execute("show tables")

for x in mycursor:
    print(x)

mycursor.close()
mydb.close()