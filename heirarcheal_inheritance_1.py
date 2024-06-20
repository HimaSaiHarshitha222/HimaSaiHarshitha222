class Father:
    def method(self):
        print("This is Parent Class")

class Son1(Father):
    def method1(self):
        print("This is Child 1 Class")

class Son2(Father):
    def method2(self):
        print("This is Child 2 Class")

class Son3(Father):
    def method3(self):
        print("This is Child 3 Class")


obj = Son3()
obj.method()
obj.method3()
