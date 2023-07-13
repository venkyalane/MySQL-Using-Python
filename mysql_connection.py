import mysql.connector


#check MySQL connection established or not
conn = mysql.connector.connect(host='localhost', user='root',password='', port=3307)

if conn.is_connected():
    print("connection established....")
else:
    print("something went wrong!!!")

conn.close()