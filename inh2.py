from teach import *
class Student(Teacher): 
   def setmarks(self, marks): 
      self.marks = marks 
   def getmarks(self): 
      return self.marks
    
s = Student() 
s.setid(100) 
s.setname('Rakesh')
s.setaddress('H.No.-231, Old Town, Anantapur') 
s.setmarks(970)

print('id=', s.getid()) 
print('name=', s.getname()) 
print('address=', s.getaddress()) 
print('marks=', s.getmarks())
