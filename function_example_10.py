def calc(a,b):
   w=(a+b)**2
   x=(a-b)**2
   y=(a+b)**3
   z=(a-b)**3
   return w,x,y,z

a=int(input("Enter value of 'a' : "))
b=int(input("Enter value of 'b' : "))

w,x,y,z=calc(a,b)
print("(a+b)^2 = :",w)
print("(a+b)^3 = :",y)
print("(a-b)^2 = :",x)
print("(a-b)^3 = :",z)
