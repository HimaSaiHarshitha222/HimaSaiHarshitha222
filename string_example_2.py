"""
2) Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
   Sample String: We Love Python
   Sample Output: ne Love PythoW
"""
s = input("Enter a String: ")
print(s[-1]+s[1:-1]+s[0])
