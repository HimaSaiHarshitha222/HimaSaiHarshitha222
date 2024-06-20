import empl, pickle 
f = open('emp.dat', 'rb') 
print('Employees details:') 
while True: 
   try: 
     obj = pickle.load(f) 
     obj.display() 
   except EOFError: 
     print('End of file reached...') 
     break
f.close()
