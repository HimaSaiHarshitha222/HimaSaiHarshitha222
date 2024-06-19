"""
8)Write a Python program to convert a list of multiple integers into a single integer. 
  Sample list: [11, 33, 50]. 
  Expected Output: 113350
"""
a = list(map(int,input().split()))
print(''.join(map(str,a)))
