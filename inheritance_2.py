class Parent:
    def method1(self):
        print("This is Method 1")

class Child(Parent):
    def method2(self):
        print("This is Method 2")

obj = Child()
obj.method1()
