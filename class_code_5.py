class Student: 
   def __init__(self): 
      self.name = 'Vishnu' 
      self.age = 20 
      self.marks = 900 

   def talk(self): 
      print('Hi, I am', self.name) 
      print('My age is', self.age) 
      print('My marks are', self.marks) 

s1 = Student() 
s1.talk()
print("********************")
s2 = Student() 
s2.talk()
print("********************")
s3 = Student() 
s3.talk()
