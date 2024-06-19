#4) Write a Python program to reverse a string without using builtin functions.

s = input("Enter a String: ")
ans = ''

for ch in s:
    ans = ch + ans
    
print(ans)
