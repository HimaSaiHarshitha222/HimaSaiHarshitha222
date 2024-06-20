import mysql.connector  
myconn = mysql.connector.connect(host = "localhost", user = "root",password = "root")  
cur = myconn.cursor()  

  
try:  
    cur.execute("create database py37")  
except:  
    myconn.rollback()  



myconn.close()
