class One:
    def method(self):
        print("This is Parent Method")

class Two(One):
    def method(self):
        print("This is Child Method")

obj = Two()
obj.method()
