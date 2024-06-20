print("Welcome")
try:
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    c = a/b
    print(c)
except:
    print("Exception Occured")
finally:
    print("The End")
