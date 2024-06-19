#3) Write a Python program to remove the characters which have odd index values of a given string.

s = input("Enter a String: ")

for ch in s[::2]:
    print(ch,end='')
