"""
5) Write a Python program to count repeated characters in a string. 
   Sample String: 'thequickbrownfoxjumpsoverthelazydog'
   Sample output:  {'t': 2, 'h': 2, 'e': 3, 'u': 2, 'r': 2, 'o': 4}
"""

s = input("Enter a String: ")
ans = {}

for ch in s:
    if s.count(ch)>1:
        ans[ch] = s.count(ch)
print(ans)
