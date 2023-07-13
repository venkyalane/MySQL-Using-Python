# insert record in table (single row and multiple rows)
import mysql.connector

mydb=mysql.connector.connect(host='localhost',password='',user='root',port=3307, database='mydb') 

mycursor=mydb.cursor()                                
sql="INSERT INTO customer (id,name,address) values (2,'dinesh','nanded'),(3,'mohan','Nagar')"
try:
    mycursor.execute(sql)  
    mydb.commit()
    print(mycursor.rowcount,"Rows inserted...")
    print(mycursor.lastrowid)
except:
    mydb.rollback()
    print("unable to insert data...")

mycursor.close()
mydb.close()