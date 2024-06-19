#9) Write a Python program to remove all consecutive duplicates of a given string.

s = input("Enter a String: ")
ans = ''
prev = None
for ch in s:#n,a,v,e,e,n
    if ch != prev:
        ans = ans + ch
        prev = ch

print(ans)
        


    
