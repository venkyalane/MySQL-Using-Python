# creating a Table >tablename:customer
import mysql.connector

mydb = mysql.connector.connect(host='localhost', password='', user='root',port=3307, database='mydb')

mycursor=mydb.cursor()
sql_qry = 'create table customer (id int, name varchar(20), address varchar(50))'
try:
    mycursor.execute(sql_qry)
    print("Table successfully created...")
except:
    print("Unable to create...!!")

mycursor.close()
mydb.close()

#create primary key when creating table.
#if table already exist then hadle this error.
#we can check the table is already exist or not with the help of try and except block.

import mysql.connector

try:
    mydb=mysql.connector.connect(host='localhost',password='',user='root',port=3307, database='mydb') 

    mycursor=mydb.cursor()  
    sql_qry = "create table customer (id int auto_increment primary key,name varchar(20),address varchar(20))"                              
    mycursor.execute()  
    mycursor.close()
    mydb.close()

except:
    print("customer Table is already exist...")


