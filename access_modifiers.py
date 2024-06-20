class Company:
    def __init__(self, name, proj):
        self.name = name      
        self._proj = proj
    
    def show(self):
        print("The code of the company is = ",self.ccode)

class Emp(Company):
    def __init__(self, eName, sal, cName, proj):
        Company.__init__(self, cName, proj)
        self.name = eName   
        self.__sal = sal    
    
    def show_sal(self):
        print("The salary of ",self.name," is ",self.__sal)

c = Company("IBM", "Foodgenics Ecommerce")
e = Emp("Harish", 9999999, c.name, c._proj)

print("Welcome to ", c.name)
print("Here ", e.name," is working on ",e._proj)

e.show_sal()
