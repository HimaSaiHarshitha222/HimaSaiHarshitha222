a=1 

def myfunction():
   global a
   b=2 
   print('a=', a) 
   print('b=', b)
   a = a+5
   b = b+5
   print('a=', a) 
   print('b=', b) 

myfunction() 

print(a) 
print(b)
