"""
10) Write a Python Program to print REVERSE order of words present in the given string.
    Input: Python is Simple
    Output:Simple is Python
"""
s = input("Enter a String ").split()[::-1]
print(' '.join(s))
