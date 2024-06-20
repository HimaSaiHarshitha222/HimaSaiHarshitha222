import empl, pickle 
f = open('emp.dat', 'wb') 
n = int(input('How many employees?')) 
for i in range(n): 
   id = int(input('Enter id:')) 
   name = input('Enter name:') 
   sal = float(input('Enter salary:')) 
 
   e = empl.Emp(id, name, sal)
   pickle.dump(e, f) 
f.close()
