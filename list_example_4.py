	#4) Write a Python program to get the frequency of the elements in a list.

a = list(map(int,input().split()))
ans = {}

for ele in a:
    ans[ele] = a.count(ele)
print(ans)
