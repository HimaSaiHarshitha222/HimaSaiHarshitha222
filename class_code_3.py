class Employee:
    def __init__(self):
        self.id = 1001
        self.name = 'Gagan'
        self.salary = 60000
    def details(self):
        print("Hello I'm",self.name)
        print("I earn {} per month".format(self.salary))

gagantej = Employee()
gagantej.details()
