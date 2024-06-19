a=1
def myfunction(): 
   global a 
   print('global a=', a) 
   a=2 
   print('modifed a=', a)
   
myfunction() 
print('global a=', a)
