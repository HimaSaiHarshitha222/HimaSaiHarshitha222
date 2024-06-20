print("Welcome")
try:
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    c = a/b
    
except (ValueError,ZeroDivisionError):
    print("Please Provide Integer only or")
    print("Denominator shouldn't be Zero")
else:
    print("Result =",c)
finally:
    print("Close Files")
