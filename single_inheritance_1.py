class Father:
    def methodA(self):
        print("This is Parent Class")

class Son(Father):
    def methodB(self):
        print("This is Child Class")

obj = Son()
obj.methodA()
obj.methodB()
