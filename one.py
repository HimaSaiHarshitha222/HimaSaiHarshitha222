def display():
    print('Hello Python!') 

if __name__ == '__main__': 
    display() 
    print('This code is run as a program') 
else:
    print("Value inside special variable",__name__)
    print('This code is run as a module')
