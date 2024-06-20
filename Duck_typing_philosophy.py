
class Duck: 
   def talk(self): 
      print('Quack, quack!') 

class Human: 
   def talk(self): 
      print('Hello, hi!')

def call_talk(obj): 
      obj.talk()
            
x = Duck()
call_talk(x) 
x = Human() 
call_talk(x)
