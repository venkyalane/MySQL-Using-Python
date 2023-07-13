import mysql.connector
# create database (databasename:mydb)
mydb=mysql.connector.connect(host='localhost', password='', user='root', port=3307)

#create cursor object
mycursor = mydb.cursor()

#Sql Query
sql_qry = 'create database mydb'

try:
    #query run in execue method
    mycursor.execute(sql_qry)
    print("Database Successfully created...")

except:
    print("Something went wrong")

mycursor.close()
mydb.close()
