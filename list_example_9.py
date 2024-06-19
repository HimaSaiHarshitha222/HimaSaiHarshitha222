
#9) Write a program to find the sum of the element in the list.

a = list(map(int,input().split(',')))
s = 0

for ele in a:#3,5,1,6
    s = s+ ele

print(s)
