






def fun(n): 
   if n==0 or n==1: 
      return 1 
   else: 
      return n*fun(n-1) 


n=int(input("Enter a Number: "))
res=fun(n)
print("Factorial of %d is %d " %(n,res))
