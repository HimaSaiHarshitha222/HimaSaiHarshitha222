class A:
    def methodA(self):
        print("This Method is in Super Class")

class B(A):
    def methodB(self):
        print("This Method is in Sub Class")

obj = B()
obj.methodA()
obj.methodB()
print("***********************")

obj1 = A()
obj1.methodA()
obj1.methodB()
