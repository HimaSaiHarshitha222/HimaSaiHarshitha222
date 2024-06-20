class MethodOverloading:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

obj = MethodOverloading()
obj.add(3,4,5)
