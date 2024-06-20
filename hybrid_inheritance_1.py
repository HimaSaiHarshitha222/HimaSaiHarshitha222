class GrandFather:
    def method(self):
        print("This is Grand Father class")
        
class Father(GrandFather):
    def method1(self):
        print("This is Father Class")

class Mother(GrandFather):
    def method2(self):
        print("This is Mother Class")

class Child(Father, Mother):
    def method3(self):
        print("This is Child Class")

obj = Child()
obj.method3()
obj.method1()
obj.method2()
obj.method()
