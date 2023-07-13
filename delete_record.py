# Delete record from table.
import mysql.connector

mydb=mysql.connector.connect(host='localhost',password='',user='root', port=3307, database='mydb') 

mycursor=mydb.cursor()                                
sql='delete from customer where name="venky"'
try:
    mycursor.execute(sql)  
    mydb.commit()
    print(mycursor.rowcount,"Rows deleted...")
    
except:
    mydb.rollback()
    print("unable to delete data...")

mycursor.close()
mydb.close()
