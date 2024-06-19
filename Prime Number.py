
num = int(input("Enter a Number "))

if num>1:
    for i in range(2,num):#2,3,4,5,6,7,8,9,10
        if num%i==0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
        
else:
    print("Not a Prime Number")
    
