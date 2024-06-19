#2) Write a Python program to get the largest number from a list.

a = list(map(int,input().split()))
maxi = 0

for ele in a:#785, 920, 800, 813
    if ele > maxi:
        maxi = ele

print(maxi)
