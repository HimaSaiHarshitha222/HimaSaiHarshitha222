class Student:
    def __init__(self):
        self.id = 1001
        self.name = 'Ravindra'
        self.marks = 961
        self.branch = 'ECE'
    def display(self):
        print("Hai I'm",self.name)
        print("I belong to {} department".format(self.branch))
        print("I got {} marks".format(self.marks))

s1 = Student()
s1.display()
