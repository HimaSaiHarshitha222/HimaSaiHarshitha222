#10) Write a program to find the lists consist of at least one common element 

a = list(map(int,input().split(',')))
b = list(map(int,input().split(',')))

ans = []

for i in a:#3,6,1,78,11,5
    if i in b:
        ans.append(i)

print(ans)
