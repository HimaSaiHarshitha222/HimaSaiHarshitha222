class MyException(Exception): 
   def __init__(self,arg): 
      self.msg = arg

def check(list): 
      for i in list:#25,78,65,94,112,77,49 
         print(i,end='\t') 
         if(i<0 or i>100): 
            raise MyException('Exception Occured at %d'%i) 

marks=[25,78,65,94,112,77,49]

try: 
  check(marks) 
except MyException as me: 
  print(me)
