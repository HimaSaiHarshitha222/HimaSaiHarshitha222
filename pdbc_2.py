import mysql.connector  
  
myconn = mysql.connector.connect(host = "localhost", user = "root",password = "root", database = "py35")  
print(myconn) 

cur = myconn.cursor()  
print(cur)
