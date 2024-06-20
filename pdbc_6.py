import mysql.connector  
myconn = mysql.connector.connect(host = "localhost", user = "root",password = "root", database = "py37")  
cur = myconn.cursor()  

  
try:  
    cur.execute("create table reg_form(  id int primary key auto_increment,  name varchar(65),  mobile char(10),  course varchar(30),  doj date)")
    print("Successfully Created")
except:  
    myconn.rollback()  



myconn.close()
