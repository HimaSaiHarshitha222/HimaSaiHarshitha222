"""
11) Write a Python Program to REVERSE internal content of each word?
    Input: Python is Simple
    Output: nohtyP si elpmiS
"""
s = input("Enter a String: ").split()
ans = []
for ele in s:
    ans.append(ele[::-1])
print(' '.join(ans))
