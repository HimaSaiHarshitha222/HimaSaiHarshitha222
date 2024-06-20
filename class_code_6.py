class Student: 
   def __init__(self, name,age,marks): 
      self.name = name 
      self.age = age 
      self.marks = marks

   def talk(self): 
      print('Hi, I am', self.name) 
      print('My age is', self.age) 
      print('My marks are', self.marks) 

s1 = Student('Vishnu',20,900) 
s1.talk()
print("********************")
s2 = Student('Praveen',19, 800) 
s2.talk()
print("********************")
s3 = Student('Ganesh', 22, 700) 
s3.talk()
