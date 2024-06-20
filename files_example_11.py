


f1 = open('dog.jpg', 'rb') 
f2 = open('new.jpg', 'wb') 

b = f1.read() 
f2.write(b) 
f1.close()
f2.close()
