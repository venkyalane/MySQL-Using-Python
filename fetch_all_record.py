#fetch all data from table using fetchone() method.
import mysql.connector

mydb=mysql.connector.connect(host='localhost', password='', user='root', port=3307, database='mydb') 

mycursor=mydb.cursor()
sql='select * from customer'
mycursor.execute(sql)
row=mycursor.fetchone()
while row is not None:
    print(row)
    row = mycursor.fetchone()
print('Total rows:',mycursor.rowcount)
mycursor.close()

mydb.close()


#fetch all data from table using for loop.
import mysql.connector

mydb=mysql.connector.connect(host='localhost',port=3307, user='root',database='mydb') 

mycursor=mydb.cursor()
mycursor.execute('select * from customer')
for i in mycursor:
    print(i)
print('Total rows:',mycursor.rowcount)
mycursor.close()

mydb.close()


#Fetch all data from table in different format.
import mysql.connector

mydb=mysql.connector.connect(host='localhost', port=3307, user='root', database='mydb') 

mycursor=mydb.cursor()
mycursor.execute("select * from customer where name='dinesh'")
for i in mycursor:
    id =i[0]
    name = i[1]
    address = i[2]
    print(f'id:{id} name:{name} address:{address}')
print('Total rows:',mycursor.rowcount)
mycursor.close()

mydb.close()
