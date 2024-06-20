class Man:
    def __init__(self):
        self.name = 'Jasmine'
        self.age = 31
        self.place = 'Delhi'
    def talk(self):
        print("Hai I'm",self.name)
        print("I belong to",self.place)
        
    
obj = Man()
obj.talk()
print(obj.age)
