print("Welcome")
try:
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    c = a/b
    
except ValueError:
    print("Please Provide Integer only")
except ZeroDivisionError:
    print("Denominator shouldn't be Zero")
else:
    print("Result =",c)
finally:
    print("Close Files")
