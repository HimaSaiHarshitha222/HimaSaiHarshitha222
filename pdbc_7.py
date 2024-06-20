import mysql.connector  
myconn = mysql.connector.connect(host = "localhost", user = "root",password = "root", database = "py37")  
cur = myconn.cursor()  

  
try:  
    sql = "insert into reg_form(name,mobile, course, doj) values (%s, %s, %s, %s)"
    val = ("Haritha", '9666123401', 'Python' , "2024-01-22")
    cur.execute(sql,val)
    myconn.commit()  

except:  
    myconn.rollback()  

print(cur.rowcount,"record inserted!")  


myconn.close()
