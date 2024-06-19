#3) Write a Python program to remove duplicates from a list.

a = list(map(int,input().split(',')))
ans = []

for ele in a:#3,67,8,12,3,8,9,23,8,12
    if ele not in ans:
        ans.append(ele)
print(ans)
    
