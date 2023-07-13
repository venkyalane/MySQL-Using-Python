import mysql.connector

#show all databases in your system
mydb=mysql.connector.connect(host='localhost',password='', port=3307, user='root')

mycursor = mydb.cursor()

mycursor.execute("show databases")

for x in mycursor:
    print(x)

mycursor.close()
mydb.close()