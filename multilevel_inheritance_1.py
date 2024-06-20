class GrandFather:
    def method1(self):
        print("This is Grand Parent Class")
        
class Father(GrandFather):
    def method2(self):
        print("This is Parent Class")

class Son(Father):
    def method3(self):
        print("This is Child Class")



obj = Son()
obj.method1()
obj.method2()
obj.method3()
