#update record from customer table.
import mysql.connector

mydb=mysql.connector.connect(host='localhost', password='', user='root', port=3307, database='mydb') 

mycursor=mydb.cursor()                                
sql='update customer set address="pune" where id=3'
try:
    mycursor.execute(sql)  
    mydb.commit()
    print(mycursor.rowcount,"Rows updated...")
    
except:
    mydb.rollback()
    print("unable to update data...")

mycursor.close()
mydb.close()