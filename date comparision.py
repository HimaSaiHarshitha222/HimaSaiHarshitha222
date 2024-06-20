from datetime import * 

d1, m1, y1 = [int(x) for x in input("Enter first person's birth date (DD/MM/YYYY): ").split('/')] 
b1 = date(y1, m1, d1) 

d2, m2, y2 = [int(x) for x in input("Enter second person's birth date (DD/MM/YYYY): ").split('/')] 
b2 = date(y2, m2, d2) 

if b1 == b2: 
   print('Both persons are of equal age') 
elif b1 > b2: 
   print('The second person is elder') 
else: 
   print('The first person is elder')
