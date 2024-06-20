class GrandPa:
    def grand(self):
        print("I am GrandPa")

class Father(GrandPa):
    def father(self):
        print("I am Father")

class Mother(GrandPa):
    def mother(self):
        print("I am Mother")

class Child(Father,Mother):
    def child(self):
        print("I am  child of Father and Mother")

f = Father()
m = Mother()
c = Child()

f.grand()
f.father()
print("\n")
c.father()
c.mother()
c.child()
print("\n")
c.grand()
