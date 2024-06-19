start = int(input("Enter starting Number "))
stop = int(input("Enter ending Number "))
c = s = 0
for num in range(start, stop+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end = '\t')
            c += 1
            s = s+num
print("\nNo of Primes",c)
print("Sum of Primes",s)
