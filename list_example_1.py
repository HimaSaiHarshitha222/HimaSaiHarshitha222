#1) Write a Python program to multiply all the items in a list.

a = list(map(int,input().split(',')))

ans = 1

for ele in a:
    ans = ans * ele

print(ans)
