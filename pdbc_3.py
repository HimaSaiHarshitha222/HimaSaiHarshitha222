import mysql.connector  
myconn = mysql.connector.connect(host = "localhost", user = "root",password = "root", database = "py35")  
cur = myconn.cursor()  

  
try:  
    cur.execute("show databases")  
except:  
    myconn.rollback()  
for x in cur:  
    print(x)  



myconn.close()
