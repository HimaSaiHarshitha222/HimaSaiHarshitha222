"""
6) Write a Python program to lowercase first n characters in a string.
   Example:
   String: DIGI BRAINS ACADEMY
   No of chars: 6
   Output: digi bRAINS ACADEMY
"""

s = input("Enter a String: ")
n = int(input("Enter No of Characters: "))

ans = s[:n].lower() + s[n:]
print(ans)
