import sys
num = int(sys.argv[1])

if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not a Prime")
            break
    print("Prime Number")
